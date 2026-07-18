# Fujicolor Pro 400H — Grade Analysis & Derivation

> Original (datasheet + video-comparison validated). See [`recipe.md`](recipe.md) and the [Knowledge base](../../../Knowledge/README.md).

## The film
Fujifilm's flagship professional colour negative (discontinued 2021 in 35mm, 2022 in 120) — for over a decade the default choice for wedding and portrait photographers wanting a cool, soft, "airy" look. The datasheet (archived: [`_reference-sources/datasheets/fujifilm/fujicolor-pro-400h.pdf`](../../_reference-sources/datasheets/README.md)) specifies:

- Diffuse RMS granularity value: 4: the finest grain of any film in this bank (finer than Acros' RMS 7, finer than Portra's PGI 37, finer than Ektar's PGI <25).
- **"Superb skin tones with smoothly continuous gradation from highlights to shadows."**
- "Excellent three-dimensional appearance": clearer highlight colours, **"appropriately controlled color saturation in the shadows"** — i.e. shadows are deliberately less saturated than highlights, which is what reads as the film's signature cool/blue-green shadow cast.
- **Faithful reproduction of neutral grays** with sharply improved fidelity across a wide exposure range, under to over.

## Corroborating evidence: a direct film-vs-simulation study
Unlike most recipes in this bank, Pro 400H has an existing **[side-by-side video comparison](../../../Knowledge/pro400h-vs-proneghi-analog-comparison.md)** of real Pro 400H scans against the PRO Neg. Hi in-camera simulation on an X-Pro3. Its findings, used directly in this derivation:
- PRO Neg. Hi is the closest built-in match (contrast level, cool-neutral skin direction, highlight rolloff shape) but runs **warmer and more saturated in greens/shadows** than the real film.
- The real film's cyan-green shadow cast comes from its emulsion layer balance — something the simulation's LUT doesn't reproduce on its own, so it has to be added back via **Color Chrome FX Blue** and a cool WB shift.
- Pro Neg. Hi was modelled on Fuji's NPS/NS 160 studio portrait film, not on Pro 400H directly — explaining the gap.

## The grade in one line
Cool, soft, extraordinarily fine-grained pro-portrait negative — clean highlights, gently blue-green shadows, never punchy, "airy" wedding-photography colour.

## How the settings embody it
PRO Neg. Hi supplies the reduced-contrast, cool-neutral skin foundation. **CCFXB Weak** (rather than Off) is the key correction the video comparison identified — it restores the shadow cyan-green depth the base sim lacks. The cool WB shift (−1R/+2B) pushes the whole image toward the real film's blue-green lean. DR400 + Highlight −2 model the exceptionally long highlight shoulder. Shadow −1 keeps blacks lifted and soft. Color 0 + CCE Off keep saturation "appropriately controlled," never vivid. RMS-4 grain means Weak/Small — the finest grain setting used anywhere in this bank.

## vs the rest of the bank
- **[Kodak Portra 400](../kodak-portra-400/knowledge.md):** both are "invisible grain, wide latitude, skin-first" pro negatives, but Portra 400 is **warm** (Classic Chrome, +2R/−4B) where Pro 400H is **cool** (PRO Neg. Hi, −1R/+2B) — a useful warm/cool pairing for portrait work, the same relationship as Gold↔Superia for consumer negatives.
- **[Ektar 100](../kodak-ektar-100/knowledge.md):** Ektar is vivid/punchy/landscape-first; Pro 400H is muted/soft/portrait-first — opposite poles of Kodak-vs-Fuji pro colour negative philosophy (though Pro 400H is a Fuji stock, its market position mirrors Kodak's Portra rather than Ektar).

## Validation status
**Datasheet-validated** (RMS 4, shadow-saturation control, wide latitude — archived PDF) + **validated against a direct film-vs-simulation video study** (stronger evidence than characteristic-only reviews, since it isolates exactly where the base sim needs correcting). Scan-validation (independent real scans beyond the video) pending — drop into [`references/`](references/).
