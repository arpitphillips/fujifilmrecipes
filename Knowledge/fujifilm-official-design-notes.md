# Fujifilm official design notes: what the Image Design team says about its own simulations

First-party statements from Fujifilm's own Image Design team about how the film simulations were engineered, extracted from the official X Stories series and film-simulation product pages. The X-T5 manual links to these pages and almost nobody reads them, which is a shame, because this is the most authentic simulation-design source that exists: the manufacturer describing its own intent.

*Fetched 2026-07-16: [The Newest Film Simulation "ACROS"](https://www.fujifilm-x.com/global/stories/the-newest-film-simulation-acros/) · [CLASSIC Neg. official page](https://www.fujifilm-x.com/global/products/film-simulation/classic-neg/). Fetched 2026-07-20: [ETERNA](https://www.fujifilm-x.com/global/products/film-simulation/eterna/) · [NOSTALGIC Neg.](https://www.fujifilm-x.com/global/products/film-simulation/nostalgic-neg/) · [REALA ACE](https://www.fujifilm-x.com/global/products/film-simulation/reala-ace/) official pages. Mined on the second-machine session and merged into this copy 2026-07-20.*

---

## ACROS: the official engineering story

- It took over 10 years and two hardware prerequisites. Fujifilm states the fine detail "is only possible with the resolution power of 24MP" (X-Trans III) and "the complex grain effect is only possible with the powerful X-Processor Pro engine". ACROS could not exist before 2016 for engineering reasons, not marketing ones.
- The official tonality description: against plain Monochrome, ACROS applies harder compression in the midtone-to-highlight range (details read more prominent and sharper without changing dynamic range) and softer treatment in shadows to preserve detail with depth. Fujifilm's designers call the shadow region's tonal handling the thing that "determines monochrome image quality fundamentally."
- The grain architecture: grain is generated at the file's core level, not overlaid like software grain. It is tone-differentiated, with minimal dotted graininess in highlights and more pronounced grain in shadows, exactly how silver-halide film behaves, and it scales with ISO. Higher ISO means stronger grain, replicating real film stock.

### What this means for the recipes
1. The ISO dial is an authentic grain control on every Acros-based recipe. The bank's high-ISO conventions, from Tri-X's 12800 ceiling to [T-Max P3200's ISO-as-push-control](../X-T5/reference-recipes/kodak-t-max-p3200/recipe.md) and [Delta 3200's](../X-T5/originals/black-and-white/ilford-delta-3200/recipe.md), aren't workarounds. They drive Fujifilm's own film-modelled grain engine the way it was designed to be driven.
2. Acros's shadow softness is built in, so B&W recipes adding Shadow +2 or +3 are working with a curve that protects shadow detail by design. That is why deep-shadow Acros recipes (Tri-X, HP5) hold texture where a plain Monochrome curve would crush it.
3. Highlight grain stays fine no matter what. A bright high-key Acros shot will always read cleaner than a moody one at the same ISO, so grain-forward looks should expose down rather than only raising ISO.

---

## CLASSIC Neg.: the official design story

- The official colour behaviour: "colors biased toward cyan-green in the shadows and magenta in the highlights." The knowledge base had long recorded the cyan-teal shadow lean; the magenta highlight bias is the other half of the official signature.
- Tonality: "hard contrast and color contrast," with deliberate mid-tone saturation emphasis, "colorful even in the midtones."
- Design intent: modelled on consumer negative film rather than pro stock, including its degradation. Fujifilm describes film "left in cameras extended periods" and "the magic of aging" improving the image, "simulating the excitement of going to pick up your negatives after they have been developed." The look is intentionally "unbalanced and lo-fi, but nonetheless comforting… a memory of a day gone by."

### What this means for the recipes
1. The teal-orange split on Classic Neg is partly built in as cyan shadows against magenta highlights. Recipes that warm the highlights via WB red shifts ([2383 Print](../X-T5/originals/cinema/kodak-2383-print/recipe.md), [Silent Atlas](../X-T5/originals/creative/silent-atlas/recipe.md), [Mumbai](../X-T5/originals/mumbai/recipe.md)) are stacking warmth onto an already magenta-leaning highlight, which is why Classic Neg highlights can drift pink-warm rather than yellow-warm. The tuning rule that follows: if highlights look too pink, reduce the Red shift rather than adding Blue. The magenta is the sim's own bias, not a WB error.
2. Mid-tone saturation emphasis explains familiar recipe behaviour. Color adjustments on Classic Neg hit mid-tones hardest (skin, painted walls, clothing) rather than already-saturated extremes, which is why Color +3 or +4 on Classic Neg (Pacific Blues, Mumbai) pops accents without turning the whole frame neon.
3. It is an emulation of aged consumer film, by design. The datasheet-against-recipe gaps flagged in the validation audit, where recipes read grainier or more degraded than emulsion specs, mirror Fujifilm's own philosophy. The artifact-faithful target has first-party precedent.

---

## ETERNA: the official design story

- Deliberately "weak" as stills. Fujifilm openly states Eterna's muted palette and flat gradation produce a "weak look" on isolated still images, by design, mirroring how ungraded cinema footage looks outside post-production. Eterna is framed as "opening the door" to motion-picture workflows, not as a finished look straight out of camera.
- No specific film stock is named. Despite the name matching Fuji's cine-stock family, the official page describes Eterna as a cinematic colour science, not an emulation of one emulsion.

### What this means for the recipes
This is first-party confirmation of the entire cinema-family approach: the Vision3 recipes' Color +2/+3 lifts, CCE Strong, and tone shaping exist precisely because Eterna is an ungraded canvas that expects grading. In-camera cinema sims are structurally incomplete without a finishing layer, and in these recipes the settings are that finishing layer.

---

## NOSTALGIC Neg.: the official design story

- Based on the 1960s "New American Color" movement: photographers transitioning from B&W who "portrayed their complex feelings toward a disappearing era."
- The amber lives in the shadows. Where negative-film shadows normally sink cool, Nostalgic Neg. deliberately floods them with amber warmth, and Fujifilm notes this amber "does not change easily when adjusted via white balance alone" because of its perceptual strength. The X-T5 manual's "amber tinted highlights" is the other half; the warmth spans both ends, anchored in the shadows.
- Officially recommended for street at natural focal lengths, scenes where "opposites coexist" (backlight and frontal, urban and rural, present and past), and portraits in shadow, where skin keeps its richness in shade.

### What this means for the recipes
1. WB shifts on Nostalgic Neg. recipes can't neutralise the amber; Fujifilm says so directly. Cooling [California Summer](../X-T5/reference-recipes/california-summer/), [1976 Kodak](../X-T5/reference-recipes/1976-kodak/), [Thommy's Ektachrome](../X-T5/reference-recipes/thommys-ektachrome/) or [Pumpkin Soup](../X-T5/reference-recipes/ross-pumpkin-soup/) via WB will shift skies and whites while the shadow amber stays. A build that needs genuinely neutral shadows should change base sim, not WB.
2. Shadow portraits are a native strength of this base, worth remembering across the vintage-warm recipes.

---

## REALA ACE: the official design story

- Nonlinear saturation compression: "the more saturated the subject, the more muted the color." Vivid subjects are pulled back, preventing digital oversaturation. This is per-subject behaviour, not a global saturation level.
- Complex-colour reproduction, particularly purple and yellow-green, the hues that defeated traditional negative stock and drove the original Reala film's fourth-layer breakthrough.
- Tonality: "deep, soft shadows and hard highlights," the inverse of most sims' architecture, recreating era-accurate photographic prints while avoiding digital muddiness.
- Positioned as the "all-round negative for the new era" for everyday snapshots under uncontrolled light.

### What this means for the recipes
1. Color adjustments on Reala Ace behave differently from every other sim. A +Color push mostly lifts low-saturation content while the compression tames the vivid stuff. That is why [fujifilm-negative](../X-T5/reference-recipes/fujifilm-negative/) at Color +2 reads natural rather than punchy, and why Reala Ace is a poor base for deliberately vivid looks.
2. Purples and yellow-greens render uniquely well. Flowers, dusk skies and spring foliage are Reala Ace territory.
3. The deep-soft-shadows, hard-highlights split explains why the sim reads true-to-life with snap. Recipes shouldn't fight it with heavy Highlight softening.

---

## Cross-references
- Practical per-sim characters: [film-simulations.md](film-simulations.md)
- Spectral and history deep dive: [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md)
- Grain mechanics: [grain-and-detail.md](grain-and-detail.md)
- The emulsion-against-artifact fidelity framework: [validation-methodology.md](validation-methodology.md)

*Last updated: 2026-07-20*
