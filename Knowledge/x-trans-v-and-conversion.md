# X-Trans V & Recipe Conversion Notes

The X-T5 uses Fujifilm's **X-Trans V** sensor generation (a 40MP X-Trans CMOS 5 HR sensor + X-Processor 5). Recipes are written per sensor generation because the same settings render slightly differently across generations. This file explains the X-T5-specific behaviour and how to safely borrow recipes written for other cameras.

## Sensor generations (for context)

| Gen | Representative bodies |
|---|---|
| X-Trans V | **X-T5**, X-H2, X-H2S, X-S20, X100VI, X-T50, X-M5, X-E5 |
| X-Trans IV | X-T4, X-T3, X-Pro3, X100V, X-S10, X-E4, X-T30 II |
| X-Trans III | X-T2, X-Pro2, X100F, X-H1 |

The X-T5's processor also unlocks the full modern feature set the recipes rely on: Grain **Size**, Color Chrome FX Blue, Clarity, Nostalgic Neg., and (on some bodies/firmware) the Reala Ace film simulation.

## The blue-rendering difference (the #1 conversion rule)

X-Trans V renders **blue more deeply/saturated** than X-Trans IV on these film simulations:
**Classic Chrome, Classic Negative, Eterna, Eterna Bleach Bypass.**

To make an X-Trans IV recipe (using one of those sims) look the same on the X-T5, **drop Color Chrome FX Blue by one notch**:

| IV recipe | → X-T5 |
|---|---|
| CCFXB **Strong** | **Weak** |
| CCFXB **Weak** | **Off** |
| CCFXB **Off** | leave Off (blues will be slightly deeper; unavoidable) |

Most of the "X-Trans V version" recipes in this collection already have this adjustment baked in; the per-recipe `knowledge.md` notes where it applied.

## AWB (Auto White Balance) considerations

X-Trans V bodies have a newer AI-driven Auto White Balance. On recipes that call for **AWB**, the X-T5 may choose a slightly different balance than an older body would, especially in mixed/artificial light. If an AWB recipe looks off, options are:
- switch to a **fixed** WB (Daylight or a Kelvin value) close to the intended cast, or
- adjust the WB shift to compensate.

This is why colour-critical recipes tend to prefer fixed WB, while versatility-first recipes accept AWB's scene-to-scene variation.

## Borrowing recipes from other generations

- **X-Trans IV → V:** usually only the CCFXB one-notch drop (above); occasionally an AWB tweak. Otherwise settings transfer directly.
- **X-Trans III → V:** III bodies lack Grain Size, CCFXB, Clarity, and Color Chrome FX Blue, and some lack Classic Neg./Eterna. Converting means *adding* those modern settings, so it's less mechanical — treat III recipes as inspiration rather than a direct port.
- **GFX / other:** the medium-format GFX bodies share film sims but render tonality differently; expect a slightly different result.

## Practical setup notes on the X-T5

- Store recipes in the **C1–C7 custom presets** (Image Quality → Edit/Save Custom Setting). The X-T5 (X-Pro3-and-newer) **remembers a White Balance Shift per custom preset**, so each recipe keeps its own WB shift — older bodies did not.
- The X-T5 also has the film-simulation/recipe-friendly **Q menu** and can map Film Simulation to a function button for quick switching.
- Firmware: the bundled New Features Guide (`x-t5_nfg_en_s_f.pdf`) documents **v4.30** changes, which are **connectivity/menu items only** (wireless comms, instax printer support, smartphone pairing) — none affect image quality or the recipes.
