# Mumbai Monsoon — Grade Analysis & Understanding

> Original design. Read alongside [`recipe.md`](recipe.md), [`recipe-video.md`](recipe-video.md), and the [Knowledge base](../../../Knowledge/README.md).

## The problem this grade solves
Mumbai's monsoon presents a specific and difficult set of conditions, and the grade is engineered against each one:

| Monsoon condition | Consequence for the image | Design response |
|---|---|---|
| Heavy overcast, diffused light | **Flat, low-contrast, lifeless** frames | A film sim with *hard tonality* (Classic Negative) + deliberate shadow deepening to rebuild contrast |
| Bright grey sky | **Clipped, blown highlights** | DR400 + Highlight −2 for a soft, protected roll-off |
| Cool blue-grey ambient (~6500–7500K) | **Depressing blue cast**, dead skin | A warm WB nudge (+2R/−2B at 6500K) to restore life without killing the mood |
| Rain, wet streets, reflections | Wants **cool, moody, reflective** tones | Classic Neg's teal shadows + CCFXB Weak deepening blues/teals |
| Colour accents (umbrellas, taxis, signage) | Need to **pop** against grey | CCE Strong + a small Color bump so accents stay rich |
| Humidity/haze | Soft, atmospheric | Sharpness −1, Clarity 0 (mist filter for extra haze), coarse grain |
| Low light on dark days | **High ISO / noise** | ISO ceiling raised to 12800; grain masks noise |

## The look in one line
A cinematic, moody, cool-shadowed monsoon grade: teal-leaning wet shadows and protected grey highlights, with just enough warmth and saturation to keep skin and colour accents alive.

## Why Classic Negative (not Eterna or Classic Chrome)
- Eterna is the obvious "cinematic" pick, but it is low contrast, and layering it on already-flat overcast light compounds the flatness into mush. (See the alternative below if you want maximum softness.)
- Classic Chrome is muted and calm but lacks the teal-shadow character that reads as "rain".
- Classic Negative is the sweet spot. Its hard tonality actively fights the flat light, and its cool, hue-separated shadows are exactly the wet-street rain palette we want. It also holds colour accents well.

## The teal-and-warm cinematic split
The signature of this grade is a subtle teal-shadow, warm-mid split, the classic cinematic monsoon look:
- Cool side: Classic Neg's native teal-leaning shadows, reinforced by Color Chrome FX Blue (Weak) deepening the blues and teals in wet surfaces, rain, and the grey sky.
- Warm side: the +2 Red WB shift keeps skin, headlights, shop windows and taxis warm.
The two pull against each other for depth and mood without heavy editing.

## Contrast logic
- Highlight −2 with DR400: grey skies are the enemy here. They blow out and turn into white voids, and this combination softens and holds them.
- Shadow +1 rebuilds the contrast the flat light removed, adding weight and mood. Only +1, though, because monsoon scenes are already dim and +3 would crush the wet-street detail that makes these frames work. Push to +2 for heavier weather.

## Exposure approach
Overcast fools the meter: the bright grey sky makes the camera underexpose your subject. But for a moody result you don't want to over-brighten either. Meter for the subject and lean slightly under (−1/3) for atmosphere, going to +1/3 when you need faces clean. Judge per scene. This is a mood grade, not a documentation grade.

## Alternative: "Monsoon Cinema" (softer/moodier)
For a dreamier, more filmic take, swap the base to Eterna, keep DR400 and Highlight −2, and set Shadow +2, Color +2 (Eterna is desaturated so it needs the bump), Clarity −2, and WB 6300K +1R/−2B. Flatter and softer. Better for slow, atmospheric rain work, worse for snappy street.

## Related
- For **night rain with neon**, use [CineStill 800T](../../reference-recipes/cinestill-800t/knowledge.md) instead (tungsten-blue night specialist).
- Shares the Classic Negative base with [Pacific Blues](../../reference-recipes/pacific-blues/knowledge.md) (cooler, beachy) and [Reala Ace](../../reference-recipes/reala-ace/knowledge.md) (neutral). Compare them to see how the same base is steered to very different moods.
