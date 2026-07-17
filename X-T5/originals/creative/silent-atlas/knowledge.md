# Silent Atlas — Grade Analysis & Knowledge

## Target aesthetic
A **cinematic documentary teal-and-warm** travel-film grade, derived from studying Merlin Krumme's *The Silent Atlas* (2026) — a short film shot in the Atlas Mountains of Morocco. The look is characterised by:
- **Warm amber/terracotta midtones and highlights** (earth, walls, skin)
- **Cool teal shadows** (building shade, overcast sky, mist)
- **Deep, rich blacks** with retained shadow detail
- **Soft, non-clipping highlights** (misty/cloudy mountain scenes)
- **Muted overall saturation** — filmic, not digital-vivid
- **Slightly soft/halated rendering** (physical Glimmerglass filter in the reference)

This is the "teal-and-orange" cinematic split expressed through Moroccan earth tones rather than Hollywood neon.

## Why Classic Negative (not Eterna or Classic Chrome)

| Candidate | Pros | Cons | Verdict |
|---|---|---|---|
| **Classic Negative** | Native teal-cyan shadow cast; hard tonality adds contrast depth to flat/overcast light; colour separation shifts hues toward exactly the amber-teal axis we need | Can be crunchy; strong character | ✅ **Selected** — the teal shadow character is the core of this grade |
| Classic Chrome | More muted and editorial; great for Kodak emulations | Shadow contrast is grey-blue, not teal-cyan; would need more WB pushing | ❌ Close second, but missing the teal shadow key |
| Eterna | Low-contrast cine base; designed for cinema | Too flat and desaturated for this level of contrast; needs heavy contrast boosting | ❌ Too much departure needed |

## White Balance strategy: +3R / −2B *(corrected from −3B — see verification below)*

The reference film has a clear warm lean on sunlit surfaces and skin, against cool teal backgrounds. Classic Negative already has a cool shadow tone; the warm WB shift (+3R from Daylight) pushes:
- Skin → golden/peach warmth
- Earth/terracotta walls → rich amber

While Classic Neg's shadow character stays teal, creating the colour split.

The blue shift is deliberately **gentler than the red push** (−2B, not −3B): the second frame-verification pass showed the reference's skies and mist land consistently **teal-cyan** — a −3B shift would strip too much blue and push the atmosphere toward khaki/yellow-grey, whereas −2B leaves enough blue for Classic Negative's native cyan lean to do the teal work.

## Frame verification — second independent pass (2026-07-16)

The original derivation (2026-07-15, other machine) studied frames at ~60s/105s/150s/195s via browser capture. A second, independent pass re-fetched **4 actual video frames** (YouTube's auto-generated stills: ~25% mist landscape, ~50% portrait, ~75% clear-sky, plus the full-res hero frame) and checked every design decision:

| Observation across all 4 frames | Recipe element | Verdict |
|---|---|---|
| Skin consistently warm golden-peach; earth/coats warm amber-tan | +3 Red WB | ✅ confirmed |
| Skies/mist/atmosphere consistently **teal-cyan**, never warm or royal-blue | Blue WB shift | ⚠️ **corrected −3B → −2B** (−3B would yellow the atmosphere) |
| Deep, held shadows (silhouettes keep shape; jackets near-black) | Shadow +2, DR200 | ✅ confirmed |
| Soft, non-clipping highlights with visible bloom at bright edges | Highlight −1 + Glimmerglass note + Sharpness −1 | ✅ confirmed |
| Muted overall saturation (teal-warm split carries the colour interest) | Color +3 video / +2 stills | ✅ within range; drop stills to +1 if results read richer than the reference |
| **Fine grain texture visible in the mist** (hero frame) | Stills Grain Weak/Large | ✅ confirmed — grain is genuinely part of the reference look |

One caveat kept in mind during this pass: YouTube's auto-frames are heavily compressed, which mutes absolute saturation — so hue relationships (teal vs warm) were treated as reliable evidence, absolute saturation only loosely.

## DR200 + Highlight −1 + Shadow +2

- **DR200** (not 400): the reference has real contrast — deep blacks, present shadows. DR400 would flatten this too much. DR200 gives 1 stop of highlight headroom for the misty/cloudy skies without sacrificing the punchy shadow character.
- **Highlight −1**: gentle roll-off — the reference preserves cloud/sky detail without flat-looking highlights.
- **Shadow +2**: deepens blacks, giving the moody cinematic depth. Classic Neg's teal cast intensifies in deep shadows, which is the desired effect.

## Color +3 (compensating for absent CCE/CCFXB)

In stills, Color Chrome Effect and FX Blue add richness and depth to reds/blues. In video, these are unavailable. Color +3 (up from the usual +2 in cinema recipes) compensates, bringing the warm earth tones to life and ensuring the amber/terracotta isn't too muted.

## Sharpness −1 and the Glimmerglass question

The reference film uses a **Tiffen Glimmerglass** diffusion filter — a physical optical element that creates halation (highlight bloom/glow) and reduces micro-contrast. This can't be replicated in-camera. Sharpness −1 is the closest in-camera approximation: slightly soft, filmic edges without going blurry. The real Glimmerglass look requires the physical filter.

## Video-first design, stills companion added

The recipe was designed from scratch for movie mode (the reference is a film), with settings chosen knowing that Grain, CCE, CCFXB, and Clarity are unavailable there. A **[stills companion](recipe.md)** was added 2026-07-16: same WB split, tone curve, and softness, but with Color pulled back to +2 (Color Chrome Effect Strong now carries the warm-tone depth), CCFXB Weak adding teal shadow depth, and Weak/Large grain for a subtle cine texture — i.e. the stills build uses the richer toolset to express the same grade, rather than the video build's saturation-compensation approach.

## Relationship to the 2383 Print recipe

This is conceptually a sibling of the [Kodak 2383 Print](../../cinema/kodak-2383-print/knowledge.md) recipe — same Classic Negative base, same teal-orange concept. The differences:

| | 2383 Print (video) | Silent Atlas |
|---|---|---|
| WB Red | +2 | **+3** (warmer amber) |
| WB Blue | −2 | −2 (same — corrected from −3 after frame verification; both looks need blue preserved for teal skies) |
| Highlight | 0 | **−1** (softer roll-off for misty conditions) |
| Sharpness | 0 | **−1** (filmic softness for Glimmerglass feel) |
| Color | +3 | +3 (same) |
| DR | DR200 | DR200 (same) |
| Intent | Theatrical print projection | Documentary travel-film |

## Source
- Merlin Krumme, *The Silent Atlas*, YouTube, Mar 2026.
- Shot on Sony FX30 with Sigma 18-35 f/1.8 + Sony 11mm f/1.8, Tiffen Glimmerglass filter.
- Post-graded with custom LUTs (available at tinted.sellfy.store).
- Location: Atlas Mountains, Morocco (Imlil, mountain villages).

*Last updated: 2026-07-16. Originally derived 2026-07-15 in a session on the second machine (frame-by-frame study of the reference video at ~60s/105s/150s/195s); ported into this repo copy 2026-07-16, when the stills companion was added.*
