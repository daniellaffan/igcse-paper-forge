import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import type { SubjectIndex } from '../types'
import { loadIndex } from '../lib/data'

const ICON: Record<string, string> = {
  maths: '∑', 'further-maths': '∫', physics: '⚛', chemistry: '⚗', biology: '❦', economics: '£',
  history: '⌛', 'english-language': '✎', 'english-literature': '❧', spanish: 'ñ',
}

export default function Home() {
  const [subs, setSubs] = useState<SubjectIndex[] | null>(null)
  const [err, setErr] = useState('')
  useEffect(() => { loadIndex().then(setSubs).catch(e => setErr(String(e))) }, [])
  const total = subs?.reduce((a, s) => a + s.questions, 0) || 0
  return (
    <div className="wrap">
      <section className="hero">
        <h1>Make a practice paper in a minute</h1>
        <p>Pick a subject, tick the topics you want, and get an exam-style question paper with a separate mark scheme — both as A4 PDFs.
          {total > 0 && <> The bank holds <b>{total.toLocaleString()}</b> original questions.</>}</p>
      </section>
      {err && <p className="error">{err}</p>}
      {!subs && !err && <p className="muted">Loading subjects…</p>}
      <ul className="subject-grid">
        {subs?.map(s => (
          <li key={s.subject}>
            <Link to={`/s/${s.subject}`} className="subject-card">
              <span className="sc-icon" aria-hidden="true">{ICON[s.subject] || '•'}</span>
              <span className="sc-title">{s.title}</span>
              <span className="sc-code">{s.board} · {s.code}</span>
              <span className="sc-count">{s.questions.toLocaleString()} questions · {s.papers.map(p => p.name).join(', ')}</span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
