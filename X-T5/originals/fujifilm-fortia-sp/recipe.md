# Fujichrome Fortia SP — Fujifilm X-T5 (X-Trans V) · STILLS

Fujifilm's most saturated emulsion ever made, a Japan-only ISO 50 reversal film (2004–2007) that out-punched Velvia 50. Built for cherry blossom and autumn foliage, and gloriously unusable for anything else. Grade rationale in [`knowledge.md`](knowledge.md).

> ### ⚠️ Read this before shooting it
> **This is the least-evidenced recipe in the bank.** Fortia SP was a limited Japan-only run, discontinued in 2007; no manufacturer datasheet and no genuine film scans could be located on open sources (a Wikimedia search returns only *Fortià*, a Catalan town). It is characteristic-validated only, it does not meet the [promotion bar](../../../Knowledge/validation-methodology.md) for a flagship original, and is filed here because the derivation is ours, not because the evidence is strong.
>
> **What makes it more than guesswork:** Fujifilm states that Color Chrome Effect itself was developed from Fortia, *"to replicate its higher contrast and more vivid colour while maintaining tonality."* So this recipe isn't reverse-engineered from memory; it's built by driving Fujifilm's own Fortia model at strength. That is an unusually direct derivation path. ([official design notes](../../../Knowledge/fujifilm-official-design-notes.md))
>
> Real scans would settle it, drop any into [`references/`](references/).

| Setting | Value |
|---|---|
| Film Simulation | **Velvia / VIVID** |
| Grain Effect | **Off** |
| **Color Chrome Effect** | **Strong** |
| Color Chrome FX Blue | Weak |
| White Balance | **Daylight, +2 Red / −1 Blue** |
| Dynamic Range | **DR100** |
| Tone Curve — Highlight | **0** |
| Tone Curve — Shadow | **0** |
| Color | **+1** |
| Sharpness | **+2** |
| High ISO NR | −4 |
| **Clarity** | **0** |
| ISO | Auto, **125–1600** |
| Exposure Compensation | **−1/3 to −2/3** (see notes) |

### Notes

- Velvia base + Color Chrome Effect Strong deliberately breaks the bank's own rule. [The guidance elsewhere](../../README.md) is *never stack CCE on Velvia*, Velvia applies a uniform saturation gain, CCE runs a gradation-recovery pass on already-saturated colour, and together they go plastic. This is the one recipe where that is the point. Fortia was Fujifilm's deliberate over-saturation extreme, and CCE is Fujifilm's own model of it. Expect it to look absurd on the wrong subject, so did the real film.
- Color only +1. With Velvia and CCE Strong already stacked, pushing Color hard would take the frame past where gradation survives. The saturation is coming from the base and the chrome effect; +1 is the nudge that lands it "beyond Velvia" without collapsing colour into flat patches.
- DR100 is a faithfulness choice, not an oversight. Reversal film has famously narrow latitude (~5 stops) and clips highlights hard. DR200/400 would roll them gently, which is exactly what slide film does *not* do. If you blow a highlight on this recipe, that's correct behaviour.
- Highlight 0 / Shadow 0 is already high-contrast. Velvia is officially hard at *both* ends of the curve, so neutral values here sit near the top of the contrast ladder. Do not add positive values; see [TONE-CURVE-AUDIT.md](../../TONE-CURVE-AUDIT.md).
- WB +2R/−1B: Fortia SP was explicitly warmer than the original Fortia. Fixed Daylight, not Auto: this is a colour-critical slide emulation and needs to be repeatable.
- Expose down. The real film was rated ISO 50 but commonly shot at ISO 64, mild underexposure, the standard slide-film trick to deepen saturation and protect highlights. EC −1/3 to −2/3 reproduces it.
- Grain Off, Sharpness +2: ISO 50 reversal film is very fine-grained and crisp.
- ISO capped at 1600 honours the slow-film character, as with [Kodachrome 25](../../reference-recipes/kodachrome-25/recipe.md).
- HEIF-safe and fast-saving (Clarity 0).

### Best use

**Cherry blossom, autumn foliage, flower fields, festival colour, painted architecture, sunsets.** This is a specialist, not a daily driver, exactly as the real film was marketed in Japan.

**Avoid:** portraits (skin goes lurid), overcast/muted scenes (nothing for CCE to work on; see [colour & chrome](../../../Knowledge/color-and-chrome.md)), and anything where subtlety matters. For restrained landscape use [Ektar 100](../kodak-ektar-100/recipe.md); for a strong-but-sane Velvia look use [BewareMyVelvia Bold](../creative/bewaremyvelvia-bold/recipe.md).

### Movie mode

Movie mode has no Grain, no Color Chrome Effect and no Clarity, which removes the single control this recipe is built on. A faithful Fortia video look is not achievable in-camera; use Velvia with Color +3 and grade the rest in post. See [video-mode-settings.md](../../../Knowledge/video-mode-settings.md).
