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

### Deeper: the X-H1 development story *(added iteration 11)*
Source: [X Stories, X-H1 Development Story #4](https://www.fujifilm-x.com/global/stories/x-h1-development-story-4/), the camera that introduced Eterna.

- Purpose: designed to achieve the "Cinema Look" in one take, drawing on Fujifilm's motion-picture film heritage back to 1934.
- Hard technical figure: "12-stop wide" dynamic range, which Fujifilm calls comparable to F-Log, with "room for post production." Eterna is a *latitude* profile as much as a colour one.
- Tonality (officially confirmed): "The highlight and shadow tones are both soft."
- Blues are shifted toward cyan. Explicitly: *"the colour is shifted toward cyan"* in blue tones "so that the blue sky in the background will then complement the story" rather than compete with it.
- Method, the inverse of Velvia: where Velvia enhances, Eterna is *"an art of omission"*, with saturation suppressed and "slightly adjusted on each key colour."
- Why cinema differs from stills: *"In photographic expression, the basic communication is complete in a single frame"* with enhanced colour, whereas *"cinema communicates differently"*, and saturation must be suppressed so that "a particular colour would not stand out" across a sequence.

### What this means for our recipes
1. The 12-stop / F-Log-comparable figure is the strongest argument for the cinema recipes' shape: Eterna is engineered as a *gradeable* profile with latitude in reserve, which is exactly why the Vision3 recipes' Highlight −2 doesn't produce mush: there is real range underneath. It is also directly relevant to any F-Log2 workflow question, since Eterna sits in the same latitude class.
2. The cyan blue-shift is the missing piece of the cinema look. Vision3 recipes need *less* cooling than instinct suggests, the base is already shifting blue toward cyan. If skies read too teal, the fix is a +Red / −Blue WB nudge, not more cooling.
3. "A particular colour would not stand out" is the design rationale behind every Color-restraint decision in the cinema family, and explains why Eterna stills recipes need a Color lift to work as single frames, a stills viewer has only one frame to be moved by.

This is first-party confirmation of the entire cinema-family approach: our Vision3 recipes' Color +2/+3 lifts, CCE Strong, and tone shaping exist precisely because Eterna is an ungraded canvas that *expects* grading. It also officially validates the broader point that in-camera cinema sims are structurally incomplete without a finishing layer (in-camera settings for stills, post/LUTs for footage).

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

## CLASSIC CHROME: the official design story *(added iteration 5)*

Source: Fujifilm X global film-simulation page, CLASSIC CHROME.

- It is not based on any analog film at all. Fujifilm states they created "an imaginary film" to emulate 20th-century photojournalism magazines, the "golden age of documentary and print media". There is no Kodachrome heritage to be faithful to; the target is a *printed-page* aesthetic.
- Colour vs PROVIA: "more subdued with suppressed magenta and cool shadows." Both halves matter, the muting is specifically magenta-suppressing, and the shadows are natively cool by design.
- Character: an "assured, composed look" rather than a bright or transparent one.
- Officially recommended for "fashion, interior, and product photography", and pitched as *"the first look to try when you think, 'I want to make a cool photo today!'"*

### What this means for our recipes
1. Stop treating Classic Chrome as a Kodachrome stand-in. It has no film ancestor, so a Classic Chrome recipe can never be "datasheet-validated" against a stock, it can only be validated against the *look* it targets. Our Kodachrome recipes sit on Classic Chrome for practical reasons, and that should be stated as a deliberate approximation rather than implied lineage.
2. "Cool shadows" is official, not an artifact. Any recipe wanting warm shadows on this base *must* correct with a +Red WB shift. This is now first-party justification, not inference.
3. "Suppressed magenta" explains why reds fall to terracotta/brick rather than staying pure red, and why skin stays neutral rather than going pink. Recipes wanting a true red must add it back with Color/CCE, not expect the base to deliver it.
4. Fujifilm itself points this base at interiors and fashion: direct first-party backing for the editorial/interior recipes built on it.

---

## ASTIA: the official design story *(added iteration 5)*

Source: Fujifilm X global film-simulation page, ASTIA/Soft.

- Headline: "Balanced Tone and Saturation."
- The defining behaviour: "The transition from highlights to shadows is smooth, while saturation is maintained." Soft at *both* ends of the curve, but unlike a flat log-style profile, it does not pay for that softness in colour.
- Character: "a graceful look with a rich mixture of tonal gradation and saturation."
- Engineered for uncontrollable light: Fujifilm names *bright, uncontrolled outdoor lighting* (weddings in dappled sun) and *mixed colour-temperature scenes* (night with varied sources) as the design targets.
- History: "When analog film was losing popularity, many photographers asked for ASTIA to continue."

### What this means for our recipes
1. Astia is the correct base for high-key work, and now provably so: soft highlights *with* saturation retained is exactly what a bright, white-forward look needs. You can push exposure without the frame going pale and lifeless.
2. It is the mixed-light base. Recipes that must survive dappled sun or mixed colour temperature should prefer Astia over Provia/Velvia, that is its stated engineering purpose, not a stylistic preference.
3. Don't stack heavy Highlight softening on it. The softness is already in the base; −1 to −1.5 is plenty, and more flattens the gradation Fujifilm designed in.
4. Astia's soft *shadow* tone is easy to forget, recipes wanting genuine depth on this base need to get it from DR/Shadow, not from the simulation.

---

## PROVIA: the official design story *(added iteration 6)*

Source: Fujifilm X global film-simulation page, PROVIA/Standard.

- The baseline is not neutral. Provia is built on "memory colours", Fujifilm's stated principle that photographs should match how a scene *felt*, not how it measured. "Memories of the feelings they create never fade."
- Per-hue tuning is explicit, via selective magenta control: skies get clarity and definition, sunsets are intensified, foliage renders lusher/richer green, and skin tones are deliberately muted in orange for "appealing portraits."
- Positioning: "a high level of versatility that makes you think, *'Let's try it with PROVIA first.'*"

### What this means for our recipes
1. Never describe Provia as "the neutral/unmodified base." It is an opinionated memory-colour rendering with four documented per-hue interventions. A recipe built on Provia inherits boosted skies, boosted sunsets, lusher greens and *deliberately damped orange skin*, that last one matters most, because it means Provia damps skin saturation before your Color setting ever applies.
2. This reframes the whole simulation ladder in the [comparison table](film-simulations.md): the axis is not "neutral → stylised" but "memory-colour → differently-stylised." Classic Chrome's "subdued vs Provia" is subdued *relative to an already-warmed baseline*.

---

## VELVIA: the official design story *(added iteration 6)*

Source: Fujifilm X global film-simulation page, VELVIA/Vivid.

- The non-obvious fact: Velvia "maintains colour balance so that no colour is emphasised more than another." The saturation lift is uniform across hues, Velvia is a global gain, not a selective enhancer.
- Tone: **hard highlights *and* hard shadows**, "deep shadows" that "leave a bold impression."
- Design intent: to "convey the excitement of colour" and capture "strong emotion", aimed at "expansive skies, deep oceans, vivid greenery, or autumn leaves."
- Official use: "ideally suited to landscapes and nature, but its strong contrast of colour and light also looks dramatic in urban nightscapes and sports scenes."

### Deeper: the Velvia development story *(added iteration 7)*
Source: [X Stories, The World of Film Simulation, episode 3](https://www.fujifilm-x.com/global/stories/the-world-of-film-simulation-episode-3/).

- Velvia's concept is "Memorized Colour": "the colour of how photographers remember the scene… also the colour of how the viewers expect to see upon looking at the photographs." Photography as "a medium of emotional communication," not literal reproduction. Their justification is sharp: *"if the colour is truly a reflection of reality, then people would often find that 'the photo is missing something.'"*
- Sky blues get magenta added. Explicitly: "a bit of magenta is being added" to blue to make it "more memorable" and produce "the most comfortable and eye-pleasing blue." Greens were separately optimised against human memory of natural scenes.
- Where the data came from: Fujifilm is uniquely "a camera manufacturer, a film manufacturer, and a print developer," and mined a "tremendous volume of *printed* feedback" on which colours "stay strong in people's memory."
- Practical: unlike real Velvia (ISO 50/100 only), the simulation can be driven at any ISO, "control as freely as you like."

> **⚠️ Source nuance, recorded rather than silently resolved.** The Velvia *product page* says the sim "maintains colour balance so that no colour is emphasised more than another," while this development story says magenta is added to blues. These are best read as different scopes: no single hue dominates the *overall* balance, but there is a targeted magenta lift in the blue channel. Treat "uniform gain" as true at the global level and false at the per-hue level.

### The blue/sky axis: the single most actionable cross-simulation finding
**Three** first-party statements, each moving blue in a different direction. Fujifilm has published exactly how each base treats the sky:

| Simulation | Blue/sky treatment (official) | Result | Reach for it when |
|---|---|---|---|
| **VELVIA** | **"a bit of magenta is being added"** to blue | Deep, rich, "memorable" sky | You want the sky to be the subject |
| **CLASSIC CHROME** | **"removed the magenta component"** from skies | Pale, airy, documentary sky | The sky should recede behind the story |
| **ETERNA** | **"the colour is shifted toward cyan"** | Cinematic teal sky that "complements the story" | You want a graded, filmic backdrop |

**Recipe-selection rule:** the base sim decides your sky before any setting you choose. Trying to reach one of these from another via Color / WB shift / Color Chrome FX Blue is fighting a deliberate design decision, and it shows.

**Corollaries worth memorising:**
- Blues reading purple on Velvia? That's the designed magenta lift, correct with WB Blue up / Red down, not by cutting Color.
- Want a deep sky on Classic Chrome? You can't get there, change base. FX Blue fights the removal.
- Skies too teal on Eterna? The cyan shift is already in the base, nudge +Red / −Blue; don't add more cooling.

### What this means for our recipes
1. Velvia and Color Chrome Effect are opposite tools, and this is the cleanest statement of why. Velvia raises *every* hue equally; CCE adds density only where colour is *already* saturated. Stacking both is how a frame goes plastic, on a Velvia base, prefer CCE Weak/Off and let the simulation carry saturation.
2. Hard at both ends of the curve is official: so Velvia recipes need Highlight/Shadow *negative* values just to reach normal contrast. A Velvia recipe at Highlight 0 / Shadow 0 is already a high-contrast recipe.
3. Fujifilm's own "urban nightscapes" recommendation is under-exploited in the bank, Velvia is more than a landscape base.

---

## PRO Neg. Hi / Std: the official design story *(added iteration 6)*

Source: Fujifilm X global film-simulation page, PRO Neg., billed as "The Pinnacle of Negative Film."

- PRO Neg. Std: "optimized for use in situations with good lighting and moderate contrast, such as studio photography." Parameters apply straightforwardly, making it the best base for learning what each adjustment does.
- PRO Neg. Hi: "boosts contrast, creating shadows even in flat light, making it easier for creating outdoor portraits." Aimed at natural light you cannot modify, and at street work in bright conditions for its contrast and highlight retention.
- Design rationale: "negative film's characteristic softer look and compatibility with prints made it a favorite of many photographers."

### What this means for our recipes
1. "Creates shadows even in flat light" is the single most useful sentence here. It is precisely why Pro Neg Hi is the right base for soft-light portrait stocks like [Pro 400H](../X-T5/originals/fujicolor-pro-400h/recipe.md), the film is famously flat and pastel, but its *scans* still show structure. The base supplies the structure the light doesn't.
2. The Hi/Std choice is a lighting decision, not a taste one: controlled/studio light → Std; uncontrolled/flat outdoor light → Hi. Recipes should state which lighting they assume.
3. Std is the honest base for teaching and for tuning: because adjustments land predictably, it is the right place to prototype a new look before porting it to a more opinionated base.

---

## CLASSIC CHROME: the *development story* *(added iteration 7, deeper than the product page)*

Source: [X Stories, Film Simulation "CLASSIC CHROME"](https://www.fujifilm-x.com/global/stories/film-simulation-classic-chrome/). This long-form piece goes well past the product page.

- Method: the team analysed "hundreds of documentary-style images" before designing the mode. The target is "the ambience found in documentary-style photographs and magazines," and the name refers to "a mode reminiscent of the images each individual carries in their mind."
- **The sky decision, magenta was *removed*. The developers were "particularly struck by how tones in skies were reproduced"; where traditional colour design added magenta to skies, Classic Chrome "removed the magenta component"** to "create new colours" instead.
- Reds and greens are hue-shifted rather than merely desaturated: the mode **"controls the saturation *and hue* of reds and greens to produce a unique chromatic balance."**
- Overall: images "generally have low colour saturation and full-bodied tones."
- It was tuned for screens, not paper: Fujifilm "worked to create a mode that looks like a print when viewed on an LCD screen in JPEG format," acknowledging photos are now viewed on devices rather than printed.

### What this means for our recipes
1. The olive-green and terracotta-red signature is officially designed in. "Controls the saturation *and hue* of reds and greens" is first-party confirmation that greens shift toward olive and reds toward brick, these are not scanner artifacts or our imagination. Any recipe relying on that palette (interiors, European travel, documentary street) is riding the base's intent.
2. Removed sky magenta explains the pale, hazy blue Classic Chrome gives, and warns that adding Color Chrome FX Blue fights a deliberate design decision. If you want deep skies, this is the wrong base.
3. "Looks like a print on an LCD" is why Classic Chrome recipes so often need *no* Clarity and little Sharpness: the base is already doing print-emulation work at the tone level. Piling micro-contrast on top double-processes it.

---

## CLASSIC CHROME: the tonality data *(added iteration 9, the most actionable set yet)*

Source: [X Stories, The World of Film Simulation, episode 2](https://www.fujifilm-x.com/global/stories/the-world-of-film-simulation-episode-2/).

- It is the lowest-saturation simulation Fujifilm makes. Stated flatly: *"The saturation is the lowest among all film simulations. The saturation has been minimized to the limit."*
- The tone curve is asymmetric: *"The shadow end is hard, but the tonality is soft on the highlight end."* Classic Chrome protects highlights natively and crushes shadows natively.
- Contrast ranking: *"The tonality is a little above the centre line and is the second hardest after Velvia."* Also: Monochrome shares Provia's tonality design, so Classic Chrome is harder than Monochrome, counter-intuitive, and worth remembering when choosing between them for high-contrast scenes.
- Design philosophy: *"Photography is often called 'Art of omission.' CLASSIC CHROME omits the element of colour in order to make the story you want to tell stand out."* The intended user is "photographers that advocate for contents."
- Official shooting technique: underexpose the shadows while preserving the highlights. This "makes the subject more live and the texture remains present."

### What this means for our recipes
1. The asymmetric curve rewrites how we should set tone on this base. Highlights are *already* soft, so heavy Highlight-negative values are redundant, −1 is usually enough, −2 goes limp. Shadows are *already* hard, so this base needs a Shadow lift (−1/−2) just to reach normal shadow detail. Every Classic Chrome recipe in the bank should be checked against this asymmetry.
2. "Lowest saturation of all simulations" settles a long-running question: Color +1 on Classic Chrome is not a "boosted" recipe, it is a mild correction from a deliberately floored baseline. Recipes need not apologise for it.
3. "Second hardest after Velvia" is a surprise: Classic Chrome *looks* gentle because saturation is low, but its tonality is near the top of the contrast ladder. Muted ≠ flat. This explains why Classic Chrome recipes can feel punchy despite their quiet palette.
4. The exposure advice is free technique to pass to users: protect highlights, let shadows fall. It pairs exactly with the native curve (soft highlights can take the protection; hard shadows *want* to go dark).

---

## The Image Design team: cross-cutting philosophy *(added iteration 7)*

Source: [X Stories, Film Simulation, Revolution by Continuous Evolution](https://www.fujifilm-x.com/global/stories/film-simulation-revolution-by-continuous-evolution/).

- What a film simulation actually is: "Image design is a work of converting the raw signal while understanding the difference of the spectral sensitivity", i.e. the sensor does not see as the eye sees, so the conversion is intentional interpretation, never reproduction.
- The vision is fixed; the machinery isn't: "The vision of ideal colour reproduction for FUJIFILM remains the same. It's just that devices have evolved, processor has evolved, and the algorithm has evolved." And candidly: "there are still hundreds of things to do to reach the ideal vision."
- Newer processors extract more from the same signal: "it picks up signals that were not previously picked up… the camera got better at extracting information from the raw signals," enabling "more detail without supersaturation." All colour sims gained "toughness against colour supersaturation."
- A hard constraint most people miss: the EVF must render the sim live, "If the film simulation is set to Velvia, then we have to show the world of Velvia in real time. EVF has to be that *what you see is what you get*."

### What this means for our recipes
1. This is the strongest available argument for the bank's core premise: that the in-camera JPEG is the archival primary. A simulation is a spectral-sensitivity-aware conversion of raw sensor signal; post-processing an already-demosaiced file cannot reconstruct that step. It belongs alongside [why film cannot be faked](color-science-why-film-cannot-be-faked.md).
2. "Toughness against colour supersaturation" is a generational trait: it is *why* an X-Trans IV recipe ported to X-Trans V can take a Color value that would have looked garish on older bodies, and part of why the [conversion rules](x-trans-v-and-conversion.md) exist at all.
3. WYSIWYG EVF is a practical workflow gift: you are previewing the finished JPEG before the shutter. Recipes should be judged in the viewfinder in the actual light, not guessed at from a settings table.

---

## COLOR CHROME EFFECT: the origin story *(added iteration 12)*

Source: [X Stories, GFX Technologies #6](https://www.fujifilm-x.com/global/stories/gfx-technologies-6/). Nearly every recipe in this bank sets this control; almost none of this was previously recorded.

- It is modelled on a real film: FORTIA. Color Chrome Effect was developed from Fortia reversal film, Fujifilm's notoriously ultra-saturated slide stock, to replicate its "higher contrast and more vivid colour" *while maintaining tonality*.
- The design premise, in their words: *"One of the characteristics of reversal colour film is that tonality remains even in high contrast range."* That retained tonality is what CCE is reproducing.
- The mechanism is gradation detection, not saturation: *"By analysing the light and information received on the sensor surface, one can detect slight gradation. Color Chrome Effect uses this to create tonality while maintaining high contrast."*
- A processing cost, historically: on the X-Processor Pro generation, CCE "needs about 1.0 sec. to process," which blocked continuous shooting and AF-C. *(Generational caveat. This is the 2016-era processor. The X-T5's X-Processor 5 carries no such documented restriction; I have found no first-party statement of a modern figure, so treat the 1.0 s as historical context for why the control exists the way it does, not as current X-T5 behaviour.)*
- The capstone statement: *"no matter what you do in Velvia mode, it will never turn into Fortia."* Simulations are not reachable from one another by adjusting settings.
- On philosophy: *"Every photographer seeks different colour. But if a few clicks on the camera could save you an hour of labour, then you might as well just take advantage of it."*

### What this means for our recipes
1. CCE is a tonality tool, not a saturation tool, now sourced. The bank has described it as "adds density and gradation *inside* already-saturated colours rather than adding overall saturation." Fujifilm's mechanism description confirms this exactly. It is why CCE Strong makes wood, brass, terracotta and deep foliage look rich without the frame reading over-saturated.
2. It explains the Velvia conflict precisely. Velvia is a *uniform gain*; CCE is a *gradation-preserving* pass on already-saturated areas. Stacking them doesn't just over-saturate, it puts a tonality-recovery algorithm to work on colour that has already been pushed past where gradation survives. Hence the plastic look.
3. "Never turn into Fortia" is the capstone of this whole research seam. Fujifilm states outright that no combination of settings converts one simulation into another. That is the authoritative backing for everything in the [blue/sky axis](#-the-bluesky-axis--the-single-most-actionable-cross-simulation-finding) and the [per-sim curve table](dynamic-range-and-tone.md): choose the base first, settings tune a look, they do not relocate it.
4. Fortia lineage is a genuine gap-filler. Fortia SP never had a Fujifilm X recipe in this bank, yet its DNA ships inside every recipe that sets CCE. Worth considering as a future original.

---

## Coverage status

All nine colour bases plus ACROS now have first-party design notes: Provia, Velvia, Astia, Classic Chrome, Pro Neg Hi/Std, Classic Neg., Nostalgic Neg., Eterna, Reala Ace, ACROS. *(Eterna Bleach Bypass and Sepia/Monochrome have no dedicated official page.)*

---

## Cross-references
- Practical per-sim characters: [film-simulations.md](film-simulations.md)
- Spectral and history deep dive: [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md)
- Grain mechanics: [grain-and-detail.md](grain-and-detail.md)
- The emulsion-against-artifact fidelity framework: [validation-methodology.md](validation-methodology.md)

*Last updated: 2026-07-20*
