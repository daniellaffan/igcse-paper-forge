import { useEffect, useMemo, useState } from 'react'
import { Link, useNavigate, useParams } from 'react-router-dom'
import type { Question, TestConfig } from '../types'
import { clearSeen, loadBank, markSeen, save, seenIds, store } from '../lib/data'
import { assemble, filterPool, marksPerMinute } from '../lib/assemble'
import { encodeConfig, newSeed } from '../lib/rng'
import { useSelection, useSpec } from './Subject'

const DIFF_PRESETS: { id: string; label: string; w: [number, number, number] }[] = [
  { id: 'mixed', label: 'Mixed, like the real exam', w: [3, 4, 3] },
  { id: 'build', label: 'Confidence builder (mostly grades 1–6)', w: [5, 4, 1] },
  { id: 'stretch', label: 'Stretch (mostly grades 6–9)', w: [1, 4, 5] },
  { id: 'top', label: 'Grade 7–9 only', w: [0, 0, 1] },
]

export default function Builder() {
  const { subject = '' } = useParams()
  const nav = useNavigate()
  const { spec, err } = useSpec(subject)
  const [sel] = useSelection(subject)
  const [bank, setBank] = useState<Question[] | null>(null)
  const [bankErr, setBankErr] = useState('')
  const saved = store<Partial<TestConfig> & { diffPreset?: string }>('cfg:' + subject, {})
  const [mode, setMode] = useState<'topic' | 'full'>(saved.mode || 'topic')
  const [paper, setPaper] = useState(saved.paper || '')
  const [lenBy, setLenBy] = useState<'marks' | 'minutes'>(saved.length?.by || 'marks')
  const [lenVal, setLenVal] = useState(saved.length?.value || 40)
  const [qtypes, setQtypes] = useState<Set<string>>(new Set(saved.qtypes || []))
  const [diffPreset, setDiffPreset] = useState(saved.diffPreset || 'mixed')
  const [calc, setCalc] = useState<TestConfig['calculator']>(saved.calculator || 'any')
  const [options, setOptions] = useState<Set<string>>(new Set(saved.options || []))
  const [seed, setSeed] = useState(newSeed())
  const [seenCount, setSeenCount] = useState(() => seenIds(subject).size)

  useEffect(() => { loadBank(subject).then(setBank).catch(e => setBankErr(String(e))) }, [subject])
  useEffect(() => {
    if (spec && mode === 'full' && !paper) setPaper(spec.papers[0].id)
  }, [spec, mode, paper])

  const diff = DIFF_PRESETS.find(d => d.id === diffPreset)?.w || [3, 4, 3]
  const cfg: TestConfig = useMemo(() => ({
    subject, mode, paper, subtopics: mode === 'full' ? [] : [...sel], qtypes: mode === 'full' ? [] : [...qtypes],
    length: { by: lenBy, value: lenVal }, diff, calculator: calc, options: [...options], seed,
  }), [subject, mode, paper, sel, qtypes, lenBy, lenVal, diff, calc, options, seed])

  const pool = useMemo(() => (bank && spec ? filterPool(bank, spec, { ...cfg, qtypes: [] }) : []), [bank, spec, cfg])
  const typeCounts = useMemo(() => {
    const m = new Map<string, number>()
    pool.forEach(q => m.set(q.qtype, (m.get(q.qtype) || 0) + 1))
    return m
  }, [pool])
  const hasCalcSplit = useMemo(() => !!bank && bank.some(q => q.calculator === false) && bank.some(q => q.calculator === true), [bank])

  if (err) return <div className="wrap"><p className="error">{err}</p></div>
  if (!spec) return <div className="wrap"><p className="muted">Loading…</p></div>
  const mpm = marksPerMinute(spec, paper || spec.papers[0].id)
  const poolMarks = filterPool(bank || [], spec, cfg).reduce((a, q) => a + q.marks, 0)

  const build = () => {
    if (!bank) return
    save('cfg:' + subject, { ...cfg, diffPreset })
    const seen = seenIds(subject)
    const a = assemble(bank, spec, cfg, seen)
    const ids = a.sections.map(s => s.questions.map(q => q.id))
    markSeen(subject, ids.flat())
    const c = encodeConfig(cfg)
    const q = encodeConfig(ids)
    nav(`/s/${subject}/paper?c=${c}&q=${q}`)
  }

  return (
    <div className="wrap narrow">
      <nav className="crumbs"><Link to="/">Subjects</Link> › <Link to={`/s/${subject}`}>{spec.short || spec.title}</Link> › Test builder</nav>
      <h1>Build a test</h1>
      {bankErr && <p className="error">{bankErr}</p>}
      <form className="builder" onSubmit={e => { e.preventDefault(); build() }}>
        <fieldset>
          <legend>What kind of test?</legend>
          <label className="radio"><input type="radio" name="mode" checked={mode === 'topic'} onChange={() => setMode('topic')} /> <b>Topic test</b> — only the sub-topics you ticked, the length you choose</label>
          <label className="radio"><input type="radio" name="mode" checked={mode === 'full'} onChange={() => setMode('full')} /> <b>Full paper in the real structure</b> — same sections, question order and marks as the real paper</label>
        </fieldset>

        <fieldset>
          <legend>Paper / component</legend>
          <select value={paper} onChange={e => setPaper(e.target.value)} aria-label="Paper">
            {mode === 'topic' && <option value="">Any paper</option>}
            {spec.papers.map(p => <option key={p.id} value={p.id}>{p.name} — {p.minutes} min, {p.marks} marks{p.calculator === false ? ', non-calculator' : ''}</option>)}
          </select>
        </fieldset>

        {spec.options && spec.options.length > 0 && (
          <fieldset>
            <legend>Options to include</legend>
            {spec.options.filter(o => !paper || !o.paper || o.paper === paper).map(o => (
              <label key={o.id} className="chk"><input type="checkbox" checked={options.size === 0 || options.has(o.id)} onChange={() => {
                const base = options.size === 0 ? new Set(spec.options!.map(x => x.id)) : new Set(options)
                if (base.has(o.id)) base.delete(o.id); else base.add(o.id)
                setOptions(base.size === spec.options!.length ? new Set() : base)
              }} /> {o.name}</label>
            ))}
          </fieldset>
        )}

        {mode === 'topic' && (
          <>
            <fieldset>
              <legend>Sub-topics</legend>
              <p>{sel.size ? <><b>{sel.size}</b> sub-topics ticked</> : <>Nothing ticked, so <b>the whole course</b> is used</>} · <Link to={`/s/${subject}`}>change on the checklist</Link></p>
            </fieldset>
            <fieldset>
              <legend>Length</legend>
              <div className="row">
                <select value={lenBy} onChange={e => setLenBy(e.target.value as 'marks' | 'minutes')} aria-label="Length measured by">
                  <option value="marks">Total marks</option>
                  <option value="minutes">Minutes</option>
                </select>
                <input type="number" min={1} max={300} value={lenVal} onChange={e => setLenVal(Math.max(1, Number(e.target.value) || 1))} aria-label="Length value" />
                <span className="muted">{lenBy === 'marks' ? `≈ ${Math.round(lenVal / mpm)} minutes` : `≈ ${Math.round(lenVal * mpm)} marks`}</span>
              </div>
              <div className="chips">{[10, 20, 30, 45, 60].map(v => <button type="button" key={v} className="chip" onClick={() => { setLenBy('minutes'); setLenVal(v) }}>{v} min</button>)}</div>
            </fieldset>
            <fieldset>
              <legend>Question types <span className="muted">(none ticked = all)</span></legend>
              <div className="types">
                {spec.qtypes.map(t => (
                  <label key={t.id} className={'chk' + (typeCounts.get(t.id) ? '' : ' dim')} title={t.description}>
                    <input type="checkbox" checked={qtypes.has(t.id)} onChange={() => { const n = new Set(qtypes); if (n.has(t.id)) n.delete(t.id); else n.add(t.id); setQtypes(n) }} />
                    {t.label}{t.marks ? <span className="muted"> ({t.marks})</span> : null} <span className="count">{typeCounts.get(t.id) || 0}</span>
                  </label>
                ))}
              </div>
            </fieldset>
            <fieldset>
              <legend>Difficulty</legend>
              {DIFF_PRESETS.map(d => <label key={d.id} className="radio"><input type="radio" name="diff" checked={diffPreset === d.id} onChange={() => setDiffPreset(d.id)} /> {d.label}</label>)}
            </fieldset>
            {hasCalcSplit && (
              <fieldset>
                <legend>Calculator</legend>
                <select value={calc} onChange={e => setCalc(e.target.value as TestConfig['calculator'])} aria-label="Calculator">
                  <option value="any">Either</option>
                  <option value="calc">Calculator questions</option>
                  <option value="noncalc">Non-calculator questions</option>
                </select>
              </fieldset>
            )}
          </>
        )}

        <fieldset>
          <legend>Seed</legend>
          <div className="row">
            <input type="number" value={seed} onChange={e => setSeed(Number(e.target.value) || 1)} aria-label="Seed" />
            <button type="button" className="btn" onClick={() => setSeed(newSeed())}>New seed</button>
            <span className="muted">The seed and your choices are saved in the paper's link, so you can reopen or share the exact paper.</span>
          </div>
        </fieldset>

        <div className="build-bar">
          <button type="submit" className="btn primary big" disabled={!bank}>{bank ? 'Make my paper' : 'Loading questions…'}</button>
          {bank && mode === 'topic' && <span className="muted">{pool.length} questions ({poolMarks} marks) match these settings.</span>}
          <span className="muted">You have seen {seenCount} questions in this subject. <button type="button" className="linkish" onClick={() => { clearSeen(subject); setSeenCount(0) }}>Reset</button></span>
        </div>
      </form>
    </div>
  )
}
