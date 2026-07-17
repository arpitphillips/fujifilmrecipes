# Video / Movie Mode — settings, differences, and photo→video translation

Film-look recipes for **movie recording** are not the same as stills recipes, because the X-T5 exposes a **reduced set of image-quality controls** in movie mode. This file documents exactly what's available (from the X-T5 manual, *Image Quality Setting (Movie Recording)*, printed pp.201–204) and how to translate a photo grade into a faithful video grade.

## Accessing movie image-quality settings
Press **MENU/OK** in the movie shooting display and select the **H (IMAGE QUALITY SETTING)** tab. These are stored **separately** from the still-photo settings — even for controls that exist in both modes, "settings must be adjusted separately" (manual). Changing Film Simulation for stills does **not** change it for movies, and vice versa.

## What IS available in movie mode
| Control | Notes vs stills |
|---|---|
| **Film Simulation** | Same options as stills (Provia → Acros), set separately. The base look carries over fully. |
| **Monochromatic Color** | Same (warm/cool + G/M) for Acros/Monochrome, set separately. |
| **White Balance** (+ WB Shift) | Same options and the same R/B shift grid, set separately. **The colour cast translates 1:1** — this is your main grading tool in video. |
| **Dynamic Range** | DR100/200/400 — but **AUTO is not available** in movie. DR200 needs ISO ≥250, DR400 needs ISO ≥500 (same floors as stills). **DR200/400 are only selectable when `MOVIE SETTING > F-Log/HLG RECORDING` is set appropriately** — see below. |
| **Tone Curve** (Highlight/Shadow) | Same −2…+4 range, set separately. Contrast shaping carries over. |
| **Color** | Same −4…+4 saturation, set separately. |
| **Sharpness** | Same −4…+4, set separately. |
| **High ISO NR** | Same −4…+4, set separately. |
| **Interframe NR** *(movie only)* | AUTO/OFF temporal noise reduction. Can cause ghosting on motion. |
| **Peripheral Light Correction** *(movie only)* | ON/OFF vignetting correction. |

## What is NOT available in movie mode (critical)
These stills controls are **absent** from the movie Image Quality menu, so their character **cannot be baked into video**:

- **Grain Effect** (roughness/size) — no in-camera film grain in video.
- **Color Chrome Effect** — no extra depth in reds/yellows/greens.
- **Color Chrome FX Blue** — no extra blue depth. *(This also means the X-Trans IV→V blue conversion rule is irrelevant to video.)*
- **Clarity** — no mid-tone micro-contrast control.
- **Smooth Skin Effect** — unavailable.

Consequence: **a stills recipe can never be reproduced 1:1 in video.** The colour and tonal *foundation* transfers (Film Sim + WB + DR + Tone Curve + Color + Sharpness), but the *texture and colour-richness layer* (grain, chrome effects, clarity) is lost.

## Translating a photo recipe → video recipe
When adapting one of our stills recipes to movie mode:

1. **Copy directly:** Film Simulation, White Balance + WB Shift, Dynamic Range, Tone Curve (Highlight/Shadow), Color, Sharpness, High ISO NR. These behave the same.
2. **Drop (unavailable):** Grain, Color Chrome Effect, Color Chrome FX Blue, Clarity.
3. **Compensate for the dropped controls:**
   - Lost **Color Chrome Effect / FX Blue** removed some richness/depth → consider a small **Color** bump (e.g. +1) to partly restore saturation weight, judged by eye.
   - Lost **negative Clarity** (which softened mids for a dreamy look) → you may nudge **Sharpness** down slightly to keep a soft feel; there's no true clarity substitute in-camera.
   - Lost **grain** → grain, if wanted, must be added in **post** (it's a texture, not a colour, so it doesn't compromise the SOOC colour goal).
4. **Set Dynamic Range deliberately:** since AUTO isn't available, pick DR100/200/400 to match the stills recipe's value (and remember the F-Log/HLG dependency and ISO floors).
5. **Verify separately:** because movie settings are independent, re-enter every value in the movie IQ menu; don't assume the stills preset applies.

## F-Log / HLG vs SOOC film-look (important distinction)
The `MOVIE SETTING > F-Log/HLG RECORDING` option changes the intent entirely:
- **F-Log / F-Log2 / HLG** = flat/log capture meant to be **colour-graded in post**. Film Simulation looks are *not* baked in the same way; DR options and film-sim behaviour change. Use this when the deliverable is edited/graded footage.
- **Standard (film-simulation) recording** = the **SOOC film-look** path, directly analogous to our stills recipes — the Film Simulation and IQ settings are baked into the footage. **This is the mode our video recipes target.**

> When building video recipes we will target **standard film-simulation recording** (baked-in look) unless a recipe is explicitly a log/grade-in-post workflow.

## Where video recipes will live
Video recipes will be organised parallel to stills, e.g. `X-T5/<recipe>/recipe-video.md` (or a dedicated `video/` area) with their own `knowledge.md` grade notes, cross-referencing the stills version and noting exactly what was dropped/compensated. Structure to be confirmed when we build the first one.
