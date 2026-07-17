# Black & White Film Originals

Faithful B&W film emulations for the X-T5, each built on Fujifilm's **Acros** simulation (the premium B&W profile — richest tonality, finest grain structure, best detail) and tuned per stock. Grounded in datasheets **and real film scans** (per the [core principle](../../../Knowledge/validation-methodology.md): always fetch and analyse real images).

## The six, and how they differ
| Recipe | Character | Grain | Contrast | Sharpness | Clarity | ISO ceiling |
|---|---|---|---|---|---|---|
| [Ilford Pan F Plus 50](ilford-pan-f-plus-50/) | Slowest, finest, sharpest, "etched" | ultra-fine (Weak/Small) | firm/contrasty | **+2** | **+2** | 400 |
| [Fujifilm Acros 100](fujifilm-acros-100/) | Clean, smooth, sharp, wide tonality | **ultra-fine** (Weak/Small) | medium | +1 | 0 | 3200 |
| [Ilford HP5 Plus 400](ilford-hp5-plus-400/) | Balanced, forgiving, deep natural shadows | visible, **even** (Strong/Small) | medium | 0 | 0 | 12800 |
| [Kodak Tri-X 400](kodak-tri-x-400/) | Gritty, punchy, deep rich blacks | heavy, **clumpy** (Strong/Large) | high | +1 | **+3** | 12800 |
| [Ilford Delta 3200](ilford-delta-3200/) | Heaviest grain, smooth "organic" push | heaviest (Strong/Large) | moderate | 0 | +1 | 12800 |

These span the full B&W range: slowest/sharpest → fine/smooth → balanced → gritty → heaviest-grain-pushed. (See also the reference-tier [Kodak T-Max P3200](../../reference-recipes/kodak-t-max-p3200/) — Delta 3200's snappier Kodak-side counterpart.)

## The Clarity note (why three of the six deviate)
Per the standard, **Clarity defaults to 0** — Acros and HP5 keep it there (smooth, balanced stocks). Three deviate because the datasheet evidence demands it: **Tri-X (+3)** for its gritty, tactile mid-tone "bite"; **Pan F Plus 50 (+2)** because Ilford's own sheet calls out "edge contrast" as a defining trait, which Clarity directly models; **Delta 3200 (+1)**, a lighter touch befitting its pushed-reportage character. Each is a documented exception where *faithfulness overrides the 0 default*.

## Validation (datasheets + real scans fetched from Wikimedia Commons, analysis-only)
- **Acros 100:** ✅ datasheet (RMS 7) + characteristic + **2 real scans** (soft lakeside light + harsh temple sun) → confirmed ultra-fine grain, smooth wide tonality, deep-but-detailed blacks, sharp.
- **HP5 Plus 400:** ✅ datasheet + characteristic + **1 real scan** (foggy skyline) → confirmed prominent even grain, medium contrast, gentle roll-off.
- **Tri-X 400:** ✅ datasheet (F-4017; contrast index 0.56 at box speed — the recipe knowingly targets the *pushed* reportage look, documented in its knowledge.md) + characteristic. Scan-fetch still pending.
- **Delta 3200:** ✅ datasheet (true ISO 1000, EI-3200-by-design) + **1 real scan** (overcast street) → confirmed heavy grain, moderate contrast, retained shadow detail.
- **Pan F Plus 50:** ✅ datasheet (extremely fine grain, "outstanding... edge contrast"). A found "reference" turned out to be a **software-emulated preset, not real film** — correctly discarded rather than used. Real scans still needed.

## Filters (Acros +Ye/+R/+G)
Acros takes a coloured-filter suffix that mimics a B&W contrast filter: **+Ye** mild contrast/darker sky (all-rounder), **+R** strong contrast/dark sky, **+G** flatters skin. Each recipe notes its default and alternatives.

## Video note
In movie mode **Grain and Clarity are unavailable**, so the grain-and-grit distinctions between these three collapse — video B&W relies on Film Sim + Tone Curve + Sharpness only. Add grain in post; there's no in-camera Clarity substitute for Tri-X's grit on video.

## Sources
- Ilford HP5 Plus & Kodak Tri-X 400 & Fuji Acros datasheets (contrast curves, RMS granularity, resolving power).
- Real scans: [Wikimedia Commons](https://commons.wikimedia.org/) (Acros: Cospudener See series + Neopan samples; HP5: skyline).
- Comparison references: [The Darkroom](https://thedarkroom.com/kodak-tri-x-vs-ilford-hp5/), [Analogue Wonderland](https://analoguewonderland.co.uk/blogs/film-photography-blog/kodak-tri-x-vs-ilford-hp5-comparison).
