# Film chemistry fundamentals: why film looks the way it does

*Source: [The Chemistry of Black and White Photography — Tim Johnson, UW–Eau Claire Chem 115](https://www.chem.uwec.edu/Chem115_F00/johnstim/Chemandphoto.htm) · cross-referenced by the [Imaging Resource Definitive Guide](https://www.imaging-resource.com/news/2020/08/18/fujifilm-film-simulations-definitive-guide), which cites this exact page as its film-chemistry reference.*

---

## Why this file exists

Every Fujifilm simulation setting, from Grain Effect and the ISO/grain relationship to Acros's tonality and even Sepia, is a digital model of a chemical process. Understanding the chemistry explains why the settings behave the way they do, and why the film look has the structure it has. This file covers the black-and-white foundation; [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md) extends it to colour film's multi-layer dye system.

---

## A very short history

- Early 1800s: Thomas Wedgwood and Sir Humphry Davy made shadow images on leather and paper impregnated with silver nitrate (AgNO₃), but the images darkened uncontrollably. There was no way to stop the reaction.
- 1802 onward: Henry Fox Talbot treated paper sequentially in salt solution then silver nitrate, forming silver chloride crystals inside the paper fibres. Exposure times fell from around an hour to around ten minutes.
- 1839: Talbot adopted sodium thiosulfate (Na₂S₂O₃), "hypo", as a fixing agent. Fixing is what made photography permanent, and the same chemical is still the basis of fixer today.

---

## The structure of film (4 layers)

| Layer | Function |
|---|---|
| **Gelatin coating** | Protective layer against scratching |
| **Photo emulsion** | The light-sensitive layer — where the latent image forms |
| **Organic base** | Structural substrate (typically polyethylene terephthalate) |
| **Antihalation backing** | Absorbs light that passes through, preventing halos around bright point sources |

> **Digital parallel:** the "emulsion" is what a film simulation models. The antihalation backing is why real film doesn't bloom around streetlights the way early digital sensors did, and why halation is a separate look. CineStill 800T's signature red halos exist because that stock has the backing removed.

---

## The photo emulsion

### Silver halide salts

Three light-sensitive silver halide compounds form crystalline lattice "grains":

| Halide | Responds to |
|---|---|
| Silver chloride (AgCl) | Violet / ultraviolet light (highest energy required) |
| Silver bromide (AgBr) | Blue light |
| Silver iodide (AgI) | Green light (lowest energy threshold) |

By varying the ratio of the three halides, manufacturers tune a film's spectral response. This is the first hint of why every emulsion renders colours differently, even in black and white. (Panchromatic emulsions respond to all wavelengths; orthochromatic ones are blind to red.)

### Gelatin

The halide crystals are suspended in gelatin, a clear gel of starches, gums or glues, forming a nearly homogeneous suspension: the photographic emulsion. The gelatin prevents the crystals from precipitating out.

### Sensitizing agents

Iso-thiocyanate compounds (the –SCN group) form silver sulfide (Ag₂S) specks on the surface of the halide crystals. These specks act as electron traps, and they are what make fast shutter speeds (1/100 to 1/1000 s) possible at all.

---

## Latent image formation (the exposure)

When photons strike the emulsion, silver bromide decomposes:

1. AgBr → Ag⁺ + Br⁻ (primary decomposition)
2. Br⁻ + energy → Br + e⁻ (bromine atoms pair into Br₂; electrons are released)

The freed electrons migrate through the crystal lattice and accumulate in the silver sulfide electron traps. The negatively charged trap attracts interstitial Ag⁺ ions, and electrons combine with them to form tiny specks of metallic silver. Only a few atoms per grain are converted, so the image at this stage is invisible. That is the latent image.

---

## Development (the amplification)

Developers are reducing agents (electron donors), typically benzene-derivative organics, that convert exposed grains to metallic silver while leaving unexposed grains mostly untouched. Kodak D-76, for example, uses hydroquinone as its active reducing agent, with typical development times of 8 to 14 minutes.

The key mechanism is autocatalysis:

> The metallic silver speck on the outside of a silver halide crystal acts as a catalyst for the reduction of the entire grain. As the silver speck grows, the reaction rate accelerates on the grains that were marked by exposure.

This is an enormous chemical amplification. A few photon-struck atoms decide the fate of an entire crystal about a micron wide. It is why film has a characteristic threshold-and-shoulder tonal response rather than the linear response of a digital sensor, and it is the physical origin of the S-shaped tone curves that the Highlight and Shadow Tone settings emulate.

## Stop bath

Developer solutions are slightly alkaline, and alkalinity accelerates development. A mildly acidic stop bath, commonly 3% acetic acid (CH₃COOH), neutralises the developer and halts the reaction. Clean running water is the gentler alternative.

## Fixing (making it permanent)

After development, undeveloped silver halide crystals remain in the emulsion. They are still light-sensitive, and they would fog the image on exposure. Sodium thiosulfate (Na₂S₂O₃) converts them into soluble complexes that wash away:

1. AgBr + 2Na₂S₂O₃ → Na₃[Ag(S₂O₃)₂] + NaBr
2. Na₃[Ag(S₂O₃)₂] → 3Na⁺ + Ag(S₂O₃)₂³⁻ (dissociates in solution)

The soluble complex is washed out, leaving only the developed metallic-silver image: the negative.

---

## Grain: the physics behind the Grain Effect setting

### Grain size, film speed and contrast are coupled

> **"The sensitivity of film is determined primarily by the size of grains in the emulsion."**

- Larger crystals present more area to incoming light, which makes it more likely that a few molecules get struck and the whole grain develops. Larger grain means faster film (higher ISO) but coarser texture.
- Smaller grains mean slower film, finer texture, and higher contrast.
- This coupling is structural. It is difficult to make a fast, high-contrast film or a slow, low-contrast film. Manufacturers also blend a distribution of grain sizes within one emulsion to shape the contrast curve.

### Grain is a development artifact, not a capture artifact

Individual silver particles are too small to see, at roughly a micron; the Imaging Resource guide shows an electron micrograph of grains isolated from Fujicolor Superia 100. What we perceive as "film grain" is silver particles clumping together during development. The original crystal size and shape plus the clumping behaviour set the grain's character, and grain structure differs between highlight and shadow regions of the same frame.

### Mapping to the Fujifilm Grain Effect menu

| Chemical reality | Fujifilm setting |
|---|---|
| Large halide crystals (fast/vintage stock) | Grain **Size: LARGE** |
| Fine crystals (slow/pro stock) | Grain **Size: SMALL** |
| Heavy development clumping (pushed film, high ISO) | Grain **Roughness: STRONG** |
| Gentle clumping (box speed, fine developer) | Grain **Roughness: WEAK** |
| Grain rises with ISO (bigger effective crystals needed) | Shoot **higher ISO** for a naturally grainier result |

See [grain-and-detail.md](grain-and-detail.md) for how recipes pair these settings, and the ACROS grain-simulation section of [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md) for why Fujifilm's grain is structurally different from Photoshop grain overlays.

---

## Sepia: chemistry, not aesthetics

Sepia toning replaced the metallic silver particles in a print with silver sulfide (Ag₂S). The warm brown cast was a side effect; the purpose was archival. Silver sulfide is far more resistant to environmental sulfur, the dominant pollutant of the coal-burning Industrial Revolution, and it sidestepped fading from incompletely fixed or washed prints. Sepia's association with "old photos" exists because the chemistry made it near-ubiquitous for formal portraits of that era. The SEPIA film simulation models the result of that chemical substitution.

---

## From B&W chemistry to colour film

Colour film stacks multiple emulsion layers (9 or more, including filters and interlayers), each sensitised to a different band of the spectrum, each developing into a different dye (cyan, magenta or yellow) rather than metallic silver. Every layer has its own spectral sensitivity curve, every dye has its own absorption curve, and the interactions between them are what give each colour stock its signature. That story, and why it cannot be reproduced with image-editor sliders, is covered in [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md).

---

*Last updated: 2026-07-17*
