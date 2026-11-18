export type Band = '1-3' | '4-6' | '7-9'

export interface Figure {
  type: 'svg' | 'table' | 'source' | 'passage' | 'audio' | 'poem' | 'image-note'
  svg?: string
  width?: number
  caption?: string
  note?: string
  headers?: string[]
  rows?: string[][]
  label?: string
  title?: string
  text?: string
  provenance?: string
  numbered?: boolean
  lang?: string
  transcript?: string
  voices?: string[]
}

export interface Part {
  label?: string
  text: string
  marks: number
  lines?: number
  space?: 'lines' | 'working' | 'box' | 'none' | 'mcq' | 'graph' | 'table'
  answer_prefix?: string
  answer_suffix?: string
  choices?: string[]
  figures?: Figure[]
  parts?: Part[]
}

export interface MSRow { part: string; answer: string; marks: string; notes?: string; ao?: string }
export interface LevelGrid {
  part: string
  title?: string
  ao_split?: string
  grid: { level: string; marks: string; descriptor: string }[]
  indicative?: string[]
  credit_note: string
}
export interface MarkScheme { style?: string; rows: MSRow[]; levels?: LevelGrid[]; general?: string }

export interface Question {
  id: string
  subject: string
  paper: string[]
  option?: string
  section?: string
  spec_refs: string[]
  topic: string
  subtopic: string
  qtype: string
  command_word: string
  marks: number
  difficulty: Band
  minutes: number
  calculator?: boolean | null
  paper2_only?: boolean
  intro?: string
  figures?: Figure[]
  parts: Part[]
  markscheme: MarkScheme
  ao: string[]
  answer?: { method?: string; values?: Record<string, unknown>; checked?: boolean }
  provenance?: string
  tags?: string[]
  template?: string
}

export interface Slot { qtypes?: string[]; marks?: number; count?: number; choice?: number; option?: string; topics?: string[]; label?: string }
export interface Section { id: string; title: string; instructions?: string; marks?: number; option_group?: string; slots?: Slot[] }
export interface PaperSpec {
  id: string
  name: string
  paper_code?: string
  minutes: number
  marks: number
  calculator?: boolean | null
  instructions?: string[]
  information?: string[]
  advice?: string[]
  materials?: string
  reference_sheet?: string
  answer_style?: string
  sections?: Section[]
}
export interface SpecPoint { ref: string; summary: string; paper2_only?: boolean; higher_only?: boolean }
export interface Subtopic { id: string; ref: string; title: string; summary: string; papers?: string[]; qtypes: string[]; points: SpecPoint[] }
export interface Topic { id: string; ref: string; title: string; papers?: string[]; option?: string; subtopics: Subtopic[] }
export interface QType { id: string; label: string; description?: string; marks?: string }
export interface Spec {
  subject: string
  code: string
  board: string
  title: string
  short?: string
  official_url: string
  spec_url?: string
  papers: PaperSpec[]
  qtypes: QType[]
  options?: { id: string; name: string; paper?: string; section?: string }[]
  topics: Topic[]
}

export interface SubjectIndex {
  subject: string
  title: string
  code: string
  board: string
  questions: number
  papers: { id: string; name: string }[]
}

export interface ReferenceSheet { id: string; title: string; blocks: Figure[] }

export interface TestConfig {
  subject: string
  mode: 'topic' | 'full'
  paper: string           // paper id, or '' = any
  subtopics: string[]     // empty = all
  qtypes: string[]        // empty = all
  length: { by: 'marks' | 'minutes'; value: number }
  diff: [number, number, number] // weights for 1-3, 4-6, 7-9
  calculator: 'any' | 'calc' | 'noncalc'
  options?: string[]      // history options / sections to include
  seed: number
}
