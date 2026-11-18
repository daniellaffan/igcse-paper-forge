/**
 * Export the A4 pages inside `root` as a paginated PDF. Each `.page` element is
 * exactly one A4 sheet on screen, so the PDF pagination matches what you see.
 */
export async function exportPdf(root: HTMLElement, filename: string, onProgress?: (done: number, total: number) => void) {
  const [{ default: html2canvas }, { jsPDF }] = await Promise.all([import('html2canvas'), import('jspdf')])
  await document.fonts?.ready
  const pages = Array.from(root.querySelectorAll<HTMLElement>('.page'))
  const pdf = new jsPDF({ unit: 'mm', format: 'a4', orientation: 'portrait', compress: true })
  root.classList.add('exporting')
  try {
    for (let i = 0; i < pages.length; i++) {
      const canvas = await html2canvas(pages[i], {
        scale: 2,
        backgroundColor: '#ffffff',
        useCORS: true,
        logging: false,
        windowWidth: 1200,
        ignoreElements: el => el.classList?.contains('no-print'),
      })
      const img = canvas.toDataURL('image/jpeg', 0.9)
      if (i > 0) pdf.addPage('a4', 'portrait')
      pdf.addImage(img, 'JPEG', 0, 0, 210, 297, undefined, 'FAST')
      onProgress?.(i + 1, pages.length)
      await new Promise(r => setTimeout(r, 0))
    }
  } finally {
    root.classList.remove('exporting')
  }
  pdf.setProperties({ title: filename.replace(/\.pdf$/, ''), subject: 'Practice paper — not an official exam board paper', creator: 'IGCSE Paper Forge' })
  pdf.save(filename)
}
