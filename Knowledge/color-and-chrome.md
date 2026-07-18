# Color, Color Chrome Effect & FX Blue, the saturation/richness controls

These control how intense and how rich colours render. They sit on top of the film-sim base and the WB cast.

## Color (manual p.131)

- Range −4 to +4. "Adjust color density", i.e. global saturation.
- Positive = more saturated; negative = more muted/pastel.
- It scales saturation *uniformly*, so it can't shift hues, that's the job of WB shift and the Chrome effects.

Reading it in a grade: a recipe with Color +3/+4 wants vivid, punchy colour; Color 0/+2 is natural; negative values (rare in these recipes) push toward desaturated/pastel.

## Color Chrome Effect (CCE) (manual p.125)

- Options: STRONG / WEAK / OFF.
- Manual: "Increase the range of tones available for rendering colors that tend to be highly saturated, such as reds, yellows, and greens."
- What it actually does: adds tonal separation and depth to already-saturated warm/green colours that would otherwise clip into a flat block. Think of it as recovering gradation in a saturated flower, autumn leaf, or a red car, the colour looks *richer and more three-dimensional* rather than just brighter.
- STRONG = maximum richness/depth in those hues; OFF = flatter, more "digital" saturated colour.

Because it deepens reds/yellows/greens, CCE STRONG is common in recipes emulating rich film stocks (it stops saturated foliage and skies from looking plasticky).

## Color Chrome FX Blue (CCFXB) (manual p.125)

- Options: STRONG / WEAK / OFF.
- Manual: "Increase the range of tones available for rendering blues."
- The blue-channel counterpart to CCE: it deepens and adds gradation to blues (skies, water), making them richer and darker rather than washed out.
- STRONG = deepest, most dramatic blues; OFF = lighter, flatter blues.

### The X-Trans V blue caveat (critical for recipes)
X-Trans V sensors already render blue more deeply than X-Trans IV on several film sims (Classic Chrome, Classic Neg, Eterna, Eterna Bleach Bypass). So when an X-Trans IV recipe is ported to the X-T5, the CCFXB step is reduced by one notch to compensate:

| X-Trans IV recipe says | On X-T5 (X-Trans V) use |
|---|---|
| CCFXB **Strong** | **Weak** |
| CCFXB **Weak** | **Off** |
| CCFXB **Off** | (can't go lower — blues will simply render a bit deeper) |

This one-notch reduction is the most common IV→V conversion adjustment and appears throughout the recipes. See [x-trans-v-and-conversion.md](x-trans-v-and-conversion.md).

## Monochromatic Color (manual p.124)

Only active on Acros and Monochrome bases. Two axes:
- WARM ↔ COOL: adds a red/warm or blue/cool tone to the greys.
- G (Green) ↔ M (Magenta): the tint's secondary direction.

Used to tone a black-and-white image (e.g. a subtle cool or warm cast) without turning it into full sepia. Most classic B&W recipes leave this at 0/0 (neutral) but it's available for split-toned looks.

## Putting colour together

The colour identity of a grade is built in layers:
1. Film-sim base sets the fundamental hue rendering and how much it shifts colours.
2. WB + shift sets the overall cast (warm/cool, green/magenta).
3. Color (±) sets overall intensity.
4. CCE / CCFXB add richness/depth to warm colours and blues respectively.

A "vivid" grade stacks Velvia/Classic-Neg + positive Color + Strong Chrome effects; a "muted vintage" grade stacks Classic Chrome + modest Color + a warm WB shift.
