import { useEffect, useMemo, useState, type ReactNode } from 'react'
import type { Figure, Question, ReferenceSheet, Spec } from '../types'
import type { Assembled } from '../lib/assemble'
import { loadReference } from '../lib/data'
import { Rich } from '../lib/rich'
import { Cover, DISCLAIMER, type CoverInfo } from './Cover'
import { FigureView, Figures } from './Figures'
import { CONTENT_H_MM, Page, usePagination } from './Paginator'
import { fmtLabel, isInsertFigure, questionBlocks, type Block } from './QuestionBlocks'

function Footer({ n, last, code, seed }: { n: number; total: number; last: boolean; code: string; seed: number }) {
  return (
    <>
      <span className="pf-left">{DISCLAIMER} · {code} · seed {seed}</span>
      <span className="pf-mid">{n}</span>
      <span className="pf-right">{last ? '' : 'Turn over ▸'}</span>
    </>
  )
}

function useReference(id?: string) {
  const [ref, setRef] = useState<ReferenceSheet | null>(null)
  useEffect(() => {
    if (!id) { setRef(null); return }
    loadReference(id).then(setRef).catch(() => setRef(null))
  }, [id])
  return ref
}

// ---------------------------------------------------------------- question paper

export function QuestionPaperDoc({ spec, a, cover }: { spec: Spec; a: Assembled; cover: CoverInfo }) {
  const ref = useReference(a.paper?.reference_sheet || (spec.papers.length === 1 ? spec.papers[0].reference_sheet : undefined))
  const code = a.paper?.paper_code || spec.code

  const { blocks, insertBlocks } = useMemo(() => {
    const insertRefs = new Map<Figure, string>()
    const insertBlocks: Block[] = []
    let num = 0
    const blocks: Block[] = []
    a.sections.forEach((sec, si) => {
      if (sec.title) {
        blocks.push({
          key: 'sec' + si, keepWithNext: true,
          node: <div className="sec-head"><div className="sec-title">{sec.title}</div>{sec.instructions && <Rich className="sec-instr" text={sec.instructions} />}</div>,
        })
      } else if (si === 0) {
        blocks.push({ key: 'all', keepWithNext: true, node: <div className="answer-all">Answer ALL questions. Write your answers in the spaces provided.</div> })
      }
      sec.questions.forEach(q => {
        num++
        const figs = (q.figures || []).filter(isInsertFigure)
        figs.forEach((f, k) => {
          const label = f.label || f.title || `Text for Question ${num}${figs.length > 1 ? ' ' + String.fromCharCode(65 + k) : ''}`
          insertRefs.set(f, `Read **${label.replace(/\*/g, '')}** in the Insert before answering this question.`)
          // split long passages into paragraph blocks so they can flow across pages
          const paras = (f.text || '').split(/\n\s*\n/)
          if (paras.length > 3 && f.type !== 'poem') {
            paras.forEach((para, pi) => insertBlocks.push({
              key: `ins-${q.id}-${k}-${pi}`,
              keepWithNext: pi === 0,
              node: <FigureView fig={{ ...f, title: pi === 0 ? (f.title || f.label) : undefined, label: pi === 0 ? f.label : undefined, provenance: pi === 0 ? f.provenance : undefined, text: para }} />,
            }))
          } else {
            insertBlocks.push({ key: `ins-${q.id}-${k}`, node: <FigureView fig={f} /> })
          }
        })
        const alt = sec.alts?.[q.id]
        if (alt) blocks.push({ key: q.id + '-alt', keepWithNext: true, node: <div className="either-or">{alt}</div> })
        blocks.push(...questionBlocks(q, num, insertRefs))
      })
    })
    blocks.push({ key: 'end', node: <div className="paper-end"><div>TOTAL FOR PAPER IS {a.totalMarks} MARKS</div><div className="end-small">END OF PAPER</div></div> })
    return { blocks, insertBlocks }
  }, [a])

  const qp = usePagination(blocks, 'page-content', [blocks])
  const ins = usePagination(insertBlocks, 'page-content', [insertBlocks], CONTENT_H_MM - 16)
  const total = qp.pages ? qp.pages.length : 0
  const refPages = ref ? 1 : 0
  const before = 1 + refPages
  return (
    <div className="doc">
      {qp.measure}{ins.measure}
      <Page side={false} className="cover-page"><Cover {...cover} /></Page>
      {ref && (
        <Page footer={<Footer n={2} total={0} last={false} code={code} seed={cover.seed} />}>
          <div className="ref-sheet">
            <div className="ref-title">{ref.title}</div>
            {ref.blocks.map((b, i) => <FigureView key={i} fig={b} />)}
            <div className="ref-foot">Do not write on this page. Answer all questions.</div>
          </div>
        </Page>
      )}
      {qp.pages?.map((pg, i) => (
        <Page key={i} footer={<Footer n={before + i + 1} total={total} last={i === total - 1 && !insertBlocks.length} code={code} seed={cover.seed} />}>
          <div className="page-content">{pg.map(bi => <div key={blocks[bi].key} className="blk">{blocks[bi].node}</div>)}</div>
        </Page>
      ))}
      {ins.pages?.map((pg, i) => (
        <Page key={'i' + i} side={false} className="insert-page" footer={<Footer n={i + 1} total={0} last={i === (ins.pages?.length || 0) - 1} code={code + ' Insert'} seed={cover.seed} />}>
          {i === 0 && <div className="insert-head"><div className="ins-title">Insert</div><div>{spec.short || spec.title} · {cover.title}</div><div className="muted">Do not return this Insert with the question paper.</div></div>}
          <div className="page-content">{pg.map(bi => <div key={insertBlocks[bi].key} className="blk">{insertBlocks[bi].node}</div>)}</div>
        </Page>
      ))}
    </div>
  )
}

// ---------------------------------------------------------------- mark scheme

const GUIDANCE: Record<string, string[]> = {
  maths: [
    'All candidates must receive the same treatment. Mark the first answer to each part unless the candidate clearly crosses it out.',
    '**M** marks: method marks, awarded for a correct method that could lead to a correct answer.',
    '**A** marks: accuracy marks, which depend on the preceding M mark(s). **B** marks: unconditional accuracy marks, independent of method.',
    'Abbreviations: **cao** correct answer only · **ft** follow through · **oe** or equivalent · **isw** ignore subsequent working · **SC** special case · **dep** dependent on the previous mark · **awrt** answers which round to.',
    'With working: if the answer is wrong, mark the working. If there is a choice of methods shown, mark the method that leads to the answer on the answer line.',
    'Without working: a correct answer with no working gains full marks unless the question says "show your working" or "show that".',
  ],
  science: [
    'Mark the first answer to each part. Credit any answer that is correct even if it is not listed, if it shows the required understanding.',
    '**/** separates alternative acceptable answers. Words in **( )** are not needed for the mark. **ecf** error carried forward · **owtte** or words to that effect · **ignore** neither credit nor penalise · **reject** do not award the mark if this is given.',
    'For calculations, award full marks for a correct final answer with correct unit unless working is required. Award method marks for correct working with a wrong answer.',
    'For extended (levels-marked) answers, decide the level from the descriptor that best fits the whole answer, then the mark within the level.',
  ],
  levels: [
    'Mark the answer as a whole: first decide which level descriptor best fits the response, then decide the mark within that level.',
    'Indicative content shows the kind of points a candidate might make. It is not a checklist and it is not exhaustive: examiners must credit other valid points.',
    'An answer can reach a level without covering every bullet of the indicative content. Weigh the quality of the argument as well as the range of points.',
  ],
  spanish: [
    'Accept answers in the language required by the question. Minor spelling errors are accepted if the meaning is clear and unambiguous.',
    '**/** separates alternative answers. Words in **( )** are not needed. Answers in **[ ]** are not accepted on their own.',
    'For writing tasks, use the assessment grids: award marks for communication of the required information first, then for language.',
  ],
}

function guidanceFor(subject: string): string[] {
  if (subject === 'maths' || subject === 'further-maths') return GUIDANCE.maths
  if (['physics', 'chemistry', 'biology'].includes(subject)) return GUIDANCE.science
  if (subject === 'spanish') return GUIDANCE.spanish
  return [...(subject === 'economics' ? GUIDANCE.science.slice(0, 2) : []), ...GUIDANCE.levels]
}

function msColumns(subject: string) {
  if (subject === 'maths' || subject === 'further-maths') return { cols: ['Question', 'Working / Answer', 'Mark', 'Notes'], w: ['14%', '44%', '12%', '30%'], order: ['q', 'a', 'm', 'n'] }
  if (subject === 'spanish') return { cols: ['Question', 'Answer', 'Marks', 'Guidance'], w: ['13%', '47%', '10%', '30%'], order: ['q', 'a', 'm', 'n'] }
  return { cols: ['Question number', 'Answer', 'Notes', 'Marks'], w: ['14%', '50%', '26%', '10%'], order: ['q', 'a', 'n', 'm'] }
}

function msRowsFor(q: Question, num: number, cols: ReturnType<typeof msColumns>): Block[] {
  const out: Block[] = []
  const cg = <colgroup>{cols.w.map((w, i) => <col key={i} style={{ width: w }} />)}</colgroup>
  const rows = q.markscheme.rows
  const audio = (q.figures || []).filter(f => f.type === 'audio')
  if (audio.length) {
    out.push({ key: q.id + '-tr', keepWithNext: true, node: <div className="ms-transcript"><b>Question {num} — transcript</b><Figures figs={audio} inMarkScheme /></div> })
  }
  rows.forEach((r, i) => {
    const cells: Record<string, ReactNode> = {
      q: <b>{i === 0 || rows[i - 1].part !== r.part ? `${num}${r.part ? fmtLabel(r.part) : ''}` : ''}</b>,
      a: <Rich text={r.answer} />,
      m: <Rich as="span" text={r.marks} />,
      n: <Rich text={r.notes} />,
    }
    out.push({
      key: `${q.id}-r${i}`, keepWithNext: i === 0,
      node: <table className={'ms-table' + (i > 0 ? ' cont' : '')}>{cg}<tbody><tr>{cols.order.map(k => <td key={k} className={'c-' + k}>{cells[k]}</td>)}</tr></tbody></table>,
    })
  })
  ;(q.markscheme.levels || []).forEach((lv, li) => {
    out.push({
      key: `${q.id}-lv${li}`,
      node: (
        <div className="lv-block">
          <div className="lv-head"><b>{num}{lv.part ? fmtLabel(lv.part) : ''}</b> {lv.title || 'Levels-based mark scheme'}{lv.ao_split ? <span className="muted"> · {lv.ao_split}</span> : null}</div>
          {lv.indicative && lv.indicative.length > 0 && (
            <div className="lv-ind"><b>Indicative content</b><ul>{lv.indicative.map((t, i) => <li key={i}><Rich as="span" text={t} /></li>)}</ul></div>
          )}
          <table className="lv-table">
            <colgroup><col style={{ width: '12%' }} /><col style={{ width: '12%' }} /><col /></colgroup>
            <thead><tr><th>Level</th><th>Mark</th><th>Descriptor</th></tr></thead>
            <tbody>{lv.grid.map((g, i) => <tr key={i}><td>{g.level}</td><td>{g.marks}</td><td><Rich text={g.descriptor} /></td></tr>)}</tbody>
          </table>
          <div className="lv-credit"><Rich as="span" text={lv.credit_note} /></div>
        </div>
      ),
    })
  })
  if (q.markscheme.general) out.push({ key: q.id + '-gen', node: <div className="ms-general"><Rich text={q.markscheme.general} /></div> })
  out.push({ key: q.id + '-tot', node: <div className="ms-qtotal">Total for Question {num}: {q.marks} mark{q.marks === 1 ? '' : 's'}</div> })
  return out
}

export function MarkSchemeDoc({ spec, a, cover }: { spec: Spec; a: Assembled; cover: CoverInfo }) {
  const cols = useMemo(() => msColumns(spec.subject), [spec.subject])
  const code = a.paper?.paper_code || spec.code
  const blocks = useMemo(() => {
    const b: Block[] = [{
      key: 'guid',
      node: <div className="ms-guidance"><div className="ms-g-title">General marking guidance</div><ul>{guidanceFor(spec.subject).map((t, i) => <li key={i}><Rich as="span" text={t} /></li>)}</ul></div>,
    }]
    let num = 0
    a.sections.forEach((sec, si) => {
      if (sec.title) b.push({ key: 'msec' + si, keepWithNext: true, node: <div className="sec-head"><div className="sec-title">{sec.title}</div></div> })
      sec.questions.forEach(q => { num++; b.push(...msRowsFor(q, num, cols)) })
    })
    b.push({ key: 'msend', node: <div className="paper-end"><div>TOTAL FOR PAPER: {a.totalMarks} MARKS</div></div> })
    return b
  }, [a, spec.subject, cols])
  const ms = usePagination(blocks, 'page-content ms', [blocks], CONTENT_H_MM - 10)
  const head = (
    <table className="ms-table ms-head"><colgroup>{cols.w.map((w, i) => <col key={i} style={{ width: w }} />)}</colgroup>
      <thead><tr>{cols.cols.map(c => <th key={c}>{c}</th>)}</tr></thead></table>
  )
  return (
    <div className="doc">
      {ms.measure}
      <Page side={false} className="cover-page"><Cover {...cover} kind="ms" /></Page>
      {ms.pages?.map((pg, i) => (
        <Page key={i} side={false} footer={<Footer n={i + 2} total={0} last={i === (ms.pages?.length || 0) - 1} code={code + ' mark scheme'} seed={cover.seed} />}>
          {head}
          <div className="page-content ms">{pg.map(bi => <div key={blocks[bi].key} className="blk">{blocks[bi].node}</div>)}</div>
        </Page>
      ))}
    </div>
  )
}
