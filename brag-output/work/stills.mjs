import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const times = process.argv.slice(2).map(Number);
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
await p.goto('file://' + process.cwd() + '/index.html');
await p.evaluate(() => document.fonts.ready);
await p.waitForFunction(() => [...document.images].every(i => i.complete));
for (const t of times) {
  await p.evaluate(t => window.render(t), t);
  await p.screenshot({ path: `stills/t${t.toFixed(2)}.jpg`, quality: 70, type: 'jpeg' });
}
console.log(await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + f.style).join(',')));
await b.close();
