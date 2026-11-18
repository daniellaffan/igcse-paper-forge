// Spanish listening check without a web browser: the site's own <Speaker> component is mounted in
// jsdom (a DOM emulator in Node), its buttons are clicked, and the Web Speech API calls it makes are
// recorded. Run over EVERY listening recording in the live bank.
//   node scripts/verify/offline/.out/listening.mjs <site-url> <out.json>
import fs from 'node:fs'
import { JSDOM } from 'jsdom'
const [base, outFile] = process.argv.slice(2)
const dom = new JSDOM('<!doctype html><div id="root"></div>', { pretendToBeVisual: true })
globalThis.window = dom.window
globalThis.document = dom.window.document
globalThis.IS_REACT_ACT_ENVIRONMENT = true
const spoken = []
let cancelled = 0
const VOICES = [{ name: 'Mónica', lang: 'es-ES' }, { name: 'Jorge', lang: 'es-ES' }, { name: 'Paulina', lang: 'es-MX' }, { name: 'Daniel', lang: 'en-GB' }]
window.speechSynthesis = { getVoices: () => VOICES, speak: u => spoken.push(u), cancel: () => { cancelled++ } }
globalThis.SpeechSynthesisUtterance = window.SpeechSynthesisUtterance = class { constructor(t) { this.text = t } }

const { act } = await import('react')
const { createRoot } = await import('react-dom/client')
const { Speaker } = await import('../../../site/src/paper/Figures')

const bank = await (await fetch(base + 'data/spanish/bank.json')).json()
const qs = Array.isArray(bank) ? bank : bank.questions
const figs = []
const walk = (q, f) => { for (const g of f || []) if (g.type === 'audio') figs.push({ id: q.id, fig: g }) }
for (const q of qs) { walk(q, q.figures); for (const p of q.parts || []) walk(q, p.figures) }

const root = createRoot(document.getElementById('root'))
const fails = []
let n = 0
for (const { id, fig } of figs) {
  spoken.length = 0
  await act(async () => root.render(<Speaker key={id + n++} fig={fig} />))
  const [play, tr] = [...document.querySelectorAll('button')]
  const err = []
  if (!play || play.disabled || !/Play recording/.test(play.textContent)) err.push('no enabled play button')
  await act(async () => play.click())
  const lines = (fig.transcript || '').split('\n').map(l => l.trim()).filter(Boolean)
  if (!lines.length) err.push('empty transcript')
  if (spoken.length !== 2 * lines.length + 1) err.push(`spoke ${spoken.length} utterances, expected ${2 * lines.length + 1}`)
  if (spoken.some(u => !/^es/i.test(u.lang))) err.push('utterance not Spanish')
  if (spoken.some(u => u.voice && !/^es/i.test(u.voice.lang))) err.push('non-Spanish voice chosen')
  const said = spoken.slice(0, lines.length).map(u => u.text)
  const want = lines.map(l => (l.match(/^([^:]{1,30}):\s*(.*)$/) || [0, 0, l])[2])
  if (JSON.stringify(said) !== JSON.stringify(want)) err.push('spoken text differs from transcript')
  if (!/Stop/.test(play.textContent)) err.push('button did not switch to Stop')
  await act(async () => spoken[spoken.length - 1]?.onend?.())
  if (!/Play recording/.test(play.textContent)) err.push('button did not reset after playback ended')
  await act(async () => tr.click())
  const shown = document.querySelector('.transcript')?.textContent || ''
  if (!shown.includes(want[0].slice(0, 15))) err.push('show-transcript did not show the transcript')
  if (err.length) fails.push({ id, err })
}
await act(async () => root.unmount())
const res = { recordings: figs.length, questions: new Set(figs.map(f => f.id)).size, passed: figs.length - fails.length, fails: fails.slice(0, 50),
  sample: figs[0] && { id: figs[0].id, lang: figs[0].fig.lang || 'es-ES', transcript: figs[0].fig.transcript } }
fs.writeFileSync(outFile, JSON.stringify(res, null, 1))
console.log(`listening: ${res.passed}/${res.recordings} recordings in ${res.questions} questions passed`)
if (fails.length) { console.log(JSON.stringify(fails.slice(0, 5), null, 1)); process.exit(1) }
process.exit(0)
