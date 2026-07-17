# CineStill 800T — Grade Analysis & Understanding

> Read alongside [`recipe.md`](recipe.md) and the [Knowledge base](../../../Knowledge/README.md).

## The film being emulated
**CineStill 800T** is a cult **tungsten-balanced** film: repackaged Kodak Vision3 500T motion-picture stock with the anti-halation *Remjet* layer removed so it develops in standard C41. Two consequences define its look:
1. **Tungsten balance** → shot in daylight it goes strongly **blue**; it's designed for **artificial/night** light.
2. **No Remjet** → bright light sources **bloom/halate** with a red-pink glow (streetlights, neon).

So the target look is **cool, cinematic night photography** with glowing lights.

## The grade in one line
A **cool, tungsten-blue, cinematic low-contrast night look** with soft mids, deep-but-lifted shadows, heavy grain, and rich colour around light sources.

## How the settings build that grade
| Setting | Value | What it contributes |
|---|---|---|
| **Eterna** base | — | Cine profile: low contrast, low saturation, rich shadow tone → the filmic foundation. See [film-simulations](../../../Knowledge/film-simulations.md). |
| **White Balance** | **Fluorescent 3, −6R / −4B** | The key move: Fluorescent 3 (cool white) plus a big −red pushes a strong **cool/blue tungsten-night cast** even in mixed light. Used creatively, not literally. |
| **Dynamic Range** | **DR400** | Soft highlight latitude → protects bright lights and windows at night; ISO floor 500. |
| **Highlight** | 0 | Neutral highlights (Eterna + DR400 already soft). |
| **Shadow** | +2 | Deeper shadows for night contrast/mood — but not crushed (Eterna keeps shadow detail). |
| **Color** | +4 | Boosts Eterna's naturally-low saturation so neon/streetlight colour reads richly. |
| **Color Chrome Effect** | Strong | Depth in the saturated warm light sources. |
| **Color Chrome FX Blue** | **Weak** | Deepens the blues (the cast) — reduced from Strong for X-Trans V. |
| **Sharpness** | −3 | Soft outlines → cinematic, not clinical. |
| **Clarity** | **−5** | Maximum softness/mid-tone reduction → the dreamy nighttime glow that stands in for the Remjet halation. |
| **Grain** | **Strong, Large** | Heavy coarse grain → motion-picture-stock texture. |
| **High ISO NR** | −4 | Preserve detail/grain (important at the high ISOs night shooting needs). |

## Reading the tonal/colour signature
- **Contrast:** low overall (Eterna + −5 clarity + −3 sharpness) with a modest shadow deepening (+2) for night weight.
- **Saturation:** pushed up (Color +4) specifically so light sources glow with colour against the dark.
- **Cast:** strongly cool/blue — the defining tungsten-film characteristic.
- **Texture:** the softest *and* grainiest combination here — soft edges/mids over heavy coarse grain = pure cinematic night.

## Best use
**After-dark photography** — city streets, neon, streetlamps, windows, interiors with mixed artificial light. Can give interesting cool results in daylight too (as tungsten film does), but it's built for night.

## X-Trans V note
X-Trans V port of the X-Trans IV CineStill 800T; the only IV→V change was **Color Chrome FX Blue Strong → Weak** (Eterna blues render deeper on V). See [conversion notes](../../../Knowledge/x-trans-v-and-conversion.md).

## Related in this collection
- The only Eterna-based (cinematic) recipe in this set, and the go-to for night/mood. For a *warm* vintage look instead, see [Kodak Gold 200](../../originals/kodak-gold-200/knowledge.md); for cool-but-not-night, [Pacific Blues](../pacific-blues/knowledge.md).
