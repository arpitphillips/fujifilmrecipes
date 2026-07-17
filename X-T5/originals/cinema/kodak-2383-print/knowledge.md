# Kodak 2383 Print — Grade Analysis

> Original (research-backed). See [`recipe.md`](recipe.md), the [cinema README](../README.md), and the [Knowledge base](../../../../Knowledge/README.md).

## What it emulates
**Kodak Vision 2383** is the colour **release-print** film most cinema prints are struck on. The camera negative (e.g. Vision3) is low-contrast; when printed to 2383 for projection, contrast and saturation increase and the image takes on 2383's characteristic curve — **deep, cool-leaning shadows and warm, luminous highlights/skin**. This "print" rendering, amplified by modern digital grading, is the ubiquitous **teal-and-orange cinematic look**.

## The grade in one line
A **contrasty, saturated, teal-shadow / warm-skin theatrical print** look — the classic Hollywood colour grade.

## Why Classic Negative (not Eterna) here
Unlike the Vision3 *negative* recipes (Eterna — low contrast, neutral shadows), the 2383 *print* look needs **teal shadows + added contrast + saturation**. **Classic Negative** natively provides teal-leaning shadows and hard tonality, so it reproduces the print characteristic far better than Eterna. The warm WB shift supplies the "orange" side; Classic Neg supplies the "teal."

## How it's built
Classic Negative for teal shadows + print contrast. DR200 + Shadow +2 deepen and enrich (print contrast). Warm WB (+2R/−2B) pushes skin/highlights warm for the teal-orange split. Color +2 + CCE Strong give rich, controlled print saturation. Clean fine grain + Clarity 0 keep the projected-print smoothness.

## Datasheet confirmation (Kodak 2383/3383 data sheet, fetched & extracted)
The official sheet confirms 2383 is a **high-contrast projection print stock**: a steep tone scale calibrated to **Laboratory Aim Densities (LAD)**, deep D-max via intragrain absorbing dyes and superior halation protection, and RGB sensitometric curves that steepen the (deliberately flat) camera negative into the final projected contrast. That is exactly the transformation this recipe models — Classic Negative's hard tonality + DR200 + Shadow +2 standing in for the print stock's steep curve and dense blacks over the negative's soft capture.

## vs the other cinema recipes
- **[Vision3 250D](../kodak-vision3-250d/knowledge.md) / [500T](../kodak-vision3-500t/knowledge.md):** the *negatives* — low contrast, clean, gradeable. This is the *print* — the finished, contrasty, teal-orange look.
- Related in mood to [Mumbai Monsoon](../../mumbai-monsoon/knowledge.md), which also uses a Classic-Neg teal/warm split (for rain rather than Hollywood).
