#!/usr/bin/env python3
"""
Patch essay HTML files to add og:image + twitter:image meta tags pointing
at per-essay preview PNGs. Idempotent: re-running upgrades the cache-bust
version if the tags already exist.

Run: python3 scripts/patch-essay-og-tags.py
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
CACHE_BUST = "v=2"
BASE_URL = "https://sagarsutaria.com/assets"

# Map essay HTML path -> preview slug (filename minus -preview.png)
PAGES = [
    ("writing/fractional-cto-vs-full-time-cto.html", "fractional-cto-vs-full-time-cto"),
    ("writing/fractional-cto-vs-technical-cofounder.html", "fractional-cto-vs-technical-cofounder"),
    ("writing/do-you-need-a-fractional-cto-at-seed-stage.html", "do-you-need-a-fractional-cto-at-seed-stage"),
    ("writing/hiring-fractional-cto-from-india.html", "hiring-fractional-cto-from-india"),
    ("writing/what-to-ask-before-signing-fractional-cto-contract.html", "what-to-ask-before-signing-fractional-cto-contract"),
    ("writing/quantalynk-vs-toptal.html", "quantalynk-vs-toptal"),
    ("writing/replatforming-legacy-saas.html", "replatforming-legacy-saas"),
    ("writing/what-ai-integration-actually-costs.html", "what-ai-integration-actually-costs"),
    ("writing/ai-integration-in-regulated-industries.html", "ai-integration-in-regulated-industries"),
    ("writing/fractional-cto/index.html", "fractional-cto-hub"),
    ("writing/replatforming/index.html", "replatforming-hub"),
    ("answers.html", "answers"),
]


def patch_file(path: Path, slug: str) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    original = text

    og_image_url = f"{BASE_URL}/{slug}-preview.png?{CACHE_BUST}"
    og_image_tag = f'<meta property="og:image" content="{og_image_url}">'
    og_image_w = '<meta property="og:image:width" content="1200">'
    og_image_h = '<meta property="og:image:height" content="630">'
    twitter_image_tag = f'<meta property="twitter:image" content="{og_image_url}">'

    # If og:image already exists, replace it (idempotent upgrade)
    if 'property="og:image"' in text:
        text = re.sub(
            r'<meta property="og:image"[^>]*>',
            og_image_tag,
            text,
            count=1,
        )
        text = re.sub(
            r'<meta property="og:image:width"[^>]*>',
            og_image_w,
            text,
            count=1,
        )
        text = re.sub(
            r'<meta property="og:image:height"[^>]*>',
            og_image_h,
            text,
            count=1,
        )
    else:
        # Insert after og:description
        og_desc_match = re.search(
            r'(<meta property="og:description"[^>]*>)',
            text,
        )
        if not og_desc_match:
            return (False, "no og:description anchor found")
        insert = (
            og_desc_match.group(1)
            + "\n"
            + og_image_tag
            + "\n"
            + og_image_w
            + "\n"
            + og_image_h
        )
        text = text.replace(og_desc_match.group(1), insert, 1)

    # twitter:image
    if 'property="twitter:image"' in text:
        text = re.sub(
            r'<meta property="twitter:image"[^>]*>',
            twitter_image_tag,
            text,
            count=1,
        )
    else:
        # Insert after twitter:description (or twitter:card if no description)
        anchor_match = re.search(
            r'(<meta property="twitter:description"[^>]*>)',
            text,
        )
        if not anchor_match:
            anchor_match = re.search(
                r'(<meta property="twitter:card"[^>]*>)',
                text,
            )
        if not anchor_match:
            return (False, "no twitter anchor found")
        insert = anchor_match.group(1) + "\n" + twitter_image_tag
        text = text.replace(anchor_match.group(1), insert, 1)

    if text == original:
        return (False, "no change")
    path.write_text(text, encoding="utf-8")
    return (True, "patched")


def main():
    for rel_path, slug in PAGES:
        path = ROOT / rel_path
        if not path.exists():
            print(f"  SKIP (missing): {rel_path}")
            continue
        ok, msg = patch_file(path, slug)
        status = "OK" if ok else "--"
        print(f"  [{status}] {rel_path}  ->  {slug}-preview.png?{CACHE_BUST}  ({msg})")


if __name__ == "__main__":
    main()
