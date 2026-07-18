# Dynamic Range & Tone Curve — the contrast controls

These settings shape the **contrast curve**: how highlights and shadows are rendered, and how much tonal range is preserved. Together with the film-sim base they define whether a grade is punchy or flat, and where detail is protected.

## Dynamic Range: DR100 / DR200 / DR400 (manual p.130)

Dynamic Range protects **highlights** from clipping by underexposing the sensor and lifting the mid/shadow tones back up in processing.

| Setting | Effect | ISO floor required |
|---|---|---|
| **DR100 (100%)** | Baseline. Most contrast, highlights clip earliest. | Any ISO |
| **DR200 (200%)** | ~1 stop more highlight headroom, slightly softer contrast. | ISO 250+ |
| **DR400 (400%)** | ~2 stops more highlight headroom, softest of the three, flattest highlights. | ISO 500+ |

Key points from the manual:
- **AUTO** picks DR100 or DR200 automatically per scene.
- Higher DR = more highlight retention but **"mottling may appear at higher values"** (noise in recovered areas) — choose to suit the scene.
- Because DR200/DR400 force a minimum ISO, a recipe that specifies **DR400** effectively sets an **ISO floor of 500**. This is why many recipes pair DR400 with "Auto ISO up to 6400" — the camera can't drop below 500 anyway.

### How DR reads as a grade
- **DR400** → gentler highlight roll-off, more "negative-film"-like latitude, flatter and more forgiving. Common in Portra/Gold/Classic-Neg recipes for that soft-highlight print look.
- **DR200** → a middle ground; a mild highlight lift with still-present contrast. Common in slide-film emulations (Kodachrome).
- **DR100** → maximum native contrast; used when the look wants punch and the light is controlled.

## D Range Priority (manual p.130)

A separate, more aggressive tone-flattening mode (AUTO / STRONG / WEAK / OFF) that reduces loss of detail in **both** highlights and shadows for very high-contrast scenes.

- When D Range Priority is **anything other than OFF**, it *takes over* **Tone Curve** and **Dynamic Range** and adjusts them automatically — you lose manual control of contrast.
- Therefore recipes that grade contrast by hand keep **D Range Priority OFF** (it isn't listed in the recipes precisely because it must stay off for Tone Curve/DR to be honoured).

## Tone Curve: Highlight & Shadow (manual p.131)

The Tone Curve independently bends the two ends of the contrast curve. Both run **−2 to +4**:

- **Higher value = harsher** (more contrast at that end).
- **Lower value = softer** (less contrast, more retained detail / a "lifted" look).

Recipes list these as **Highlight** and **Shadow** (a.k.a. "H Tone" / "S Tone").

| Reading | Result |
|---|---|
| **Highlight −2 / −1** | Soft, protected highlights — gentle, filmic, no harsh whites |
| **Highlight +1…+4** | Bright, snappy, contrasty highlights |
| **Shadow −2 / −1** | Lifted, open shadows — faded / low-contrast blacks (matte look) |
| **Shadow +2…+3** | Deep, rich, inky shadows — punchy or moody |

### Highlight/Shadow shape the "grade signature"
- A **faded** look = negative Highlight *and* negative Shadow (both ends soft). 
- A **moody/rich** look = negative Highlight (soft highlights) but positive Shadow (deep blacks) — e.g. Pacific Blues (H −2 / S +3), CineStill 800T (H 0 / S +2).
- A **bright, clean** look = higher Highlight with modest Shadow.

> Note the interaction: **DR400 already softens highlights**, so a recipe pairing DR400 with a low/negative Highlight value pushes hard toward a soft, print-like highlight roll-off; pairing DR400 with a positive Shadow deepens blacks while keeping highlight latitude — a classic "moody but not muddy" combination.
