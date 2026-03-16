/**
 * Generate LinkedIn carousel screenshots from the Platypus architecture diagram.
 *
 * Output: 1080x1350px (4:5 ratio) PNGs at 2x retina (actual 2160x2700 pixels).
 * Strategy: For each slide, we isolate the target section(s) and capture a
 * viewport-sized screenshot. The background color fills any unused space.
 */

import puppeteer from 'puppeteer-core';
import path from 'path';
import fs from 'fs';

const HTML_PATH = '/Users/sagarsutaria/Herd/platypus-platform/docs/architecture-diagram.html';
const OUTPUT_DIR = '/Users/sagarsutaria/Herd/tech-portfolio/carousel/platypus';

// LinkedIn carousel ideal dimensions
const W = 1080;
const H = 1350;

// Each slide: name + CSS selectors to show + optional setup function
const SLIDES = [
  {
    name: '01-title-hook',
    desc: 'Title / Header + Stats Bar',
    show: ['header.header', '.stats-bar'],
  },
  {
    name: '02-client-apps',
    desc: 'Client Applications Layer',
    // nth-of-type to get the first .layer (delay-2)
    show: ['.layer.delay-2'],
  },
  {
    name: '03-api-services',
    desc: 'API & Services (expanded)',
    show: ['.layer.delay-3'],
  },
  {
    name: '04-data-layer',
    desc: 'Data Layer + External Services',
    show: ['.layer.delay-4'],
  },
  {
    name: '05-patterns',
    desc: 'Architecture Patterns',
    show: ['.layer.delay-5'],
  },
  {
    name: '06-infra-cta',
    desc: 'Infrastructure + CTA',
    show: ['.layer.delay-6', 'footer.footer'],
    addCTA: true,
  },
];

async function main() {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();

  await page.setViewport({
    width: W,
    height: H,
    deviceScaleFactor: 2,
  });

  console.log('\nGenerating LinkedIn carousel slides (1080x1350 @2x)...\n');

  for (const slide of SLIDES) {
    // Load fresh each time so we can isolate sections
    await page.goto(`file://${HTML_PATH}`, { waitUntil: 'networkidle0', timeout: 30000 });

    // Prep: kill animations, expand sections, isolate target elements
    await page.evaluate((showSelectors, addCTA) => {
      // Force all animations done
      document.querySelectorAll('.animate-in').forEach(el => {
        el.style.animation = 'none';
        el.style.opacity = '1';
        el.style.transform = 'none';
      });

      // Expand API modules
      const apiSection = document.getElementById('apiSection');
      if (apiSection) apiSection.classList.add('expanded');
      const apiIcon = document.getElementById('apiExpandIcon');
      if (apiIcon) {
        apiIcon.style.transform = 'rotate(45deg)';
        apiIcon.style.color = 'var(--gold)';
      }

      // Expand all app cards to show tech details
      document.querySelectorAll('.app-card').forEach(card => {
        card.classList.add('expanded');
      });

      // Hide everything first
      const container = document.querySelector('.container');
      Array.from(container.children).forEach(child => {
        child.style.display = 'none';
      });

      // Show only the target elements
      for (const sel of showSelectors) {
        const el = document.querySelector(sel);
        if (el) {
          el.style.display = '';
        }
      }

      // Set container to center content vertically
      container.style.display = 'flex';
      container.style.flexDirection = 'column';
      container.style.justifyContent = 'center';
      container.style.minHeight = '100vh';
      container.style.padding = '48px 56px';
      container.style.gap = '32px';

      // Remove margin-bottom from header since it's isolated
      const header = document.querySelector('header.header');
      if (header) {
        header.style.marginBottom = '0';
      }

      // Add CTA for the last slide
      if (addCTA) {
        const cta = document.createElement('div');
        cta.style.cssText = `
          text-align: center;
          padding: 40px 32px;
          margin-top: 24px;
          border: 1px solid rgba(232, 185, 49, 0.2);
          border-radius: 16px;
          background: linear-gradient(135deg, rgba(232, 185, 49, 0.06), rgba(91, 160, 224, 0.04));
        `;
        cta.innerHTML = `
          <div style="font-family: 'Instrument Serif', serif; font-size: 32px; color: #E8B931; margin-bottom: 8px;">
            Want to see the code?
          </div>
          <div style="font-family: 'DM Sans', sans-serif; font-size: 16px; color: rgba(232, 226, 214, 0.55); margin-bottom: 16px;">
            Follow for deep dives into architecture decisions, scaling patterns, and real-world trade-offs.
          </div>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 14px; color: rgba(232, 226, 214, 0.3);">
            @sagarsutaria
          </div>
        `;
        container.appendChild(cta);
      }
    }, slide.show, slide.addCTA);

    // Wait for layout + fonts
    await new Promise(r => setTimeout(r, 1500));

    await page.screenshot({
      path: path.join(OUTPUT_DIR, `${slide.name}.png`),
      clip: { x: 0, y: 0, width: W, height: H },
    });

    console.log(`  [OK] ${slide.name}.png — ${slide.desc}`);
  }

  await browser.close();

  console.log(`\nAll 6 slides saved to:\n  ${OUTPUT_DIR}\n`);
  console.log('Output: 2160x2700px PNGs (1080x1350 @2x retina)');
  console.log('Ready to upload directly to LinkedIn carousel.\n');
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
