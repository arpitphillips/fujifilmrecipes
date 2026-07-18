# Kodak Ektachrome 100D (5294) — Fujifilm X-T5 (X-Trans V) · CINEMA

A color reversal (slide/positive) motion-picture stock, structurally different from every Vision3 stock in this collection, which are all negatives. Daylight-balanced, EI 100, marketed by Kodak as offering "moderately enhanced color saturation... while maintaining a neutral gray scale and accurate flesh reproduction" with "exceptional sharpness... unsurpassed by any other 100-speed reversal film." It was notably used in Poor Things (2023), where its elevated colour and contrast were central to the film's sensory visual style. The base is Provia: Fuji's own balanced-slide profile is the correct structural analogue to a reversal stock, distinct from the negative-modelled Eterna used for the Vision3 recipes. Grounded in the Kodak technical data sheet (archived: [`kodak-motion/ektachrome-100d_5294.pdf`](../../../_reference-sources/datasheets/README.md)). See [`knowledge.md`](knowledge.md).

## Stills settings
| Setting | Value |
|---|---|
| Film Simulation | Provia / STD |
| Grain Effect | Weak, Small |
| Color Chrome Effect | Strong |
| Color Chrome FX Blue | Weak |
| White Balance | Daylight, +1 Red & −1 Blue |
| Dynamic Range | DR200 |
| Highlight (Tone Curve) | 0 |
| Shadow (Tone Curve) | 0 |
| Color | +2 |
| Sharpness | +1 |
| High ISO NR | −4 |
| Clarity | 0 |
| ISO | Auto, up to ISO 800 |
| Exposure Compensation | −1/3 to 0 (typically — reversal-film discipline: expose for highlights) |

This stills recipe uses the grain and Color Chrome effects that movie mode can't. For the movie-mode adaptation see [`recipe-video.md`](recipe-video.md).

### Why these values
- Provia base, not Eterna. This is the one cinema recipe in the bank that deliberately skips Eterna: Eterna models negative-film cinema tonality with its low contrast and soft shoulder, while Ektachrome 100D is a reversal stock, structurally a slide film. It needs Provia's balanced-slide character, the same reasoning used for the still [Kodak Ektachrome E100](../../kodak-ektachrome-e100/) original.
- DR200 with Highlight 0 and Shadow 0, rather than the Vision3 negatives' DR400 and Highlight −2. Reversal film has a shorter, firmer tonal latitude than a negative, and with no long soft shoulder to model, the tone curve stays neutral.
- Color +2 and CCE Strong deliver the sheet's own words, "moderately enhanced color saturation": a clear step up from neutral but not Velvia-level. Poor Things' use of the stock for elevated, sensory imagery echoes this.
- WB +1R/−1B is a small warm nudge to protect the sheet's stated "accurate flesh reproduction" against Fuji's native cool lean.
- Sharpness +1, since the sheet calls its sharpness "unsurpassed by any other 100-speed reversal film."
- Grain Weak, Small: "excellent" grain performance per the sheet, in the same fine-grain tier as the still Ektachrome E100.
- ISO ceiling 800, higher than the still E100 original's cap and lower than the negative cinema stocks. A 100-speed reversal stock is sometimes pushed a stop or two in practice, but it doesn't have Vision3's extreme speed range.
- A slight underexposure bias, which is universal reversal-film discipline. Protect the highlights, because there's no negative-style latitude to save them in.

### A stylised "Poor Things" variant
For a heavier, more overtly stylised push closer to that film's specific grade, set Grain Strong/Large, Clarity +2 and Color +3. It trades the emulsion-faithful reading for a more dramatic, grain-forward interpretation.

Validation tier: datasheet-validated (the saturation, sharpness and balance language, from the archived PDF) and characteristic-validated against a specific, well-documented recent production (*Poor Things*, 2023) rather than a generic review. That is a strong, independently checkable evidence class. No Commons frame-grabs exist for actual cinema footage, so scan-validation would need a user-supplied reference.
