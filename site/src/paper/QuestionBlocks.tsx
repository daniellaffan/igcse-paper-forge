import type { ReactNode } from 'react'
import type { Figure, Part, Question } from '../types'
import { Rich } from '../lib/rich'
import { Figures } from './Figures'

export interface Block { key: string; node: ReactNode; keepWithNext?: boolean }

export const fmtLabel = (l?: string) => {
  if (!l) return ''
  const t = l.trim()
  return /^\(.*\)$/.test(t) ? t : `(${t})`
}

/** Figures too long for the question page go into the separate source/insert booklet. */
export function isInsertFigure(f: Figure) {
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
          <div className="graph-grid" />
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

function leafBlocks(q: Question, parts: Part[], keyBase: string, parentHead: ReactNode[] = []): Block[] {
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
      out.push(...leafBlocks(q, p.parts, `${keyBase}-${i}`, [<div className={'nest'} key={'n' + i}>{head}</div>]))
    } else {
      out.push({
        key: `${keyBase}-${i}`,
        node: (
          <div className={'qpart depth' + (parentHead.length ? '1' : '0')}>
            {head}
            <div className="ans-indent"><AnswerSpace q={q} p={p} /></div>
          </div>
        ),
      })
    }
  })
  return out
}

export function questionBlocks(q: Question, num: number, insertRefs: Map<Figure, string>): Block[] {
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
  blocks.push(...leafBlocks(q, q.parts, q.id).map(b => ({ ...b, node: <div className={'qbody' + (single ? ' single' : '')}>{b.node}</div> })))
  blocks.push({
    key: q.id + '-total',
    node: <div className="qtotal">(Total for Question {num} is {q.marks} mark{q.marks === 1 ? '' : 's'})</div>,
  })
  return blocks
}
