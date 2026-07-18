# Kodak Double-X 5222 — Grade Analysis & Derivation

> Original (datasheet + characteristic validated). See [`recipe.md`](recipe.md), the [cinema README](../README.md), and the [Knowledge base](../../../../Knowledge/README.md).

## The stock
Eastman Double-X Negative Film 5222/7222, in continuous production since 1959, making it one of the longest-lived film stocks in history. Kodak's datasheet (archived: [`kodak-motion/double-x_5222.pdf`](../../../_reference-sources/datasheets/README.md), pub. H-1-5222) describes a "high-speed, panchromatic material" with "good image-structure characteristics and excellent sharpness," suited to both studio and location work, including dim-light photography without added illumination.

## Why it's on the "most notable and pleasing" list
This isn't a guess, researched directly. Double-X's filmography is one of the strongest credibility signals of any stock in this bank: Raging Bull, Schindler's List, Manhattan, and it remains the reference point critics reach for whenever describing "the moody intensity of Old Hollywood and film noir." It is *the* stock people mean when they say a modern film "looks like classic black-and-white cinema."

## Datasheet specifics used in the derivation
- Diffuse RMS granularity: 14: moderately heavy; heavier than any fine-grain still stock in this bank, in the same territory as the bank's dedicated push stocks (Delta 3200, T-Max P3200), though Double-X isn't itself a push stock. This is its *native* grain.
- Control gamma 0.65–0.70 (developed to this contrast target, measured via Status M blue densitometry), a moderate, versatile contrast, not an extreme one.
- Resolving power 32 lines/mm (1.6:1) to 100 lines/mm (1000:1): lower than still-photo B&W stocks, appropriate for cinema (motion, projection, and telecine don't demand still-print-level per-frame resolution).
- EI 250 daylight / 200 tungsten: a genuinely fast negative, usable in dim conditions.

## The grade in one line
Classic cinema black & white, moderate contrast with rich, deep blacks, moderately heavy grain, built for both studio control and available-light location work.

## How the settings embody it
Acros carries real tonal richness under the grain. Grain Strong/Large matches the RMS-14 reality, heavier than fine-grain still stocks. DR200 + Highlight 0 + Shadow +2 model the moderate-gamma, rich-shadow curve. Clarity +1 (a small, deliberate deviation from the 0 default) adds the tactile grit associated with its on-screen reputation, more restrained than Tri-X's +3 since Double-X's contrast target is genuinely gentler than Tri-X pushed.

## A stylistic variant: period-drama warmth
The datasheet gives no colour cast (B&W has none), but films styled after 1940s–60s cinematography sometimes want a subtle warm *toning* rather than neutral grey. Try Monochromatic Color WC +2/MG 0 for a gentle sepia-adjacent period lean, keeping everything else the same.

## vs the bank's still-photography B&W family
Double-X lives in `cinema/`, not `black-and-white/`, deliberately, it's a different creature from Acros/HP5/Tri-X/Delta/Pan F even though all are monochrome. Those are still-photography stocks with still-photography grain/resolution targets; Double-X is built for projection, telecine, and motion, and its RMS-14 grain plus moderate gamma give it a specific "classic cinema," not "photojournalism," character.

## Validation status
Datasheet-validated (RMS, gamma, resolving power, speed, archived PDF) + characteristic-validated against specific named productions (a stronger evidence class than generic reviews, since it's independently verifiable). No Commons frame-grabs exist (real film footage isn't Commons material), scan-validation would need a user-supplied reference frame, e.g. a still from one of the cited films or your own Double-X test roll.
