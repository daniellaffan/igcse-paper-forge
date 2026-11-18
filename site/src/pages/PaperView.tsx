import { useEffect, useMemo, useRef, useState } from 'react'
import { Link, useLocation, useNavigate, useParams } from 'react-router-dom'
import type { Question, TestConfig } from '../types'
import { loadBank, markSeen, seenIds } from '../lib/data'
import { assemble, fromIds, type Assembled } from '../lib/assemble'
import { decodeConfig, encodeConfig, newSeed } from '../lib/rng'
import { exportPdf } from '../lib/pdf'
import { MarkSchemeDoc, QuestionPaperDoc } from '../paper/Documents'
import type { CoverInfo } from '../paper/Cover'
import { useSpec } from './Subject'

export default function PaperView({ kind }: { kind: 'qp' | 'ms' }) {
  const { subject = '' } = useParams()
  const loc = useLocation()
  const nav = useNavigate()
  const params = new URLSearchParams(loc.search)
  const c = params.get('c') || ''
  const qParam = params.get('q') || ''
  const cfg = useMemo(() => decodeConfig<TestConfig>(c), [c])
  const ids = useMemo(() => (qParam ? decodeConfig<string[][]>(qParam) : null), [qParam])
  const { spec, err } = useSpec(subject)
  const [bank, setBank] = useState<Question[] | null>(null)
  const [busy, setBusy] = useState('')
  const [copied, setCopied] = useState(false)
  const qpRef = useRef<HTMLDivElement>(null)
  const msRef = useRef<HTMLDivElement>(null)
  useEffect(() => { loadBank(subject).then(setBank).catch(() => setBank([])) }, [subject])

  const a: Assembled | null = useMemo(() => {
    if (!spec || !bank || !cfg) return null
    if (ids && ids.length) return fromIds(bank, spec, cfg, ids)
    return assemble(bank, spec, cfg, new Set())
  }, [spec, bank, cfg, ids])

  if (!cfg) return <div className="wrap"><p className="error">This link is missing its paper settings.</p><Link to={`/s/${subject}/build`}>Build a test</Link></div>
  if (err) return <div className="wrap"><p className="error">{err}</p></div>
  if (!spec || !a) return <div className="wrap"><p className="muted">Building your paper…</p></div>

  const paper = a.paper
  const topicNames = (() => {
    if (cfg.mode === 'full') return ''
    const names = new Set<string>()
    a.sections.forEach(s => s.questions.forEach(q => {
      const t = spec.topics.find(t => t.id === q.topic)
      if (t) names.add(t.title)
    }))
    const list = [...names]
    return list.length > 4 ? `${list.slice(0, 4).join(', ')} and ${list.length - 4} more` : list.join(', ')
  })()
  const cover: CoverInfo = {
    spec, paper,
    title: cfg.mode === 'full' && paper ? paper.name : 'Topic test',
    subtitle: cfg.mode === 'full' ? undefined : topicNames,
    minutes: a.minutes, marks: a.totalMarks, seed: cfg.seed, kind: 'qp',
  }
  const base = `${spec.code}-${cfg.mode === 'full' && paper ? paper.id : 'topic-test'}-seed${cfg.seed}`.replace(/[^A-Za-z0-9-]/g, '')
  const doExport = async (which: 'qp' | 'ms') => {
    const root = which === 'qp' ? qpRef.current : msRef.current
    if (!root) return
    setBusy(which === 'qp' ? 'Making question paper PDF…' : 'Making mark scheme PDF…')
    try {
      await exportPdf(root, `${base}-${which === 'qp' ? 'question-paper' : 'mark-scheme'}.pdf`, (d, t) => setBusy(`Page ${d} of ${t}…`))
    } finally { setBusy('') }
  }
  const remake = () => {
    if (!bank) return
    const next = { ...cfg, seed: newSeed() }
    const na = assemble(bank, spec, next, seenIds(subject))
    const nids = na.sections.map(s => s.questions.map(q => q.id))
    markSeen(subject, nids.flat())
    nav(`/s/${subject}/paper?c=${encodeConfig(next)}&q=${encodeConfig(nids)}`)
  }
  const other = kind === 'qp' ? 'markscheme' : 'paper'
  return (
    <div className="paper-view">
      <div className="paper-bar no-print">
        <nav className="crumbs"><Link to="/">Subjects</Link> › <Link to={`/s/${subject}`}>{spec.short || spec.title}</Link> › <Link to={`/s/${subject}/build`}>Builder</Link></nav>
        <div className="tabs" role="tablist">
          <Link role="tab" aria-selected={kind === 'qp'} className={'tab' + (kind === 'qp' ? ' on' : '')} to={`/s/${subject}/paper${loc.search}`}>Question paper</Link>
          <Link role="tab" aria-selected={kind === 'ms'} className={'tab' + (kind === 'ms' ? ' on' : '')} to={`/s/${subject}/markscheme${loc.search}`}>Mark scheme</Link>
        </div>
        <div className="actions">
          <button type="button" className="btn primary" onClick={() => doExport('qp')} disabled={!!busy}>⤓ Question paper PDF</button>
          <button type="button" className="btn primary" onClick={() => doExport('ms')} disabled={!!busy}>⤓ Mark scheme PDF</button>
          <button type="button" className="btn" onClick={() => { navigator.clipboard?.writeText(location.href).then(() => { setCopied(true); setTimeout(() => setCopied(false), 1500) }).catch(() => {}) }}>{copied ? 'Link copied' : 'Copy link'}</button>
          <button type="button" className="btn" onClick={remake}>New paper, same settings</button>
          <Link className="btn" to={`/s/${subject}/${other}${loc.search}`}>{kind === 'qp' ? 'Show mark scheme' : 'Show questions'}</Link>
        </div>
        <div className="paper-meta muted">
          {a.totalMarks} marks · {a.minutes} minutes · seed {cfg.seed}{busy && <b className="busy"> · {busy}</b>}
          {a.warnings.map((w, i) => <div key={i} className="warn">{w}</div>)}
        </div>
      </div>
      <div className={kind === 'qp' ? 'doc-holder' : 'doc-holder offscreen'} ref={qpRef} aria-hidden={kind !== 'qp'}>
        <QuestionPaperDoc spec={spec} a={a} cover={cover} />
      </div>
      <div className={kind === 'ms' ? 'doc-holder' : 'doc-holder offscreen'} ref={msRef} aria-hidden={kind !== 'ms'}>
        <MarkSchemeDoc spec={spec} a={a} cover={{ ...cover, kind: 'ms' }} />
      </div>
    </div>
  )
}
