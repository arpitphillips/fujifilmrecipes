# Vintage Kodachrome — Fujifilm X-T5 (X-Trans V) · STILLS

**Status:** Reference recipe **translated by us** from an X-Trans III original → X-T5, as a worked example of older-model→X-T5 porting.
**Original source/credit:** [Fuji X Weekly (Ritchie Roesch), X100F / X-Trans III](https://fujixweekly.com/2017/10/21/my-fujifilm-x100f-vintage-kodachrome-film-simulation-recipe/)

Emulates the **1935–1960 (first-era) Kodachrome** slide look: cyan-leaning blues, darkened reds, and bronze/orange skin — an old, painterly transparency aesthetic. Classic Chrome base. Translation reasoning in [`knowledge.md`](knowledge.md).

## X-T5 (X-Trans V): translated
| Setting | Value | Note |
|---|---|---|
| Film Simulation | Classic Chrome | direct |
| Grain Effect | Strong, **Large** | III has no Grain *Size*; **Large** chosen for the coarse vintage look |
| Color Chrome Effect | **Off** | III (X100F) had no CCE; kept Off to preserve the original rendering (try **Weak** for more depth) |
| Color Chrome FX Blue | **Off** | III had none; Off is the floor — see caveat below |
| White Balance | Auto, +2 Red & −4 Blue | direct (AWB differs slightly on V — see caveat) |
| Dynamic Range | DR200 | direct |
| Highlight | +4 | direct (Tone Curve range −2…+4 unchanged) |
| Shadow | −2 | direct |
| Color | +4 | direct |
| Sharpness | +1 | direct |
| High ISO NR | −3 | direct (or −4 to match house default) |
| Clarity | **0** | III had none; kept neutral for faithfulness |
| ISO | Auto, up to ISO 6400 | direct |
| Exposure Compensation | −1/3 to −1 (typically) | direct — note this recipe *underexposes* for richness |

## Original X-Trans III settings (for reference)
Classic Chrome · DR200 · Highlight +4 · Shadow −2 · Color +4 · Sharpening +1 · Noise Reduction −3 · Grain Strong · WB Auto +2R/−4B · ISO Auto 6400 · Exp −1/3 to −1.

> Two translation **caveats** (concrete evidence, not assumption):
> 1. **Blues will render slightly deeper on X-T5.** X-Trans V deepens Classic Chrome blues, and Color Chrome FX Blue can't go below Off — so the V result is a touch more saturated in the blues than the original III look. Unavoidable.
> 2. **Auto WB differs.** X-Trans V uses a newer AI AWB; if the cast drifts from the original, substitute a fixed WB (~5500K, +2R/−4B) to lock it.
