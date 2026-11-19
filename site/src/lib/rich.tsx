import katex from 'katex'
import 'katex/dist/katex.min.css'
import { pictureSvg } from './pictures'

const esc = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')

function inline(s: string): string {
  let h = esc(s)
  h = h.replace(/\*\*((?:[^*]|\*(?!\*))+?)\*\*/g, '<strong>$1</strong>') // bold may contain *italic*
  h = h.replace(/(^|[^*])\*([^*\s][^*]*?)\*(?!\*)/g, '$1<em>$2</em>')
  h = h.replace(/\[\[blank\]\]/g, '<span class="ans-box"></span>')
  h = h.replace(/\[\[dots\]\]/g, '<span class="ans-dots"></span>')
  // Spanish pictures: a line drawing (caption kept for the mark scheme), or the caption in a box
  h = h.replace(/\[picture: ([^\]]+)\]/g, (_, cap: string) => {
    const svg = pictureSvg(cap.replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&'))
    return svg ? `<span class="pic">${svg}<span class="pic-cap">[picture: ${cap}]</span></span>` : `<span class="pic pic-text">${cap}</span>`
  })
  h = h.replace(/\n/g, '<br/>')
  return h
}

function math(src: string, display: boolean): string {
  try {
    // Exam papers print inline fractions full size, so use display style for
    // inline maths that has fractions (but not inside powers/indices).
    if (!display && /\\frac/.test(src) && !/[\^_]/.test(src)) src = '\\displaystyle ' + src
    return katex.renderToString(src, { displayMode: display, throwOnError: false, strict: 'ignore', output: 'html' })
  } catch {
    return esc(src)
  }
}

/** Convert our markup (see docs/DATA_FORMAT.md) to HTML. `\$` is a literal dollar sign. */
export function richHtml(src: string | undefined): string {
  if (!src) return ''
  const DOLLAR = '\u0000D\u0000'
  const text = src.replace(/\\\$/g, DOLLAR)
  const paras = text.split(/\n\s*\n/)
  return paras
    .map(p => {
      let out = ''
      const re = /\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g
      let last = 0
      let m: RegExpExecArray | null
      while ((m = re.exec(p))) {
        out += inline(p.slice(last, m.index))
        out += m[1] !== undefined ? math(m[1].replace(new RegExp(DOLLAR, 'g'), '\\$'), true) : math(m[2].replace(new RegExp(DOLLAR, 'g'), '\\$'), false)
        last = m.index + m[0].length
      }
      out += inline(p.slice(last))
      return `<p>${out.replace(new RegExp(DOLLAR, 'g'), '$')}</p>`
    })
    .join('')
}

export function Rich({ text, className, as = 'div' }: { text?: string; className?: string; as?: 'div' | 'span' }) {
  const html = richHtml(text)
  if (as === 'span') return <span className={className} dangerouslySetInnerHTML={{ __html: html.replace(/^<p>|<\/p>$/g, '') }} />
  return <div className={'rich ' + (className || '')} dangerouslySetInnerHTML={{ __html: html }} />
}
