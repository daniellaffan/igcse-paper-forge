import esbuild from '../../../site/node_modules/esbuild/lib/main.js'
const { build } = esbuild
import path from 'node:path'
import { fileURLToPath } from 'node:url'
const here = path.dirname(fileURLToPath(import.meta.url))
await build({
  entryPoints: [path.join(here, 'entry.jsx')], bundle: true, platform: 'node', format: 'esm', outfile: path.join(here, '.out/entry.mjs'),
  jsx: 'automatic', plugins: [{ name: 'katex-shim', setup(b) {
    b.onResolve({ filter: /^katex$/ }, () => ({ path: path.join(here, 'katex-shim.mjs') }))
    b.onResolve({ filter: /\.css$/ }, a => ({ path: a.path, namespace: 'empty' }))
    b.onLoad({ filter: /.*/, namespace: 'empty' }, () => ({ contents: '', loader: 'js' }))
  } }], loader: { '.css': 'empty' },
  nodePaths: [path.join(here, '../../../site/node_modules'), path.join(here, '../node_modules')],
  banner: { js: "import { createRequire } from 'module'; const require = createRequire(import.meta.url);" },
  logLevel: 'warning', external: ['mathjax-full'], define: { 'import.meta.env.BASE_URL': '"./"' },
})
