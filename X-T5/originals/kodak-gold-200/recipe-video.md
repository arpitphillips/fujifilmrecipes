# Kodak Gold 200 — Fujifilm X-T5 (X-Trans V) · VIDEO / MOVIE

Movie-mode adaptation of the [stills recipe](recipe.md). Movie mode **drops Grain, Color Chrome Effect, Color Chrome FX Blue, and Clarity** (see [video-mode-settings](../../../Knowledge/video-mode-settings.md)), so this reproduces Gold's *colour and tone* foundation and compensates for the lost richness/softness controls. Target: **standard film-simulation recording** (baked-in look), not F-Log/HLG.

Set these in the movie shooting display → **IMAGE QUALITY SETTING** tab (stored separately from stills).

| Setting | Value | vs stills |
|---|---|---|
| Film Simulation | Classic Chrome | same |
| White Balance | Daylight, +3 Red & −5 Blue | same — the warmth transfers 1:1 |
| Dynamic Range | DR400 | same value, but set **manually** (no AUTO in video); needs ISO ≥ 500 |
| Tone Curve — Highlight | −2 | same |
| Tone Curve — Shadow | +0.5 | same |
| Color | **+4** | +1 vs stills, to offset the loss of Color Chrome Effect's warm-tone depth |
| Sharpness | **−3** | −1 vs stills, to substitute for the lost negative Clarity (keeps the soft, un-clinical feel) |
| High ISO NR | −4 | same |
| Interframe NR | AUTO | movie-only (use OFF for fast motion to avoid ghosting) |
| ISO | Auto, up to ISO 6400 | same |

### What was dropped and how it's handled
- **Grain (Strong/Small):** unavailable in video → add film grain in **post** if wanted (it's texture, not colour, so it doesn't compromise the SOOC colour goal).
- **Color Chrome Effect (Weak):** unavailable → partially offset with **Color +4**.
- **Color Chrome FX Blue (Off):** was already Off — no effect lost.
- **Clarity (−2):** unavailable → **Sharpness −3** (and, optionally, a physical **mist/diffusion filter** like a 1/8 Black Pro-Mist) recreates the soft consumer-film mid-tone feel.

### Notes
- Same warm-light dependency as stills — best in sunny daylight; reduce Red shift in flat light.
- If you shoot **F-Log/HLG** for grading in post instead, treat this as a *starting LUT target* rather than a bake-in recipe; the film-sim look is applied in the grade, not the camera.
