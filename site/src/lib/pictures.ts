// Line drawings for the Spanish "[picture: …]" items.  Icons are Tabler Icons (MIT licence, https://tabler.io/icons);
// clock faces and the body figure are drawn here.  Captions with no drawing stay as a caption in a box.
import data from './spanish-pictures.json'

const PICS = data.pictures as Record<string, string>
const ICONS = data.icons as Record<string, string>

function icon(name: string, x: number, y: number, s: number) {
  return `<g transform="translate(${x} ${y}) scale(${s})" fill="none" stroke="currentColor" stroke-width="${(1.5 / s).toFixed(2)}" stroke-linecap="round" stroke-linejoin="round">${ICONS[name] || ''}</g>`
}

function clock(h: number, m: number) {
  const ticks = Array.from({ length: 12 }, (_, i) => {
    const a = (i * Math.PI) / 6
    const r1 = i % 3 === 0 ? 16 : 18
    return `<line x1="${24 + r1 * Math.sin(a)}" y1="${24 - r1 * Math.cos(a)}" x2="${24 + 20 * Math.sin(a)}" y2="${24 - 20 * Math.cos(a)}" stroke-width="${i % 3 === 0 ? 1.6 : 0.9}"/>`
  }).join('')
  const ha = ((h % 12) + m / 60) * (Math.PI / 6)
  const ma = (m / 60) * 2 * Math.PI
  return `<g stroke="currentColor" fill="none" stroke-linecap="round"><circle cx="24" cy="24" r="21.5" stroke-width="1.6"/>${ticks}` +
    `<line x1="24" y1="24" x2="${24 + 10 * Math.sin(ha)}" y2="${24 - 10 * Math.cos(ha)}" stroke-width="2.4"/>` +
    `<line x1="24" y1="24" x2="${24 + 16.5 * Math.sin(ma)}" y2="${24 - 16.5 * Math.cos(ma)}" stroke-width="1.4"/>` +
    `<circle cx="24" cy="24" r="1.3" fill="currentColor"/></g>`
}

// a plain standing figure; `back` hides the face so it reads as seen from behind
const RINGS: Record<string, [number, number, number, number]> = {
  head: [24, 7, 6.5, 6.5], neck: [24, 13, 4.6, 3], throat: [24, 13, 4.6, 3], stomach: [24, 24, 4.8, 4.2], back: [24, 19, 6, 4.5],
  arm: [34.5, 20.5, 3.4, 6], hand: [37, 28.5, 3, 3], leg: [27.8, 37, 3, 7.5], knee: [27.6, 37, 2.6, 2.6], foot: [29, 44.5, 3.6, 2.4],
}
function body(part: string) {
  const [cx, cy, rx, ry] = RINGS[part] || RINGS.head
  const face = part === 'back' ? '' : '<circle cx="22.4" cy="6.3" r="0.6" fill="currentColor"/><circle cx="25.6" cy="6.3" r="0.6" fill="currentColor"/><path d="M22.5 8.8 q1.5 1 3 0" />'
  return `<g fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round">` +
    `<circle cx="24" cy="7" r="4.5"/>${face}<path d="M24 11.5 V14 M17 14 H31 L30 30 H18 Z M17 15 L11 27 M31 15 L37 27 M21 30 L20 44 L17 45 M27 30 L28 44 L31 45"/>` +
    `<circle cx="11" cy="28" r="1.4"/><circle cx="37" cy="28" r="1.4"/></g>` +
    `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="2.6 1.4"/>`
}

/** SVG markup for a caption, or null when there is no drawing for it. */
export function pictureSvg(caption: string): string | null {
  const spec = PICS[caption]
  if (!spec) return null
  const [art, label] = spec.split('|')
  const parts = art.split('+')
  let g: string
  if (parts[0].startsWith('clock:')) {
    const [, h, m] = parts[0].split(':')
    g = clock(+h, +m)
  } else if (parts[0].startsWith('body:')) {
    g = body(parts[0].slice(5))
  } else if (parts.length === 1) {
    g = label ? icon(parts[0], 9, 1, 1.25) : icon(parts[0], 4, 4, 1.67)
  } else {
    const y = label ? 3 : 12
    g = icon(parts[0], 0, y, 1) + icon(parts[1], 24, y, 1)
  }
  const text = label ? `<text x="24" y="46" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" font-weight="700" fill="currentColor">${label.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</text>` : ''
  return `<svg class="pic-svg" viewBox="0 0 48 48" aria-hidden="true">${g}${text}</svg>`
}

export const isPictureChoice = (s: string) => /^\s*\[picture: [^\]]+\]\s*$/.test(s)
