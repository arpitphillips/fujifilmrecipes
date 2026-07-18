# Validation Methodology, Proof of Faithfulness

The standard every recipe must meet to be promoted to `originals/` and sold. The goal: faithful reproduction, proven against real film, not a single pretty example, and not vibes.

## ⭐ CORE PRINCIPLE: always study BOTH datasheets and real images
For every film look or simulation you MUST, without exception:
1. Read the manufacturer datasheet: characteristic curve (contrast/gamma), RMS granularity / grain index, spectral sensitivity, exposure latitude, balance. The objective physics.
2. Fetch and analyse real reference images: ≥5 across lighting/subjects. A datasheet tells you the physics; only real scans tell you how the film actually renders once shot, developed, and scanned.

Never build a recipe from memory, or from only one of the two. And keep finding new strategies to improve authenticity, new image sources (Reddit, Flickr, Commons, lab galleries, user drops), new datasheets, side-by-side comparisons. This is a continuous discipline, not a one-time check.

Image-fetching strategies (in rough order of reliability):
1. User-provided reference files (downloaded PDFs / scans placed in `X-T5/_reference-sources/`), render with `pdftoppm` and view every page/image. *Best when available.*
2. Direct image download: `Invoke-WebRequest`/`curl` a real scan JPG to disk, then Read it. Works on open hosts (Wikimedia Commons `upload.wikimedia.org`, Flickr static, blog media dirs). Bypasses the browser.
3. Manufacturer / lab galleries: datasheets (fetch PDF → `pdftotext`/`pdftoppm`) for curves + grain, plus lab film-index galleries for real scans.
4. Search → collect many: always gather ≥5 across lighting/subjects (see scan rules) so you're not fitting to an outlier.
5. When a source is bot-protected (Cloudflare), don't fight it; switch hosts, or ask the user to download the page/scans (as was done for Gold 200).
6. Video references (YouTube): the player blocks browser screenshots in this environment, but YouTube serves real auto-generated frame stills as plain JPGs, `https://i.ytimg.com/vi/<VIDEO_ID>/sd1.jpg`, `sd2.jpg`, `sd3.jpg` (~25/50/75% points) and `maxresdefault.jpg` (hero frame). Four genuine frames across different scenes, fetchable with a plain browser-UA request. Caveat: heavy compression → trust hue relationships and treat absolute saturation loosely. (Proven on the Silent Atlas verification, 2026-07-16.)

Record which images were viewed (source, light, subject) in the recipe's `validation.md`. Images are analysis-only, never redistributed in the product.

## The three evidence tiers
A recipe's validation status is one of:

1. Datasheet-validated: grounded in the manufacturer's technical data (balance, ISO/EI, contrast, grain/RMS or grain index, latitude, spectral/skin notes). Establishes the *objective* baseline.
2. Characteristic-validated: corroborated by ≥3 independent, reputable reviews describing the look (cast, contrast, saturation, grain, per-hue behaviour). Establishes the *consensus* look.
3. Scan-validated (pixel): checked against multiple real film scans (see rules below). Establishes the *actual* rendering. Required for the top "validated original" tier.

An original ships with its tier stated. Gold 200 is the reference example (all three tiers → fully scan-validated).

## Scan-validation rules (to avoid building on outliers)
- ≥5 scans per film, from different photographers/sources where possible.
- Spread across lighting: direct sun, flat/overcast, open shade, golden hour, and artificial/night where the film is used there.
- Spread across subjects: at least one each of skin/portrait, foliage/greens, sky/blues, neutral whites/greys, and a saturated accent (red/yellow).
- Note the pipeline: lab scan vs home scan, and scanner, shift results, flag when known, since scanning changes colour as much as the film.
- Read per-channel behaviour explicitly: where do whites sit (warm/cool), how are greens shifted, how saturated are blues, how do highlights roll and shadows hold.
- Reject outliers: if one scan disagrees with the other four, weight the consensus, don't chase the odd one.

## From evidence → settings → proof
Each original records, in its `validation.md` (or `research.md`):
1. The datasheet facts used.
2. The scans analysed (source, light, subject), analysis only, never redistributed; source files kept locally in `X-T5/_reference-sources/`.
3. A trait → setting table (each observed trait mapped to the specific control producing it).
4. What changed because of the evidence (e.g. Gold 200: WB +4R→+3R and Clarity −2→0 after scan analysis).
5. A faithfulness verdict and what's still open (missing conditions, pipeline caveats).

## Quality rules that always apply
- **Clarity = 0 is the *default*, not a hard rule. Keep it at 0 whenever the look allows (avoids halos/artifacts, faster saves). But faithfulness wins**: if the real film's rendering genuinely needs a non-zero Clarity (e.g. the gritty micro-contrast of Tri-X, or a soft dreamy stock), change it, and justify why in the validation. Quality and faithfulness above the preference.
- Faithful reproduction beats stylistic flourish. A recipe is judged by how close it lands, not how "nice" it looks in isolation.
- Prefer fixed WB for colour-critical films (repeatable); use Auto only when the look tolerates scene-to-scene drift.

## Promotion: reference → original
A `reference` recipe (attributed capture) becomes a validated `original` only after it is re-derived from evidence and passes at least datasheet + characteristic validation (scan-validation for the top tier). Copying values is not derivation; the analysis and write-up must be our own. This is both a quality bar and the clean-IP basis for selling the bank.

## Current validation ledger

> **2026-07-15 datasheet audit:** all originals below re-verified against locally archived manufacturer PDFs (`X-T5/_reference-sources/datasheets/`); see [X-T5/VALIDATION-AUDIT.md](../X-T5/VALIDATION-AUDIT.md). The datasheet tier for every film-based original is now archive-backed rather than fetch-based.

| Recipe | Tier | Notes |
|---|---|---|
| Kodak Gold 200 | Datasheet + Characteristic + **Scan (full)** | ~35 scans, all light conditions; WB & Clarity refined from evidence |
| Kodak Portra 400 (original) | **Datasheet (E-4050 archived: PGI 37@4×6, latitude, skin aims)** + Characteristic (strong) | derived 2026-07-15; scan pass pending |
| Kodak Ektachrome E100 (original) | **Datasheet (E-4000 archived: RMS 8, curves, low-contrast tone scale)** | derived 2026-07-15; characteristic log + scan pass pending |
| Fujicolor Superia 400 | Datasheet + Characteristic + Scan (partial) | 2 scans, one photographer — cool palette/tone confirmed; grain level provisional |
| Fujifilm Acros 100 | **Datasheet (RMS 7 extracted)** + Characteristic + Scan | 2 scans (soft + harsh light) |
| Ilford HP5 Plus 400 | **Datasheet (extracted)** + Characteristic + Scan (partial) | 1 scan; more conditions wanted |
| Kodak Tri-X 400 | **Datasheet (F-4017 extracted)** + Characteristic | scans pending; recipe deliberately targets the *pushed* reportage look (documented in its knowledge.md) |
| Vision3 500T | Datasheet + Characteristic + Proxy-scan | 1 real CineStill night frame (same emulsion) — validates clean/stylised split |
| Vision3 250D | Datasheet + Characteristic | scan pass pending |
| Kodak 2383 Print | **Datasheet (LAD/tone-scale extracted)** + Characteristic | scan/frame-grab pass pending |
| Kodak Vision3 50D (original) | **Datasheet (finest-grain claim, archived)** + Characteristic (Red Rocket, Vanessa Whyte BSC) + **Scan** | 2 real Commons scans (daylight + overcast); derived 2026-07-16 |
| Kodak Double-X 5222 (original) | **Datasheet (RMS 14, gamma 0.65–0.70, archived)** + Characteristic (Raging Bull, Schindler's List, Manhattan) | no Commons frame-grabs exist (real footage isn't Commons material); derived 2026-07-16 |
| Kodak Ektachrome 100D (original) | **Datasheet (saturation/sharpness language, archived)** + Characteristic (Poor Things, 2023) | no Commons frame-grabs exist; derived 2026-07-16 |
| Kodak Ektar 100 (original) | **Datasheet (E-4046: PGI<25, saturation/sharpness)** + Characteristic + Scan | 2 scans (saturated autumn street, night long-exposure) — derived 2026-07-16 |
| Fujicolor Pro 400H (original) | **Datasheet (RMS 4, shadow-saturation control)** + **video-comparison** (real film vs Pro Neg Hi sim) | strongest non-scan evidence in the bank; derived 2026-07-16 |
| Ilford Delta 3200 (original) | **Datasheet (true ISO 1000, EI-3200-by-design)** + Scan (1, overcast street) | derived 2026-07-16 |
| Ilford Pan F Plus 50 (original) | **Datasheet (extremely fine grain, "edge contrast")** | a found "reference" was a synthetic software preset — correctly discarded, not used; genuine scans still needed; derived 2026-07-16 |
| Mumbai (General) | **11-image place study** across 7 condition types | refined once from evidence (Highlight −1.5) |
| Mumbai Monsoon | Original design | field-test pending |
| Creative looks | Aesthetic designs | tune against user-dropped `references/` |
| All `reference` recipes | Attributed captures | not yet re-derived |
