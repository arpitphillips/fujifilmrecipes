# Kodak Ektachrome E100 — Fujifilm X-T5 (X-Trans V) · STILLS

Research-backed **original**, derived from the Kodak E-4000 datasheet (archived: [`_reference-sources/datasheets/kodak-still/ektachrome-e100_e4000.pdf`](../../_reference-sources/datasheets/README.md)). Reproduces the 2018-revival Ektachrome E100 transparency look: **clean neutral colour, bright low-D-min whites, extremely fine grain, gentle (for a slide film) contrast**. Cooler and more restrained than any Fujichrome. Derivation in [`knowledge.md`](knowledge.md).

Distinct from [thommys-ektachrome](../../reference-recipes/thommys-ektachrome/) (reference), which emulates the *printed NatGeo page* — this recipe targets the **transparency itself**, per datasheet.

| Setting | Value |
|---|---|
| Film Simulation | Provia/STD |
| Grain Effect | Weak, Small |
| Color Chrome Effect | Weak |
| Color Chrome FX Blue | Weak |
| White Balance | Daylight, −1 Red & +1 Blue |
| Dynamic Range | DR200 |
| Highlight (Tone Curve) | −1 |
| Shadow (Tone Curve) | −0.5 |
| Color | +1 |
| Sharpness | +1 |
| High ISO NR | −4 |
| Clarity | 0 |
| ISO | Auto, up to ISO 6400 |
| Exposure Compensation | 0 to +1/3 (typically) |

### Why these values (short)
- Provia base: Fuji's balanced-slide standard is the structural analogue of Kodak's balanced slide: vivid-but-faithful, moderate contrast. (Classic Chrome is too desaturated/hard; Astia too skin-biased.)
- Grain Weak/Small: datasheet: diffuse **RMS 8, "extremely fine."**
- WB Daylight −1R/+1B: E100 is daylight-balanced with a **neutral-to-cool** rendering (its R/G/B characteristic curves run tightly bundled — no warm crossover). The cool nudge counteracts Fuji's native warmth.
- H−1 / S−0.5: datasheet: "**low contrast tone scale**, extended tonal range"; curve shows a gentle shoulder into a high D-max — so soften highlights, keep most shadow density (slides still go deep).
- Color +1, CCE Weak: "**moderately** enhanced color saturation with a **neutral** balance."
- CCFXB Weak: E100's clean but not exaggerated blue skies (Strong would push toward Fuji-slide blues).
- Sharpness +1: MTF holds ~100% response past 20 cycles/mm; a crisp transparency.
- Clarity 0: per quality standard; nothing in the sheet argues for grit or glow.

### Handling
- **Daylight or flash only by design** (5500K film) — under tungsten it goes deep amber unless you correct WB, exactly like the film.
- Slide-film discipline: expose for highlights; EC stays near 0.
- **Push look:** the sheet notes push +1 (EI 200) slightly raises contrast and sharpens highlights — emulate with H0/S0 and EC −1/3.

**Validation tier:** Datasheet-validated (E-4000: RMS, curves, tone-scale, balance — archived PDF). Characteristic pass partial; **scan-validation pending** — drop real E100 scans into [`references/`](references/).
