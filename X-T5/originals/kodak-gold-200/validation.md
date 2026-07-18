# Kodak Gold 200 — Validation & Proof of Faithfulness

Recipe validated against real Gold 200 film scans across multiple lighting conditions, plus the Kodak datasheet. This is the proof layer behind [`recipe.md`](recipe.md). Reference scans were analysed only (not redistributed); source is [The Darkroom's Gold 200 gallery](https://thedarkroom.com/film/gold-200/) (local copy in `X-T5/_reference-sources/`).

## Scans analysed (the FULL Darkroom gallery: ~35 images across every condition)
Rather than a handful, the entire user gallery was reviewed to avoid outliers. Coverage:

| Light condition | Example scans |
|---|---|
| Flat / overcast | "Chuey's" white building, black van alley, Shiloh cemetery, Dominator coaster (aerial), teal chairs |
| Soft diffused | blonde portrait, boy in white sweater |
| Direct sun | red-awning building, Ferris wheel, lifeguard tower, orange locomotive, yellow bench, Goddess Pomona statue, beach overpass |
| Golden hour / backlit | Cranbrook hay fields, dirt-road sunset, Newland Café sun-flare |
| Twilight / dusk | Steffen's Restaurant signs, Busch Gardens swing ride |
| Indoor / artificial | "ELLA" store fridge (strong amber), tabby cat by window, banana |
| Subjects covered | skin/portrait, foliage/greens, sky/blues, neutral whites/greys, saturated accents (red/yellow/orange), water, metal, stone |

## What the real scans show (measured by eye, cross-image)
| Trait | Observation across the 5 scans | Consistent? |
|---|---|---|
| **Warmth** | Whites render **cream/warm**, strongest in sun (#4) and skin (#2); in flat light (#1,#3,#5) warmth is **mild, near-neutral** | Yes — moderate, light-dependent |
| **Greens** | Consistently **muted / yellow-olive**, never vivid (#2 grass, #5 field) | Yes |
| **Blues** | **Muted, pale** — sky in #4 soft not deep; denim in #2 restrained. Least-saturated channel | Yes |
| **Reds/oranges** | **Rich and saturated** — red awning (#4), warm skin, striped shirt reds (#2) | Yes |
| **Contrast** | **Medium-low**; highlights soft & holding detail (white walls, blonde hair not blown); shadows **open**, retaining detail (van #3) | Yes |
| **Overall saturation** | **Moderate**, selective — warm colours pop, cool colours muted; not globally punchy | Yes |
| **Grain** | Visible in 35mm (#3,#4), smoother in 120 | Yes |

## Mapping evidence → settings (and what changed because of it)
| Evidence | Setting decision |
|---|---|
| Muted greens + muted pale blues, warm-selective | **Classic Chrome** base confirmed (it inherently mutes greens/blues) + **Color +3** (global lift that Classic Chrome keeps muted in cool hues while warm hues reach the observed saturation) |
| Warmth is **moderate**, near-neutral in flat light | **WB shift reduced from +4R to +3 Red / −5 Blue** — the flat-light scans showed +4R over-warms; +3R matches the moderate average while −5B keeps blues muted/pale as observed. *(This is a change made *because of* the scans.)* |
| Rich reds specifically | **Color Chrome Effect Weak** (depth in warm tones, not slide-strong) |
| Muted pale blues | **Color Chrome FX Blue Off** |
| Soft highlights holding detail | **DR400 + Highlight −2** confirmed |
| Open shadows retaining detail | **Shadow +0.5** (minimal deepening; scans are open, so kept low) |
| Consumer-film softness, but no clarity artifacts wanted | **Clarity 0** (per quality standard) + **Sharpness −2** carry the softness without Clarity processing. *(Changed from −2 → 0.)* |
| Visible-but-fine grain | **Grain Strong, Small** confirmed |

## Changes made from the pre-validation recipe
1. White Balance: +4 Red → +3 Red (−5 Blue unchanged). Evidence: flat-light scans showed +4R over-warms.
2. Clarity: −2 → 0. Per the quality standard (Clarity 0 unless needed); softness preserved via base + Sharpness −2. Verified the scans' softness doesn't *require* negative Clarity.

## Additional confirmations from the full gallery
- Warmth scales with the light: near-neutral in overcast, clearly golden in sun and golden hour, and strongly amber indoors (the "ELLA" fridge shot). This is exactly the behaviour the recipe notes describe, and it makes +3R the right all-conditions average.
- Warm accents (red, orange, yellow) consistently pop in the locomotive, yellow bench, restaurant sign and lifeguard tower scans, which validates Color +3 with CCE Weak.
- Greens are reliably muted olive and blues medium-to-pale across every sky, which validates Classic Chrome with CCFXB Off.
- Low contrast with soft warm highlights and open shadows holds across all 35 scans, which validates DR400, Highlight −2 and Shadow +0.5.

## Faithfulness verdict
High. Confirmed across roughly 35 real scans spanning overcast, sun, golden hour, twilight and indoor light, plus every subject type, plus the Kodak E-7022 datasheet (see [`research.md`](research.md)). After the two evidence-based edits above, nothing else needed changing. This meets the top scan-validated tier of the [validation methodology](../../../Knowledge/validation-methodology.md).

## Still open
- Confirm on your own Gold 200 frames (scan pipelines vary warmth by ±1–2 on the WB shift) to personalise the WB lock.
