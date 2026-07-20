# Knowledge Base — Fujifilm Settings & Film-Simulation Grading

This folder explains **what each camera setting does** and **how settings combine to create a "grade"** (a look). It is the reference layer behind the recipes stored under each camera folder (e.g. `X-T5/`).

Everything here is grounded in the **Fujifilm X-T5 Owner's Manual** (`X-T5/x-t5_manual_en_s_f.pdf`, Chapter 6 — *The Shooting Menus → Image Quality Setting*, printed pp. 122–132) and cross-checked against the recipe sources on [Fuji X Weekly](https://fujixweekly.com/).

## What a "recipe" actually is

A Fujifilm **Film Simulation Recipe** is a saved bundle of JPEG-processing settings applied *in-camera at capture time*. The camera bakes the look into the JPEG (or HEIF) — there is no editing step. A recipe is therefore a **grade** (a colour/tone treatment) expressed entirely through the camera's Image Quality menu:

1. A **Film Simulation** base (the master colour/contrast profile).
2. A set of **modifiers** layered on top — white balance + shift, dynamic range, tone curve, colour, sharpness, grain, clarity, the Color Chrome effects, and noise reduction.

Understanding a recipe = understanding the base profile, then reading each modifier as a deviation from neutral.

## Files in this folder

| File | Covers |
|---|---|
| [film-simulations.md](film-simulations.md) | Every film-simulation base (Provia → Acros), what each renders, and which "film family" it belongs to |
| [white-balance.md](white-balance.md) | WB presets, Kelvin, and the Red/Blue **WB Shift** grid — the main colour-cast control |
| [dynamic-range-and-tone.md](dynamic-range-and-tone.md) | Dynamic Range (DR100/200/400), D Range Priority, and the Tone Curve (Highlight/Shadow) — the contrast controls |
| [color-and-chrome.md](color-and-chrome.md) | Color (saturation), Color Chrome Effect, Color Chrome FX Blue, Monochromatic Color |
| [grain-and-detail.md](grain-and-detail.md) | Grain Effect (roughness/size), Sharpness, Clarity, High ISO NR — the texture/detail controls |
| [iso-and-exposure.md](iso-and-exposure.md) | Auto-ISO, exposure compensation philosophy, and how DR ties to ISO floors |
| [x-trans-v-and-conversion.md](x-trans-v-and-conversion.md) | X-Trans V sensor specifics, the blue-rendering shift, and how to convert X-Trans IV recipes |
| [video-mode-settings.md](video-mode-settings.md) | **Movie mode** — which controls exist in video, which are missing (grain, chrome, clarity), and how to translate a photo recipe into a faithful video grade |
| [flog-and-raw-workflow.md](flog-and-raw-workflow.md) | **F-Log, F-Log2 & RAW** — which log to shoot, the ISO-floor and data-level traps, the correct Resolve/Premiere node order, in-camera RAW conversion and X RAW Studio, RAW video and its cost, plus ready-made [conversion LUTs](luts/README.md) |
| [validation-methodology.md](validation-methodology.md) | **Proof-of-faithfulness standard** — the datasheet/characteristic/scan evidence tiers, scan rules, and how a reference recipe is promoted to a validated original |
| [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md) | **Color science foundations** — why simulations cannot be replicated in Photoshop/ACR, how colour film's layer/dye system works, simulation history timeline (2003–2020), memory color theory, per-simulation spectral behavior incl. Eterna Bleach Bypass, the ACROS grain model, Ye/R/G filters (from Imaging Resource + YouTube deep dives) |
| [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md) | **Film chemistry** — silver halide crystals, latent image formation, development/stop/fix reactions, why grain size ↔ film speed ↔ contrast are chemically coupled, sepia toning chemistry (from the UW–Eau Claire chemistry-of-photography reference cited by the Imaging Resource guide) |
| [pro400h-vs-proneghi-analog-comparison.md](pro400h-vs-proneghi-analog-comparison.md) | **Analog vs. digital comparison** — Fujifilm Pro 400H film stock vs. Pro Neg Hi simulation, key differences in shadow cast, highlight shoulder, green rendering, and recipe settings to bridge the gap |
| [film-stocks-master-list.md](film-stocks-master-list.md) | **The canon of top film stocks** (Fujifilm, Kodak, Ilford, CineStill, Agfa+) with the bank's recipe-coverage status and the priority queue for closing gaps |
| [nerd-guide-datasheet-to-recipe.md](nerd-guide-datasheet-to-recipe.md) | **The nerd guide** — how to read a film datasheet (characteristic curves, granularity, spectral sensitivity) and turn the numbers into X-T5 settings, with the full measurement-to-menu mapping table and a worked example |
| [fujifilm-official-design-notes.md](fujifilm-official-design-notes.md) | **Fujifilm's own words** — first-party design statements from the Image Design team's X Stories and product pages (Acros grain engine, Classic Neg's magenta highlights, Eterna as ungraded canvas, Nostalgic Neg's shadow amber, Reala Ace saturation compression), each mapped to recipe implications |

## How to read the per-recipe knowledge files

Each recipe folder (e.g. `X-T5/reference-recipes/kodachrome-64/`) contains:
- `recipe.md` — the raw settings to program into the camera.
- `knowledge.md` — the **grade analysis**: what look it produces, the film it emulates, and the reasoning behind every setting, referencing the concepts in this folder.
