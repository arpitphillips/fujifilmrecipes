#!/usr/bin/env python3
"""Scan the built site for AI-writing tells (Wikipedia "Signs of AI writing").

Run after build.py:  python3 site/audit.py [--top N]

Checks rendered page text (tags stripped) for the patterns most associated
with machine-generated prose: em dash overuse, AI vocabulary, negative
parallelisms, superficial participle endings, curly quotes, emoji in prose,
and heavy boldface. Prints per-page counts so the worst pages can be fixed
first, and exits non-zero if the template-authored pages are not clean.
"""

import re
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "_site"

# Pages whose prose lives in the Jinja templates (must be spotless).
TEMPLATE_PAGES = {"index.html", "about/index.html", "contact/index.html",
                  "community/index.html", "knowledge/index.html"}

AI_VOCAB = [
    r"\bdelve", r"\btestament\b", r"\bshowcas(?:e|es|ing)\b",
    r"\bunderscor(?:e|es|ing)\b", r"\bpivotal\b", r"\bcrucial\b",
    r"\btapestry\b", r"\bboasts?\b", r"\bnestled\b", r"\bseamless",
    r"\bbreathtaking\b", r"\bstunning\b", r"\bgroundbreaking\b",
    r"\belevat(?:e|es|ing)\b", r"\bgame.chang", r"\bmust.visit\b",
    r"\bserves? as\b", r"\bstands? as\b", r"\bmarks? a\b",
    r"\bat its core\b", r"\bthe real question\b", r"\bin today's\b",
    r"\bever.evolving\b", r"\brich cultural\b", r"\bvibrant\b",
]
NEG_PARALLEL = [r"\bnot just\b", r"\bnot only\b", r"\bnot merely\b",
                r"\bisn't just\b", r"\bmore than just\b"]
ING_TAILS = [r",\s+(?:highlighting|underscoring|emphasizing|reflecting|"
             r"symbolizing|showcasing|fostering|cultivating|ensuring|"
             r"contributing to|demonstrating)\b"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")

# Glyphs that are data notation, not prose decoration: the gallery placeholder
# frame and the coverage/status marks used in comparison tables and legends.
EXEMPT_GLYPHS = {"🎞️", "🎞", "✅", "❌", "📗", "🔎", "🔶", "⚠️", "⚠", "🎬"}


def strip_tables(html: str) -> str:
    return re.sub(r"<table.*?</table>", " ", html, flags=re.S)


def page_text(html: str) -> str:
    html = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    html = re.sub(r"<title>.*?</title>", " ", html, flags=re.S)
    return re.sub(r"<[^>]+>", " ", html)


def audit_page(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    text = page_text(html)
    # Style patterns (em dash, quotes, bold) are prose tells; tables use em
    # dashes as empty-value markers and bold as row keys, so measure prose only.
    prose_html = strip_tables(html)
    prose = page_text(prose_html)
    for glyph in EXEMPT_GLYPHS:
        text = text.replace(glyph, "")
        prose = prose.replace(glyph, "")
    counts = {
        "em_dash": prose.count("—"),
        "curly_quotes": len(re.findall(r"[“”]", prose)),
        "ai_vocab": sum(len(re.findall(p, text, re.I)) for p in AI_VOCAB),
        "neg_parallel": sum(len(re.findall(p, text, re.I)) for p in NEG_PARALLEL),
        "ing_tails": sum(len(re.findall(p, text, re.I)) for p in ING_TAILS),
        "emoji": len(EMOJI.findall(text)),
        "bold": prose_html.count("<strong>"),
    }
    counts["score"] = (counts["em_dash"] + counts["curly_quotes"]
                       + 3 * counts["ai_vocab"] + 3 * counts["neg_parallel"]
                       + 3 * counts["ing_tails"] + 2 * counts["emoji"]
                       + max(0, counts["bold"] - 8))
    return counts


def main():
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 15
    results = {}
    for page in sorted(OUT.rglob("index.html")):
        rel = str(page.relative_to(OUT))
        results[rel] = audit_page(page)

    template_dirty = {p: c for p, c in results.items()
                      if p in TEMPLATE_PAGES and c["score"] > 0}
    worst = sorted(results.items(), key=lambda kv: -kv[1]["score"])[:top]

    print(f"{'page':58} {'score':>5} {'—':>4} {'“”':>4} {'vocab':>5} "
          f"{'negpar':>6} {'-ing':>5} {'emoji':>5} {'bold':>4}")
    for p, c in worst:
        print(f"{p:58} {c['score']:>5} {c['em_dash']:>4} {c['curly_quotes']:>4} "
              f"{c['ai_vocab']:>5} {c['neg_parallel']:>6} {c['ing_tails']:>5} "
              f"{c['emoji']:>5} {c['bold']:>4}")

    total = sum(c["score"] for c in results.values())
    clean = sum(1 for c in results.values() if c["score"] == 0)
    print(f"\ntotal score {total} across {len(results)} pages ({clean} clean)")

    if template_dirty:
        print("\nTEMPLATE PAGES NOT CLEAN:")
        for p, c in template_dirty.items():
            print(f"  {p}: {c}")
        sys.exit(1)
    print("template pages clean")


if __name__ == "__main__":
    main()
