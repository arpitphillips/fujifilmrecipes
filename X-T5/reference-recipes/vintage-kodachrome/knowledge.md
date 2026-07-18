# Vintage Kodachrome, Translation Notes (X-Trans III → X-T5)

> This file documents the methodology for porting an older-generation recipe to the X-T5, using concrete evidence. It's the template we apply to any III/IV recipe. See [`recipe.md`](recipe.md) and [x-trans-v-and-conversion](../../../Knowledge/x-trans-v-and-conversion.md).

## The look
First-era (1935–1960) Kodachrome: a painterly slide look with cyan-shifted blues, darkened reds, and bronze/orange skin, achieved on Classic Chrome with high highlight contrast (+4), pulled shadows (−2), boosted Color (+4), and deliberate underexposure (−1/3 to −1) for density and richness.

## What changes between X-Trans III (X100F) and X-Trans V (X-T5)
The X100F (III) lacks four controls the X-T5 has. Porting = deciding what to do about each missing control, backed by evidence rather than guesswork:

| Control | On X-Trans III | Decision for X-T5 | Evidence / reasoning |
|---|---|---|---|
| **Grain Size** | absent (only Strong/Weak/Off) | add **Large** | The look is old/coarse-grained; Large is the faithful choice. Small would read too modern. |
| **Color Chrome Effect** | absent (X100F predates it) | **Off** | The original never had CCE, so Off reproduces the source rendering. Weak is a valid enhancement, but changes the look. |
| **Color Chrome FX Blue** | absent | **Off** (floor) | Can't go lower. **Caveat:** X-Trans V renders Classic Chrome blues *deeper* than III did, so V blues come out a bit more saturated than the 2017 original — an unavoidable, documented delta. |
| **Clarity** | absent | **0** | Neutral preserves the original mid-tone contrast. |

Everything else (Film Sim, DR, Tone Curve, Color, Sharpness, WB + shift, ISO, Exp) maps 1:1 because those controls and their scales are unchanged across generations.

## The two hard-evidence deltas you can't fully eliminate
1. Deeper blues on V. Documented X-Trans V behaviour on Classic Chrome/Neg/Eterna. With CCFXB already at Off, there's no headroom to compensate in-camera. Accept it, or pull blue saturation via a −Color-adjacent workaround (there isn't a per-hue control in-camera, so: accept it).
2. Newer AWB on V. The original used Auto WB; V's AI AWB may pick a slightly different balance. Fix by substituting a fixed Kelvin (~5500K) with the same +2R/−4B shift to lock the cast.

## Why this recipe is the porting template
It exercises all four of the missing-control decisions at once (Grain Size, CCE, CCFXB, Clarity) plus both hard deltas (blue rendering, AWB). Any III→V port is a subset of these decisions; any IV→V port is usually just the single CCFXB one-notch drop. Apply this table and you can translate any older recipe with defensible reasoning.
