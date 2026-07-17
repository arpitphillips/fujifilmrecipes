# Kodak Portra 400 — Grade Analysis & Derivation

## The film
Kodak Professional Portra 400 (current emulsion 2010→, T-GRAIN). The modern professional portrait negative — the sheet (pub. **E-4050**, archived in [`_reference-sources/datasheets/`](../../_reference-sources/datasheets/README.md)) specifies:

- "**World's finest grain** high-speed color negative film"
- **Print Grain Index 37** for a 4×6 print from 135 (25 = visual threshold of graininess) — i.e. grain just barely perceptible at album size
- "Exceptional colour saturation over a wide range of lighting conditions" — in the Portra register: natural, never punchy
- **Beautiful, neutral skin tones**; optimized sharpness (T-GRAIN)
- Wide exposure latitude; optimized for printing to ENDURA papers
- Skin-density aims (Status M, red channel): normally-lit forehead 1.08–1.18 (light complexion) — the film expects **generously exposed skin**
- Daylight balanced; CC-filter tables for fluorescent/HID confirm it is *not* meant to self-correct artificial light

## Trait → setting derivation

| Datasheet trait | Recipe setting | Reasoning |
|---|---|---|
| Muted-warm pro-negative palette | **Classic Chrome base** | Restrained saturation + gentle separation; warmth restored via WB (the family consensus base, independently justified) |
| "World's finest grain," PGI 37@4×6 | Grain **Weak, Small** | Below-visibility grain at normal size; Strong grain would model scans/pushes, not the emulsion |
| Warm-neutral balance, neutral skin | WB **Daylight +2R/−4B** | Fixed, repeatable warm-neutral; not golden-hour baked (that's the v2 reference's 5200K/−6B) |
| Huge overexposure latitude, soft shoulder | **DR400 + Highlight −1.5** | Long non-biting highlight rolloff |
| Low contrast, open shadows | **Shadow −1** | Portra never crushes blacks |
| Natural "exceptional" saturation | **Color +1**, CCE **Weak** | Above-neutral colour that stays skin-first |
| T-GRAIN sharpness, negative acuity | **Sharpness −1** | Detail without digital edge |
| X-Trans V deep blues | CCFXB **Off** | Portra blues are soft; V-generation already deepens blues ([x-trans-v](../../../Knowledge/x-trans-v-and-conversion.md)) |
| No grit traits | **Clarity 0** | Quality standard |
| Skin-density aims sit high | EC **+1/3…+1** | Expose skin bright, as the film expects |

## Relationship to the reference recipes

| | This original | [kodak-portra-400-v2](../../reference-recipes/kodak-portra-400-v2/) | [reggies-portra](../../reference-recipes/reggies-portra/) |
|---|---|---|---|
| Target | **Emulsion as manufactured** (E-4050 datasheet) | *Scanned*/golden-hour Portra as usually seen online | Reggie's own portrait interpretation of the palette |
| Grain | Weak, Small (PGI 37 → below visibility) | Strong, Small (models a scan, not the film) | Weak, Small |
| WB | Daylight +2R/−4B (fixed, repeatable) | 5200K, +1R/−6B (fixed, warmer/golden-hour) | Auto, +2R/−4B (adapts per scene) |
| Dynamic Range | DR400 | DR400 | DR-Auto |
| Highlight / Shadow | −1.5 / −1 | 0 / −2 | −1 / −1 |
| Color | +1 (restrained, skin-first) | +2 | +2 |
| Sharpness | −1 | −2 | −2 |
| Clarity | 0 | −2 | 0 |
| Design intent | Match the datasheet's stated grain/latitude/skin numbers | Match how Portra scans *look* once developed, scanned, and often warmed for golden hour | Versatile, adaptive, tuned by eye for Reggie's own portrait work |

**None of the three is "wrong"** — they answer different questions ([VALIDATION-AUDIT](../../VALIDATION-AUDIT.md): emulsion-faithful vs artifact-faithful). This original is the one to reach for if you want *what Kodak's own data says the film does*; the other two are closer to *what people actually remember Portra looking like* in a photo. See also the parallel [Superia comparison](../fujicolor-superia-400/knowledge.md#relationship-to-reggies-superia) — the same three-way tension shows up there too.

## What would make it unfaithful
- Strong/Large grain (PGI says no), crushed shadows, heavy warm WB baked in (turns "wide range of lighting" film into a one-light look), Color above +2.

## Validation status
- **Datasheet tier: ✅** (E-4050 archived PDF; PGI table + exposure/latitude + skin aims read directly, 2026-07-15)
- **Characteristic tier: strong** — the most-documented colour negative in circulation; formal ≥3-source log to be added
- **Scan tier: pending** — needs ≥5 scans across light/subjects (note scanner pipeline per [methodology](../../../Knowledge/validation-methodology.md)); drop into [`references/`](references/)

*Derived 2026-07-15 from the archived datasheet. See also [VALIDATION-AUDIT.md](../../VALIDATION-AUDIT.md).*
