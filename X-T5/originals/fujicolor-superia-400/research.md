# Fujicolor Superia X-Tra 400 — Research & Validation Status

Evidence base for [`recipe.md`](recipe.md). Reference images analysed only, not redistributed.

## Authoritative source: Fujifilm datasheet (AF3-0217E)
- Daylight-type ISO 400 colour negative. Under tungsten it's effectively ISO 100 with an 80A filter, so the native look is a daylight look.
- "New Super Uniform Fine Grain Technology": fine grain for a high-speed film.
- High speed with wide exposure latitude. It captures in low light and forgives mistakes.
- Excellent skin colour reproduction; smooth, natural skin.
- Excellent sharpness, from overall form down to fine texture.
- Excellent gray balance maintained from the brightest highlights to the deepest shadows.
- No colour-compensating filters needed in daylight or flash.

## Corroborating reviews (analysed)
Consensus (The Darkroom, Analog.Cafe, Alex Luyckx, Digital Camera World, Wikipedia):
- The classic "Fuji look": cool tones with a green-magenta lean, cooler than Kodak, with striking blue highlights.
- Medium saturation and medium contrast. Fine grain when well-exposed, rising indoors.
- A fourth cyan layer ("4th colour layer technology") for better rendering under fluorescent light.
- Wide dynamic range that holds shadow and highlight detail across over- and under-exposure.
- Discontinued April 2024.

## Evidence → settings
| Trait | Setting |
|---|---|
| Cool, green-magenta, blue highlights | Classic Negative base + Daylight −1R/+1B + CCFXB Weak |
| Medium contrast, good gray balance, wide latitude | DR200, Highlight −1, Shadow +1 |
| Medium saturation | Color +2, CCE Weak |
| Fine grain, sharp | Grain Weak/Small, Sharpness 0 |
| Excellent skin (don't over-cool) | small −1R only, not a heavy cool shift |

### Why Classic Negative is the correct base
Fujifilm designed the Classic Negative film simulation to emulate Superia consumer film, so of all bases it is definitionally the closest starting point. Its native teal-leaning shadows and hue separation are the Superia character; the recipe only tunes contrast, warmth and grain around it.

## Validation status
- Datasheet-validated: ✅. Grain (fine), sharpness (high), daylight balance, latitude and skin are all mapped to settings.
- Characteristic-validated: ✅ across 5+ independent reviews (cool green-magenta cast, blue highlights, medium saturation and contrast).
- Scan validation, first pass: ✅. 2 real Superia scans analysed (Beartooth Highway alpine landscapes, overcast, Wikimedia Commons, analysis-only) confirmed the cool-neutral palette, muted olive greens, grey-blue sky with soft held highlights, medium contrast, and visible even grain. All of it matches the recipe's cool lean and tone curve.
  - Caveats: both frames come from one photographer and one roll, and the grain reads slightly stronger than "Weak", plausibly from an older roll or scan sharpening. Keep Grain Weak/Small pending more scans; if your `references/` drops confirm heavier grain, move to Strong/Small.
- Next: sunny, indoor and skin scans to lock the WB cool-shift (±1). Drop them into [`references/`](references/).

## Sources
- [Fujifilm Superia X-Tra 400 datasheet (AF3-0217E, PDF)](https://asset.fujifilm.com/master/emea/files/2020-10/9a958fdcc6bd1442a06f71e134b811f6/films_superia-xtra400_datasheet_01.pdf)
- [The Darkroom — Superia X-Tra 400](https://thedarkroom.com/film/superia-x-tra-400/)
- [Analog.Cafe — Superia X-Tra 400 review](https://www.analog.cafe/r/fujifilm-superia-x-tra-400-film-review-zc0y)
- [Alex Luyckx — Film Review No.80](http://www.alexluyckx.com/blog/2022/02/14/film-review-blog-no-80-fujifilm-superia-x-tra-400/)
- [Wikipedia — Fujifilm Superia X-tra 400](https://en.wikipedia.org/wiki/Fujifilm_Superia_X-tra_400)
