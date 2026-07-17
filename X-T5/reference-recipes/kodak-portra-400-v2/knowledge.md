# Kodak Portra 400 v2 — Grade Analysis & Understanding

> Read alongside [`recipe.md`](recipe.md) and the [Knowledge base](../../../Knowledge/README.md).

## The film being emulated
**Kodak Portra 400** is a professional **colour negative** film (current line introduced 1998, refined since) designed for **portraiture** and known for beautiful skin tones, wide latitude, and a warm, gentle palette. Compared with Portra 160 it has a little more contrast, saturation, and grain. This "v2" recipe models a specific warm, golden-hour Portra rendering.

## The grade in one line
A **warm, gentle, flattering portrait colour** with soft highlights, controlled shadows, and fine grain — beautiful skin and golden-hour light.

## How the settings build that grade
| Setting | Value | What it contributes |
|---|---|---|
| **Classic Chrome** base | — | Restrained, editorial colour that renders skin pleasingly. |
| **White Balance** | **5200K, +1R / −6B** | Fixed Kelvin daylight, pushed warm (−6 blue) → golden, but with a controlled red (+1) so skin doesn't go orange. |
| **Dynamic Range** | **DR400** | Soft, negative-film highlight roll-off; protects bright skin/backlight. ISO floor 500. |
| **Highlight** | 0 | Neutral highlights (DR400 already softens them). |
| **Shadow** | −2 | *Lifted, open shadows* → the low-contrast, airy Portra base. This is the key move. |
| **Color** | +2 | Natural, slightly rich colour — not loud. |
| **Color Chrome Effect** | Strong | Depth in warm tones so skin and warm light stay dimensional. |
| **Color Chrome FX Blue** | Off | Blues stay natural/unemphasised (X-Trans V setting). |
| **Sharpness** | −2 | Soft outlines → flattering, non-clinical rendering of faces. |
| **Clarity** | −2 | Reduced mid-tone contrast → smooth skin and a gentle glow. |
| **Grain** | Strong, Small | Visible-but-fine grain — a 400-speed pro negative. |
| **High ISO NR** | −4 | Preserve detail/grain. |

## Reading the tonal/colour signature
- **Contrast:** low, and *specifically open in the shadows* (Shadow −2). This is what makes it airy and forgiving — distinct from Gold (which deepens highlights) by instead lifting the bottom end.
- **Saturation:** natural and warm-leaning (Color +2), tuned around skin.
- **Cast:** warm/golden from 5200K −6B, but restrained on red for accurate skin.
- **Texture:** soft edges + smooth mid-tones (−2 sharpness, −2 clarity) over fine grain — the classic dreamy-portrait feel.

## Best use
**Portraits and people**, especially in **daylight and golden hour**. The warm shift makes it less ideal for indoor artificial light (it will render very warm) — for that, expect to correct WB or pick a cooler recipe.

## X-Trans V note
X-Trans V port of the X-Trans IV Portra 400 v2; the only IV→V change was **Color Chrome FX Blue Weak → Off** (deeper V blues). See [conversion notes](../../../Knowledge/x-trans-v-and-conversion.md).

## Related in this collection
- [Reggie's Portra](../reggies-portra/knowledge.md) — a more *versatile* Portra using Auto WB and no Clarity. Use Portra 400 v2 when you want a fixed, dependable warm/golden portrait cast; use Reggie's when you want it to adapt to the scene.
