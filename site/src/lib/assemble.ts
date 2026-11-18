import type { Band, PaperSpec, Question, Spec, TestConfig } from '../types'
import { mulberry32, shuffle } from './rng'

export interface AssembledSection { id: string; title: string; instructions?: string; questions: Question[]; marks?: number; alts?: Record<string, string> }
export interface Assembled {
  sections: AssembledSection[]
  totalMarks: number
  targetMarks: number
  minutes: number
  paper?: PaperSpec
  warnings: string[]
}

const BANDS: Band[] = ['1-3', '4-6', '7-9']
const bandIdx = (b: Band) => BANDS.indexOf(b)

export function marksPerMinute(spec: Spec, paperId: string): number {
  const p = spec.papers.find(x => x.id === paperId) || spec.papers[0]
  return p.marks / p.minutes
}

export function filterPool(bank: Question[], spec: Spec, cfg: TestConfig): Question[] {
  const subs = new Set(cfg.subtopics)
  const types = new Set(cfg.qtypes)
  const opts = new Set(cfg.options || [])
  return bank.filter(q => {
    if (cfg.paper && !q.paper.includes(cfg.paper)) return false
    if (subs.size && !subs.has(q.subtopic)) return false
    if (types.size && !types.has(q.qtype)) return false
    if (opts.size && q.option && !opts.has(q.option)) return false
    if (cfg.calculator === 'calc' && q.calculator === false) return false
    if (cfg.calculator === 'noncalc' && q.calculator === true) return false
    return true
  })
}

/** Topic test: hit the mark target with a balanced spread of subtopics and the requested difficulty mix. */
function assembleTopic(pool: Question[], target: number, cfg: TestConfig, seen: Set<string>): { qs: Question[]; warn: string[] } {
  const rnd = mulberry32(cfg.seed)
  const warn: string[] = []
  // unseen first, then seen, each shuffled
  const fresh = shuffle(pool.filter(q => !seen.has(q.id)), rnd)
  const old = shuffle(pool.filter(q => seen.has(q.id)), rnd)
  if (fresh.length < pool.length && fresh.reduce((a, q) => a + q.marks, 0) < target)
    warn.push('You have seen most questions in this selection, so some repeats were used. Reset "seen" history on the builder to start fresh.')
  const ordered = [...fresh, ...old]
  const wsum = cfg.diff[0] + cfg.diff[1] + cfg.diff[2] || 1
  const wantBand = cfg.diff.map(w => (w / wsum) * target)
  const gotBand = [0, 0, 0]
  const bySub = new Map<string, number>()
  const chosen: Question[] = []
  const used = new Set<string>()
  const usedTemplate = new Map<string, number>()
  let total = 0
  for (let guard = 0; guard < 400 && total < target; guard++) {
    const remaining = target - total
    // band with largest deficit
    const deficits = wantBand.map((w, i) => w - gotBand[i])
    const order = [0, 1, 2].sort((a, b) => deficits[b] - deficits[a])
    let pick: Question | undefined
    for (const bi of order) {
      if (cfg.diff[bi] === 0 && order.some(o => cfg.diff[o] > 0)) continue
      const cands = ordered.filter(q => !used.has(q.id) && bandIdx(q.difficulty) === bi && q.marks <= remaining)
      if (!cands.length) continue
      // prefer least-used subtopic and template
      cands.sort((a, b) => ((bySub.get(a.subtopic) || 0) * 3 + (usedTemplate.get(a.template || '') || 0) * 2) -
        ((bySub.get(b.subtopic) || 0) * 3 + (usedTemplate.get(b.template || '') || 0) * 2))
      const best = cands.slice(0, Math.min(6, cands.length))
      pick = best[Math.floor(rnd() * best.length)]
      break
    }
    if (!pick) {
      const any = ordered.filter(q => !used.has(q.id) && q.marks <= remaining)
      if (!any.length) break
      pick = any[0]
    }
    used.add(pick.id)
    chosen.push(pick)
    total += pick.marks
    gotBand[bandIdx(pick.difficulty)] += pick.marks
    bySub.set(pick.subtopic, (bySub.get(pick.subtopic) || 0) + 1)
    usedTemplate.set(pick.template || '', (usedTemplate.get(pick.template || '') || 0) + 1)
  }
  if (total < target) warn.push(`Only ${total} of the ${target} marks could be filled from this selection — tick more sub-topics or question types for a longer test.`)
  // ramp: easy → hard, then smaller → larger inside a band
  chosen.sort((a, b) => bandIdx(a.difficulty) - bandIdx(b.difficulty) || a.marks - b.marks)
  return { qs: chosen, warn }
}

/** Full paper in the real structure. */
function assembleFull(bank: Question[], spec: Spec, cfg: TestConfig, seen: Set<string>): Assembled {
  const paper = spec.papers.find(p => p.id === cfg.paper) || spec.papers[0]
  const rnd = mulberry32(cfg.seed)
  const warnings: string[] = []
  const inPaper = bank.filter(q => q.paper.includes(paper.id))
  const used = new Set<string>()
  const sections: AssembledSection[] = []
  const pickFrom = (cands: Question[]) => {
    const fresh = cands.filter(q => !used.has(q.id) && !seen.has(q.id))
    const list = fresh.length ? fresh : cands.filter(q => !used.has(q.id))
    if (!list.length) return undefined
    return list[Math.floor(rnd() * list.length)]
  }
  const hasSlots = (paper.sections || []).some(s => s.slots && s.slots.length)
  if (hasSlots) {
    for (const sec of paper.sections || []) {
      if (cfg.options && cfg.options.length && sec.slots?.every(sl => sl.option && !cfg.options!.includes(sl.option))) continue
      const qs: Question[] = []
      const alts: Record<string, string> = {}
      for (const sl of sec.slots || []) {
        if (sl.option && cfg.options && cfg.options.length && !cfg.options.includes(sl.option)) continue
        for (let k = 0; k < (sl.choice || sl.count || 1); k++) {
          let cands = inPaper.filter(q =>
            (!sl.qtypes || sl.qtypes.includes(q.qtype)) &&
            (!sl.option || q.option === sl.option) &&
            (!sl.topics || sl.topics.includes(q.topic)) &&
            (sec.id ? !q.section || q.section === sec.id : true))
          if (sl.marks) {
            const exact = cands.filter(q => q.marks === sl.marks)
            if (exact.length) cands = exact
          }
          const q = pickFrom(cands)
          if (q) {
            used.add(q.id); qs.push(q)
            // "answer one of these": either a slot with choice>1, or slots labelled (EITHER)/(OR)
            const w = sl.choice && sl.choice > 1 ? (k === 0 ? 'EITHER' : 'OR') : /\bEITHER\b/.test(sl.label || '') ? 'EITHER' : /\bOR\b/.test(sl.label || '') ? 'OR' : ''
            if (w) alts[q.id] = w
          } else warnings.push(`No question available for ${sec.title} ${sl.label || ''}`)
        }
      }
      sections.push({ id: sec.id, title: sec.title, instructions: sec.instructions, questions: qs, marks: sec.marks, alts: Object.keys(alts).length ? alts : undefined })
    }
  } else {
    // mixed-topic paper (maths, sciences): fill the paper's marks, spread across topics, ramped
    const target = paper.marks
    const topics = shuffle([...new Set(inPaper.map(q => q.topic))], rnd)
    const chosen: Question[] = []
    let total = 0
    // first pass: one question per topic so coverage is broad, preferring 4–12 mark structured questions
    const pool = shuffle(inPaper, rnd)
    const bandPlan = (i: number, n: number): Band => (i < n * 0.3 ? '1-3' : i < n * 0.75 ? '4-6' : '7-9')
    const estN = Math.max(8, Math.round(target / Math.max(3, avg(pool.map(q => q.marks)))))
    let i = 0
    for (let round = 0; round < 6 && total < target; round++) {
      for (const t of topics) {
        if (total >= target) break
        const want = bandPlan(i, estN)
        const remaining = target - total
        let cands = pool.filter(q => q.topic === t && !used.has(q.id) && q.marks <= remaining && q.difficulty === want)
        if (!cands.length) cands = pool.filter(q => q.topic === t && !used.has(q.id) && q.marks <= remaining)
        const q = pickFrom(cands)
        if (!q) continue
        used.add(q.id); chosen.push(q); total += q.marks; i++
      }
    }
    // top-up with any small question
    while (total < target) {
      const q = pickFrom(pool.filter(x => !used.has(x.id) && x.marks <= target - total))
      if (!q) break
      used.add(q.id); chosen.push(q); total += q.marks
    }
    if (total !== target) warnings.push(`Paper totals ${total} marks (real paper: ${target}).`)
    chosen.sort((a, b) => bandIdx(a.difficulty) - bandIdx(b.difficulty) || rnd() - 0.5)
    sections.push({ id: '', title: '', questions: chosen })
  }
  // a section with EITHER/OR alternatives only counts the marks a candidate actually answers
  const totalMarks = sections.reduce((a, s) => {
    const sum = s.questions.reduce((b, q) => b + q.marks, 0)
    return a + (s.alts && s.marks ? Math.min(sum, s.marks) : sum)
  }, 0)
  return { sections, totalMarks, targetMarks: paper.marks, minutes: paper.minutes, paper, warnings }
}

const avg = (xs: number[]) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : 0)

export function assemble(bank: Question[], spec: Spec, cfg: TestConfig, seen: Set<string>): Assembled {
  if (cfg.mode === 'full') return assembleFull(bank, spec, cfg, seen)
  const paper = spec.papers.find(p => p.id === cfg.paper)
  const mpm = marksPerMinute(spec, cfg.paper || spec.papers[0].id)
  const target = cfg.length.by === 'marks' ? cfg.length.value : Math.max(1, Math.round(cfg.length.value * mpm))
  const pool = filterPool(bank, spec, cfg)
  const { qs, warn } = assembleTopic(pool, target, cfg, seen)
  // group into sections when the subject's questions carry sections/options (e.g. History options)
  const groups = new Map<string, Question[]>()
  for (const q of qs) {
    const k = q.option || q.section || ''
    if (!groups.has(k)) groups.set(k, [])
    groups.get(k)!.push(q)
  }
  const optName = (k: string) => spec.options?.find(o => o.id === k)?.name || ''
  const sections = [...groups.entries()].map(([k, list]) => ({ id: k, title: optName(k), questions: list }))
  const totalMarks = qs.reduce((a, q) => a + q.marks, 0)
  return {
    sections, totalMarks, targetMarks: target,
    minutes: Math.round(totalMarks / mpm), paper, warnings: warn,
  }
}

/** Re-derive the EITHER/OR labels by walking the section's slots in order. */
function altsFor(sec: NonNullable<PaperSpec['sections']>[number], qs: Question[], cfg: TestConfig) {
  const alts: Record<string, string> = {}
  let i = 0
  for (const sl of sec.slots || []) {
    if (sl.option && cfg.options && cfg.options.length && !cfg.options.includes(sl.option)) continue
    const n = sl.choice || sl.count || 1
    for (let k = 0; k < n && i < qs.length; k++, i++) {
      const w = sl.choice && sl.choice > 1 ? (k === 0 ? 'EITHER' : 'OR') : /\bEITHER\b/.test(sl.label || '') ? 'EITHER' : /\bOR\b/.test(sl.label || '') ? 'OR' : ''
      if (w) alts[qs[i].id] = w
    }
  }
  return Object.keys(alts).length ? alts : undefined
}

/** Rebuild an exact paper from question ids carried in the URL. */
export function fromIds(bank: Question[], spec: Spec, cfg: TestConfig, ids: string[][]): Assembled {
  const byId = new Map(bank.map(q => [q.id, q]))
  const paper = spec.papers.find(p => p.id === cfg.paper)
  const fullSecs = cfg.mode === 'full' ? (paper?.sections || []).filter(s => s.slots?.length) : []
  const sections: AssembledSection[] = ids.map((list, i) => {
    const qs = list.map(id => byId.get(id)).filter(Boolean) as Question[]
    const first = qs[0]
    const sec = fullSecs.length ? fullSecs.find(s => s.id === (first?.section || '')) || fullSecs[i] : undefined
    const k = first?.option || first?.section || ''
    return {
      id: sec?.id || k,
      title: sec?.title || spec.options?.find(o => o.id === k)?.name || '',
      instructions: sec?.instructions,
      questions: qs,
      marks: sec?.marks,
      alts: sec ? altsFor(sec, qs, cfg) : undefined,
    }
  })
  // a section with EITHER/OR alternatives only counts the marks a candidate actually answers
  const totalMarks = sections.reduce((a, s) => {
    const sum = s.questions.reduce((b, q) => b + q.marks, 0)
    return a + (s.alts && s.marks ? Math.min(sum, s.marks) : sum)
  }, 0)
  const mpm = marksPerMinute(spec, cfg.paper || spec.papers[0].id)
  return {
    sections, totalMarks,
    targetMarks: cfg.mode === 'full' && paper ? paper.marks : totalMarks,
    minutes: cfg.mode === 'full' && paper ? paper.minutes : Math.round(totalMarks / mpm),
    paper, warnings: [],
  }
}
