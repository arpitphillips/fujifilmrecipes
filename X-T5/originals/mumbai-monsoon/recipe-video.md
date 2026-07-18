# Mumbai Monsoon — Fujifilm X-T5 (X-Trans V) · VIDEO / MOVIE

Movie-mode version of the [stills recipe](recipe.md). Movie mode drops Grain, Color Chrome Effect, Color Chrome FX Blue and Clarity (see [video-mode-settings](../../../Knowledge/video-mode-settings.md)), so the teal-warm colour split is preserved through the WB shift and Classic Negative, and the lost richness is partly compensated. The target is standard film-simulation recording with the look baked in, not F-Log/HLG.

Set in the movie shooting display → IMAGE QUALITY SETTING tab.

| Setting | Value | vs stills |
|---|---|---|
| Film Simulation | Classic Negative | same |
| White Balance | 6500K, +2 Red & −2 Blue | same — the teal/warm split transfers |
| Dynamic Range | DR400 | same value, set **manually** (no AUTO in video); ISO ≥ 500 |
| Tone Curve — Highlight | −2 | same |
| Tone Curve — Shadow | +1 | same |
| Color | **+2** | +1 vs stills, to offset the lost Color Chrome Effect / FX Blue richness |
| Sharpness | −1 | same (already soft; don't over-soften moving footage) |
| High ISO NR | −4 | same |
| Interframe NR | AUTO | movie-only; use OFF if fast motion ghosts |
| ISO | Auto, up to ISO 12800 | same — dark monsoon light |

### What was dropped and how it's handled
- Color Chrome FX Blue (Weak) doesn't exist in video, so the cool teal depth in wet surfaces is slightly reduced. Color +2 and the WB base recover most of it; for more teal, nudge WB to 6300K.
- Color Chrome Effect (Strong) doesn't exist either, and Color +2 restores the accent richness.
- Clarity doesn't exist in video. The stills recipe keeps it at 0 anyway; keep Sharpness −1, and a physical mist or diffusion filter adds the humid atmosphere convincingly on video.
- Grain (Strong/Large) is missing too. Add grain in post for the filmic monsoon texture.

### Notes
- Handheld in low light: rely on IBIS, keep the shutter near 1/50 (25/30p) or 1/100 (50/60p), and let Auto-ISO climb.
- For rain-at-night with neon practicals, switch to the [CineStill 800T](../../reference-recipes/cinestill-800t/recipe.md) approach.
