# Kodak Gold 200 — Grade Analysis & Understanding

> Read alongside [`recipe.md`](recipe.md) (stills), [`recipe-video.md`](recipe-video.md) (movie), [`research.md`](research.md) (evidence base), and the [Knowledge base](../../../Knowledge/README.md).

## The film being emulated
Kodak Gold 200 is a consumer colour negative film introduced in 1986, originally as Kodacolor VR-G. It's the quintessential "drugstore film" look: warm, a little soft, gently faded, forgiving. These are the colours of 1980s and 90s family snapshots. Because it's a negative film, its highlights roll off gently and its palette stays warm and low-key rather than crisp and saturated.

## The grade in one line
A warm, softly faded, low-contrast daylight look with amber-leaning colour, gentle highlights, visible fine grain, and a strong pull of sunny-day nostalgia.

## How the settings build that grade
| Setting | Value | What it contributes |
|---|---|---|
| **Classic Chrome** base | — | Muted, calm foundation that takes a warm shift gracefully. |
| **White Balance** | Daylight **+3R / −5B** | Moderate warm/amber cast, the defining Gold warmth. (Scan-validated down from +4R; see [`validation.md`](validation.md).) |
| **Dynamic Range** | **DR400** | Maximum highlight latitude → soft, negative-film highlight roll-off. Forces ISO ≥ 500. |
| **Highlight** | −2 | Softens highlights so whites never turn harsh; leans into Gold's gentle roll-off (datasheet: +3 stops over-exposure latitude). |
| **Shadow** | +0.5 | Just enough shadow depth to avoid mushiness. |
| **Color** | +3 | Saturated warmth. Gold is colourful despite being soft. |
| **Color Chrome Effect** | Weak | Mild richness; keeps colour from getting too heavy. |
| **Color Chrome FX Blue** | Off | Natural, unemphasised blues (X-Trans V already deepens them). |
| **Sharpness** | −2 | Soft outlines, the gentle, un-clinical consumer-film feel. |
| **Clarity** | 0 | Kept neutral per the quality standard; softness comes from the base and Sharpness −2, avoiding Clarity artifacts. |
| **Grain** | Strong, Small | Clearly visible but fine grain, right for a 200-speed consumer negative. |
| **High ISO NR** | −4 | Preserve detail/grain. |

## Reading the tonal/colour signature
- Contrast: low. DR400 with Highlight −2 flattens the curve toward that faded print look.
- Saturation: warm-biased and fairly full (Color +3), softened by Weak CCE.
- Cast: strongly warm amber (+3R / −5B), the most overtly warm of the daylight recipes here.
- Texture: soft edges (−2 sharpness) over visible fine grain. Reads as real consumer film.

## Best light / caveat
Built for sunny daylight, where Gold's warmth sings. In flat, overcast or artificial light the strong warm shift can look too yellow. The DR400 ISO-500 floor means slightly more baseline grain even in bright light, which is intended.

## X-Trans V note
Fully compatible with X-Trans V as written. To run it on newer X-Trans IV bodies instead, set Color Chrome FX Blue to Weak (one notch up) per the [conversion rule](../../../Knowledge/x-trans-v-and-conversion.md).

## Related in this collection
- Warmer, softer sibling to [Kodachrome 64](../../reference-recipes/kodachrome-64/knowledge.md) (crisper) and [Kodak Portra 400 v2](../../reference-recipes/kodak-portra-400-v2/knowledge.md) (portrait-tuned). Reach for Gold when you want overt sunny-day nostalgia rather than editorial crispness.
