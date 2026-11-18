// End-to-end check of the site in headless Chrome.
//   node scripts/verify/verify.mjs <baseUrl> <outDir> [subject ...]
// For each subject: opens the checklist, builds one topic test and one
// full-structure paper through the builder UI, screenshots them, exports both
// PDFs with the site's own buttons, and checks KaTeX / SVG / Spanish audio.
import puppeteer from 'puppeteer-core'
import fs from 'node:fs'
import path from 'node:path'

const [base = 'http://localhost:5199/', out = 'docs/verification', ...only] = process.argv.slice(2)
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
const sleep = ms => new Promise(r => setTimeout(r, ms))

async function waitPages(page, sel = '.doc-holder:not(.offscreen) .page') {
  for (let i = 0; i < 60; i++) {
    const n = await page.$$eval(sel, e => e.length).catch(() => 0)
    const pending = await page.$$eval('.measure', e => e.length).catch(() => 1)
    if (n > 1 && pending === 0) return n
    await sleep(500)
  }
  throw new Error('pages did not render')
}

async function exportBoth(page, cdp, dir, stem) {
  const files = {}
  for (const [label, kind] of [['Question paper PDF', 'question-paper'], ['Mark scheme PDF', 'mark-scheme']]) {
    const before = new Set(fs.readdirSync(dir))
    await page.evaluate(l => [...document.querySelectorAll('button')].find(b => b.textContent.includes(l)).click(), label)
    let got
    for (let i = 0; i < 240 && !got; i++) {
      await sleep(500)
      got = fs.readdirSync(dir).find(f => !before.has(f) && f.endsWith('.pdf'))
    }
    if (!got) throw new Error('no PDF for ' + kind)
    await sleep(500)
    const dest = `${stem}-${kind}.pdf`
    fs.renameSync(path.join(dir, got), path.join(dir, dest))
    files[kind] = dest
  }
  return files
}

async function build(page, base, subject, mode, paperIdx) {
  await page.goto(`${base}#/s/${subject}/build`, { waitUntil: 'networkidle0' })
  await page.waitForFunction(() => [...document.querySelectorAll('button')].some(b => b.textContent === 'Make my paper'), { timeout: 60000 })
  await page.evaluate((mode) => {
    const radios = [...document.querySelectorAll('input[name=mode]')]
    radios[mode === 'full' ? 1 : 0].click()
  }, mode)
  await sleep(300)
  await page.evaluate((idx) => {
    const sel = document.querySelector('select[aria-label=Paper]')
    const opts = [...sel.options].filter(o => o.value)
    const v = opts[idx % opts.length].value
    const setter = Object.getOwnPropertyDescriptor(HTMLSelectElement.prototype, 'value').set
    setter.call(sel, v)
    sel.dispatchEvent(new Event('change', { bubbles: true }))
  }, paperIdx)
  await sleep(300)
  if (mode === 'topic') {
    await page.evaluate(() => {
      const sel = document.querySelector('select[aria-label="Length measured by"]')
      const setter = Object.getOwnPropertyDescriptor(HTMLSelectElement.prototype, 'value').set
      setter.call(sel, 'marks'); sel.dispatchEvent(new Event('change', { bubbles: true }))
      const inp = document.querySelector('input[aria-label="Length value"]')
      const iset = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set
      iset.call(inp, '30'); inp.dispatchEvent(new Event('input', { bubbles: true }))
    })
    await sleep(200)
  }
  await page.evaluate(() => [...document.querySelectorAll('button')].find(b => b.textContent === 'Make my paper').click())
  await page.waitForFunction(() => location.hash.includes('/paper?'), { timeout: 30000 })
  return waitPages(page)
}

async function checks(page) {
  return page.evaluate(() => {
    const root = document.querySelector('.doc-holder:not(.offscreen)')
    const svgs = [...root.querySelectorAll('.svg-wrap svg')]
    return {
      pages: root.querySelectorAll('.page').length,
      katex: root.querySelectorAll('.katex').length,
      katexErrors: root.querySelectorAll('.katex-error').length,
      svgs: svgs.length,
      svgsVisible: svgs.filter(s => s.getBoundingClientRect().width > 20 && s.getBoundingClientRect().height > 20).length,
      audio: root.querySelectorAll('.fig-audio').length,
      marks: document.querySelector('.paper-meta')?.textContent?.trim(),
      warnings: [...document.querySelectorAll('.paper-meta .warn')].map(w => w.textContent),
    }
  })
}

const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ['--autoplay-policy=no-user-gesture-required', '--window-size=1280,1000'] })
const page = await browser.newPage()
await page.setViewport({ width: 1280, height: 1000, deviceScaleFactor: 1 })
const errors = []
page.on('pageerror', e => errors.push(String(e)))
const outAbs = path.resolve(out)
fs.mkdirSync(outAbs, { recursive: true })
const cdp = await browser.target().createCDPSession()
page.on('error', e => errors.push('CRASH ' + String(e)))
await cdp.send('Browser.setDownloadBehavior', { behavior: 'allow', downloadPath: outAbs, eventsEnabled: true })

await page.goto(base, { waitUntil: 'networkidle0' })
await page.screenshot({ path: path.join(outAbs, 'home.png') })
const index = await page.evaluate(async () => (await fetch('./data/index.json')).json())
const results = {}
for (const s of index) {
  if (only.length && !only.includes(s.subject)) continue
  const dir = path.join(outAbs, s.subject)
  fs.mkdirSync(dir, { recursive: true })
  await cdp.send('Browser.setDownloadBehavior', { behavior: 'allow', downloadPath: dir })
  const r = { subject: s.subject }
  try {
    // checklist: tick the first two topics
    await page.goto(`${base}#/s/${s.subject}`, { waitUntil: 'networkidle0' })
    await page.waitForSelector('.tree .topic')
    await page.evaluate(() => {
      document.querySelectorAll('.tree .topic .topic-row input[type=checkbox]').forEach((c, i) => { if (i < 2) c.click() })
      document.querySelector('.tree .topic .disclose')?.click()
    })
    await sleep(400)
    await page.screenshot({ path: path.join(dir, 'checklist.png') })
    // topic test
    await build(page, base, s.subject, 'topic', 0)
    r.topicUrl = page.url()
    r.topic = await checks(page)
    if (s.subject === 'spanish' && r.topic.audio === 0) {
      // make sure a listening item is checked: build a listening-only test
      r.topicNote = 'no audio in topic test'
    }
    const qp = await page.$$('.doc-holder:not(.offscreen) .page')
    await qp[Math.min(2, qp.length - 1)].screenshot({ path: path.join(dir, 'topic-question-page.png') })
    r.topicFiles = await exportBoth(page, cdp, dir, 'topic-test')
    await page.goto(page.url().replace('/paper?', '/markscheme?'), { waitUntil: 'networkidle0' })
    await waitPages(page)
    const ms = await page.$$('.doc-holder:not(.offscreen) .page')
    await ms[1].screenshot({ path: path.join(dir, 'topic-markscheme-page.png') })
    // full structured paper (first paper)
    await build(page, base, s.subject, 'full', 0)
    r.fullUrl = page.url()
    r.full = await checks(page)
    const fp = await page.$$('.doc-holder:not(.offscreen) .page')
    await fp[0].screenshot({ path: path.join(dir, 'full-cover.png') })
    await fp[Math.min(2, fp.length - 1)].screenshot({ path: path.join(dir, 'full-question-page.png') })
    r.fullFiles = await exportBoth(page, cdp, dir, 'full-paper')
    if (s.subject === 'spanish') {
      r.speech = await page.evaluate(async () => {
        const btn = [...document.querySelectorAll('.audio-ctl button')].find(b => b.textContent.includes('Play'))
        if (!btn) return { button: false }
        const voices = speechSynthesis.getVoices().filter(v => v.lang.startsWith('es')).map(v => v.lang)
        btn.click()
        await new Promise(r => setTimeout(r, 1500))
        const speaking = speechSynthesis.speaking || speechSynthesis.pending
        const tbtn = [...document.querySelectorAll('.audio-ctl button')].find(b => b.textContent.includes('transcript'))
        tbtn?.click()
        await new Promise(r => setTimeout(r, 300))
        const transcriptShown = !!document.querySelector('.transcript')
        return { button: true, speaking, spanishVoices: voices.length, transcriptShown }
      })
      const a = await page.$('.doc-holder:not(.offscreen) .fig-audio')
      if (a) await a.screenshot({ path: path.join(dir, 'listening-player.png') })
    }
  } catch (e) {
    r.error = String(e)
  }
  results[s.subject] = r
  console.log(JSON.stringify(r))
}
// phone layout screenshot
await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2, isMobile: true })
await page.goto(base, { waitUntil: 'networkidle0' })
await page.screenshot({ path: path.join(outAbs, 'home-phone.png') })
results.pageErrors = errors
fs.writeFileSync(path.join(outAbs, 'results.json'), JSON.stringify(results, null, 1))
await browser.close()
