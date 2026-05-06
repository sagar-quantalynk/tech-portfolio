#!/usr/bin/env python3
"""
Generate per-essay OG preview HTML files from a single template.
Reads scripts/essay-preview-template.html, writes assets/{slug}-preview.html
for each essay in MANIFEST.

Run: python3 scripts/generate-essay-previews.py
Then: node scripts/generate-og-images.mjs   # to render PNGs
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "scripts" / "essay-preview-template.html"
ASSETS = ROOT / "assets"

# Per-essay manifest. Headline_html is the raw <h1> markup with <em> on the
# emphasized phrase (matches portfolio-preview.html's <em> + .stamped pattern).
# Tagline = TL;DR-style subhead, ~15-20 words. Key stat is OPTIONAL — emit
# only when the essay has a quotable single number worth surfacing.
#
# Headline-size auto-tuning: longer headlines get smaller font.
MANIFEST = [
    # === ESSAYS ===
    {
        "slug": "fractional-cto-vs-full-time-cto",
        "slug_path": "writing/fractional-cto-vs-full-time-cto",
        "title": "Fractional CTO vs full-time CTO",
        "sheet": "W-01",
        "category": "ESSAY",
        "eyebrow": "Engineering leadership / decision frame",
        "headline_html": "Fractional CTO <em>vs</em> full-time CTO: when each makes sense.",
        "headline_size": 56,
        "tagline": "A stage decision, not a price decision. How to tell which one your company actually needs this quarter.",
        "read_time": "9 MIN READ",
        "pub_date": "4 MAY 2026",
        "topic": "Fractional CTO",
        "key_stat_label": "Threshold",
        "key_stat_value": '<span class="v-pencil">8 engineers</span>',
    },
    {
        "slug": "fractional-cto-vs-technical-cofounder",
        "slug_path": "writing/fractional-cto-vs-technical-cofounder",
        "title": "Fractional CTO vs technical co-founder",
        "sheet": "W-02",
        "category": "ESSAY",
        "eyebrow": "Founder choice / cash vs equity",
        "headline_html": "Fractional CTO vs <em>technical co-founder</em>: which fits your stage?",
        "headline_size": 54,
        "tagline": "Cash versus equity. Bounded engagement versus lifetime commitment. Two shapes that are not substitutes for each other.",
        "read_time": "7 MIN READ",
        "pub_date": "5 MAY 2026",
        "topic": "Founder hiring",
        "key_stat_label": "Trade",
        "key_stat_value": '<span class="v-blue">Cash &harr; Equity</span>',
    },
    {
        "slug": "do-you-need-a-fractional-cto-at-seed-stage",
        "slug_path": "writing/do-you-need-a-fractional-cto-at-seed-stage",
        "title": "Do you actually need a fractional CTO at seed stage",
        "sheet": "W-03",
        "category": "ESSAY",
        "eyebrow": "Seed stage / honest answer",
        "headline_html": "Do you <em>actually</em> need a fractional CTO at seed stage?",
        "headline_size": 54,
        "tagline": "Most seed-stage founders do not. Here is how to tell if you are the exception, and what to spend the money on instead.",
        "read_time": "7 MIN READ",
        "pub_date": "5 MAY 2026",
        "topic": "Seed stage CTO",
        "key_stat_label": "Verdict",
        "key_stat_value": '<span class="v-pencil">Probably not yet</span>',
    },
    {
        "slug": "hiring-fractional-cto-from-india",
        "slug_path": "writing/hiring-fractional-cto-from-india",
        "title": "Hiring a fractional CTO from India",
        "sheet": "W-04",
        "category": "ESSAY",
        "eyebrow": "Cross-border hiring / EU + US buyers",
        "headline_html": "Hiring a fractional CTO <em>from India</em>: the buyer&rsquo;s checklist.",
        "headline_size": 54,
        "tagline": "Every objection European and US founders raise in diligence, the real answer, and the pricing arbitrage you actually capture.",
        "read_time": "9 MIN READ",
        "pub_date": "4 MAY 2026",
        "topic": "Cross-border CTO",
        "key_stat_label": "Arbitrage",
        "key_stat_value": '<span class="v-blue">35-50% lower</span>',
    },
    {
        "slug": "what-to-ask-before-signing-fractional-cto-contract",
        "slug_path": "writing/what-to-ask-before-signing-fractional-cto-contract",
        "title": "What to ask before signing a fractional CTO contract",
        "sheet": "W-05",
        "category": "ESSAY",
        "eyebrow": "Diligence / discovery call",
        "headline_html": "<em>Eleven questions</em> to ask before signing a fractional CTO retainer.",
        "headline_size": 54,
        "tagline": "Asked in the last fifteen minutes of discovery, they cut a wrong-fit retainer in 30 minutes instead of 3 months.",
        "read_time": "8 MIN READ",
        "pub_date": "4 MAY 2026",
        "topic": "Contract diligence",
        "key_stat_label": "Saves",
        "key_stat_value": '<span class="v-pencil">3 wrong-fit months</span>',
    },
    {
        "slug": "quantalynk-vs-toptal",
        "slug_path": "writing/quantalynk-vs-toptal",
        "title": "QuantaLynk vs Toptal",
        "sheet": "W-06",
        "category": "ESSAY",
        "eyebrow": "Comparison / boutique vs network",
        "headline_html": "QuantaLynk <em>vs</em> Toptal: when each makes sense.",
        "headline_size": 60,
        "tagline": "Two different shapes of senior engineering help. A boutique senior studio versus a vetted freelancer network. Honest comparison.",
        "read_time": "8 MIN READ",
        "pub_date": "4 MAY 2026",
        "topic": "Buyer comparison",
        "key_stat_label": "Shape",
        "key_stat_value": '<span class="v-blue">Studio vs Network</span>',
    },
    {
        "slug": "replatforming-legacy-saas",
        "slug_path": "writing/replatforming-legacy-saas",
        "title": "Replatforming legacy SaaS",
        "sheet": "W-07",
        "category": "ESSAY",
        "eyebrow": "Migration / without a full rewrite",
        "headline_html": "Replatforming legacy SaaS <em>without</em> a full rewrite.",
        "headline_size": 56,
        "tagline": "Stranglers, parallel runs, traffic gates. Four moves that keep customers happy while engineering migrates to a modern stack.",
        "read_time": "11 MIN READ",
        "pub_date": "4 MAY 2026",
        "topic": "Replatforming",
        "key_stat_label": "Without",
        "key_stat_value": '<span class="v-pencil">Stopping shipping</span>',
    },
    {
        "slug": "what-ai-integration-actually-costs",
        "slug_path": "writing/what-ai-integration-actually-costs",
        "title": "What an AI integration project actually costs",
        "sheet": "W-08",
        "category": "ESSAY",
        "eyebrow": "AI integration / 2026 pricing reality",
        "headline_html": "What an AI integration <em>actually</em> costs in 2026.",
        "headline_size": 60,
        "tagline": "Honest pricing for adding AI to a product that already has users. Bands a senior shop will quote, the variables that move the price.",
        "read_time": "10 MIN READ",
        "pub_date": "4 MAY 2026",
        "topic": "AI cost reality",
        "key_stat_label": "Range",
        "key_stat_value": '<span class="v-blue">&euro;25K-150K typical</span>',
    },
    {
        "slug": "ai-integration-in-regulated-industries",
        "slug_path": "writing/ai-integration-in-regulated-industries",
        "title": "AI integration in regulated industries",
        "sheet": "W-09",
        "category": "ESSAY",
        "eyebrow": "Regulated / cost multipliers",
        "headline_html": "AI integration in <em>regulated</em> industries: what changes the budget.",
        "headline_size": 54,
        "tagline": "HR, healthcare, legal, finance. The seven cost multipliers, the contract clauses that matter, how to scope what ships compliantly.",
        "read_time": "9 MIN READ",
        "pub_date": "4 MAY 2026",
        "topic": "Regulated AI",
        "key_stat_label": "Multipliers",
        "key_stat_value": '<span class="v-pencil">7 of them</span>',
    },
    # === HUBS ===
    {
        "slug": "fractional-cto-hub",
        "slug_path": "writing/fractional-cto",
        "title": "Fractional CTO: founder's guide",
        "sheet": "W-H1",
        "category": "HUB",
        "eyebrow": "Founder&rsquo;s guide / five essays",
        "headline_html": "Fractional CTO: <em>when</em>, <em>what it costs</em>, <em>what to verify</em>.",
        "headline_size": 50,
        "tagline": "Five essays answering every question that comes up at every stage of the fractional CTO hiring decision.",
        "read_time": "5 ESSAYS",
        "pub_date": "MAY 2026",
        "topic": "Fractional CTO",
        "key_stat_label": "Essays",
        "key_stat_value": '<span class="v-blue">W-01 &rarr; W-06</span>',
    },
    {
        "slug": "replatforming-hub",
        "slug_path": "writing/replatforming",
        "title": "Replatforming SaaS: hub",
        "sheet": "W-H2",
        "category": "HUB",
        "eyebrow": "Founder&rsquo;s hub / three essays",
        "headline_html": "Replatforming a SaaS <em>without</em> a full rewrite: the framework.",
        "headline_size": 52,
        "tagline": "A founder&rsquo;s hub on migrating legacy SaaS, on adding AI to a product that has users, on what regulated constraints do to budget.",
        "read_time": "3 ESSAYS",
        "pub_date": "MAY 2026",
        "topic": "Replatforming + AI",
        "key_stat_label": "Essays",
        "key_stat_value": '<span class="v-blue">W-07 &rarr; W-09</span>',
    },
    # === REFERENCE ===
    {
        "slug": "answers",
        "slug_path": "answers",
        "title": "Answers: fractional CTO, AI integration, replatforming",
        "sheet": "W-A",
        "category": "REFERENCE",
        "eyebrow": "Reference / twenty answers",
        "headline_html": "<em>Answers</em>: fractional CTO, AI integration, replatforming.",
        "headline_size": 54,
        "tagline": "Direct answers to twenty common questions. Distilled from longer essays. Prices effective May 2026, reviewed quarterly.",
        "read_time": "20 ANSWERS",
        "pub_date": "MAY 2026",
        "topic": "Reference",
        "key_stat_label": "Updated",
        "key_stat_value": '<span class="v-pencil">Quarterly</span>',
    },
]


def render(template: str, entry: dict) -> str:
    key_stat_block = ""
    if entry.get("key_stat_label") and entry.get("key_stat_value"):
        key_stat_block = (
            f"<dt>{entry['key_stat_label']}</dt>"
            f"<dd>{entry['key_stat_value']}</dd>"
        )
    return (
        template
        .replace("{{TITLE}}", entry["title"])
        .replace("{{SHEET_NUMBER}}", entry["sheet"])
        .replace("{{CATEGORY}}", entry["category"])
        .replace("{{EYEBROW}}", entry["eyebrow"])
        .replace("{{HEADLINE_HTML}}", entry["headline_html"])
        .replace("{{HEADLINE_SIZE}}", str(entry["headline_size"]))
        .replace("{{TAGLINE}}", entry["tagline"])
        .replace("{{READ_TIME}}", entry["read_time"])
        .replace("{{PUB_DATE}}", entry["pub_date"])
        .replace("{{TOPIC}}", entry["topic"])
        .replace("{{SLUG_PATH}}", entry["slug_path"])
        .replace("{{KEY_STAT_BLOCK}}", key_stat_block)
    )


def main():
    template = TEMPLATE.read_text(encoding="utf-8")
    print(f"Loaded template: {TEMPLATE} ({len(template)} bytes)")

    written = []
    for entry in MANIFEST:
        out_path = ASSETS / f"{entry['slug']}-preview.html"
        rendered = render(template, entry)
        out_path.write_text(rendered, encoding="utf-8")
        written.append(out_path)
        print(f"  wrote {out_path.relative_to(ROOT)} (sheet {entry['sheet']})")

    print(f"\nGenerated {len(written)} essay preview HTML files.")
    print("Next: node scripts/generate-og-images.mjs")


if __name__ == "__main__":
    main()
