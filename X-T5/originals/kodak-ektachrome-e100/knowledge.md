# Ektachrome E100 — Grade Analysis & Derivation

## The film
Kodak Professional Ektachrome E100 (2018 revival of the E100G lineage; original Ektachrome discontinued 2013). Kodak's only current colour transparency stock, Process E-6, daylight balanced. The datasheet (pub. E-4000, archived in [`_reference-sources/datasheets/`](../../_reference-sources/datasheets/README.md)) specifies:

- Diffuse RMS granularity 8: "extremely fine"
- Low contrast tone scale with "extended tonal range"
- Neutral color balance with "moderately enhanced color saturation"
- Low D-min → "whiter, brighter whites"
- "Pleasing, natural skin tone"
- Characteristic curves (Status A): R/G/B tightly bundled across the range, minimal channel crossover, i.e. genuinely neutral rendering; D-max ≈ 3.2–3.8; gentle shoulder
- MTF: ~100% response holds past 20 cycles/mm, high sharpness
- Push +1 (EI 200): slight contrast increase, sharper highlights

Cultural register: the *National Geographic* slide of the 1990s–2000s, clean, honest, slightly cool documentary colour ([color-science: Classic Chrome cousin territory](../../../Knowledge/color-science-why-film-cannot-be-faked.md), but E100 keeps more saturation and neutrality than Kodachrome-era looks).

## Trait → setting derivation

| Datasheet trait | Recipe setting | Reasoning |
|---|---|---|
| Balanced slide film, vivid-but-faithful | **Provia base** | Fuji's own balanced-slide profile; the correct structural starting point ([film-simulations](../../../Knowledge/film-simulations.md)) |
| RMS 8, extremely fine | Grain **Weak, Small** | Matches the RMS ladder (Acros RMS 7 = Weak/Small; K64 RMS 10 = Weak/Small) |
| Neutral, tightly-bundled RGB curves | WB **Daylight −1R/+1B** | Neutral-to-cool signature; cancels Fuji's native warm bias |
| Low-contrast tone scale, gentle shoulder | **Highlight −1** | Softens Provia's highlight contrast toward E100's gentler rolloff |
| High D-max (slides stay dense in shadow) | **Shadow −0.5** (not −1) | Slightly gentler shadows without losing slide depth |
| "Moderately enhanced" saturation, neutral | **Color +1**, CCE **Weak** | Above neutral, below Fuji-slide punch |
| Clean-but-real skies | CCFXB **Weak** | Deep blues without the Fuji magenta-lean |
| High MTF sharpness | **Sharpness +1** | Crisp transparency acuity |
| No grit/glow traits in sheet | **Clarity 0** | Quality standard holds |
| Daylight/flash design, low D-min whites | EC **0…+1/3** | Slide exposure discipline; protect highlights |

## What would make it unfaithful
- Strong grain (it's an RMS-8 film, grain is invisible at normal viewing)
- Warm WB shifts (E100's identity is its neutrality against warm Fuji slides)
- High contrast tone curve (the sheet explicitly says low-contrast tone scale, the common mistake, since most slide emulations assume punch)

## Validation status
- Datasheet tier: ✅ (E-4000 archived PDF; curves + RMS + MTF read directly, 2026-07-15)
- Characteristic tier: partial: community consensus (neutral, fine-grained, clean whites, cooler than Fujichrome) is well established but ≥3 sources not yet formally logged
- Scan tier: pending: needs ≥5 real E100 scans across light/subjects per [validation methodology](../../../Knowledge/validation-methodology.md); drop scans in [`references/`](references/)

*Derived 2026-07-15 from the archived datasheet. See also [VALIDATION-AUDIT.md](../../VALIDATION-AUDIT.md).*
