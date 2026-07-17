# Why Fujifilm Film Simulations Cannot Be Replicated in Post-Production

*Sources: [Imaging Resource Definitive Guide (Aug 2020)](https://www.imaging-resource.com/news/2020/08/18/fujifilm-film-simulations-definitive-guide) · [Zen & The Art of Fujifilm Film Simulations](https://www.youtube.com/watch?v=sS_e19J7OaU) · [Pro 400H vs Pro Neg Hi comparison](https://www.youtube.com/watch?v=0uT2k0e3OGg)*

---

## The Core Problem: Film Is Multi-Dimensional, Sliders Are Not

When you adjust Hue/Saturation or Selective Color in Photoshop, you apply a **single scalar transformation** to a region of the color wheel. It does not know whether a pixel is bright or dark, saturated or dull — every pixel with that hue gets the same treatment.

Real photographic film does not work this way. Fujifilm's simulations are a **mathematical characterisation** of actual emulsions, where color transforms vary simultaneously across **three independent axes**:

1. **Hue** — where the color sits on the color wheel
2. **Saturation** — how saturated the original color is
3. **Luminance** — how bright the color is

No Photoshop tool operates across all three axes at once. This is not a limitation of skill — it is a structural impossibility. The transformations Fujifilm's ISP applies cannot be replicated with any combination of standard adjustments.

> **Recipe implication:** Recipes built in-camera are the *only* mechanism by which Fujifilm's proprietary color science is engaged. They are not stylistic presets — they are activation of a unique physics-based model.

---

## Fujifilm's 85-Year Film Heritage

Fujifilm has manufactured emulsions since 1934. Their digital simulations are built from:

- **Spectral sensitivity curves** of the actual film stocks (per-wavelength response of each emulsion layer)
- **Dye density curves** — how silver halide grains translate to dye clouds through development chemistry
- **Frontier minilab calibration data** — Fujifilm's professional photo printing system colour profiles
- **Memory colour research** — empirical data on which colour renditions humans perceive as most emotionally satisfying

This data does not exist outside Fujifilm. Third-party profiles (Lightroom, ACR, Capture One) are visual approximations, not physics reconstructions.

---

## How Colour Film Actually Works (and why sliders can't touch it)

*(For the black-and-white chemical foundation — silver halides, latent image, development — see [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md).)*

Colour film is a stack of **9 or more layers**: multiple light-sensitive emulsion layers for red, green and blue light, with colour-filtering and interface layers between them. Two independent curve families define the look:

1. **Spectral sensitivity curves** — how each light-sensitive layer responds across the wavelength spectrum (input side)
2. **Dye absorption/density curves** — how the cyan, magenta and yellow dyes that form the final image block light per wavelength (output side)

### Case study: PROVIA vs Velvia dye purity

The Imaging Resource guide reproduces Fujifilm's actual curves for both stocks, and the finding is counter-intuitive:

- Velvia's **sensitivity layers overlap more** than Provia's (its red and blue layers react more to greens) — which would normally *reduce* saturation.
- But Velvia's **dyes have much less spectral overlap** than Provia's. Perfect dyes would block only their target colour; Provia's magenta and cyan dyes absorb a lot of blue light they shouldn't, while Velvia's dyes are far purer.
- Net result: Velvia's legendary saturation comes primarily **from the output dyes, not the input sensitivity** — a two-stage interaction no single-stage editing tool can model.

Also note Velvia's green sensitivity layer is simply more sensitive than Provia's — part of why its foliage greens glow.

> **Why Photoshop fails structurally:** an editor adjustment operates on the *final* RGB values. Film's look is the product of input sensitivity curves × interlayer filtering × output dye curves, where each colour channel contaminates the others differently at each stage. Tweaking per-channel tone curves cannot represent a red layer that is partially sensitive to green, feeding a cyan dye that partially absorbs blue.

---

## History of the Film Simulations

| Year | Camera | Milestone |
|---|---|---|
| 2003 | FinePix F700 | First variant, called **FinePix COLOR** — F-Standard, F-Chrome, F-B&W (not tied to named films) |
| 2004 | S3 Pro DSLR | The name "Film Simulation" first appears |
| 2007 | S5 Pro | More film types added |
| 2009 | FinePix F200EXR | First use of **classic film names**: PROVIA, Velvia, ASTIA (+ generic B&W, SEPIA) |
| 2012 | X-Pro1 | PRO Neg.Hi & Std added; B&W renamed MONOCHROME; Ye/R/G filters added |
| 2014 | X30 | CLASSIC CHROME |
| 2016 | X-Pro2 | ACROS |
| 2018 | X-H1 | ETERNA |
| 2019 | X-Pro3 | CLASSIC Neg. |
| 2020 | X-T4 | ETERNA BLEACH BYPASS |

As of the guide's writing (Aug 2020) there were **17 simulations covering 10 distinct film types**. The X-T5 generation later added Nostalgic Neg. and REALA ACE. Fujifilm also continually *refines existing simulations* as processors improve — the same simulation name can render slightly differently across camera generations (relevant when converting recipes between X-Trans versions; see [x-trans-v-and-conversion.md](x-trans-v-and-conversion.md)).

---

## Memory Colors: Why Fuji Optimises for Perception, Not Truth

Fujifilm's colour science philosophy is explicit: **the goal is not colorimetric accuracy — it is perceptual satisfaction.**

Human visual memory is systematically biased:
- Skies are remembered as bluer and more saturated than measured
- Foliage is remembered as greener and more vivid
- Skin is remembered as warmer and more even

Simulations intentionally **push toward memory colours**, not toward neutral measurement. This is why Fuji images feel emotionally "right" even when a color chart would show them as off.

Different simulations implement different memory-colour strategies:

| Simulation | Memory Colour Strategy |
|---|---|
| Velvia | Maximum exaggeration across the board |
| PROVIA | Moderate, naturalistic bias |
| ASTIA | Optimised for skin — less rosy, hides blemishes |
| Classic Chrome | Inverted for blues/skies — magenta deliberately removed |
| Pro Neg simulations | Prioritises skin-tone smoothness over vibrancy |

---

## Why Adobe Camera Raw / Lightroom Don't Match

The author of the Imaging Resource guide spent hours converting shots in ACR, then saw the camera JPEG of the same frame — and described the result as "a *lot* different." Key reasons:

1. **ACR presets are visual approximations** — reverse-engineered from the look, not from spectral physics
2. **Tone curve handling diverges dramatically** — especially highlights. ASTIA's soft rolloff cannot be reproduced in ACR's Profile system
3. **Per-hue non-linearity is irreproducible** — Classic Chrome in ACR gets the general direction (low saturation, harder contrast) but cannot reproduce the specific per-hue shifts that vary simultaneously by saturation and brightness
4. **Capture One vs Adobe** — Capture One displays the embedded camera-generated JPEG thumbnail; Adobe ignores it and substitutes its own profile. This means in Lightroom, your RAF files will look different from your JPEGs even for the same shot

### The Only Authentic Simulation Workflow

> In-camera JPEG, or **X RAW STUDIO** (which routes through the camera's own ISP). Any other RAW converter produces a different image — not a variant of the simulation, but a different colour science entirely.

This is the foundational reason why this project treats JPEG as the archival primary and RAW as a recovery fallback only.

---

## Post-Processing Safety Boundaries

Some adjustments are safe after the simulation is applied; others break the per-hue colour model:

| Adjustment | Safety | Reason |
|---|---|---|
| Global exposure ±0.5 EV | ✅ Safe | Within the tone curve's linear region |
| White balance correction | ✅ Safe | Global colour temperature shift pre-demosaic is clean |
| Clarity / local contrast | ✅ Safe | Texture-layer only, does not touch colour |
| Vibrance | ⚠️ Caution | Can break hue-saturation balance built into the sim |
| Saturation (global) | ❌ Avoid | Overrides the sim's per-hue saturation strategy |
| Selective hue shifts | ❌ Avoid | Fights the sim's own hue-shift curves |
| Changing film sim in ACR | ❌ Avoid | Produces a different image — not a variation |

---

## Per-Simulation Spectral Behaviour (from Imaging Resource spectral data)

### PROVIA / Standard
- Baseline reference — moderate saturation lift, slight red and green exaggeration
- Sky: moderate blue saturation boost with a hint of magenta retained
- Oranges shift slightly toward yellow — without this shift, yellows and oranges look muddy and hard to separate visually
- Light cyan-blues shift toward pure blue — an industry-wide digital convention for pleasing skies, and Provia applies it conservatively
- Fujifilm's marketing calls it "the ace of spades — the strongest card of all"; it is the factory default on every camera

### VELVIA 50
- Based on FUJICHROME Velvia, introduced **1991** — professional reversal film beloved by landscape photographers
- Extreme saturation lift, especially greens and magentas; dark greens, dark blues and pure reds most extreme
- Blues deliberately skew toward **magenta** — producing the "royal blue" skies Velvia is famous for
- Can clip sRGB gamut for bright reds and pinks (flowers, sunsets) — visible loss of detail in the most saturated areas
- Hard S-curve shadow contrast; bright yellows also rendered with higher contrast than other hues
- Designed to represent scenes "as photographers remember them" — memory colour pushed to maximum
- Choose ASTIA when you want colour pop but need to preserve tonal gradation in bright subjects

### ASTIA / Soft
- Highlights: substantially softer rolloff than PROVIA
- Shadows: *darker* than PROVIA — overall contrast stays high despite soft highlights
- Skin: less rosy, lower saturation — not merely "softer PROVIA". Caucasian skin lands almost dead-on its true colour; **darker skin tones get increased saturation**, producing richer tones for darker complexions
- Hides skin blemishes and blotchiness better than any other simulation
- Colour map reads like a blend of Provia and Velvia: dark greens more saturated than Provia, yellows/oranges less; darker blues noticeably more saturated
- Fujifilm also recommends it for **adapted vintage lenses** — its harder shadows compensate for older optics' lower contrast

### CLASSIC CHROME
- No single-film lineage — designed to evoke **Kodachrome-era reversal film** and printed-magazine imagery
- Lowest saturation of any colour simulation (until Eterna Bleach Bypass)
- Shadow contrast is harder; highlight contrast is softer (opposite of ASTIA)
- **Sky: magenta component intentionally and completely removed** — documented Fujifilm design decision
- Cyan/blue hues behave non-monotonically: bright cyan stays near true colour; medium blue desaturates and shifts toward cyan; dark blue shifts differently again
- Explicitly stated by Imaging Resource: "cannot be approximated in Photoshop — the sorts of changes just aren't possible through any manual adjustment"
- Target use: street and documentary; evokes Life/Look magazine aesthetic of the 1970s

### PRO Neg.Std
- Based on **Fujifilm NPS 160 / NS 160** — professional studio portrait negative film
- The actual NPS 160 emulsion contained a **fourth, cyan-sensitive layer** that gave Fujifilm's chemists superior skin-tone control
- Very flat tone curve + muted, direction-accurate (not hue-shifted) colours
- Designed for studio use where lighting creates contrast; looks intentionally flat outdoors
- Hides blemishes and wrinkles through contrast reduction, not hue manipulation

### PRO Neg.Hi
- "Pro Neg.Std Lite" — same colour direction, less extreme
- Slightly more saturation and contrast than Std
- Preferred for outdoor, wedding, and casual portrait situations

### CLASSIC Neg.
- Based on **Fujifilm Superia 100** consumer negative film (introduced 1998)
- High contrast, slight red-magenta tint, lower saturation
- Colour gamut behaviour: **squashed away from bright yellows, greens, purples and blues — ballooned out in the reds**. The most complex colour map of any simulation
- Tone curve varies **between colour channels** more than any other profile — some channels deliberately flatter than others to increase inter-colour contrast
- "Old family shoebox print" aesthetic — evokes colour-negative prints of the 1960s–1980s more strongly than any other simulation

### ETERNA Cinema
- Based on Fujifilm's motion picture negative stocks — never sold to consumers
- **~12-stop dynamic range** with softened shadows and highlights — extended latitude without going to full log-gamma
- Lifted shadows (milky blacks — never pure black); extreme highlight protection
- Colour palette squashed like Classic Neg (greens, magentas, purples desaturated most) but far gentler, and per Fujifilm with deliberately **low hue shift — colour accuracy was a design goal**, unlike most simulations
- Requires colour grading to reach a finished look — not a standalone aesthetic; it is a neutral *starting point*
- Correct workflow: ETERNA in-camera → grade in Resolve/FCPX

### ETERNA Bleach Bypass
- Introduced Feb 2020 with the X-T4 — the newest simulation in the guide
- Simulates **skipping the bleaching step** of colour-negative processing, which normally removes the image silver and leaves only dye. Retained silver = a contrasty B&W image overlaid on a faint colour one
- **Lowest saturation of all colour simulations** — but the desaturation is *uniform* across the spectrum with almost no hue shifts; its hue map matches ETERNA almost exactly, just with saturation floored and contrast maxed
- Washed-out highlights + very dark shadows are the hallmark. On real film, shots destined for bleach bypass were exposed ~1 stop under; for in-camera JPEGs consider dialling exposure back similarly
- Signature use: urban-grunge, gritty editorial; also striking on normally colourful subjects

### ACROS
- Emulates the **Neopan ACROS series** black-and-white film (orthopanchromatic; the modern stock is Acros 100 II)
- Tone curve (per Fujifilm's own plot): **harder/higher-contrast from lower midtones to middle highlights, much softer through lower midtones and shadows** — richer shadow detail
- Distinctive grain structure — not equivalent to adding digital noise (see grain section below)
- More contrasty than the Monochrome simulation
- Preferred B&W simulation for most subjects
- B&W films vary widely in spectral response (panchromatic vs orthochromatic etc.) — which is why a Photoshop RGB→Grayscale conversion, which just discards colour information, produces bland results by comparison

### Monochrome
- Effectively **PROVIA with the colour information removed** (originally named "B&W" before the X-Pro1)
- Flatter than ACROS, and its grain option is a simpler random pattern — preferable for high-key, dreamy, or extremely contrasty subjects where ACROS would clip

### SEPIA
- Historical note: sepia toning replaced silver particles with **silver sulfide**, which is chemically more resistant to environmental sulfur from industrial coal combustion
- Practical archival function in the 19th century; now purely aesthetic — full chemistry in [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md)

---

## The ACROS Grain Simulation — Why It Isn't a Noise Overlay

Film grain is silver-halide crystals that clumped into visible particles during development (chemistry in [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md)). Fujifilm's ACROS simulation **models that entire process algorithmically** rather than scattering random dots:

- The simulated grain reproduces the **structure** of real ACROS grain, including how the texture **changes between highlight and shadow regions** of the same frame — real grain clumps differently at different densities
- The base grain processing is always identical, but it **combines with natural sensor noise**, so images at higher ISO look grainier — just like film. *Practical trick: if you want a grainy look, deliberately shoot at higher ISO even in bright light*
- The separate Grain Effect menu (Weak/Strong, plus Size on newer bodies) layers on top of this
- Adobe's grain sliders (amount/size/roughness) can match the overall visual *weight* but have visibly **less structure** — the gap widens the harder the effect is pushed
- Photoshop's demosaicing can produce serpentine noise patterns that superficially resemble ACROS grain, but that is a demosaicing artifact seen across many cameras, not grain modelling
- **Only ACROS gets the structured grain model.** The Monochrome simulation's grain option is a simpler random digital pattern

## Ye / R / G Filters and B&W Adjust

Both B&W simulations (ACROS and Monochrome) can apply a simulated colour filter *before* the monochrome conversion, replicating the classic screw-on filters of the film era:

| Filter | Effect |
|---|---|
| **Yellow** | Darkens blue skies slightly so clouds pop; minimal effect on foliage — the classic all-purpose landscape filter |
| **Red** | Yellow "only more so" — skies go very dark and dramatic; foliage lightens slightly |
| **Green** | Slightly darkens sky; mainly softens contrast within green foliage; flatters skin in portraits |

Cameras since the X-T3/X-T30 also offer **B&W Adjust**: ±9 steps of warm/cool toning on the monochrome image, mimicking the distinctive paper tones of different B&W printing papers (warm for portraits, cool for snowscapes).

---

*Last updated: 2026-07-15*
