import { useEffect, useState } from 'react'
import { Link, Route, Routes, useLocation } from 'react-router-dom'
import Home from './pages/Home'
import SubjectPage from './pages/Subject'
import Builder from './pages/Builder'
import PaperView from './pages/PaperView'
import { save, store } from './lib/data'

type Theme = 'system' | 'light' | 'dark'

export default function App() {
  const [theme, setTheme] = useState<Theme>(() => store<Theme>('theme', 'system'))
  const loc = useLocation()
  useEffect(() => {
    const r = document.documentElement
    if (theme === 'system') r.removeAttribute('data-theme')
    else r.setAttribute('data-theme', theme)
    save('theme', theme)
  }, [theme])
  useEffect(() => { window.scrollTo(0, 0) }, [loc.pathname])
  const docView = /\/(paper|markscheme)$/.test(loc.pathname)
  return (
    <div className={'app' + (docView ? ' doc-view' : '')}>
      <a className="skip" href="#main">Skip to content</a>
      <header className="topbar no-print">
        <Link to="/" className="brand" aria-label="IGCSE Paper Forge home">
          <svg viewBox="0 0 32 32" width="26" height="26" aria-hidden="true"><rect width="32" height="32" rx="7" fill="var(--accent)" /><path d="M9 7h11l4 4v14H9z" fill="var(--bg)" /><path d="M12 14h9M12 18h9M12 22h6" stroke="var(--accent)" strokeWidth="1.6" /></svg>
          <span>IGCSE Paper Forge</span>
        </Link>
        <label className="theme">
          <span className="sr">Theme</span>
          <select value={theme} onChange={e => setTheme(e.target.value as Theme)} aria-label="Colour theme">
            <option value="system">Auto theme</option>
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </label>
      </header>
      <main id="main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/s/:subject" element={<SubjectPage />} />
          <Route path="/s/:subject/build" element={<Builder />} />
          <Route path="/s/:subject/paper" element={<PaperView kind="qp" />} />
          <Route path="/s/:subject/markscheme" element={<PaperView kind="ms" />} />
          <Route path="*" element={<div className="wrap"><h1>Page not found</h1><Link to="/">Go home</Link></div>} />
        </Routes>
      </main>
      <footer className="sitefoot no-print">
        <p><b>Practice papers — not official exam board papers.</b> Every question here is original. IGCSE Paper Forge has no connection with Pearson, Edexcel or Cambridge International. Use the official past papers on the exam boards' websites as well.</p>
        <p>No sign-in, no tracking. Your settings and which questions you have seen are kept only in this browser.</p>
      </footer>
    </div>
  )
}
