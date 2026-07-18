# Kodak Gold 200 — Fujifilm X-T5 (X-Trans V) · VIDEO / MOVIE

Movie-mode adaptation of the [stills recipe](recipe.md). Movie mode drops Grain, Color Chrome Effect, Color Chrome FX Blue, and Clarity (see [video-mode-settings](../../../Knowledge/video-mode-settings.md)), so this version reproduces Gold's colour and tone foundation and compensates for the missing richness and softness controls. The target is standard film-simulation recording with the look baked in, not F-Log/HLG.

Set these in the movie shooting display → IMAGE QUALITY SETTING tab (stored separately from stills).

| Setting | Value | vs stills |
|---|---|---|
| Film Simulation | Classic Chrome | same |
| White Balance | Daylight, +3 Red & −5 Blue | same — the warmth transfers 1:1 |
| Dynamic Range | DR400 | same value, but set **manually** (no AUTO in video); needs ISO ≥ 500 |
| Tone Curve — Highlight | −2 | same |
| Tone Curve — Shadow | +0.5 | same |
| Color | **+4** | +1 vs stills, to offset the loss of Color Chrome Effect's warm-tone depth |
| Sharpness | **−3** | −1 vs stills, extra softness to stand in for the grain and film texture video can't render |
| High ISO NR | −4 | same |
| Interframe NR | AUTO | movie-only (use OFF for fast motion to avoid ghosting) |
| ISO | Auto, up to ISO 6400 | same |

### What was dropped and how it's handled
- Grain (Strong/Small) doesn't exist in video. Add film grain in post if you want it; grain is texture rather than colour, so skipping it doesn't compromise the straight-out-of-camera colour goal.
- Color Chrome Effect (Weak) doesn't exist in video, so Color +4 partially covers the lost warm-tone depth.
- Color Chrome FX Blue was already Off in the stills recipe, so nothing is lost.
- Clarity doesn't exist in video either. The stills recipe keeps Clarity at 0 anyway (softness comes from the base and Sharpness), and here Sharpness −3 keeps the video image similarly soft. A physical mist or diffusion filter, like a 1/8 Black Pro-Mist, pushes the consumer-film feel further if you want it.

### Notes
- Same warm-light dependency as stills: best in sunny daylight, and worth reducing the Red shift in flat light.
- If you shoot F-Log/HLG for grading in post instead, treat this as a starting LUT target rather than a bake-in recipe. The film-sim look then gets applied in the grade, not the camera.
