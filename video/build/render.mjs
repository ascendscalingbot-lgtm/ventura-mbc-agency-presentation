// Frame-by-frame renderer: seeks the master timeline to each frame time and pipes PNGs into ffmpeg.
// Usage: node render.mjs <out.mp4> [--v] [--fps 60] [--start 0] [--end DUR] [--audio file] [--stills t1,t2,...]
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const out = args[0];
const flag = (k, d) => { const i = args.indexOf(k); return i < 0 ? d : args[i + 1]; };
const vert = args.includes('--v');
const fps = Number(flag('--fps', 60));
const audio = flag('--audio', null);
const stills = flag('--stills', null);

const root = path.dirname(new URL(import.meta.url).pathname);
const types = { '.html': 'text/html', '.js': 'text/javascript', '.png': 'image/png', '.woff2': 'font/woff2' };
const server = http.createServer((q, r) => {
  const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, b) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream' }); r.end(b); });
}).listen(0);
const port = server.address().port;

const W = vert ? 1080 : 1920, H = vert ? 1920 : 1080;
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
page.on('console', m => { if (m.type() === 'error') console.error('page:', m.text()); });
page.on('pageerror', e => console.error('pageerror:', e.message));
await page.goto(`http://127.0.0.1:${port}/index.html?v=${vert ? 1 : 0}`);
await page.waitForFunction(() => window.__ready === true);
const DUR = await page.evaluate(() => window.__DUR);
const start = Number(flag('--start', 0)), end = Number(flag('--end', DUR));

if (stills) {
  fs.mkdirSync(out, { recursive: true });
  for (const t of stills.split(',').map(Number)) {
    await page.evaluate(t => window.__seek(t), t);
    await page.screenshot({ path: path.join(out, `t_${t.toFixed(3)}.png`) });
  }
} else {
  const n = Math.round((end - start) * fps);
  const ff = ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-'];
  if (audio) ff.push('-ss', String(start), '-t', String(end - start), '-i', audio, '-map', '0:v', '-map', '1:a', '-c:a', 'copy');
  ff.push('-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', String(fps), '-movflags', '+faststart', out);
  const enc = spawn('ffmpeg', ff, { stdio: ['pipe', 'inherit', 'inherit'] });
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    const t = start + i / fps;
    await page.evaluate(t => window.__seek(t), t);
    const buf = await page.screenshot({ type: 'png' });
    if (!enc.stdin.write(buf)) await new Promise(r => enc.stdin.once('drain', r));
    if (i % 120 === 0) console.log(`frame ${i}/${n} t=${t.toFixed(2)} ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  }
  enc.stdin.end();
  await new Promise(r => enc.on('close', r));
}
await browser.close(); server.close();
console.log('done', out);
