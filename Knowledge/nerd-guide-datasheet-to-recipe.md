# The nerd guide: turning a film datasheet into a recipe

*Sources: the [datasheet archive](../X-T5/_reference-sources/datasheets/README.md) (48 manufacturer PDFs and a [manifest](../X-T5/_reference-sources/datasheets/MANIFEST.md) of every sheet known to exist), [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md), [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md), and the worked derivations in the recipe bank, chiefly [Kodak Gold 200](../X-T5/originals/kodak-gold-200/research.md).*

This is the guide for people who want to know why a recipe says what it says, and how to build their own from primary sources instead of vibes. Everything the bank's originals do starts here: a manufacturer measured their film in a lab, published the numbers, and those numbers map onto the X-T5's menu with surprisingly little slack.

If you just want to shoot, you never need this page. If you've ever wondered why one Portra recipe feels right and another feels like a rumour, read on.

---

## Why the datasheet is the primary source

Every claim about how a film "looks" has a chain of custody problem. A YouTube comparison depends on the scanner. A lab scan depends on the operator's corrections. A Reddit frame depends on all of that plus JPEG compression and someone's Lightroom pass. The datasheet is the one document where the manufacturer stated, under controlled conditions, what the emulsion actually does.

That doesn't make datasheets the whole story. They describe the negative, not the print, and nobody ever looked at a negative for pleasure. But they anchor the search: when the sheet says the film holds 3 stops of overexposure, any recipe that clips highlights is wrong, whatever it looks like on Instagram.

## Anatomy of a datasheet

Open any sheet in the archive and you'll find some or all of these. Here's what each one is, and what it tells you.

### The characteristic curve

The single most useful plot on the sheet: density of the developed film (D) against the log of exposure (log E). Read it left to right, shadows to highlights.

- The flat left end is base-plus-fog: the density of unexposed, developed film. Nothing lives below it.
- The toe is where shadows emerge. A long, gentle toe means shadows fade in gradually and hold detail; a short, abrupt toe means shadows snap to black.
- The straight-line section's slope is gamma, the film's core contrast. Steeper means contrastier.
- The shoulder is where highlights compress. A long shoulder means highlights roll off gently and take ages to clip, which is the signature grace of colour negative film. Slide film barely has a shoulder, which is why it clips like digital.

Colour sheets plot three curves, one per dye layer. How the three run together matters as much as their shape: parallel and tightly bundled means neutral greys stay neutral all the way up the tonal range. If a curve drifts apart from the others at one end, the film has a colour cast that appears only in shadows or only in highlights, and no single white balance setting can neutralise both ends. That drift is a look, and film sims model exactly this kind of behaviour.

### Spectral sensitivity curves

How each layer responds across the wavelength spectrum. This is the input side of the two-stage system described in [the colour science article](color-science-why-film-cannot-be-faked.md). What to look for: where the red layer's sensitivity peaks (shifted toward orange reads warm), how much the layers overlap (more overlap means more colour contamination and softer separation), and whether the film is panchromatic or orthochromatic in B&W (ortho films are blind to red, which is why skin goes dark and dramatic on them).

### Dye density curves (colour) and granularity (everyone)

Dye curves are the output side: how pure each dye is. Purer dyes mean more saturation headroom, which is the actual mechanism behind Velvia (see the Provia-Velvia case study in the colour science article).

Grain gets stated one of two ways:

- RMS granularity: the older standard, a diffuse measurement of density fluctuation. Under about 9 reads as very fine; 10 to 13 as moderate; 14 and up as visibly gritty. Double-X is RMS 14, and its recipe wears Strong/Large grain because of it.
- Print Grain Index (PGI): Kodak's newer perceptual scale, measured off a 4×6 print. 25 is the threshold where grain becomes noticeable; Gold 200's PGI of 44 is clearly visible; Portra 400 sits in the low 30s. The two scales don't convert cleanly, so compare within a scale, never across.

### Latitude, reciprocity, and the rest

Exposure latitude (Gold 200: minus 2 to plus 3 stops) tells you which direction the film forgives, and that becomes the recipe's exposure compensation guidance. Reciprocity failure tables and push-processing notes matter to film shooters but have no digital equivalent; read them for cultural literacy and move on. Resolving power and MTF curves inform the Sharpness decision at the margins.

---

## The mapping table

This is the heart of the method. Each measurable thing on the sheet lands on a specific X-T5 control.

| Datasheet fact | X-T5 control | How to read it |
|---|---|---|
| Long highlight shoulder | DR400 + negative Highlight | The more overexposure the film forgives, the more headroom and roll-off the recipe needs |
| Short shoulder (slide film) | DR200 or DR100, Highlight near 0 | Reversal clips; don't fake latitude it never had |
| Deep toe, held shadows | Positive Shadow, but gently | +1 to +2 covers almost every real film; +3 is crushing |
| Lifted toe, milky shadows | Negative Shadow | The faded-print look lives here |
| Gamma (slope) | Highlight and Shadow together | Steep slope: raise both ends' contrast; flat slope: soften both |
| Curves tightly bundled | WB shift near neutral | The film is grey-balanced; big shifts betray it |
| One layer running high | WB shift toward that bias | Gold's high blue-sensitive (yellow-forming) layer is its +3R warmth |
| RMS or PGI figure | Grain size and roughness | Fine tier: Weak/Small. Middle: Weak/Large or Strong/Small. Gritty (RMS 13+): Strong/Large |
| "Saturated" marketing plus dye purity | Color and Color Chrome Effect | "Moderately enhanced": Color +2 with CCE Weak or Strong. "Vivid": +3 and up |
| Skin-priority language | Small warm shift, restrained Color | Portrait films protect skin before saturation, and so should their recipes |
| Sharpness and edge-contrast claims | Sharpness, occasionally Clarity | "Exceptional sharpness": 0 to +2. Consumer softness: −1 to −2 |
| Film speed and intended light | ISO ceiling and WB base | A 50-speed film pushed to ISO 12800 stops being that film |

### What the sheet cannot give you

Four decisions always remain judgment calls, and honest recipes say so:

1. The base simulation. The sheet narrows it (negative stock behaviour points to Classic Chrome, Classic Negative or Eterna; reversal points to Provia, Astia or Velvia) but the final call comes from comparing renderings, which is why the bank documents a why-this-base argument for every original.
2. Color Chrome FX Blue. No datasheet measures Fujifilm's blue-deepening processing. It gets set from observed sky and shadow behaviour, and it is also the control that shifts between sensor generations (see [x-trans-v-and-conversion.md](x-trans-v-and-conversion.md)).
3. Clarity. Micro-contrast has no analogue measurement on a film sheet. The bank's default is 0, deviating only when a film's documented character demands it, like Pan F's "edge contrast" or Tri-X's grit.
4. The print or scan you're imagining. A negative was always interpreted by paper or a scanner. Decide which interpretation the recipe targets and write it down; most disagreements between competing recipes for the same film are actually disagreements about this.

---

## Worked example: Gold 200, from numbers to menu

The full dossier is in the recipe's [research notes](../X-T5/originals/kodak-gold-200/research.md); here is the skeleton, sheet fact on the left, setting on the right.

| E-7022 says | Recipe says |
|---|---|
| Daylight-balanced, filters required under tungsten | Daylight WB base |
| Blue-sensitive layer runs high; warm dye balance | +3 Red / −5 Blue shift |
| Latitude −2 to +3 stops | DR400, Highlight −2, expose +2/3 to +1 |
| "Saturated colors" on a consumer stock | Classic Chrome base, Color +3, CCE Weak |
| Print Grain Index 44 | Grain Strong, Small |
| "High sharpness" but consumer-soft rendering | Sharpness −2 |

Then real scans adjusted two values (the WB shift down from +4R, Clarity from −2 to 0), which is the point of the [validation ladder](validation-methodology.md): the datasheet proposes, the scans dispose.

---

## Nerd skepticism: reading other people's recipes

The same knowledge runs in reverse as a detector. Signals worth checking before trusting a recipe that names a film:

- A slide-film recipe on DR400 with Highlight −2 is describing a negative, whatever the title says.
- Grain settings that contradict the film's granularity class. A "Pan F" recipe with Strong/Large grain isn't Pan F; the [FP4 reference](../X-T5/reference-recipes/ilford-fp4-plus-125/) in this bank documents exactly such a conflict rather than hiding it.
- A "daylight film" recipe on Auto white balance can't hold the film's fixed colour response across scenes. Sometimes that's a deliberate, stated choice, as in [Reggie's Portra](../X-T5/reference-recipes/reggies-portra/); it stops being fine when it's unstated.
- No stated sensor generation. Blue rendering changed between X-Trans IV and V, and a recipe that doesn't say which generation it was built on will render differently on yours. The [conversion guide](x-trans-v-and-conversion.md) covers the fix.

None of this makes a disagreeing recipe bad. Purpose-faithful beats emulsion-faithful for plenty of real shooting. The skepticism is about claims: when a recipe says "this is Portra 400", the sheet is how you check.

---

## Going deeper

- [Film chemistry fundamentals](film-chemistry-fundamentals.md): why grain, speed and contrast are chemically coupled, which is the reason the mapping table works at all.
- [Why film cannot be faked in post](color-science-why-film-cannot-be-faked.md): the two-stage colour model that makes the base-simulation choice matter.
- [The validation methodology](validation-methodology.md): how a datasheet-derived draft gets promoted to scan-validated.
- [The datasheet archive](../X-T5/_reference-sources/datasheets/README.md) and its [manifest](../X-T5/_reference-sources/datasheets/MANIFEST.md): every sheet on disk, and every sheet known to exist.

*Last updated: 2026-07-19*
