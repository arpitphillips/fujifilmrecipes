# Why Fujifilm film simulations cannot be replicated in post-production

*Sources: [Imaging Resource Definitive Guide (Aug 2020)](https://www.imaging-resource.com/news/2020/08/18/fujifilm-film-simulations-definitive-guide) · [Zen & The Art of Fujifilm Film Simulations](https://www.youtube.com/watch?v=sS_e19J7OaU) · [Pro 400H vs Pro Neg Hi comparison](https://www.youtube.com/watch?v=0uT2k0e3OGg)*

---

## The core problem: film is multi-dimensional, sliders are not

When you adjust Hue/Saturation or Selective Color in Photoshop, you apply a single scalar transformation to a region of the color wheel. The tool does not know whether a pixel is bright or dark, saturated or dull. Every pixel with that hue gets the same treatment.

Real photographic film does not work this way. Fujifilm's simulations are a mathematical characterisation of actual emulsions, where color transforms vary simultaneously across three independent axes:

1. Hue: where the color sits on the color wheel
2. Saturation: how saturated the original color is
3. Luminance: how bright the color is

No Photoshop tool operates across all three axes at once. That is not a limitation of skill. It is structural. The transformations Fujifilm's ISP applies cannot be built from any combination of standard adjustments.

> **Recipe implication:** in-camera recipes are the only mechanism that engages Fujifilm's proprietary color science. A recipe is not a stylistic preset. It activates a physics-based model that exists nowhere else.

---

## Fujifilm's 85-year film heritage

Fujifilm has manufactured emulsions since 1934. Their digital simulations are built from:

- Spectral sensitivity curves of the actual film stocks (per-wavelength response of each emulsion layer)
- Dye density curves, which describe how silver halide grains translate to dye clouds through development chemistry
- Frontier minilab calibration data, from Fujifilm's professional photo printing system
- Memory colour research: empirical data on which colour renditions people find most emotionally satisfying

This data does not exist outside Fujifilm. Third-party profiles in Lightroom, ACR or Capture One are visual approximations, not physics reconstructions.

---

## How colour film actually works (and why sliders can't touch it)

*(For the black-and-white chemical foundation of silver halides, the latent image and development, see [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md).)*

Colour film is a stack of 9 or more layers: multiple light-sensitive emulsion layers for red, green and blue light, with colour-filtering and interface layers between them. Two independent curve families define the look:

1. Spectral sensitivity curves: how each light-sensitive layer responds across the wavelength spectrum (the input side)
2. Dye absorption/density curves: how the cyan, magenta and yellow dyes that form the final image block light per wavelength (the output side)

### Case study: PROVIA vs Velvia dye purity

The Imaging Resource guide reproduces Fujifilm's actual curves for both stocks, and the finding is counter-intuitive:

- Velvia's sensitivity layers overlap more than Provia's (its red and blue layers react more to greens), which would normally reduce saturation.
- But Velvia's dyes have much less spectral overlap than Provia's. Perfect dyes would block only their target colour. Provia's magenta and cyan dyes absorb a lot of blue light they shouldn't, while Velvia's dyes are far purer.
- Net result: Velvia's legendary saturation comes primarily from the output dyes, not the input sensitivity. That two-stage interaction is something no single-stage editing tool can model.

Velvia's green sensitivity layer is also simply more sensitive than Provia's, which is part of why its foliage greens glow.

> **Why Photoshop fails structurally:** an editor adjustment operates on the final RGB values. Film's look is the product of input sensitivity curves times interlayer filtering times output dye curves, and each colour channel contaminates the others differently at every stage. Tweaking per-channel tone curves cannot represent a red layer that is partially sensitive to green, feeding a cyan dye that partially absorbs blue.

---

## History of the film simulations

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

As of the guide's writing (Aug 2020) there were 17 simulations covering 10 distinct film types. The X-T5 generation later added Nostalgic Neg. and REALA ACE. Fujifilm also keeps refining existing simulations as processors improve, so the same simulation name can render slightly differently across camera generations. That matters when converting recipes between X-Trans versions; see [x-trans-v-and-conversion.md](x-trans-v-and-conversion.md).

---

## Memory colors: why Fuji optimises for perception, not truth

Fujifilm's colour science philosophy is explicit: the goal is perceptual satisfaction, not colorimetric accuracy.

Human visual memory is systematically biased:
- Skies are remembered as bluer and more saturated than measured
- Foliage is remembered as greener and more vivid
- Skin is remembered as warmer and more even

Simulations intentionally push toward memory colours rather than neutral measurement. This is why Fuji images feel emotionally right even when a color chart would show them as off.

Different simulations implement different memory-colour strategies:

| Simulation | Memory Colour Strategy |
|---|---|
| Velvia | Maximum exaggeration across the board |
| PROVIA | Moderate, naturalistic bias |
| ASTIA | Optimised for skin — less rosy, hides blemishes |
| Classic Chrome | Inverted for blues/skies — magenta deliberately removed |
| Pro Neg simulations | Prioritises skin-tone smoothness over vibrancy |

---

## Why Adobe Camera Raw and Lightroom don't match

The author of the Imaging Resource guide spent hours converting shots in ACR, then looked at the camera JPEG of the same frame and described the result as "a *lot* different." The reasons:

1. ACR presets are visual approximations, reverse-engineered from the look rather than from spectral physics
2. Tone curve handling diverges dramatically, especially in the highlights. ASTIA's soft rolloff cannot be reproduced in ACR's Profile system
3. Per-hue non-linearity is irreproducible. Classic Chrome in ACR gets the general direction (low saturation, harder contrast) but not the specific per-hue shifts that vary simultaneously by saturation and brightness
4. Capture One displays the embedded camera-generated JPEG thumbnail; Adobe ignores it and substitutes its own profile. In Lightroom, your RAF files will look different from your JPEGs even for the same shot

### The only authentic simulation workflow

> In-camera JPEG, or X RAW STUDIO, which routes through the camera's own ISP. Any other RAW converter produces a different image. Not a variant of the simulation, a different colour science entirely.

This is the foundational reason why this project treats the JPEG as the archival primary and RAW as a recovery fallback only.

---

## Post-processing safety boundaries

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

## Per-simulation spectral behaviour (from Imaging Resource spectral data)

### PROVIA / Standard
- The baseline reference: moderate saturation lift with slight red and green exaggeration
- Sky gets a moderate blue saturation boost with a hint of magenta retained
- Oranges shift slightly toward yellow. Without this shift, yellows and oranges look muddy and hard to separate visually
- Light cyan-blues shift toward pure blue, an industry-wide digital convention for pleasing skies, applied conservatively here
- Fujifilm's marketing calls it "the ace of spades, the strongest card of all", and it is the factory default on every camera

### VELVIA 50
- Based on FUJICHROME Velvia, the professional reversal film introduced in 1991 and beloved by landscape photographers
- Extreme saturation lift, especially in greens and magentas; dark greens, dark blues and pure reds move furthest
- Blues deliberately skew toward magenta, producing the "royal blue" skies Velvia is famous for
- Can clip the sRGB gamut on bright reds and pinks (flowers, sunsets), with visible loss of detail in the most saturated areas
- Hard S-curve shadow contrast; bright yellows also carry higher contrast than other hues
- Designed to represent scenes "as photographers remember them": memory colour pushed to maximum
- Choose ASTIA when you want colour pop but need to preserve tonal gradation in bright subjects

### ASTIA / Soft
- Highlights roll off substantially softer than PROVIA
- Shadows run darker than PROVIA, so overall contrast stays high despite the soft highlights
- Skin renders less rosy and at lower saturation, so the profile treats skin its own way rather than softening PROVIA's rendering. Caucasian skin lands almost dead-on its true colour, and darker skin tones get increased saturation, producing richer tones for darker complexions
- Hides skin blemishes and blotchiness better than any other simulation
- The colour map reads like a blend of Provia and Velvia: dark greens more saturated than Provia, yellows and oranges less, darker blues noticeably more saturated
- Fujifilm also recommends it for adapted vintage lenses, since its harder shadows compensate for older optics' lower contrast

### CLASSIC CHROME
- No single-film lineage. Designed to evoke Kodachrome-era reversal film and printed-magazine imagery
- Lowest saturation of any colour simulation until Eterna Bleach Bypass arrived
- Shadow contrast is harder and highlight contrast softer, the opposite of ASTIA
- The sky's magenta component is intentionally and completely removed, a documented Fujifilm design decision
- Cyan and blue hues behave non-monotonically: bright cyan stays near true colour, medium blue desaturates and shifts toward cyan, dark blue shifts differently again
- Imaging Resource states it plainly: this one "cannot be approximated in Photoshop, the sorts of changes just aren't possible through any manual adjustment"
- Target use is street and documentary. It evokes the Life/Look magazine aesthetic of the 1970s

### PRO Neg.Std
- Based on Fujifilm NPS 160 / NS 160, the professional studio portrait negative film
- The actual NPS 160 emulsion contained a fourth, cyan-sensitive layer that gave Fujifilm's chemists superior skin-tone control
- Very flat tone curve with muted, direction-accurate colours rather than hue-shifted ones
- Designed for studio use where lighting creates the contrast; it looks intentionally flat outdoors
- Hides blemishes and wrinkles through contrast reduction, not hue manipulation

### PRO Neg.Hi
- Pro Neg.Std with the same colour direction, pushed less far
- Slightly more saturation and contrast than Std
- Preferred for outdoor, wedding, and casual portrait situations

### CLASSIC Neg.
- Based on Fujifilm Superia 100, the consumer negative film introduced in 1998
- High contrast, a slight red-magenta tint, lower saturation
- The colour gamut is squashed away from bright yellows, greens, purples and blues, and ballooned out in the reds. The most complex colour map of any simulation
- The tone curve varies between colour channels more than any other profile; some channels are deliberately flatter than others to increase inter-colour contrast
- The "old family shoebox print" aesthetic. It evokes colour-negative prints of the 1960s to 1980s more strongly than any other simulation

### ETERNA Cinema
- Based on Fujifilm's motion picture negative stocks, which were never sold to consumers
- Roughly 12 stops of dynamic range with softened shadows and highlights: extended latitude without going to full log-gamma
- Lifted shadows (milky blacks, never pure black) and extreme highlight protection
- The colour palette is squashed like Classic Neg (greens, magentas and purples desaturated most) but far more gently, and per Fujifilm with deliberately low hue shift, since colour accuracy was a design goal here, unlike most simulations
- It needs colour grading to reach a finished look. Eterna is a neutral starting point, not a standalone aesthetic
- The intended workflow: ETERNA in-camera, then grade in Resolve or FCPX

### ETERNA Bleach Bypass
- Introduced in Feb 2020 with the X-T4, the newest simulation in the guide
- Simulates skipping the bleaching step of colour-negative processing, which normally removes the image silver and leaves only dye. Retained silver means a contrasty B&W image overlaid on a faint colour one
- The lowest saturation of all colour simulations, but the desaturation is uniform across the spectrum with almost no hue shifts. Its hue map matches ETERNA almost exactly, with saturation floored and contrast maxed
- Washed-out highlights over very dark shadows are the hallmark. On real film, shots destined for bleach bypass were exposed about a stop under; for in-camera JPEGs consider dialling exposure back similarly
- Signature use is urban-grunge and gritty editorial. It's also striking on normally colourful subjects

### ACROS
- Emulates the Neopan ACROS series black-and-white film (orthopanchromatic; the modern stock is Acros 100 II)
- Fujifilm's own tone curve plot shows harder, higher contrast from the lower midtones to the middle highlights, and much softer response through the lower midtones and shadows, which keeps shadow detail rich
- Distinctive grain structure that is not equivalent to adding digital noise (see the grain section below)
- More contrasty than the Monochrome simulation
- The preferred B&W simulation for most subjects
- B&W films vary widely in spectral response (panchromatic against orthochromatic and so on), which is why a Photoshop RGB-to-grayscale conversion, which just discards colour information, produces bland results by comparison

### Monochrome
- Effectively PROVIA with the colour information removed (it was named "B&W" before the X-Pro1)
- Flatter than ACROS, and its grain option is a simpler random pattern. Preferable for high-key, dreamy, or extremely contrasty subjects where ACROS would clip

### SEPIA
- A historical note: sepia toning replaced silver particles with silver sulfide, which resists environmental sulfur from industrial coal combustion
- It served a practical archival function in the 19th century and is now purely aesthetic. Full chemistry in [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md)

---

## The ACROS grain simulation: why it isn't a noise overlay

Film grain is silver-halide crystals that clumped into visible particles during development (the chemistry is in [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md)). Fujifilm's ACROS simulation models that entire process algorithmically rather than scattering random dots:

- The simulated grain reproduces the structure of real ACROS grain, including how the texture changes between highlight and shadow regions of the same frame. Real grain clumps differently at different densities
- The base grain processing is always identical, but it combines with natural sensor noise, so images at higher ISO look grainier, just like film. A practical trick: if you want a grainy look, deliberately shoot at higher ISO even in bright light
- The separate Grain Effect menu (Weak/Strong, plus Size on newer bodies) layers on top of this
- Adobe's grain sliders (amount, size, roughness) can match the overall visual weight but show visibly less structure, and the gap widens the harder the effect is pushed
- Photoshop's demosaicing can produce serpentine noise patterns that superficially resemble ACROS grain, but that is a demosaicing artifact seen across many cameras, not grain modelling
- Only ACROS gets the structured grain model. The Monochrome simulation's grain option is a simpler random digital pattern

## Ye / R / G filters and B&W Adjust

Both B&W simulations (ACROS and Monochrome) can apply a simulated colour filter before the monochrome conversion, replicating the classic screw-on filters of the film era:

| Filter | Effect |
|---|---|
| **Yellow** | Darkens blue skies slightly so clouds pop; minimal effect on foliage — the classic all-purpose landscape filter |
| **Red** | Yellow "only more so" — skies go very dark and dramatic; foliage lightens slightly |
| **Green** | Slightly darkens sky; mainly softens contrast within green foliage; flatters skin in portraits |

Cameras since the X-T3/X-T30 also offer B&W Adjust: ±9 steps of warm/cool toning on the monochrome image, mimicking the distinctive paper tones of different B&W printing papers (warm for portraits, cool for snowscapes).

---

---

## Fujifilm's own words for this argument *(added 2026-07-20)*

The strongest first-party statement of the thesis on this page comes from the Image Design team:

> **"Image design is a work of converting the raw signal while understanding the difference of the spectral sensitivity."**
> Source: [X Stories: Film Simulation, Revolution by Continuous Evolution](https://www.fujifilm-x.com/global/stories/film-simulation-revolution-by-continuous-evolution/)

That single sentence is the whole case. A film simulation is not a colour grade applied to a finished picture; it is a spectral-sensitivity-aware conversion of the raw sensor signal**, performed at the point where the sensor's response is reconciled with how the eye actually sees. Once a file has been demosaiced and handed to Lightroom, that step has already happened and cannot be re-run. This is why the in-camera JPEG is the archival primary in this bank.

Two supporting statements from the same source:
- The target never moved, only the machinery: *"The vision of ideal colour reproduction for FUJIFILM remains the same. It's just that devices have evolved, processor has evolved, and the algorithm has evolved."* And, candidly, *"there are still hundreds of things to do to reach the ideal vision."*
- Newer processors extract more from the *same* signal (*"it picks up signals that were not previously picked up"*), giving more detail *"without supersaturation"*, and granting every colour simulation greater **"toughness against colour supersaturation."** This is a generational trait, and part of why [X-Trans IV→V ports](x-trans-v-and-conversion.md) tolerate Color values that would have looked garish on older bodies.

A third, easily-missed constraint: the EVF must render the simulation live: *"If the film simulation is set to Velvia, then we have to show the world of Velvia in real time. EVF has to be that what you see is what you get."* Practically, you are previewing the finished JPEG before the shutter fires; recipes should be judged in the viewfinder in the actual light, not guessed at from a settings table.

Full extraction: [fujifilm-official-design-notes.md](fujifilm-official-design-notes.md).

*Last updated: 2026-07-17*
