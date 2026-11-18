import { useLayoutEffect, useRef, useState, type ReactNode } from 'react'
import type { Block } from './QuestionBlocks'

export const MM = 96 / 25.4
export const PAGE_W_MM = 210
export const PAGE_H_MM = 297
export const CONTENT_H_MM = 254 // 297 - 18 top - 25 bottom

/**
 * Lays blocks out onto A4 pages. Blocks are measured off-screen at the real
 * content width, then packed greedily; a block flagged keepWithNext moves to
 * the next page together with its follower.
 */
export function usePagination(blocks: Block[], contentClass: string, _deps: unknown[], limitMm = CONTENT_H_MM) {
  const measureRef = useRef<HTMLDivElement>(null)
  const [fontTick, setFontTick] = useState(0)
  const [state, setState] = useState<{ src: Block[] | null; tick: number; pages: number[][] }>({ src: null, tick: -1, pages: [] })
  const valid = state.src === blocks && state.tick === fontTick

  useLayoutEffect(() => {
    if (valid) return
    const el = measureRef.current
    if (!el) return
    const kids = Array.from(el.children) as HTMLElement[]
    const hs = kids.map(k => k.getBoundingClientRect().height)
    const limit = limitMm * MM
    const out: number[][] = []
    let cur: number[] = []
    let h = 0
    for (let i = 0; i < hs.length; i++) {
      let need = hs[i]
      if (blocks[i]?.keepWithNext && i + 1 < hs.length) need += hs[i + 1]
      if (cur.length && h + need > limit) {
        out.push(cur)
        cur = []
        h = 0
      }
      cur.push(i)
      h += hs[i]
    }
    if (cur.length) out.push(cur)
    setState({ src: blocks, tick: fontTick, pages: out })
  }, [valid, blocks, fontTick, limitMm])

  // re-measure once web fonts (KaTeX, serif) have loaded
  useLayoutEffect(() => {
    let alive = true
    document.fonts?.ready.then(() => { if (alive) setFontTick(t => t + 1) })
    return () => { alive = false }
  }, [])

  const measure = !valid ? (
    <div className="measure" aria-hidden="true">
      <div ref={measureRef} className={contentClass}>
        {blocks.map(b => <div key={b.key} className="blk">{b.node}</div>)}
      </div>
    </div>
  ) : null
  return { pages: valid ? state.pages : null, measure }
}

export function Page({ children, footer, className = '', side = true }: { children: ReactNode; footer?: ReactNode; className?: string; side?: boolean }) {
  return (
    <section className={'page ' + className}>
      {side && <div className="dnw dnw-l" aria-hidden="true">DO NOT WRITE IN THIS AREA</div>}
      {side && <div className="dnw dnw-r" aria-hidden="true">DO NOT WRITE IN THIS AREA</div>}
      <div className="page-inner">{children}</div>
      {footer && <div className="page-foot">{footer}</div>}
    </section>
  )
}
