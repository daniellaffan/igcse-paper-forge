/** Small deterministic RNG (mulberry32) so a seed always rebuilds the same paper. */
export function mulberry32(seed: number) {
  let a = seed >>> 0
  return () => {
    a = (a + 0x6d2b79f5) >>> 0
    let t = a
    t = Math.imul(t ^ (t >>> 15), t | 1)
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61)
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

export function shuffle<T>(arr: T[], rnd: () => number): T[] {
  const a = arr.slice()
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rnd() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

export const newSeed = () => Math.floor(Math.random() * 900000) + 100000

export function encodeConfig(obj: unknown): string {
  const s = JSON.stringify(obj)
  const b = btoa(unescape(encodeURIComponent(s)))
  return b.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}
export function decodeConfig<T>(s: string): T | null {
  try {
    const b = s.replace(/-/g, '+').replace(/_/g, '/')
    return JSON.parse(decodeURIComponent(escape(atob(b)))) as T
  } catch {
    return null
  }
}
