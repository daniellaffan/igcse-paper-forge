import type { Question, ReferenceSheet, Spec, SubjectIndex } from '../types'

const base = import.meta.env.BASE_URL + 'data/'
const cache = new Map<string, Promise<unknown>>()

function get<T>(path: string): Promise<T> {
  if (!cache.has(path)) {
    cache.set(path, fetch(base + path).then(r => {
      if (!r.ok) throw new Error(`Could not load ${path} (${r.status})`)
      return r.json()
    }).catch(e => { cache.delete(path); throw e }))
  }
  return cache.get(path) as Promise<T>
}

export const loadIndex = () => get<SubjectIndex[]>('index.json')
export const loadSpec = (s: string) => get<Spec>(`${s}/spec.json`)
export const loadBank = (s: string) => get<Question[]>(`${s}/bank.json`)
export const loadReference = (id: string) => get<ReferenceSheet>(`reference/${id}.json`)

/** localStorage helpers – always wrapped, the site must work without storage. */
export function store<T>(key: string, fallback: T): T {
  try {
    const v = localStorage.getItem('ipf:' + key)
    return v ? (JSON.parse(v) as T) : fallback
  } catch {
    return fallback
  }
}
export function save(key: string, value: unknown) {
  try { localStorage.setItem('ipf:' + key, JSON.stringify(value)) } catch { /* storage unavailable */ }
}

export function seenIds(subject: string): Set<string> {
  return new Set(store<string[]>('seen:' + subject, []))
}
export function markSeen(subject: string, ids: string[]) {
  const s = seenIds(subject)
  ids.forEach(i => s.add(i))
  save('seen:' + subject, [...s].slice(-5000))
}
export function clearSeen(subject: string) { save('seen:' + subject, []) }
