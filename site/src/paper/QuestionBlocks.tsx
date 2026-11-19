import type { ReactNode } from 'react'
import type { Figure, Part, Question } from '../types'
import { Rich } from '../lib/rich'
import { Figures } from './Figures'

export interface Block {
  key: string
  node: ReactNode
  keepWithNext?: boolean
  /** start this block on a new page */
  pageBreakBefore?: boolean
  /** dotted answer lines that fill whatever space is left on the page (drawn by the page renderer) */
  fill?: boolean
}

export const fmtLabel = (l?: string) => {
  if (!l) return ''
  const t = l.trim()
  return /^\(.*\)$/.test(t) ? t : `(${t})`
}

/** Figures too long for the question page go into the separate source/insert booklet. */
export function isInsertFigure(f: Figure) {
  if (f.inline) return false
  if (f.type === 'passage') return true
  if (f.type === 'source' && (f.text || '').length > 900) return true
  if (f.type === 'poem' && (f.text || '').split('\n').length > 28) return true
  return false
}

function defaultLines(q: Question, p: Part) {
  if (p.lines !== undefined) return p.lines
  const long = ['history', 'english-language', 'english-literature', 'economics'].includes(q.subject)
  return long ? Math.max(2, p.marks * 2) : Math.max(1, p.marks + 1)
}

function Lines({ n }: { n: number }) {
  return <div className="ans-lines">{Array.from({ length: n }, (_, i) => <div key={i} className="dotline" />)}</div>
}

function AnswerSpace({ q, p }: { q: Question; p: Part }) {
  const space = p.space || (q.subject === 'maths' || q.subject === 'further-maths' ? 'working' : 'lines')
  const marks = <span className="marks">({p.marks})</span>
  switch (space) {
    case 'none':
      return <div className="marks-row">{marks}</div>
    case 'mcq':
      return (
        <div className="mcq">
          {(p.choices || []).map((c, i) => (
            <div className="mcq-opt" key={i}>
              <span className="mcq-box" aria-hidden="true" />
              <span className="mcq-letter">{String.fromCharCode(65 + i)}</span>
              <Rich as="span" text={c} />
            </div>
          ))}
          <div className="marks-row">{marks}</div>
        </div>
      )
    case 'working': {
      const h = Math.min(120, Math.max(12, (p.lines ?? p.marks * 2) * 9))
      return (
        <div className="working">
          <div className="work-space" style={{ height: `${h}mm` }} />
          <div className="final-ans">
            <span className="prefix"><Rich as="span" text={p.answer_prefix || ''} /></span>
            <span className="final-dots" />
            {p.answer_suffix && <span className="suffix"><Rich as="span" text={p.answer_suffix} /></span>}
          </div>
          <div className="marks-row">{marks}</div>
        </div>
      )
    }
    case 'box':
      return (
        <div>
          <div className="ans-boxed" style={{ height: `${Math.max(2, defaultLines(q, p)) * 8}mm` }} />
          <div className="marks-row">{marks}</div>
        </div>
      )
    case 'graph':
      return (
        <div>
          {/* maths supplies its own labelled grid as a figure; sciences get blank graph paper */}
          {!(q.subject === 'maths' || q.subject === 'further-maths') && <GraphPaper />}
          <div className="marks-row">{marks}</div>
        </div>
      )
    case 'table':
      return <div className="marks-row">{marks}</div>
    default:
      return (
        <div>
          {p.answer_prefix || p.answer_suffix
            ? <div className="final-ans"><span className="prefix"><Rich as="span" text={p.answer_prefix || ''} /></span><span className="final-dots" />{p.answer_suffix && <span className="suffix"><Rich as="span" text={p.answer_suffix} /></span>}</div>
            : <Lines n={defaultLines(q, p)} />}
          <div className="marks-row">{marks}</div>
        </div>
      )
  }
}

function leafBlocks(q: Question, parts: Part[], keyBase: string, parentHead: ReactNode[] = [], questionOnly = false): Block[] {
  const out: Block[] = []
  parts.forEach((p, i) => {
    const head = [
      ...parentHead,
      <div className="part-row" key={'h' + i}>
        <span className="plabel">{fmtLabel(p.label)}</span>
        <div className="ptext">
          <Rich text={p.text} />
          <Figures figs={p.figures?.filter(f => !isInsertFigure(f))} />
        </div>
      </div>,
    ]
    if (p.parts && p.parts.length) {
      out.push(...leafBlocks(q, p.parts, `${keyBase}-${i}`, [<div className={'nest'} key={'n' + i}>{head}</div>], questionOnly))
    } else {
      out.push({
        key: `${keyBase}-${i}`,
        node: (
          <div className={'qpart depth' + (parentHead.length ? '1' : '0')}>
            {head}
            {!questionOnly && <div className="ans-indent"><AnswerSpace q={q} p={p} /></div>}
          </div>
        ),
      })
    }
  })
  return out
}

export function questionBlocks(q: Question, num: number, insertRefs: Map<Figure, string>, questionOnly = false): Block[] {
  const blocks: Block[] = []
  const figs = q.figures || []
  const inline = figs.filter(f => !isInsertFigure(f))
  const refs = figs.filter(f => isInsertFigure(f)).map(f => insertRefs.get(f)).filter(Boolean)
  blocks.push({
    key: q.id + '-head',
    keepWithNext: true,
    node: (
      <div className="qhead">
        <span className="qnum">{num}</span>
        <div className="qhead-body">
          {refs.length > 0 && <Rich className="insert-ref" text={refs.join(' ')} />}
          <Rich text={q.intro} />
          <Figures figs={inline} />
        </div>
      </div>
    ),
  })
  const single = q.parts.length === 1 && !q.parts[0].label
  blocks.push(...leafBlocks(q, q.parts, q.id, [], questionOnly).map(b => ({ ...b, node: <div className={'qbody' + (single ? ' single' : '')}>{b.node}</div> })))
  blocks.push({
    key: q.id + '-total',
    node: <div className="qtotal">(Total for Question {num} is {q.marks} mark{q.marks === 1 ? '' : 's'})</div>,
  })
  return blocks
}

/** After an EITHER/OR group (English Literature, History): the candidate marks which question they chose,
 *  then writes in one shared block of lines, as in the Pearson answer booklet. */
export function choiceAnswerBlocks(key: string, nums: number[], lines: number): Block[] {
  const out: Block[] = [{
    key: key + '-choose', keepWithNext: true,
    node: (
      <div className="choose-q">
        <div>Indicate which question you are answering by marking a cross in the box <span className="mcq-box x-box">&times;</span>. If you change your mind, put a line through the box and then indicate your new question with a cross.</div>
        <div className="choose-row">{nums.map(n => <span key={n} className="choose-opt">Question {n} <span className="mcq-box" /></span>)}</div>
      </div>
    ),
  }]
  const chunk = 12
  for (let i = 0; i < lines; i += chunk) out.push({ key: `${key}-ln${i}`, node: <Lines n={Math.min(chunk, lines - i)} /> })
  return out
}

// ---------------------------------------------------------------- Further Pure (4PM1) layout
// Real 4PM1 papers print the whole question (every part, with its marks) at the top of a new page,
// then dotted lines to the foot of the page; longer questions get "Question N continued" pages of lines.

function fmPartRows(parts: Part[], depth: number): ReactNode[] {
  return parts.map((p, i) => (
    <div key={i} className={'fm-part depth' + depth}>
      <div className="part-row">
        <span className="plabel">{fmtLabel(p.label)}</span>
        <div className="ptext">
          <Rich text={p.text} />
          <Figures figs={p.figures} />
        </div>
      </div>
      {p.parts && p.parts.length
        ? <div className="fm-sub">{fmPartRows(p.parts, depth + 1)}</div>
        : <div className="marks-row fm-marks"><span className="marks">({p.marks})</span></div>}
    </div>
  ))
}

export function fmContinuedPages(marks: number) {
  return marks >= 15 ? 2 : marks >= 9 ? 1 : 0
}

export function fmQuestionBlocks(q: Question, num: number): Block[] {
  const single = q.parts.length === 1 && !q.parts[0].label
  const blocks: Block[] = [{
    key: q.id + '-head',
    pageBreakBefore: true,
    node: (
      <div className="qhead">
        <span className="qnum">{num}</span>
        <div className="qhead-body">
          <Rich text={q.intro} />
          <Figures figs={q.figures} />
          <div className={'fm-parts' + (single ? ' single' : '')}>{fmPartRows(q.parts, 0)}</div>
        </div>
      </div>
    ),
  }, { key: q.id + '-l0', fill: true, node: null }]
  for (let k = 1; k <= fmContinuedPages(q.marks); k++) {
    blocks.push({ key: q.id + '-c' + k, pageBreakBefore: true, node: <div className="fm-cont">Question {num} continued</div> })
    blocks.push({ key: q.id + '-l' + k, fill: true, node: null })
  }
  blocks.push({
    key: q.id + '-total',
    node: <div className="qtotal fm-total">(Total for Question {num} is {q.marks} mark{q.marks === 1 ? '' : 's'})</div>,
  })
  return blocks
}

export function FillLines({ px }: { px: number }) {
  const n = Math.max(0, Math.floor((px - 6) / (8.2 * 96 / 25.4)))
  return <Lines n={n} />
}

/** Blank graph paper as printed in Pearson science papers: 2 mm squares, heavier 1 cm lines, dark left and bottom edges. */
export function GraphPaper({ w = 100, h = 140 }: { w?: number; h?: number }) {
  const lines: ReactNode[] = []
  const g = '#a8a9ab'
  for (let x = 0; x <= w; x += 2) {
    const major = x % 10 === 0
    lines.push(<line key={'v' + x} x1={x} y1={0} x2={x} y2={h} stroke={g} strokeWidth={major ? 0.5 : 0.18} />)
  }
  for (let y = 0; y <= h; y += 2) {
    const major = y % 10 === 0
    lines.push(<line key={'h' + y} x1={0} y1={y} x2={w} y2={y} stroke={g} strokeWidth={major ? 0.5 : 0.18} />)
  }
  return (
    <svg className="graph-paper" viewBox={`-0.5 -0.5 ${w + 1} ${h + 1}`} style={{ width: `${w + 1}mm`, height: `${h + 1}mm` }} aria-label="graph paper">
      {lines}
      <path d={`M 0 0 L 0 ${h} L ${w} ${h}`} stroke="#222" strokeWidth={0.4} fill="none" />
    </svg>
  )
}
