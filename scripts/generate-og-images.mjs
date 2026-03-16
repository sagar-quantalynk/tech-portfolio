import puppeteer from 'puppeteer-core';
import { readdir } from 'node:fs/promises';
import { resolve, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const assetsDir = resolve(__dirname, '..', 'assets');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const WIDTH = 1200;
const HEIGHT = 630;

async function generateOgImages() {
  const files = await readdir(assetsDir);
  const htmlFiles = files.filter(f => f.endsWith('-preview.html'));

  if (htmlFiles.length === 0) {
    console.error('No *-preview.html files found in assets/');
    process.exit(1);
  }

  console.log(`Found ${htmlFiles.length} preview HTML files`);

  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  for (const htmlFile of htmlFiles) {
    const name = basename(htmlFile, '.html');
    const pngPath = resolve(assetsDir, `${name}.png`);
    const htmlPath = resolve(assetsDir, htmlFile);

    console.log(`  Generating ${name}.png ...`);

    const page = await browser.newPage();
    await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: 2 });
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0', timeout: 15000 });

    // Wait for Google Fonts to load
    await page.evaluate(() => document.fonts.ready);

    await page.screenshot({
      path: pngPath,
      type: 'png',
      clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT },
    });

    await page.close();
    console.log(`  -> ${pngPath}`);
  }

  await browser.close();
  console.log(`\nDone! Generated ${htmlFiles.length} OG images.`);
}

generateOgImages().catch(err => {
  console.error('Failed to generate OG images:', err);
  process.exit(1);
});
