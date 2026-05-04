# Design Spec — sagarsutaria.com

**Date:** 2026-05-04
**Author:** Brainstormed via Claude Code with `superpowers:brainstorming` + `ui-ux-pro-max` + `frontend-design` skills
**Repo:** `~/Herd/tech-portfolio/` (existing portfolio repo, evolving)
**Domain:** sagarsutaria.com (purchased 2026-05-04, awaiting DNS configuration)
**Decision context:** Three LLM Council sessions on 2026-05-02 + Sagar's clarifications across the conversation. Current status: BillingZero references purged 2026-05-04; ready for marketing-site evolution.

---

## 1. Purpose & Job-to-Be-Done

The site is a **B2B inbound-lead engine** for Sagar Sutaria, an engineering leader becoming dedicated CTO at a Berlin startup (Relokate, deal closing 15–20 May 2026) with a parallel solo studio (QuantaLynk Pvt Ltd) for advisory + select build work.

**Three jobs the site must do, in priority order:**

1. **Convert qualified inbound interest into booked conversations.** A founder, COO, or peer CTO lands here from a referral / LLM citation / forwarded essay → understands what Sagar offers → books an advisory call or sends a build-engagement inquiry within one session.
2. **Withstand procurement / due-diligence read.** A prospective Berlin or US Series-A founder, an investor, or Relokate's GC during onboarding can read this site and walk away with: "credible, technical, no live red flags." That's the trust-anchor job.
3. **Compound through writing.** The `/writing` surface seeds Sagar's thinking-in-public, indexed by both humans and LLMs. Each essay is a long-tail acquisition asset. Cadence target: 1 essay every 1–2 weeks once Relokate ramp-up settles (per Council Session 1's "writing is the load-bearing asset" finding).

**Explicit non-goals:**

- Not a portfolio gallery. Selected systems become *outcome stories*, not spec sheets.
- Not a place where QuantaLynk-the-business is sold. That lives on quantalynk.com.
- Not a CV / résumé site. There's a downloadable PDF for that, but the site itself sells future engagements, not past employment.
- Not a personal blog. Writing is opinionated, professionally-relevant, not lifestyle.

---

## 2. Audience & ICP (per Council Sessions 1–2)

- **Primary:** EU founders / operators / peer CTOs at Series A → small-mid scale-ups (€5–50M revenue) considering advisory or fixed-scope build engagements. Geography: EU > US > India.
- **Secondary:** Recruiters / partners doing diligence on Sagar in his Berlin CTO role.
- **Tertiary:** Future product-platform users when Sagar's "one bet" product ships (per Council Session 1's separate workstream).

---

## 3. Information Architecture

```
/                Home — hero + thesis + dual CTA + 3 sections + footer
/services        Services overview (3 tiles linking to detail)
  /services/advisory          — fractional CTO / advisory retainers
  /services/build             — fixed-scope build sprints
  /services/ai-uplift         — AI integration into existing products
/work            Index of selected systems (filterable by vertical)
  /work/<slug>   Per-system case studies (rewritten from existing platform pages)
/writing         Index of essays
  /writing/<slug> Per-essay pages (long-form, reading-optimized)
/about           Sagar's story; the studio model; why solo+AI; Relokate context
/contact         Form + Calendly + email + LinkedIn link
```

The `/` homepage assembles representative content from each section to give a one-page-tour to fast scanners. Section order: hero → "What I do" (3 service tiles) → "Selected systems" (4–6 cards from `/work`) → "Recent thinking" (3 latest from `/writing`) → "About" strip → contact CTA.

**SEO files:** `sitemap.xml`, `robots.txt`, OG images per page, Schema.org `Person` markup on `/about` and `Article` markup on `/writing/<slug>`.

---

## 4. Visual Design System

**Locked direction: Editorial Magazine — Sienna.** Selected 2026-05-04 after `ui-ux-pro-max` design-system search, four candidate samples rendered side-by-side, and a 5-of-5 unanimous council session 5 verdict picking this direction over Atelier Modern, Editorial-Teal, and Warm-Modernist alternates.

**Pivot, not evolution.** The existing `tech-portfolio` repo uses dark + gold + Instrument Serif. This spec replaces that palette and primary display font entirely. The reasons documented: Sagar's brief explicitly de-prioritized the dark direction; the council's Outsider advisor (role-playing the Munich/Berlin buyer) reported he'd click "Book a call" on the warm-cream sienna direction and close-tab on the dark or sans-modern alternatives.

### 4.1 Tokens (locked)

Three values diverge from the visual sample on disk: the sienna accent, the body-secondary color, and an italic-accent system primitive. All three are conversion-driven adjustments from council session 5 review.

| Token | Value | Notes |
|---|---|---|
| `--paper` | `#F4ECDC` | warm cream background; primary surface |
| `--paper-elevated` | `#FAF5E9` | slightly lighter cream for cards / elevated surfaces |
| `--ink` | `#1F1A14` | warm-leaning black for primary text + display headings |
| `--ink-secondary` | `#3A2F22` | body-text-on-cream secondary; **darkened from `#4A3F2E` per council session 5 contrast review (commodity-screen WCAG AA)** |
| `--ink-tertiary` | `#6B5840` | warm gray for meta-text, dates, tertiary labels |
| `--border-fine` | `rgba(31, 26, 20, 0.12)` | hairline dividers |
| `--border-emphasis` | `rgba(31, 26, 20, 0.25)` | secondary CTA outlines, focus rings |
| `--accent-sienna` | `#9A3408` | **darkened from `#B7410E` per council session 5 contrast review.** Burnt sienna; primary accent for italic display words, CTA hover states, link color, focus rings |
| `--accent-sienna-soft` | `rgba(154, 52, 8, 0.08)` | low-opacity wash for accent-tinted surfaces |
| `--semantic-success` | `#15803D` | form success, status indicators |
| `--semantic-error` | `#B91C1C` | form errors, destructive |
| `--display-font` | Bricolage Grotesque (variable, opsz 12–96, weights 400/500/600/700/800, italic axis) | unique to sagarsutaria.com; not used on quantalynk.com |
| `--body-font` | DM Sans (variable, weights 400/500/600/700, italic axis) | reading + UI body |
| `--mono-font` | JetBrains Mono (weights 400/500/600) | code, numerics, dates, mono-tagged labels. **Shared with quantalynk.com — only typographic kinship between the two sites** |
| `--spacing-base` | 8pt rhythm | major sections; sub-spacing on 4pt grid |
| `--radius-sharp` | 4px | buttons, form inputs, sharp tiles |
| `--radius-soft` | 0px | service tiles, case study cards (editorial register: hard borders over rounded) |
| `--shadow-card` | none | borders carry the elevation; no shadows in default register |
| `--shadow-hover` | `0 1px 3px rgba(31, 26, 20, 0.06)` | minimal hover lift only |
| `--motion-duration` | 200ms (default), 150ms (color/state) | restrained motion |
| `--motion-ease` | `cubic-bezier(0.32, 0.72, 0, 1)` | spring-feel without spring physics |

### 4.2 The Italic-Sienna-Word System Primitive

The single typographic move — **`Sagar `*`Sutaria.`*** with the last name in italic Bricolage at the accent color — is treated as a brand primitive, not a hero treatment. The council's Expansionist advisor identified this as the asymmetric upside of the chosen direction; locking it as a system rule:

- **Hero (every page)** — name appears with the italicized accent word in `--accent-sienna`.
- **Essay titles (`/writing/<slug>`)** — every essay title has exactly one italicized accent word in sienna. Author chooses which word at write-time; the rule is one-and-only-one per title.
- **Service card headlines** — the verb-ish accent word (e.g. "Advise *me.*", "Build *with me.*", "Add *AI* to my product") sits in italic sienna.
- **Pull-quote treatment** — long-form essay pull-quotes elevate one word to italic-sienna for visual rhythm.
- **OG image template** — every shareable card preserves the italic-sienna-word treatment so social-network screenshots are visually recognizable as Sagar's *before the byline loads* (the screenshot-survivability mechanic the council flagged).
- **Future surfaces** (podcast cover, speaking deck template, "one bet" product splash when it ships) — same primitive carries forward. The rule outlives the website.

### 4.3 Effects and motion

Restrained. The dark-site's blueprint-grid background, ambient glow orbs, drift animations, and pulse-dots are all **out** — they belonged to the dark register and would clutter the editorial register.

What's in:

- **Page-load reveal** — single staggered fade-up on hero only. 600ms ease-out, 80ms stagger between badge → title → role → lede → CTAs. No further animation below the fold on initial load.
- **Hover states** — 150ms color transition on links / buttons / tile borders. CTAs darken ink-fill on hover OR border color shifts to sienna. No transform-based hover effects.
- **Scroll-triggered** — none on the homepage. On `/writing/<slug>` essays, optional progress bar at top of viewport using `scroll-driven animations` (CSS only).
- **Reduced-motion** — every transition wrapped in `@media (prefers-reduced-motion: no-preference)`.

### 4.4 New components required

- **HeroBlock** — paper background, badge with sienna pulse-dot, italic-accent name treatment, mono role line, 22px body lede, dual CTA. Italic-accent system primitive applied here first.
- **ServiceCard** — hard-border tile (no rounding), display headline with italic accent word, body description in DM Sans, mono price band in `--accent-sienna`, hover: border shifts to sienna + tile background lifts to `--paper-elevated`.
- **EssayCard** — display headline (Bricolage with italic accent word), date in mono small caps, one-line tease in DM Sans, read-time in mono. Card-itself unstyled save for hover: title gains sienna underline.
- **WritingLayout** (long-form) — Bricolage 48px h1 with required italic-accent word, DM Sans 18px body, 1.65 line-height, max 68 chars, generous 32px vertical rhythm, JetBrains Mono inline + block code, italic-sienna pull-quotes.
- **LeadCaptureForm** — Formspree-wired (existing); three variants (short, full, inline). Submit button: filled ink, hover sienna. Success state: quiet inline confirmation, no toast.
- **CalendlyEmbed** — inline iframe on `/contact` and `/services/advisory`. Set Calendly theme to match (light, warm).
- **Nav, Footer** — minimal; nav is link list with hover-underlines, footer is mono small-caps link group + sagarsutaria.com wordmark.

### 4.5 Anti-patterns explicitly rejected

- ❌ Inter, Roboto, Arial, system-stack fonts (frontend-design rule).
- ❌ Purple-gradient-on-white SaaS-template aesthetics (frontend-design rule).
- ❌ Emoji as icons — Lucide / Heroicons SVG only.
- ❌ Glassmorphism, drop shadows beyond the minimal hover-lift, gradient meshes, glow orbs, blueprint grids, scroll parallax (the dark-site's effect language doesn't transfer).
- ❌ Linear/Stripe register (eliminated as Direction B in council session 5; "tasteful Linear cover band" failed the conversion test against the editorial-cream alternative).
- ❌ Decorative italic everywhere — italic is reserved for the system primitive (one word per heading max).
- ❌ Multiple accent colors. Sienna is the only accent. Semantic colors (success/error) are functional, not brand.

---

## 5. Content Strategy & Voice

**Voice:** founder-essay, opinionated, warm-but-considered. First-person ("I" not "we"). Quietly confident. Refers to specific shipped work over generic claims.

**Hero copy direction (council-locked situation-first frame):**

```
   [ENGINEERING  · AI · SYSTEMS]
   Sagar Sutaria.    ← italic-sienna accent on "Sutaria."
   Engineering leader · CTO at Relokate (Berlin)
   ───
   Your AI feature is stuck in prototype.
   Your platform won't survive the next 10x.
   You need senior judgment this quarter, not a hire next year.
   I take one off your desk in 4–12 weeks, scope-locked —
   or I sit beside you as the CTO you haven't hired yet.
   ───
   [Book a 30-min call →]   [Read latest essay]
```

**Why situation-first, not feature-first** (council session 5 mini-validation, 2026-05-04):

A focused 3-advisor mini-council was run with the explicit conversion frame: *"which lede makes the EU/US founder/CTO buyer click 'Book a 30-min call'?"* Three candidate lede options (L1 speed-with-judgment, L2 direct-build, L3 sharp-anti-agency) plus the original L0 baseline were evaluated. Verdict: **L1 was least-bad of the four, but all four leak click-intent.** All three advisors converged on a deeper insight — situation-first reframing.

- **Outsider** (Munich/Berlin buyer role-play): rated L1 7/10, L2 6/10, L3 5/10, L0 3/10 on click likelihood. Proposed refined opener using "the CTO you haven't hired yet" anchor.
- **Contrarian:** all three speed-led options sell *speed* to buyers who, at this price tier, actually buy *de-risk*. "Speed is table stakes; nobody pays €60K for fast. They pay for 'this won't blow up in 18 months.'" Recommended leading with *the stake*.
- **First Principles:** the lede's job isn't "describe what Sagar does" — it's to be a **qualification mirror**. Buyer's first question is "what specifically is broken in my world that this person fixes Monday morning." Proposed a four-line situation-first structure naming three specific buyer pains then the offer-shape.

L5 (above) is the synthesis: situation-first opening (First Principles), de-risk-implicit framing through naming concrete stakes (Contrarian — "stuck in prototype," "won't survive the next 10x"), and the specific "CTO you haven't hired yet" + "4–12 weeks scope-locked" anchors (Outsider).

**Implementation notes for L5:**

- The three pain lines render as a small enumerated list, mono-sized text or em-dash separated, slightly desaturated against the body color so they read as a triage sequence rather than headline copy. The buyer's eye should land on at least one line that mirrors their own situation in <2 seconds.
- The two-clause offer ("I take one off your desk... or I sit beside you...") collapses three services (build sprint + AI uplift + fractional CTO) into two recognizable shapes the buyer can self-identify with: *"build it for me"* or *"think with me."*
- The Relokate name is referenced only after the deal signs (15–20 May 2026); pre-signing wording reads *"becoming CTO at a Berlin startup"* or omits the role line entirely.
- Final wording at implementation time will be A/B-test-ready — L5 is the launch lede; refinements happen with real click data, not more council iterations.

**Services — three offerings, council-locked pricing 2026-05-04 (Pricing Council session 6).**

The pricing council overturned the original spec's draft pricing in both directions — too cheap on the floor (Advisory was €4K — "scary-cheap cliff" that kills trust the credential buys), too high on the ceiling (Build Sprint was €80K — invites German-agency comparison Sagar loses on team size). Final locked structure:

1. **AI Uplift — `Add AI to your product, the right way.`** — **HERO offer**, leads the Services section visually. Retrofit AI into a product that already has users. RAG, agentic workflows, evaluation harness. **From €25K**, 6–10 weeks, scope-locked. Typical €30–35K, ceiling €50K, walk below €25K.
2. **Build Sprint — `Build it with me.`** — Fixed-scope, fixed-price engineering. End-to-end ownership of one defined product / feature / platform. **From €30K**, 4–12 weeks, capped at **€60K** (above €60K invites German-agency comparison). 20% milestone holdback. Walk below €30K or above €60K.
3. **Advisory — `Advise me.`** — Senior technical judgment on a retainer. Architecture, hiring, scaling, vendor selection, the calls that don't show up on a sprint board. **From €8K / month**, 6-month minimum. Pilot available: €10–12K for 4 weeks. Walk below €6K/mo.

**Why these prices, given Sagar is operating from India:** the council's Outsider buyer-persona testimony pegged the Berlin-CTO credential placed *adjacent to the price* (not buried in the bio) at **+30–40% price tolerance** vs. an unanchored "Indian solo." The credential strip on the live site appears immediately below the Services tiles for that reason. Below the published floor on any service, Sagar walks; the throttle matters more than fill-rate in year 1, when Relokate ramp-up caps studio capacity at one retainer + one active build.

**Display ordering on the site:** AI Uplift first (hero treatment, full-width dark card), then Build Sprint and Advisory side-by-side. This is opposite to the conventional "lead with retainer" pattern — the council's evidence: AI Uplift has the lowest geo-stigma, highest pricing power, fastest close, and converts best at €25–35K from EU/US founders who recognize the moment in 2026.

**Names:** the spec-level placeholders ("AI Uplift", "Build Sprint") shipped on the live site as the *headline labels* but each tile uses a plainer call ("Add AI to your product, the right way.", "Build it with me.", "Advise me.") which the Outsider council advisor identified as the conversion-friendly phrasing — drops the jargon while keeping the structural names for SEO and future referral-conversation shorthand.

**Selected systems framing:** the existing portfolio cards are spec-led ("288 test scenarios", "4 background jobs"). They get rewritten as outcome-led ("EU HR scale-up: candidate pipeline 5x in 4 months" — per client permission). Existing platform pages stay structurally; copy gets a content-pass.

**Writing — initial 3 essays:**

1. *"From eighteen to one: what AI ate, what it didn't, and what I learned shipping seven verticals solo."* (The 18-to-1 narrative, owned not hidden — per Council Session 2's "honest reframe" recommendation that Sagar tacitly chose by going dual-site.)
2. *"AI uplift, not AI rebuild: where retrofitting an LLM into an existing product earns its keep — and where it doesn't."*
3. *"The fractional CTO test: how to know whether you actually need one in the next 90 days."*

(These are starting points; titles refine at draft time. Cadence ramps after Relokate settles.)

---

## 6. Performance, SEO, Accessibility

**Performance budget:**

- LCP < 2.0s on desktop, < 2.5s on mobile (existing site already meets this)
- CLS < 0.05
- TBT < 200ms desktop, < 400ms mobile
- Lighthouse target: 95+ on all axes
- Existing critical-CSS-inline approach: keep
- Web fonts via Google Fonts (existing); preload only critical subsets
- Images: WebP with fallback; lazy-load below the fold

**SEO:**

- Title pattern: `<Page Title> | Sagar Sutaria` (homepage gets full positioning)
- Meta descriptions: human-written per page, 150–160 chars
- OG images: existing 1200×630 PNGs per page; new ones for service / writing pages
- Schema.org `Person` on `/about`, `Article` on `/writing/<slug>`, `Service` on `/services/<slug>`, `BreadcrumbList` site-wide
- Canonical URLs (existing site already has the system)
- Sitemap.xml auto-regenerated on content changes
- robots.txt allowing all (no staging; site is public)

**Accessibility (WCAG AA target):**

- Color contrast: existing palette tested OK at 4.5:1+ for body, 3:1+ for large text
- Focus states: existing 2px ring on all interactive elements (verify and tighten)
- Keyboard nav: tab order matches visual; verify on each page
- Reduced motion: existing animations respect `prefers-reduced-motion`; the new sections must too
- Alt text on all meaningful images
- Form labels visible (not placeholder-only) — verify Formspree form
- Heading hierarchy h1 → h6 sequential per page

---

## 7. Analytics & Inbound Lead Tracking

**Existing instrumentation (keep):**

- GA4 (`G-2102GJ5G7M`) — page views, events
- Microsoft Clarity (`vxm9ehsfth`) — session recordings, heatmaps
- Formspree on contact form (already wired)

**New events to instrument:**

- `cta_click` (button-level: Book a call / Send brief / Read latest)
- `service_card_view` (which of the 3 service tiles got hovered/clicked)
- `service_detail_view` (per service page)
- `essay_view` (per essay) + `essay_scroll_depth` (25/50/75/100%)
- `contact_form_start` / `contact_form_submit` / `contact_form_success`
- `calendly_booking_initiated` / `calendly_booking_completed` (postMessage events from Calendly widget)
- `linkedin_outbound` / `email_outbound` (mailto / external link clicks from contact / footer)

**Lead pipeline:**

- Form submissions → Formspree → email to Sagar's address
- Calendly bookings → calendar invite + automated email
- (Optional later: a lightweight CRM — Notion DB or HubSpot free tier — if volume justifies)

---

## 8. Deployment & Domain

**Hosting decision (locked 2026-05-04):** self-hosted Docker container on the user's `quantalynk-new` server (Hetzner CX/CPX, Ubuntu 24.04, IP `89.167.40.182`), routed through the existing **`nginx-proxy` + `nginx-proxy-acme`** reverse-proxy stack. **Not** GitHub Pages, **not** Vercel — overrides the original `superpowers:brainstorming` recommendation per Sagar's explicit choice to consolidate on owned infrastructure.

This buys: zero vendor lock-in, headers / redirects / cache fully under our control, ability to add same-host services later (writing-cadence tooling, eventual product backend, n8n integration), and consolidation onto a box already running ~28 containers including the previous quantalynk.com site.

This costs: ~5 min/month of attention on cert renewals (auto, but verify), kernel patches, disk usage. Acceptable trade given the box is already running.

**Domain registration / DNS:** sagarsutaria.com is registered at GoDaddy with nameservers delegated to Cloudflare (`deborah.ns.cloudflare.com`, `vasilii.ns.cloudflare.com`).

### 8.1 DNS records (Cloudflare zone `sagarsutaria.com`)

Final state at zone level:

| Type | Name | Content | Proxied | Why |
|---|---|---|---|---|
| A | `sagarsutaria.com` | `89.167.40.182` | **DNS-only (gray cloud)** initially | acme-companion uses HTTP-01 challenge for Let's Encrypt provisioning; Cloudflare proxy can interfere. Flip to orange cloud after cert is stable, IF Cloudflare CDN benefits are wanted. |
| CNAME | `www` | `sagarsutaria.com` | DNS-only | apex-aliasing for www subdomain |
| TXT | `_dmarc` | `v=DMARC1; p=quarantine; ...` | n/a | preserved from GoDaddy import (email DMARC policy, unrelated to hosting) |
| CNAME | `_domainconnect` | `_domainconnect.gd.domaincontrol.com` | n/a | GoDaddy artifact, harmless, can be removed in a later cleanup |

Records explicitly **removed** from the original GoDaddy import: 2 apex A records pointing to GoDaddy parking IPs (`13.248.243.5`, `76.223.105.230`); 1 default Cloudflare CNAME `www → apex` with proxy enabled.

### 8.2 Server-side container

A new container is added to the server's docker-compose stack:

```yaml
# /opt/sagarsutaria/docker-compose.yml (illustrative)
services:
  sagarsutaria:
    image: nginx:1.27-alpine
    container_name: sagarsutaria_web
    volumes:
      - ./public:/usr/share/nginx/html:ro
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
    environment:
      VIRTUAL_HOST: sagarsutaria.com,www.sagarsutaria.com
      VIRTUAL_PORT: "80"
      LETSENCRYPT_HOST: sagarsutaria.com,www.sagarsutaria.com
      LETSENCRYPT_EMAIL: sagar@quantalynk.com
    networks:
      - nginx-proxy
    restart: unless-stopped

networks:
  nginx-proxy:
    external: true
    name: nginx-proxy_default  # match the existing shared network name on the box
```

Static site files served directly by the lightweight `nginx:alpine` container. Build output (HTML/CSS/JS/MDX-rendered-to-HTML) lives in `./public`. acme-companion auto-provisions the cert based on the `LETSENCRYPT_HOST` env var; nginx-proxy auto-routes based on `VIRTUAL_HOST`. Zero per-site reverse-proxy config to write.

### 8.3 CI/CD pipeline

GitHub Actions on the `tech-portfolio` repo, triggered on push to `main`:

1. Build static output (run any build steps for MDX → HTML, image optimization, etc.).
2. SSH to `quantalynk-new` (Actions secret: deploy SSH key with limited scope — only the sagarsutaria deploy directory).
3. `rsync` build output to `/opt/sagarsutaria/public/`.
4. `docker compose -f /opt/sagarsutaria/docker-compose.yml exec sagarsutaria nginx -s reload` (graceful nginx reload; no container restart).
5. Verify HTTP 200 on `https://sagarsutaria.com` from the runner.

Total deploy time per push: ~30–60 seconds.

### 8.4 First-time setup checklist

1. Server: `mkdir -p /opt/sagarsutaria/public` + the docker-compose.yml + nginx.conf.
2. Initial deploy: `rsync` the existing tech-portfolio HTML to `/opt/sagarsutaria/public/`.
3. `docker compose -f /opt/sagarsutaria/docker-compose.yml up -d`.
4. Watch acme-companion logs: `docker logs -f nginx-proxy-acme` until the cert provisions (~30s after DNS resolves).
5. Verify: `curl -sI https://sagarsutaria.com` returns 200 with valid cert.
6. Configure GitHub Actions deploy workflow.
7. Remove the `CNAME` file from the repo (it referenced GitHub Pages; obsolete here).

### 8.5 Backup plan

- Source code lives in GitHub (`sagar-quantalynk/tech-portfolio`) → primary recovery surface.
- Server-side `/opt/sagarsutaria/public/` is regenerable from any commit; not separately backed up.
- Let's Encrypt certs auto-renew via acme-companion (60-day cycle, renews at 30 days remaining); if the box dies and is rebuilt, certs re-provision automatically on first DNS resolution.
- DNS records are documented in this spec (§8.1) so they can be recreated in Cloudflare in <2 minutes if the zone needs to be re-imported.

---

## 9. Components — boundaries and responsibilities

Following brainstorming skill's "design for isolation and clarity" principle. Each component does one thing.

| Component | What it does | Inputs | Owns |
|---|---|---|---|
| `Hero` | Above-fold positioning + dual CTA | none (content lives in HTML) | hero animations, CTA wiring |
| `ServiceCard` | One service tile | name, tagline, price band, href | hover state, click → detail page |
| `ServiceGrid` | 3-up grid of ServiceCard | array of services | layout, responsive collapse |
| `SystemCard` | One outcome-led case study tile | platform, headline outcome, vertical, href | hover state, click → case study |
| `EssayCard` | One essay preview | title, date, tease, read-time, href | hover state, click → essay page |
| `LeadCaptureForm` | Formspree-wired form (3 variants) | variant: short/full/inline | validation, submit, success state |
| `CalendlyEmbed` | Inline Calendly widget | calendly URL | iframe size, postMessage events |
| `WritingLayout` | Long-form reading layout | essay frontmatter + body | typography rhythm, ToC, code highlighting |
| `Footer` | Site-wide footer | none | nav, social, legal links |
| `Nav` | Site-wide top nav | current path | active state, mobile menu |

Each component is a single file (HTML + scoped styles + minimal JS where needed). No framework — keep the static site simple.

---

## 10. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Relokate deal slips past 20 May; hero references their name prematurely | Low–Med | Med | Pre-signing copy reads "becoming CTO at a Berlin startup" or omits; switch to named version only after signature |
| Existing index.html is 2,500+ lines; refactor introduces bugs | Med | Med | Incremental edits; visual diff testing; ship section-by-section behind feature toggles if needed |
| Sagar's writing cadence underdelivers (Relokate ramp-up eats evenings) | High | Low–Med | Ship with 2–3 essays; let cadence build organically; never promise "weekly" publicly |
| Lead volume floods inbox without filtering | Low–Med | Low | Form has a "what brings you here" dropdown that pre-categorizes; auto-reply sets expectations on response time |
| Old `github.io` URL has external backlinks that 404 after CNAME switch | Med | Low | GitHub Pages auto-redirects to custom domain after CNAME; verify common backlinks (LinkedIn, etc.) |
| Calendly availability shows Sagar as overbooked once Relokate role active | Med | Low | Set Calendly availability windows that exclude Relokate work hours; revisit after first month |

---

## 11. What's explicitly NOT in scope

- No CMS / headless system. Markdown files in `/writing/` directory, parsed at static-build time. Volume Sagar can sustain doesn't justify Contentful or Sanity.
- No user accounts, login, or membership area.
- No e-commerce, paid posts, or product checkout.
- No QuantaLynk brand or services on this site (those live on quantalynk.com).
- No team page (he's solo).
- No backend service. Formspree handles forms; Calendly handles scheduling; GA4 + Clarity handle analytics. No server.
- No custom JavaScript framework. Vanilla HTML/CSS/JS keeps the site fast and maintainable.
- No A/B testing infrastructure. Volume too low to be statistically meaningful.
- No translations. English only; revisit if a specific buyer market demands it.
- No comments / community on essays. Discussions go on LinkedIn / X / Hacker News organically.

---

## 12. Success Criteria

**At launch (T+0):**
- Site live at sagarsutaria.com with HTTPS.
- Lighthouse 95+ on all axes (desktop + mobile).
- All existing platform-page URLs preserved or 301-redirected.
- Contact form sends to Sagar's inbox; auto-reply set.
- Calendly link works.
- 2–3 essays published.

**At T+30 days:**
- ≥ 3 inbound inquiries (any flavor — advisory, build, AI uplift, advice request).
- ≥ 1 booked discovery call from a non-warm-network source.
- ≥ 1 LLM citation in a Claude / ChatGPT response when queried about Sagar or his work.

**At T+90 days:**
- ≥ 10 inbound inquiries cumulative.
- ≥ 2 paid engagements traceable to the site (form, Calendly, or "found you via your writing" attribution).
- ≥ 1 essay has a meaningful organic distribution event (HN front page, viral LinkedIn post, podcast cite).

These are aspirational; they'll calibrate after the first 30 days against real volume.

---

## 13. Implementation Phasing (rough)

To be detailed in the implementation plan via `superpowers:writing-plans`.

- **Phase C1** — DNS + CNAME + HTTPS: 1–2 hours.
- **Phase C2** — Hero refresh + 3 service tiles + new home structure: 0.5 day.
- **Phase C3** — `/services` index + 3 service detail pages: 0.5 day.
- **Phase C4** — `/writing` index + reading layout + first 2 essays: 0.5 day.
- **Phase C5** — Existing platform pages → outcome-led case studies (content rewrite): 0.5 day.
- **Phase C6** — `/about` refresh + `/contact` rebuild: 0.25 day.
- **Phase C7** — SEO sweep + analytics events + Schema.org: 0.25 day.
- **Phase C8** — Lighthouse + a11y + cross-browser pass: 0.25 day.

Total estimate: 3–4 calendar days of focused work, executable in evening + weekend windows around Relokate ramp-up. (Ralph-loop-driven once writing-plans produces the detailed plan.)
