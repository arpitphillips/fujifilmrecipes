# Analog vs. Digital: Pro 400H Film Stock vs. Pro Neg Hi Simulation

*Source: [Fuji Pro 400H compared to Pro Neg Hi simulation (X-Pro3), Pushing Film](https://www.youtube.com/watch?v=0uT2k0e3OGg)*

---

## Overview

This document captures key findings from a side-by-side comparison of actual Fujifilm Pro 400H 35mm film scans against the PRO Neg. Hi in-camera simulation shot on the X-Pro3. The comparison is practically useful for anyone building recipes intended to approximate the Pro 400H film look.

---

## What Pro 400H Actually Looks Like (Film Characteristics)

Fujifilm Pro 400H was Fujifilm's flagship professional colour negative film (discontinued 2021, 35mm; discontinued 2022, 120 format). Its characteristics:

- Box speed: ISO 400, but frequently rated at 200–320 by film photographers for smoother gradation
- Highlight retention: Exceptional, one of the longest shoulder curves in professional colour negative film; holds highlight detail far beyond what slide films or digital sensors show
- Shadow behaviour: Natural lift, blacks are never crushed; shadows retain a slight blue-green cast that is characteristic of the film's colour balance
- Colour palette: Cool, slightly desaturated with a distinctive cyan-blue lean in shadows and greens; skin tones are neutral to slightly cool
- Grain: Fine for ISO 400, visible in shadow areas but smooth across midtones
- Contrast: Lower-than-average contrast curve for the ISO class

---

## How PRO Neg. Hi Compares (Simulation Strengths and Gaps)

PRO Neg. Hi is the closest built-in simulation to Pro 400H's general aesthetic register, but it is not a direct replica.

### Where It Matches Well
- Overall contrast level: both have reduced contrast vs. PROVIA or Classic Chrome
- Skin tone direction: neutral to slightly cool, not warm-rosy like ASTIA or consumer profiles
- Highlight handling: Pro Neg. Hi's softer highlight rolloff mirrors Pro 400H's long shoulder

### Key Differences
| Characteristic | Pro 400H (Film) | PRO Neg. Hi (Simulation) |
|---|---|---|
| Shadow colour cast | Noticeably blue-green | Neutral/slightly cool |
| Green rendering | Cool, slightly desaturated | Slightly warmer and more saturated |
| Overall coolness | More pronounced | More neutral |
| Grain character | Fine silver grain, shadow-concentrated | Fujifilm grain simulation (less shadow-concentrated) |
| Highlight protection | Very long shoulder curve | Good, but slightly shorter |

### Recipe Implications for Approximating Pro 400H

To push PRO Neg. Hi closer to Pro 400H on an X-T5:

- Color Chrome Effect: Off or Weak, Pro 400H doesn't have strong inter-hue differentiation
- White Balance: Slightly cool (toward blue), approximately 5200K or custom
- White Balance Shift: B1–B2 (blue direction) to simulate shadow cast
- Highlight Tone: -1 to -2, simulate longer shoulder
- Shadow Tone: -1, retain shadow detail, simulate lifted blacks
- Color: -1 to 0, Pro 400H is not a saturated film
- Grain Effect: Size Small, Roughness Weak, fine grain character
- Sharpness: -1, film has softer acuity than digital

---

## Why the Gap Exists (Technical)

The Pro 400H's distinctive shadow blue-green cast is a product of its emulsion layer balance, the relative sensitivity and dye density curves of the cyan, magenta and yellow dye layers at shadow luminance levels. The digital simulation's equivalent behaviour is determined by how Fujifilm encoded the shadow portion of the colour LUT (Look-Up Table) when building Pro Neg. Hi.

The film was designed to perform across a wide ISO range and in difficult lighting conditions (mixed tungsten/daylight). Its broad spectral sensitivity and cool shadow balance reflect these production constraints. The Pro Neg. Hi simulation was modelled on NPS 160 / NS 160 (a studio portrait film with different design priorities), not on Pro 400H directly, hence the tonal and colour divergence.

---

## Practical Use in Recipes

When building recipes inspired by Pro 400H:

1. Base on PRO Neg. Hi: it's the closest starting point
2. Apply a blue-leaning WB shift to simulate shadow cast
3. Lower highlight tone significantly (-2) for shoulder simulation
4. Keep saturation restrained: Pro 400H is not a vivid film
5. Validate against actual Pro 400H scans: use scanned film prints as reference captures in the `X-T5/` reference folder

---

*Last updated: 2026-07-15*
*Source: [Fuji Pro 400H compared to Pro Neg Hi simulation, Pushing Film (YouTube)](https://www.youtube.com/watch?v=0uT2k0e3OGg)*
