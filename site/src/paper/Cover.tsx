import type { PaperSpec, Spec } from '../types'
import { Rich } from '../lib/rich'

export const DISCLAIMER = 'Practice paper — not an official exam board paper'

const fmtTime = (m: number) => {
  const h = Math.floor(m / 60), r = Math.round(m % 60)
  if (!h) return `${r} minutes`
  return `${h} hour${h > 1 ? 's' : ''}${r ? ` ${r} minutes` : ''}`
}

export interface CoverInfo {
  spec: Spec
  paper?: PaperSpec
  title: string        // e.g. "Paper 1H" or "Topic test"
  subtitle?: string    // e.g. "Higher Tier" or list of topics
  minutes: number
  marks: number
  seed: number
  kind: 'qp' | 'ms'
  sectionsNote?: string
}

function Boxes({ n }: { n: number }) {
  return <span className="digit-boxes">{Array.from({ length: n }, (_, i) => <span key={i} />)}</span>
}

export function Cover(c: CoverInfo) {
  const cam = /cambridge/i.test(c.spec.board)
  const p = c.paper
  const code = p?.paper_code || c.spec.code
  if (c.kind === 'ms') {
    return (
      <div className={'cover ms-cover' + (cam ? ' cam' : '')}>
        <div className="disclaimer-banner">{DISCLAIMER}</div>
        <div className="ms-title">Mark Scheme</div>
        <div className="ms-sub">Practice paper · {c.spec.short || c.spec.title}</div>
        <div className="ms-paper">{c.title}{c.subtitle ? ` — ${c.subtitle}` : ''}</div>
        <div className="ms-code">Modelled on {c.spec.title} ({code})</div>
        <div className="ms-meta">Maximum mark: {c.marks} · Seed {c.seed}</div>
        <div className="ms-note">
          This mark scheme is written in the style of the exam board's published mark schemes so that you can mark your
          own work the way an examiner would. It is not an official document and has no connection with the exam board.
        </div>
      </div>
    )
  }
  if (cam) {
    return (
      <div className="cover cam">
        <div className="disclaimer-banner">{DISCLAIMER}</div>
        <div className="cam-head">
          <div className="cam-brand">IGCSE practice</div>
        </div>
        <table className="cand-table">
          <tbody>
            <tr><td>CANDIDATE<br />NAME</td><td colSpan={3} className="line" /></tr>
            <tr><td>CENTRE<br />NUMBER</td><td><Boxes n={5} /></td><td>CANDIDATE<br />NUMBER</td><td><Boxes n={4} /></td></tr>
          </tbody>
        </table>
        <div className="cam-title">
          <div><b>{c.spec.title.replace(/^Cambridge\s+/i, '')}</b></div>
          <div className="cam-code"><b>{code}</b></div>
        </div>
        <div className="cam-paper"><b>{c.title}</b>{c.subtitle ? ` — ${c.subtitle}` : ''}<span className="cam-time">{fmtTime(c.minutes)}</span></div>
        {p?.materials && <div className="cam-mat">{p.materials}</div>}
        <div className="cam-box">
          <div className="cam-h">INSTRUCTIONS</div>
          <ul>{(p?.instructions || ['Answer all questions.', 'Write your answers in the spaces provided.']).map((t, i) => <li key={i}><Rich as="span" text={t} /></li>)}</ul>
          <div className="cam-h">INFORMATION</div>
          <ul>
            <li>The total mark for this paper is {c.marks}.</li>
            {(p?.information || []).filter(t => !/total mark/i.test(t)).map((t, i) => <li key={i}><Rich as="span" text={t} /></li>)}
          </ul>
        </div>
        <div className="cover-foot">{DISCLAIMER} · Seed {c.seed}</div>
      </div>
    )
  }
  return (
    <div className="cover pe">
      <div className="disclaimer-banner">{DISCLAIMER}</div>
      <div className="pe-check">Please check the examination details below before entering your candidate information</div>
      <table className="cand-table pe">
        <tbody>
          <tr><td className="lab">Candidate surname</td><td className="line" /><td className="lab">Other names</td><td className="line" /></tr>
          <tr><td className="lab">Centre Number</td><td><Boxes n={5} /></td><td className="lab">Candidate Number</td><td><Boxes n={4} /></td></tr>
        </tbody>
      </table>
      <div className="pe-quals">International GCSE</div>
      <div className="pe-subject">{c.spec.short || c.spec.title}</div>
      <div className="pe-paper">{c.title}</div>
      {c.subtitle && <div className="pe-sub">{c.subtitle}</div>}
      <div className="pe-row">
        <div className="pe-time"><span>Time</span> {fmtTime(c.minutes)}</div>
        <div className="pe-ref"><span>Paper reference</span> <b>{code}</b></div>
      </div>
      <div className="pe-row">
        <div className="pe-must"><b>You must have:</b> <Rich as="span" text={p?.materials || 'Ruler, pen, pencil, eraser.'} /></div>
        <div className="pe-total"><span>Total Marks</span><div className="tm-box" /></div>
      </div>
      <div className="pe-box">
        <div className="pe-h">Instructions</div>
        <ul>{(p?.instructions || ['Use **black** ink or ball-point pen.', 'Answer **all** questions.', 'Answer the questions in the spaces provided.']).map((t, i) => <li key={i}><Rich as="span" text={t} /></li>)}</ul>
        <div className="pe-h">Information</div>
        <ul>
          <li>The total mark for this paper is {c.marks}.</li>
          {(p?.information || ['The marks for **each** question are shown in brackets.']).filter(t => !/total mark/i.test(t)).map((t, i) => <li key={i}><Rich as="span" text={t} /></li>)}
        </ul>
        <div className="pe-h">Advice</div>
        <ul>{(p?.advice || ['Read each question carefully before you start to answer it.', 'Check your answers if you have time at the end.']).map((t, i) => <li key={i}><Rich as="span" text={t} /></li>)}</ul>
      </div>
      {c.sectionsNote && <div className="pe-secnote"><Rich as="span" text={c.sectionsNote} /></div>}
      <div className="cover-foot">{DISCLAIMER} · Seed {c.seed} · Turn over ▸</div>
    </div>
  )
}
