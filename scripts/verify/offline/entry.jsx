// Build both documents for a topic test and a full paper per subject, from the LIVE site's data,
// using the site's own assembly code and paper components (server-side render, no browser).
import fs from 'node:fs'
import path from 'node:path'
import { renderToStaticMarkup } from 'react-dom/server'
import { assemble } from '../../../site/src/lib/assemble'
import { encodeConfig } from '../../../site/src/lib/rng'
import { MarkSchemeDoc, QuestionPaperDoc } from '../../../site/src/paper/Documents'
import { FigureView } from '../../../site/src/paper/Figures'
import { MATH } from './katex-shim.mjs'

const [base, out] = process.argv.slice(2)
const get = async p => { const r = await fetch(base + 'data/' + p); if (!r.ok) throw new Error(p + ' ' + r.status); return r.json() }
const index = await get('index.json')
const summary = {}
for (const s of index) {
  const spec = await get(`${s.subject}/spec.json`)
  const bank = await get(`${s.subject}/bank.json`)
  const paper = spec.papers[0]
  const topics = spec.topics.filter(t => !t.papers || t.papers.includes(paper.id)).slice(0, 2)
  const seedBase = [...s.subject].reduce((a, c) => a + c.charCodeAt(0), 0)
  const cfgs = {
    'topic-test': { subject: s.subject, mode: 'topic', paper: paper.id, subtopics: topics.flatMap(t => t.subtopics.map(x => x.id)), qtypes: [], length: { by: 'marks', value: 30 }, diff: [3, 4, 3], calculator: 'any', options: [], seed: 100000 + seedBase },
    'full-paper': { subject: s.subject, mode: 'full', paper: paper.id, subtopics: [], qtypes: [], length: { by: 'marks', value: 30 }, diff: [3, 4, 3], calculator: 'any', options: [], seed: 200000 + seedBase },
  }
  const dir = path.join(out, s.subject, 'build')
  fs.mkdirSync(dir, { recursive: true })
  summary[s.subject] = {}
  for (const [stem, cfg] of Object.entries(cfgs)) {
    MATH.clear()
    const a = assemble(bank, spec, cfg, new Set())
    const ids = a.sections.map(x => x.questions.map(q => q.id))
    const names = [...new Set(a.sections.flatMap(x => x.questions.map(q => spec.topics.find(t => t.id === q.topic)?.title).filter(Boolean)))]
    const cover = {
      spec, paper: a.paper, title: cfg.mode === 'full' && a.paper ? a.paper.name : 'Topic test',
      subtitle: cfg.mode === 'full' ? undefined : (names.length > 4 ? `${names.slice(0, 4).join(', ')} and ${names.length - 4} more` : names.join(', ')),
      minutes: a.minutes, marks: a.totalMarks, seed: cfg.seed, kind: 'qp',
    }
    const qp = renderToStaticMarkup(<QuestionPaperDoc spec={spec} a={a} cover={cover} />)
    const ms = renderToStaticMarkup(<MarkSchemeDoc spec={spec} a={a} cover={cover} />)
    fs.writeFileSync(path.join(dir, `${stem}-qp.html`), qp)
    fs.writeFileSync(path.join(dir, `${stem}-ms.html`), ms)
    // formula sheet / periodic table page: the site loads it in an effect, which a server render skips
    const refId = a.paper?.reference_sheet || (spec.papers.length === 1 ? spec.papers[0].reference_sheet : undefined)
    const refFile = path.join(dir, `${stem}-ref.html`)
    if (refId) {
      const ref = await get(`reference/${refId}.json`)
      fs.writeFileSync(refFile, renderToStaticMarkup(
        <div className="ref-sheet"><div className="ref-title">{ref.title}</div>
          {ref.blocks.map((b, i) => <FigureView key={i} fig={b} />)}
          <div className="ref-foot">Do not write on this page. Answer all questions.</div></div>))
    } else if (fs.existsSync(refFile)) fs.rmSync(refFile)
    for (const [n, m] of MATH) fs.writeFileSync(path.join(dir, `${stem}-${n}`), m.svg)
    const qs = a.sections.flatMap(x => x.questions)
    summary[s.subject][stem] = {
      url: `${base}#/s/${s.subject}/paper?c=${encodeConfig(cfg)}&q=${encodeConfig(ids)}`,
      questions: qs.length, marks: a.totalMarks, target: a.targetMarks, minutes: a.minutes, warnings: a.warnings,
      formulas: MATH.size, diagrams: qs.reduce((n, q) => n + JSON.stringify(q).split('"type":"svg"').length - 1, 0),
      audio: qs.reduce((n, q) => n + JSON.stringify(q).split('"type":"audio"').length - 1, 0),
      either_or: a.sections.reduce((n, x) => n + Object.keys(x.alts || {}).length, 0),
      sections: a.sections.map(x => x.title).filter(Boolean),
      reference_sheet: refId || null,
    }
    console.log(s.subject, stem, qs.length, 'questions', a.totalMarks, 'marks', MATH.size, 'formulas')
  }
}
fs.writeFileSync(path.join(out, 'offline-build.json'), JSON.stringify(summary, null, 1))
