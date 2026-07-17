# Kodak Gold 200 — Research Dossier (analysis basis for the recipe)

This is the evidence base behind [`recipe.md`](recipe.md) and [`recipe-video.md`](recipe-video.md). Sources are cited; no copyrighted reference images are stored or redistributed. They were viewed for analysis only.

## Authoritative source: Kodak datasheet E-7022 (Feb 2016)
Concrete, manufacturer-stated characteristics of the actual film:
- ISO 200 colour negative, daylight-balanced. Kodak specifies correction filters (80A/80B) for tungsten and photolamp use, so the native look is a daylight look and artificial light needs correcting.
- Marketed on "saturated colors, fine grain, and high sharpness". In other words a colourful consumer stock, not a muted one.
- Wide exposure latitude, from 2 stops under to 3 stops over. This is the key handling fact: Gold is extremely forgiving and is conventionally shot slightly overexposed for clean, bright, saturated results.
- Print Grain Index 44 (at 4×6, 4.4× magnification). Moderate, clearly visible grain, grainier than pro films like Portra and Ektar by design.
- Characteristic curves: the blue-sensitive (yellow-forming) layer sits highest, and the overall dye balance biases warm. That matches Gold's reputation for amber highlights and mid-tones.

## Corroborating reviews (viewed for analysis)
Consensus across multiple independent film reviews (The Darkroom, 50mmF2, My Favourite Lens, Decaf Journal, Daydream):
- Warm golden-amber cast, strongest in highlights and mid-tones, noticeably warmer than Portra.
- Saturated but soft: colourful reds and yellows with gentle contrast, nothing clinical.
- Greens render slightly yellow-shifted and muted; foliage goes warm-olive rather than vivid green.
- Blues stay relatively muted and understated.
- In flat light (overcast or shade) Gold shifts cooler and greener. Its warmth depends on warm, sunny light, which is why it's beloved for sunny days and looks flat and green in dull weather.
- Moderate visible grain; forgiving; a nostalgic snapshot character.

## Deriving the X-T5 settings from the evidence
| Observed film trait | X-T5 control that reproduces it |
|---|---|
| Warm/amber cast in highlights+mids | **Daylight WB shifted +3 Red / −5 Blue** (warm, on a daylight base since Gold is daylight-balanced; initial derivation was +4R, refined to +3R by scan validation — see [`validation.md`](validation.md)) |
| Soft, negative-film highlight roll-off + overexpose-friendly latitude | **DR400** (max highlight headroom) + **Highlight −2** |
| Open-but-present shadows (not crushed) | **Shadow +0.5** |
| Saturated-yet-soft colour, warm-weighted | **Classic Chrome base** + **Color +3** |
| Extra warmth/depth in reds & yellows | **Color Chrome Effect Weak** (gentle richness, not slide-film-strong) |
| Muted, unremarkable blues | **Color Chrome FX Blue Off** |
| Consumer-film softness | **Sharpness −2** (Clarity stays 0 per the quality standard; see validation) |
| Moderate, visible-but-fine grain (Index 44) | **Grain Strong, Small** |
| Shot slightly overexposed | **Exposure comp +2/3 to +1** |

### Why Classic Chrome (not Classic Negative)?
Gold's soft, warm, moderately saturated negative character matches Classic Chrome's restrained palette and gentle shadow contrast. Classic Negative shifts shadows green-cyan, a Superia signature, and that reads as a different film; Gold is warmer and cleaner in the shadows than Superia. Classic Chrome with a warm WB shift and Color +3 is the closest faithful match.

## Benchmark comparison (validation, not source)
The most popular community Gold 200 recipe (Fuji X Weekly, [X-Trans V version](https://fujixweekly.com/2023/10/24/kodak-gold-200-fujifilm-x-t5-x-trans-v-film-simulation-recipe/)) independently lands on the same base (Classic Chrome), the same Daylight +4R/−5B warmth, DR400, Color +3, CCE Weak, and Grain Strong/Small. Our derivation converges with it, which is strong evidence these values are right for Gold. We diverge only on Highlight (−2 against their −1.5) to lean slightly further into Gold's soft highlight roll-off. This recipe is our own derivation from the datasheet and observed frames, not a copy of theirs.

## Refinement hook
WB shift precision (±1–2 on each axis) is the one value worth tuning against your own reference frames or first test shots, since Gold's exact warmth varies with the scan or print pipeline. Supply frames and we'll lock it.

## Sources
- [Kodak GOLD 200 Technical Data E-7022 (PDF)](https://business.kodakmoments.com/sites/default/files/files/resources/E7022_Gold_200.pdf)
- [Kodak GOLD 200 product page](https://www.kodak.com/en/still-film/product/consumer/gold-200-film/)
- [The Darkroom — Gold 200 review](https://thedarkroom.com/film/gold-200/)
- [50mmF2 — Gold 200 review](https://50mmf2.com/writings/kodak-gold-200-review)
- [My Favourite Lens — Gold 200 review](https://www.myfavouritelens.com/kodak-gold-200-35mm-film-review/)
