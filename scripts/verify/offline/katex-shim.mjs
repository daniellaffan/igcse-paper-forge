// Stand-in for KaTeX when the site's components are rendered in Node (no browser):
// each formula becomes an SVG file (MathJax) referenced by an <img>, which PyMuPDF can draw.
import { mathjax } from 'mathjax-full/js/mathjax.js'
import { TeX } from 'mathjax-full/js/input/tex.js'
import { SVG } from 'mathjax-full/js/output/svg.js'
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js'
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js'
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js'

const adaptor = liteAdaptor()
RegisterHTMLHandler(adaptor)
const doc = mathjax.document('', { InputJax: new TeX({ packages: AllPackages }), OutputJax: new SVG({ fontCache: 'none' }) })
export const MATH = new Map() // file name -> svg text
const EX_PT = 5.0 // 1ex at the paper's 11pt body size

function renderToString(src, opts = {}) {
  const key = (opts.displayMode ? 'D' : 'I') + src
  let name = [...MATH.keys()].find(k => MATH.get(k).key === key)
  if (!name) {
    let svg
    try {
      const node = doc.convert(src.replace(/^\\displaystyle\s*/, ''), { display: !!opts.displayMode || /^\\displaystyle/.test(src) })
      svg = adaptor.innerHTML(node)
    } catch (e) {
      return `<span class="math-error">${src}</span>`
    }
    const num = s => parseFloat(s)
    const w = num(svg.match(/width="([\d.]+)ex"/)?.[1] || '1')
    const h = num(svg.match(/height="([\d.]+)ex"/)?.[1] || '1')
    const va = num(svg.match(/vertical-align:\s*(-?[\d.]+)ex/)?.[1] || '0')
    svg = svg.replace(/width="[\d.]+ex"/, `width="${(w * EX_PT).toFixed(2)}pt"`).replace(/height="[\d.]+ex"/, `height="${(h * EX_PT).toFixed(2)}pt"`)
      .replace(/<svg /, '<svg xmlns="http://www.w3.org/2000/svg" ')
    name = `m${MATH.size}.svg`
    MATH.set(name, { key, svg, w: w * EX_PT, h: h * EX_PT, va: va * EX_PT })
  }
  const m = MATH.get(name)
  return `<img class="math${opts.displayMode ? ' display' : ''}" src="${name}" width="${m.w.toFixed(1)}" height="${m.h.toFixed(1)}" style="width:${m.w.toFixed(1)}pt;height:${m.h.toFixed(1)}pt;vertical-align:${m.va.toFixed(1)}pt"/>`
}
export default { renderToString }
