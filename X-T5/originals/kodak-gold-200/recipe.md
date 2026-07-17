# Kodak Gold 200 — Fujifilm X-T5 (X-Trans V) · STILLS

This recipe was derived from the Kodak E-7022 datasheet and analysis of reference frames (see [`research.md`](research.md)), then validated against 5 real film scans across different lighting conditions (see [`validation.md`](validation.md)). It reproduces Gold 200's warm, softly faded, sunny-day negative look: saturated but gentle. The reasoning behind each setting is in [`knowledge.md`](knowledge.md).

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

> Two settings changed after scan analysis: White Balance went from +4R to **+3R** because flat-light scans showed +4R over-warms, and Clarity went from −2 to **0** since the base simulation and Sharpness −2 already carry the softness without Clarity's processing penalty.

### Handling notes
- Best in warm, sunny daylight, which is where Gold's amber warmth sings. Real Gold shifts cooler and greener in flat overcast, so in dull light reduce the Red shift (to +2R, say) or expect a flatter result.
- Expose slightly bright (+2/3 to +1). Gold's real latitude favours overexposure (−2/+3 stops), and bright exposures come out clean and saturated.
- Gold is daylight-balanced, so under tungsten or LED it goes very warm. Correct WB toward the source if you don't want that.
- DR400 forces ISO 500 or above. The extra baseline grain is intended.

### Variant for flat/overcast light
Set White Balance to Daylight, +2 Red & −5 Blue, and raise Shadow to +1. That keeps some warmth and shadow density when the sun isn't out.

> **Provenance:** independently derived from the Kodak datasheet and observed frames. It converges with the popular [Fuji X Weekly Gold 200 (X-Trans V)](https://fujixweekly.com/2023/10/24/kodak-gold-200-fujifilm-x-t5-x-trans-v-film-simulation-recipe/) recipe, which is itself a form of validation; the one place we differ is Highlight (−2 here, −1.5 there). See [`research.md`](research.md).
