# Kodak Ektachrome 100D — Grade Analysis & Derivation

> Original (datasheet + characteristic validated). See [`recipe.md`](recipe.md), the [cinema README](../README.md), and the [Knowledge base](../../../../Knowledge/README.md).

## The stock
Kodak Ektachrome 100D Color Reversal Film (5294/7294) is a **positive/reversal** motion-picture stock — process E-6, the same reversal chemistry as still-photo slide film. This is structurally different from every other cinema stock in this bank: Vision3 (250D/500T/50D) and Double-X are all *negatives*. Kodak's datasheet (archived: [`kodak-motion/ektachrome-100d_5294.pdf`](../../../_reference-sources/datasheets/README.md), pub. H-1-5294) describes it as offering "**moderately enhanced color saturation** while maintaining a **neutral gray scale and accurate flesh reproduction**," with "**exceptional sharpness that is unsurpassed by any other 100-speed reversal film**," recommended for "advertising, nature cinematography, documentaries, music videos... telecine transfers and television filming."

## Why it's on the "most notable and pleasing" list
Researched directly, not assumed: Ektachrome's cinema reversal stock has a specific, well-documented recent credential — **Poor Things (2023)** used it, and critical/technical writeups describe its "elevated colour, contrast and grain" as central to the film's sensory visual style. That's a strong, checkable signal distinct from generic "people like slide film" reasoning.

## Why Provia, not Eterna
Every other cinema recipe in this bank (Vision3 250D/500T/50D, Double-X) is built on a **negative**-modelled base (Eterna for colour, Acros for B&W) — Eterna specifically exists to mimic the low-contrast, soft-shouldered character of negative motion-picture stock. Ektachrome 100D is the opposite kind of film: a **reversal** stock with the firmer, shorter latitude and punchier response characteristic of slide film. Provia — Fuji's own balanced-slide simulation — is the structurally correct analogue, the same logic used for the still [Kodak Ektachrome E100](../../kodak-ektachrome-e100/) original (which is also Provia-based). This is a deliberate, documented exception to "cinema recipes use Eterna."

## How the settings embody it
DR200 + neutral Highlight/Shadow (rather than the Vision3 family's DR400 + Highlight −2) reflect the reversal stock's shorter latitude — there's no long negative-style shoulder to protect. Color +2 + Color Chrome Effect Strong deliver the "moderately enhanced saturation" the sheet describes — more than a neutral reading, short of Velvia-level punch. The small warm WB nudge (+1R/−1B) protects "accurate flesh reproduction" against Fuji's cooler native lean. Sharpness +1 reflects the sheet's own "unsurpassed" sharpness claim. A slight underexposure bias in the EC guidance follows universal reversal-film shooting discipline: protect highlights, since (unlike a negative) there's no latitude to recover them afterward.

## The Poor Things variant
The film's *specific* grade reportedly pushed further — heavier grain, more saturation — than the stock's native, accurate-flesh-tone character. The recipe notes a stylised variant (Grain Strong/Large, Clarity +2, Color +3) for anyone chasing that particular film's look specifically, while keeping the primary recipe faithful to the emulsion as Kodak documents it.

## vs the rest of the cinema collection
| | Ektachrome 100D | Vision3 (250D/500T/50D) | Double-X |
|---|---|---|---|
| Process | Reversal (E-6) | Negative | Negative (B&W) |
| Base sim | **Provia** | Eterna | Acros |
| Tone curve | Firmer, shorter latitude | Soft, extended shoulder | Moderate |
| Colour | Moderately enhanced, accurate flesh | Naturalistic | — (B&W) |

## Validation status
**Datasheet-validated** (saturation/sharpness/balance language — archived PDF) + **characteristic-validated** against a specific, recent, well-documented production (*Poor Things*) — an independently-checkable evidence class. No Commons frame-grabs exist for cinema footage; scan-validation would need a user-supplied reference.
