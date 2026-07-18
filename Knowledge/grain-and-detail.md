# Grain & Detail — Grain Effect, Sharpness, Clarity, High ISO NR

These settings control **texture and micro-detail** — how film-like or how crisp/clean the image feels. They don't change colour, but they hugely affect the *character* of a grade.

## Grain Effect (manual p.124)

Two independent sub-settings:

**Roughness:**
- STRONG: rougher, more visible grain.
- WEAK: smoother, subtle grain.
- OFF: no grain.

**Size:**
- LARGE: coarser grain clumps (reads as older/higher-ISO film).
- SMALL: finer grain (reads as fine-grained/lower-ISO film).

Recipes write these together, e.g. **"Strong, Large"** or **"Weak, Small"**. The pairing sets the "film stock speed" feel:
- **Weak + Small** → clean, fine-grained, modern/slide-film feel (Kodachrome, Reala Ace).
- **Strong + Small** → visible but fine grain — a fine consumer negative (Gold 200, Portra v2).
- **Strong + Large** → heavy, coarse, obviously-film grain — high-ISO or vintage stocks (Pacific Blues, CineStill 800T, Tri-X 400).

> Grain Effect is baked into the JPEG at capture and is resolution-dependent; on the 40MP X-T5 the same setting reads slightly finer than on lower-resolution bodies.

> **Why these two axes exist:** real film grain is silver-halide crystals clumping during chemical development — crystal size set the film's speed (Size), clumping intensity its roughness (Roughness), and grain structure differs between highlights and shadows. See [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md) for the chemistry, and the ACROS grain-model section of [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md) for why Fujifilm grain beats Photoshop overlays. Practical corollary: grain also compounds with sensor noise, so shooting at **higher ISO** naturally deepens the grainy look.

## Sharpness (manual p.131)

- **Range −4 to +4.** "Sharpen or soften outlines."
- **Positive** = crisper edges; **negative** = softer, gentler outlines.
- Filmic/negative recipes often run **negative** sharpness (−2) to avoid a clinical digital edge and let the grain carry the texture. Slide-film and B&W recipes may run **positive** (+1) for crisp detail.

## Clarity (manual p.132)

- **Range −5 to +5.** "Increase definition while altering tones in highlights and shadows as little as possible."
- Affects **mid-tone local contrast / micro-contrast** (the sense of "punch" and texture) without moving the overall highlight/shadow tone much.
- **Positive** = more definition, grittier, more three-dimensional (good for B&W, gritty looks — Tri-X +4, Kodachrome +3).
- **Negative** = softer, dreamier, smoother mid-tones — flatters skin and gives a gentle "glow" (Portra/Gold/Pacific/CineStill run negative Clarity).
- **Caveat (manual):** any Clarity value other than 0 adds processing time, so each shot takes noticeably longer to save. This is the practical cost of the setting. Recipes using **Clarity 0** (e.g. Reggie's Portra) partly do so for speed and versatility.

## High ISO NR (manual p.132)

- **Range −4 to +4.** Reduces noise at high sensitivities.
- **Higher** = more noise reduction but smoother/softer outlines (detail loss).
- **Lower** = leaves noise (and fine detail) visible.
- Recipe convention: almost every recipe sets **High ISO NR −4** (minimum). This preserves fine detail and lets the *intentional* Grain Effect define the texture, rather than the camera smearing it away with noise reduction. Treat "−4" as the near-universal default in these recipes.

## Long Exposure NR (manual p.132)

- **ON / OFF.** Reduces mottling/hot pixels in long exposures via a dark-frame subtraction (doubles save time). Not part of the look; set per shooting situation (usually left ON). Rarely specified in recipes.

## How texture builds a grade

- A **clean/premium** look: Weak+Small grain, positive-ish Sharpness, low/positive Clarity, NR −4.
- A **soft/dreamy portrait** look: fine grain, negative Sharpness, negative Clarity.
- A **gritty/vintage/analog** look: Strong+Large grain, negative Sharpness (let grain do the work), and either negative Clarity (soft + grainy, e.g. CineStill) or positive Clarity (gritty + punchy, e.g. Tri-X).
