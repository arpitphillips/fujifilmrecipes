# Fujifilm Recipes — Agent Orientation

**Read this first. Then open [CHANGELOG.md](CHANGELOG.md) — and log every change you make there before ending your session.** That is the one non-negotiable rule of this repo.

## What this project is

A curated, research-backed bank of **Fujifilm film-simulation recipes** (in-camera JPEG grades) for the **X-T5 (X-Trans V)**, plus the knowledge layer that explains and validates them. The long-term goal is a **sellable recipe bank**: original, validated recipes are the product ("clean IP"); attributed third-party recipes are kept only as research/benchmarking references.

Core philosophy (grounded in [Knowledge/color-science-why-film-cannot-be-faked.md](Knowledge/color-science-why-film-cannot-be-faked.md)): Fujifilm's simulations are physics-based models that cannot be replicated in post — so the **in-camera JPEG is the archival primary**, and every recipe must be understandable as *base film sim + modifiers*.

## Structure map

```
/                        ← you are here
├── CLAUDE.md            ← this file
├── CHANGELOG.md         ← system changelog — ALWAYS update
├── Knowledge/           ← the reference layer (what settings do, color science,
│                          film chemistry, validation methodology). Start at its README.
└── X-T5/                ← the recipe bank for the X-T5 body
    ├── README.md        ← recipe index + conventions
    ├── RANKING.md       ← full bank ranked by aesthetic × popularity
    ├── x-t5_manual_en_s_f.pdf   ← Owner's Manual (IQ settings: Ch.6, pp.122–132)
    ├── x-t5_nfg_en_s_f.pdf      ← New Features Guide (fw 4.30)
    ├── _reference-sources/      ← drop-folder for source PDFs/scans used in validation
    ├── originals/       ← THE PRODUCT: validated / research-derived / original designs
    │   ├── <color recipes at root>   (kodak-gold-200, fujicolor-superia-400, mumbai…)
    │   ├── cinema/      ← Vision3 250D/500T, 2383 print
    │   ├── black-and-white/  ← Acros 100, HP5 Plus, Tri-X 400
    │   └── creative/    ← designed looks, not film emulations
    └── reference-recipes/   ← attributed recipes (Fuji X Weekly etc.) for benchmarking
```

## Per-recipe folder convention

```
<recipe-name>/
├── recipe.md        ← exact camera settings (table format — copy an existing one)
├── knowledge.md     ← grade analysis: film history, why each setting (originals + analysed refs)
├── recipe-video.md  ← movie-mode translation (originals only; sometimes inline in recipe.md)
├── research.md / validation.md  ← flagship originals only
├── references/      ← drop real film scans here to validate/tune the recipe
└── test-shots/      ← drop your own X-T5 frames shot with the recipe here
```

## Rules for agents

1. **Log every change in [CHANGELOG.md](CHANGELOG.md)** — newest entry at top, follow the entry template there.
2. **Never delete or overwrite user-dropped files** in `references/`, `test-shots/`, `_reference-sources/`.
3. **Follow the existing file formats.** New recipe.md = same table; new recipes get `references/` + `test-shots/` with the standard one-line READMEs. Copy from an existing folder.
4. **Keep the two tiers separate.** New attributed/web-sourced recipes → `reference-recipes/` with a Source hyperlink to the original page. Only research-derived or validated work goes in `originals/` (see [Knowledge/validation-methodology.md](Knowledge/validation-methodology.md) for promotion criteria).
5. **X-Trans V only** — porting an X-Trans IV recipe requires the Color Chrome FX Blue adjustment (see [Knowledge/x-trans-v-and-conversion.md](Knowledge/x-trans-v-and-conversion.md)). Note the port in the recipe file.
6. **Update the indexes** — a new recipe must be added to `X-T5/README.md` (correct tier table) and, if ranked, `RANKING.md`.
7. **All links relative**; run a quick link check after moving anything.
8. **Knowledge files carry their sources** — every claim ties to a source line at top or a citation inline; keep the `*Last updated: YYYY-MM-DD*` footer current.
9. **Continuous pro-tip enrichment (standing user directive, 2026-07-20):** every research iteration must convert findings into practical pro-tips/notes on the recipe listings themselves — not just the knowledge layer. When new evidence lands (official design notes, scan analysis, handling quirks), append a "Pro tip" note to the affected recipe files.

## Key cross-file facts (so you don't re-derive them)

- Recipes are stored in camera slots **C1–C7**; the X-T5 keeps a WB Shift per preset.
- Movie mode lacks Grain / Color Chrome / Clarity → video recipes compensate (see [Knowledge/video-mode-settings.md](Knowledge/video-mode-settings.md)).
- `High ISO NR −4` is the near-universal recipe default; `Clarity ≠ 0` slows shot-to-shot saving.
- Reddit/Cloudflare sites can't be scraped from here — ask the user to drop scans into `references/`.
- Coverage gaps vs. the classic-film canon are tracked in [Knowledge/film-stocks-master-list.md](Knowledge/film-stocks-master-list.md).
