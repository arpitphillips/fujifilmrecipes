# Kodak Portra 400 — Fujifilm X-T5 (X-Trans V) · STILLS

Research-backed original, derived from the Kodak E-4050 datasheet (archived: [`_reference-sources/datasheets/kodak-still/portra-400_e4050.pdf`](../../_reference-sources/datasheets/README.md)). Reproduces the emulsion the sheet describes: the world's finest-grain high-speed colour negative, warm-neutral skin, low contrast, wide latitude, grain you barely see. Derivation in [`knowledge.md`](knowledge.md).

Distinct from [kodak-portra-400-v2](../../reference-recipes/kodak-portra-400-v2/) (reference), which renders the grainier *scanned-Portra* look popular online. This recipe targets the film as specified.

| Setting | Value |
|---|---|
| Film Simulation | Classic Chrome |
| Grain Effect | Weak, Small |
| Color Chrome Effect | Weak |
| Color Chrome FX Blue | Off |
| White Balance | Daylight, +2 Red & −4 Blue |
| Dynamic Range | DR400 |
| Highlight (Tone Curve) | −1.5 |
| Shadow (Tone Curve) | −1 |
| Color | +1 |
| Sharpness | −1 |
| High ISO NR | −4 |
| Clarity | 0 |
| ISO | Auto, up to ISO 6400 |
| Exposure Compensation | +1/3 to +1 (typically) |

### Why these values (short)
- Classic Chrome base: Portra's palette is muted-warm with gentle hue separation; Classic Chrome's restrained saturation is the right canvas (the whole Portra recipe family agrees), warmed back via WB shift.
- Grain Weak/Small: datasheet: "world's finest grain high-speed film"; Print Grain Index 37 on a 4×6 (threshold of visibility = 25). Real Portra grain is *barely* perceptible, Strong grain models scans, not film.
- WB Daylight +2R/−4B: Portra's warm-neutral balance; fixed preset for repeatability (per [methodology](../../../Knowledge/validation-methodology.md): fixed WB for colour-critical film).
- DR400 + Highlight −1.5: the famous negative latitude (clean to +3 over) and long soft shoulder; highlights never bite.
- Shadow −1: low-contrast open shadows; Portra never crushes.
- Color +1, CCE Weak: the sheet's "exceptional colour saturation" is *for a portrait film*; in practice: natural, skin-first, never punchy.
- Sharpness −1: T-GRAIN acuity is high but negative-film edges are gentle; −1 avoids digital bite.
- Clarity 0: nothing in the film warrants grit; quality standard holds.

### Handling
- Overexpose freely: the film is optimized for generous exposure (skin density targets sit high); +2/3 is the sweet spot, +1 in flat light.
- Gray-card forehead density targets in the sheet (1.08–1.18 light complexion) are the reference for skin placement; expose skin bright.
- Under tungsten/fluorescent the real film needs colour-compensating filters; digitally, correct WB toward the source or accept the warm cast.

Validation tier: Datasheet-validated (E-4050: PGI, latitude, balance, skin-density aims, archived PDF). Characteristic pass strong (best-documented film in the bank's sources). Scan-validation pending; drop real Portra 400 scans into [`references/`](references/).

> **Scan validation, first pass:** 1 real Portra 400 scan analysed (sunny daylight, red and white coach; Wikimedia Commons, analysis-only). It confirmed restrained saturation even on a saturated red subject, warm-neutral rather than stark whites, open shadows with detail, muted natural greens, and fine non-clumpy grain, all consistent with Weak/Small grain, Shadow −1, Color +1 and the DR400 soft-highlight build. More scans (portrait skin, overcast, golden hour) are still wanted; drop them into [`references/`](references/).
