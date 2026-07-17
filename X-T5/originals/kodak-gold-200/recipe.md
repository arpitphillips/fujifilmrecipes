# Kodak Gold 200 — Fujifilm X-T5 (X-Trans V) · STILLS

Research-backed recipe derived from the Kodak E-7022 datasheet + analysis of reference frames (see [`research.md`](research.md)), and **validated against 5 real film scans across lighting conditions** (see [`validation.md`](validation.md)). Reproduces Gold 200's warm, softly-faded, saturated-yet-gentle sunny-day negative look. Grade rationale in [`knowledge.md`](knowledge.md).

| Setting | Value |
|---|---|
| Film Simulation | Classic Chrome |
| Grain Effect | Strong, Small |
| Color Chrome Effect | Weak |
| Color Chrome FX Blue | Off |
| White Balance | Daylight, +3 Red & −5 Blue |
| Dynamic Range | DR400 |
| Highlight (Tone Curve) | −2 |
| Shadow (Tone Curve) | +0.5 |
| Color | +3 |
| Sharpness | −2 |
| High ISO NR | −4 |
| Clarity | 0 |
| ISO | Auto, up to ISO 6400 |
| Exposure Compensation | +2/3 to +1 (typically) |

> **Validated changes** (from scan analysis): White Balance +4R→**+3R** (flat-light scans showed +4R over-warms); Clarity −2→**0** (softness carried by base + Sharpness −2; no Clarity artifacts, per quality standard).

### Handling notes
- **Best in warm, sunny daylight** — that's where Gold's amber warmth sings. Real Gold shifts cooler/greener in flat overcast; in dull light, reduce the Red shift (e.g. +2R) or expect a flatter result.
- **Expose slightly bright** (+2/3 to +1). Gold's real latitude favours overexposure (−2/+3 stops), giving clean, bright, saturated frames.
- **Artificial light:** Gold is daylight-balanced; under tungsten/LED it goes very warm. Correct WB toward the source if you don't want that.
- DR400 forces **ISO ≥ 500** (extra baseline grain is intended).

### Variant for flat/overcast light
Set White Balance **Daylight, +2 Red & −5 Blue** and **Shadow +1** to keep some warmth and shadow density when the sun isn't out.

> **Provenance:** independently derived from the Kodak datasheet and observed frames. It converges with the popular [Fuji X Weekly Gold 200 (X-Trans V)](https://fujixweekly.com/2023/10/24/kodak-gold-200-fujifilm-x-t5-x-trans-v-film-simulation-recipe/) recipe (validation); we differ on Highlight (−2 vs −1.5). See [`research.md`](research.md).
