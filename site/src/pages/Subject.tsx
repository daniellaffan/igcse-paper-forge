import { useEffect, useMemo, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import type { Spec, Topic } from '../types'
import { loadSpec, save, store } from '../lib/data'

export type Counts = Record<string, { total: number; byType: Record<string, number> }>
export type SpecWithCounts = Spec & { counts?: Counts }

export function useSpec(subject?: string) {
  const [spec, setSpec] = useState<SpecWithCounts | null>(null)
  const [err, setErr] = useState('')
  useEffect(() => {
    if (!subject) return
    setSpec(null)
    loadSpec(subject).then(s => setSpec(s as SpecWithCounts)).catch(e => setErr(String(e)))
  }, [subject])
  return { spec, err }
}

export function useSelection(subject: string) {
  const [sel, setSel] = useState<Set<string>>(() => new Set(store<string[]>('sel:' + subject, [])))
  useEffect(() => { setSel(new Set(store<string[]>('sel:' + subject, []))) }, [subject])
  const update = (next: Set<string>) => { setSel(new Set(next)); save('sel:' + subject, [...next]) }
  return [sel, update] as const
}

function TopicNode({ t, sel, setSel, counts, paperFilter, open, toggleOpen }: {
  t: Topic; sel: Set<string>; setSel: (s: Set<string>) => void; counts?: Counts; paperFilter: string
  open: boolean; toggleOpen: () => void
}) {
  const subs = t.subtopics.filter(s => !paperFilter || !s.papers || s.papers.includes(paperFilter))
  if (!subs.length) return null
  const ids = subs.map(s => s.id)
  const nSel = ids.filter(i => sel.has(i)).length
  const all = nSel === ids.length
  const n = ids.reduce((a, i) => a + (counts?.[i]?.total || 0), 0)
  const toggleAll = () => {
    const next = new Set(sel)
    ids.forEach(i => (all ? next.delete(i) : next.add(i)))
    setSel(next)
  }
  return (
    <li className="topic">
      <div className="topic-row">
        <button type="button" className="disclose" aria-expanded={open} onClick={toggleOpen} aria-label={(open ? 'Collapse ' : 'Expand ') + t.title}>
          {open ? '▾' : '▸'}
        </button>
        <label className="chk">
          <input type="checkbox" checked={all} ref={el => { if (el) el.indeterminate = nSel > 0 && !all }} onChange={toggleAll} />
          <span className="ref">{t.ref}</span> <b>{t.title}</b>
        </label>
        <span className="count" title="questions available">{n}</span>
      </div>
      {open && (
        <ul className="subs">
          {subs.map(s => (
            <li key={s.id} className="sub">
              <label className="chk">
                <input type="checkbox" checked={sel.has(s.id)} onChange={() => {
                  const next = new Set(sel)
                  if (next.has(s.id)) next.delete(s.id); else next.add(s.id)
                  setSel(next)
                }} />
                <span className="ref">{s.ref}</span> <span className="st-title">{s.title}</span>
                <span className="count">{counts?.[s.id]?.total || 0}</span>
              </label>
              <p className="st-sum">{s.summary}</p>
              <details className="points">
                <summary>{s.points.length} spec point{s.points.length === 1 ? '' : 's'}</summary>
                <ul>
                  {s.points.map(p => (
                    <li key={p.ref}><span className="ref">{p.ref}</span> {p.summary}
                      {p.paper2_only && <span className="tag">Paper 2 only</span>}
                      {p.higher_only && <span className="tag">Higher</span>}
                    </li>
                  ))}
                </ul>
              </details>
            </li>
          ))}
        </ul>
      )}
    </li>
  )
}

export default function SubjectPage() {
  const { subject = '' } = useParams()
  const { spec, err } = useSpec(subject)
  const [sel, setSel] = useSelection(subject)
  const [paperFilter, setPaperFilter] = useState('')
  const [open, setOpen] = useState<Set<string>>(new Set())
  const [optFilter, setOptFilter] = useState('')
  const topics = useMemo(() => (spec?.topics || []).filter(t => !optFilter || t.option === optFilter), [spec, optFilter])
  if (err) return <div className="wrap"><p className="error">{err}</p></div>
  if (!spec) return <div className="wrap"><p className="muted">Loading…</p></div>
  const allIds = topics.flatMap(t => t.subtopics.map(s => s.id))
  const total = Object.values(spec.counts || {}).reduce((a, c) => a + c.total, 0)
  return (
    <div className="wrap">
      <nav className="crumbs"><Link to="/">Subjects</Link> › {spec.short || spec.title}</nav>
      <div className="subj-head">
        <div>
          <h1>{spec.title}</h1>
          <p className="muted">{spec.board} · {spec.code} · {spec.papers.map(p => `${p.name} (${p.minutes} min, ${p.marks} marks)`).join(' · ')} · {total.toLocaleString()} questions</p>
          <p><a href={spec.official_url} target="_blank" rel="noreferrer">Official past papers and specification ↗</a></p>
        </div>
        <Link className="btn primary big" to={`/s/${subject}/build`}>Build a test →</Link>
      </div>
      <h2>Specification checklist</h2>
      <p className="muted">Tick the parts of the course you want to be tested on. Numbers on the right are how many questions the bank has. Your ticks are remembered on this device.</p>
      <div className="toolbar">
        {spec.papers.length > 1 && (
          <label>Show content for{' '}
            <select value={paperFilter} onChange={e => setPaperFilter(e.target.value)}>
              <option value="">all papers</option>
              {spec.papers.map(p => <option key={p.id} value={p.id}>{p.name}</option>)}
            </select>
          </label>
        )}
        {spec.options && spec.options.length > 0 && (
          <label>Option{' '}
            <select value={optFilter} onChange={e => setOptFilter(e.target.value)}>
              <option value="">all</option>
              {spec.options.map(o => <option key={o.id} value={o.id}>{o.name}</option>)}
            </select>
          </label>
        )}
        <button type="button" className="btn" onClick={() => setSel(new Set([...sel, ...allIds]))}>Tick all</button>
        <button type="button" className="btn" onClick={() => { const n = new Set(sel); allIds.forEach(i => n.delete(i)); setSel(n) }}>Clear</button>
        <button type="button" className="btn" onClick={() => setOpen(open.size ? new Set() : new Set(topics.map(t => t.id)))}>{open.size ? 'Collapse all' : 'Expand all'}</button>
        <span className="muted">{sel.size} sub-topics ticked</span>
      </div>
      <ul className="tree">
        {topics.map(t => (
          <TopicNode key={t.id} t={t} sel={sel} setSel={setSel} counts={spec.counts} paperFilter={paperFilter}
            open={open.has(t.id)} toggleOpen={() => { const n = new Set(open); if (n.has(t.id)) n.delete(t.id); else n.add(t.id); setOpen(n) }} />
        ))}
      </ul>
      <div className="sticky-cta"><Link className="btn primary" to={`/s/${subject}/build`}>Build a test with {sel.size || 'all'} sub-topics →</Link></div>
    </div>
  )
}
