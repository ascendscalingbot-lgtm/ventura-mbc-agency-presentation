import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import { spawn } from 'node:child_process';
const FF = '/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2';
const FPS = 30, DUR = 22, NF = FPS * DUR;
const ff = spawn(FF, ['-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-i', 'music.wav', '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
  '-c:a', 'aac', '-b:a', '192k', '-shortest', 'raw.mp4'], { stdio: ['pipe', 'inherit', 'inherit'] });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
await p.goto('file://' + process.cwd() + '/index.html');
await p.evaluate(() => document.fonts.ready);
await p.waitForFunction(() => [...document.images].every(i => i.complete));
for (let f = 0; f < NF; f++) {
  await p.evaluate(t => window.render(t), f / FPS);
  const buf = await p.screenshot({ type: 'jpeg', quality: 95 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (f % 60 === 0) console.log('frame', f);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await b.close();
console.log('done');
