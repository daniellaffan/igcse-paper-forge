import { useEffect, useState } from 'react'
import type { Figure } from '../types'
import { Rich } from '../lib/rich'

function cleanSvg(svg: string) {
  return svg
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/\son\w+="[^"]*"/gi, '')
    .replace(/(href|xlink:href)="(?!#)[^"]*"/gi, '')
}

export function Speaker({ fig }: { fig: Figure }) {
  const [show, setShow] = useState(false)
  const [playing, setPlaying] = useState(false)
  const supported = typeof window !== 'undefined' && 'speechSynthesis' in window
  useEffect(() => () => { if (supported) window.speechSynthesis.cancel() }, [supported])
  const play = () => {
    if (!supported) return
    const synth = window.speechSynthesis
    if (playing) { synth.cancel(); setPlaying(false); return }
    const voices = synth.getVoices().filter(v => v.lang.toLowerCase().startsWith((fig.lang || 'es-ES').slice(0, 2)))
    const pref = voices.filter(v => /es-ES/i.test(v.lang))
    const pool = pref.length ? pref : voices
    const lines = (fig.transcript || '').split('\n').map(l => l.trim()).filter(Boolean)
    const speakers = new Map<string, number>()
    // Real listening exams play each recording twice.
    const all = [...lines, '…', ...lines]
    all.forEach((line, i) => {
      const m = line.match(/^([^:]{1,30}):\s*(.*)$/)
      const who = m ? m[1] : ''
      const text = m ? m[2] : line
      if (who && !speakers.has(who)) speakers.set(who, speakers.size)
      const idx = speakers.get(who) || 0
      const u = new SpeechSynthesisUtterance(text === '…' ? ' ' : text)
      u.lang = fig.lang || 'es-ES'
      if (pool.length) u.voice = pool[idx % pool.length]
      u.pitch = 1 + ((idx % 3) - 1) * 0.18
      u.rate = 0.9
      if (i === all.length - 1) u.onend = () => setPlaying(false)
      synth.speak(u)
    })
    setPlaying(true)
  }
  return (
    <div className="fig-audio">
      <div className="audio-print">Listening recording — play it on the website (each recording is heard twice).</div>
      <div className="no-print audio-ctl">
        <button type="button" onClick={play} disabled={!supported} aria-pressed={playing}>
          {playing ? '■ Stop' : '▶ Play recording'}
        </button>
        <button type="button" onClick={() => setShow(s => !s)} aria-expanded={show}>
          {show ? 'Hide transcript' : 'Show transcript'}
        </button>
        {!supported && <span className="muted"> Your browser has no speech synthesis; use the transcript.</span>}
      </div>
      {show && <div className="no-print transcript"><Rich text={fig.transcript} /></div>}
    </div>
  )
}

export function FigureView({ fig, inMarkScheme = false }: { fig: Figure; inMarkScheme?: boolean }) {
  switch (fig.type) {
    case 'svg':
      return (
        <figure className="fig fig-svg">
          <div className="svg-wrap" style={{ width: fig.width ? `${fig.width}mm` : undefined }}
            dangerouslySetInnerHTML={{ __html: cleanSvg(fig.svg || '') }} />
          {fig.note && <figcaption className="fig-note">{fig.note}</figcaption>}
          {fig.caption && <figcaption><Rich as="span" text={fig.caption} /></figcaption>}
        </figure>
      )
    case 'table':
      return (
        <figure className="fig fig-table">
          {fig.caption && <figcaption className="cap-top"><Rich as="span" text={fig.caption} /></figcaption>}
          <table className={'data' + (Math.max(fig.headers?.length || 0, ...(fig.rows || []).map(r => r.length)) > 8 ? ' wide' : '')}>
            {fig.headers && <thead><tr>{fig.headers.map((h, i) => <th key={i}><Rich as="span" text={h} /></th>)}</tr></thead>}
            <tbody>{(fig.rows || []).map((r, i) => <tr key={i}>{r.map((c, j) => <td key={j}><Rich as="span" text={c} /></td>)}</tr>)}</tbody>
          </table>
          {fig.note && <figcaption className="fig-note">{fig.note}</figcaption>}
        </figure>
      )
    case 'source':
      return (
        <div className="fig fig-source">
          {fig.label && <div className="src-label">{fig.label}</div>}
          {fig.provenance && <div className="src-prov"><Rich as="span" text={fig.provenance} /></div>}
          <Rich text={fig.text} />
        </div>
      )
    case 'passage':
    case 'poem': {
      const lines = (fig.text || '').split('\n')
      return (
        <div className={'fig fig-passage' + (fig.type === 'poem' ? ' poem' : '')}>
          {fig.title && <div className="psg-title"><Rich as="span" text={fig.title} /></div>}
          {fig.provenance && <div className="src-prov"><Rich as="span" text={fig.provenance} /></div>}
          {fig.numbered || fig.type === 'poem' ? (
            <div className="numbered">
              {lines.map((l, i) => {
                const n = lines.slice(0, i + 1).filter(x => x.trim()).length
                return (
                  <div className="nl" key={i}>
                    <span className="ln">{l.trim() && n % 5 === 0 ? n : ''}</span>
                    <span className="lt"><Rich as="span" text={l || ' '} /></span>
                  </div>
                )
              })}
            </div>
          ) : <Rich text={fig.text} />}
        </div>
      )
    }
    case 'audio':
      return inMarkScheme
        ? <div className="fig fig-source"><div className="src-label">Transcript</div><Rich text={fig.transcript} /></div>
        : <Speaker fig={fig} />
    default:
      return fig.text ? <div className="fig"><Rich text={fig.text} /></div> : null
  }
}

export function Figures({ figs, inMarkScheme }: { figs?: Figure[]; inMarkScheme?: boolean }) {
  if (!figs || !figs.length) return null
  return <>{figs.map((f, i) => <FigureView key={i} fig={f} inMarkScheme={inMarkScheme} />)}</>
}
