# Fujichrome Fortia SP — grade analysis

## The film

| | |
|---|---|
| **Type** | Colour reversal (slide), daylight-balanced |
| **Speed** | ISO 50 — commonly **rated at ISO 64** in practice |
| **Produced** | Original Fortia 2004 (limited run) · **Fortia SP 2005–2007** |
| **Market** | **Japan only**, limited release |
| **Claim to fame** | **Fujifilm's highest-saturation emulsion** — stronger than Velvia 50 |

Fortia was a deliberate excess. Fujifilm already had Velvia, the most saturated mainstream slide film in the world, and built something *louder*, colour described as "stronger than natural", with warmer rendering in the SP revision than the original. It was aimed squarely at the Japanese landscape market's two obsessions: **cherry blossom (*sakura*) and autumn foliage (*kōyō*)**, subjects where viewers actively want colour beyond reality.

It was never sold as a general-purpose film, and it isn't one. That specificity is the point of the emulation.

## Why this recipe is derived the way it is

Most film emulations in this bank start from a datasheet and real scans. Fortia offers neither, no manufacturer datasheet could be located, and no genuine scans exist on open image sources. Ordinarily that would stop the work.

What rescues it is a first-party fact recovered from [Fujifilm's own development archive](../../../Knowledge/fujifilm-official-design-notes.md):

> **Color Chrome Effect was developed from Fortia**, to replicate its *"higher contrast and more vivid colour"* while maintaining tonality, on the premise that *"one of the characteristics of reversal colour film is that tonality remains even in high contrast range."*

That changes the derivation completely. Rather than guessing at a look from written descriptions, the recipe drives Fujifilm's own Fortia model, the control they built *from* this film, at strength. The emulation runs through the manufacturer's own interpretation of the emulsion.

## Trait → setting

| Observed/documented trait | Setting | Reasoning |
|---|---|---|
| Highest-saturation Fujifilm emulsion, "beyond Velvia" | **Velvia base + Color +1** | Velvia is the most saturated simulation; +1 pushes past it without collapsing gradation |
| Fujifilm's own model of Fortia's colour | **Color Chrome Effect Strong** | The literal, official Fortia model — the single most important setting here |
| Warmer than original Fortia | **WB Daylight +2R / −1B** | Documented SP revision change; fixed WB for repeatable slide emulation |
| Reversal film, ~5-stop latitude, hard highlight clipping | **DR100** | DR200/400 would roll highlights gently — the opposite of slide behaviour |
| Velvia natively hard at both curve ends | **Highlight 0 / Shadow 0** | Neutral here is *already* high-contrast; positive values would crush |
| ISO 50 reversal, very fine grain, crisp | **Grain Off, Sharpness +2** | Slow slide film shows essentially no grain |
| Commonly shot at ISO 64 | **EC −1/3 to −2/3** | Standard slide underexposure — deepens saturation, protects highlights |
| Blue not the signature hue (pink/red/gold were) | **CCFX Blue Weak** | Strong blue would fight the warm, blossom-forward palette |
| Slow film character | **ISO cap 1600** | Consistent with the bank's treatment of slow stocks |

## The deliberate rule-break

This recipe stacks Color Chrome Effect on a Velvia base, which [the bank's own guidance](../../README.md) says never to do. The reasoning behind that rule, Velvia applies a *uniform* saturation gain, CCE runs a gradation-recovery pass on already-saturated colour, and together they push past where gradation survives, is sound and comes from Fujifilm's own documentation.

It is broken here on purpose, because the target look is the over-saturation extreme. Fortia existed to go too far. A "tasteful" Fortia would be a failed emulation.

The mitigation is keeping Color at +1 rather than +3/+4: the saturation comes from the base and the chrome effect, so the Color control doesn't need to pile on. That preserves some tonal separation inside the loud colour, which is precisely what Fujifilm says CCE is *for*.

## Evidence status: honest assessment

| Tier | Status |
|---|---|
| **Datasheet** | ❌ None located. Japan-only limited run; no published technical sheet found. |
| **Characteristic** | ✅ Consistent accounts of ISO 50/64, "stronger than natural" colour, warmer SP revision, highest-saturation Fujifilm emulsion, sakura/kōyō use case. |
| **Scan (pixel)** | ❌ **None.** No genuine Fortia scans found on open sources. |
| **First-party derivation** | ✅ **Unusually strong** — Fujifilm's own Color Chrome Effect is documented as a Fortia model. |

**Verdict:** this is a *plausible, well-reasoned* emulation with a strong derivation path and no pixel evidence. It should not be sold as a validated original until real scans confirm it. The most valuable thing anyone can do for this recipe is put a genuine Fortia scan in [`references/`](references/), Japanese photo blogs, Flickr, and 2000s slide-scan archives are the likely places.

## Related
- [BewareMyVelvia (Bold)](../creative/bewaremyvelvia-bold/recipe.md), strong Velvia without the CCE stack; the sane alternative
- [Kodak Ektar 100](../kodak-ektar-100/recipe.md), vivid but restrained; the opposite philosophy
- [Colour & chrome effects](../../../Knowledge/color-and-chrome.md), what CCE actually does and why it's a tonality tool
- [Tone-curve audit](../../TONE-CURVE-AUDIT.md), why Highlight/Shadow sit at 0 on a Velvia base
