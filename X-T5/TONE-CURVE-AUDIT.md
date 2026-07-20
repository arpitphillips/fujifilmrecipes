# Tone-curve audit: every recipe vs its base simulation's native curve

**Date:** 2026-07-20 · Basis: Fujifilm's own published curve shapes ([official design notes](../Knowledge/fujifilm-official-design-notes.md), [per-sim curve table](../Knowledge/dynamic-range-and-tone.md))

---

## The principle being tested

Highlight and Shadow values are relative to the base simulation, not absolute. Each base already has a shape:

| Base | Highlight end | Shadow end |
|---|---|---|
| **Classic Chrome** | soft | **hard** |
| **Velvia** | hard | hard |
| **Astia** | soft | soft |
| **Pro Neg. Hi** | — | contrast-boosting ("creates shadows even in flat light") |
| **Eterna** | flat/soft | flat/soft |
| **Acros** | harder compression | **softer** |
| **Monochrome** | (shares Provia's design) | (shares Provia's design) |

So a setting either pushes against the base (buying back what the sim removes) or stacks with it (amplifying what the sim already does). Neither is wrong, but stacking is where mush and crushed blacks come from, and it should always be deliberate.

> **⚠️ Evidence outranks theory.** Where a recipe is scan-validated against real film, the scans win. This audit flags *tension worth understanding*, not errors to auto-correct. Nothing below was changed on the strength of theory alone.

---

## Recipes that push *against* their base: working as intended

| Recipe | Base | H / S | Why it's right |
|---|---|---|---|
| [kodak-portra-400](originals/kodak-portra-400/) | Classic Chrome | −1.5 / **−1** | Shadow −1 buys back detail the hard shadow end crushes. Textbook. |
| [kodak-portra-400-v2](reference-recipes/kodak-portra-400-v2/) | Classic Chrome | 0 / **−2** | Strong shadow lift against a hard shadow end — why it stays open. |
| [fujicolor-pro-400h](originals/fujicolor-pro-400h/) | Pro Neg. Hi | −2 / −1 | Deliberately damping the base's contrast boost. Correct for a flat pastel stock. |
| [kodak-ektar-100](originals/kodak-ektar-100/) | Velvia | −1 / 0 | Softening a hard highlight end — needed, since Velvia at 0/0 is already high-contrast. |
| [kodachrome-25](reference-recipes/kodachrome-25/) | Classic Chrome | +0.5 / −0.5 | Pushes against *both* ends. Unusually well-shaped for a reference recipe. |
| [kodak-ultramax-400](reference-recipes/kodak-ultramax-400/) | Classic Chrome | **+1** / +1 | Highlight +1 reclaims contrast the soft top end gives away. |
| All Acros B&W (HP5, Delta 3200, Tri-X, Pan F) | Acros | 0/+1 → +1/+2 | Shadow-positive works *with* Acros's natively **soft** shadow end — which is exactly why these hold texture where Monochrome would crush. Correct by design. |

---

## Recipes that stack *with* their base: deliberate, but know the risk

| Recipe | Base | H / S | What's stacking | Verdict |
|---|---|---|---|---|
| [pastel-dream](originals/creative/pastel-dream/) | Astia | **−2 / −2** | Soft-both-ends settings on a soft-both-ends base — the most stacked recipe in the bank | **Intentional** — this *is* the pastel look. But it has no reserve: any real depth must come from DR/Shadow, and it will read mushy in flat light. |
| [matte-editorial](originals/creative/matte-editorial/) | Eterna | −2 / −2 | Maximum flatness on the flattest base | **Intentional** — matte is the product. |
| [golden-hour-glow](originals/creative/golden-hour-glow/) | Astia | **−2** / −1 | Highlight softening on an already-soft top end | Watch it — glow can tip into milky. Try −1 if highlights lack shape. |
| [cinestill-400d-v2](reference-recipes/cinestill-400d-v2/) | Astia | −2 / 0 | Same stack, highlight end | Reference recipe, unmodified. |
| [bewaremyvelvia-bold](originals/creative/bewaremyvelvia-bold/) | Velvia | 0 / **+2** | Hard shadows on Velvia's already-hard shadow end | **Intentional** — "bold" is the brief. Expect genuinely crushed blacks; expose for the shadows. |
| [fashion-editorial-vogue](originals/creative/fashion-editorial-vogue/) | Pro Neg. Hi | 0 / +2 | Contrast on a contrast-boosting base | **Intentional** — punchy editorial. Note Pro Neg. **Std** is the officially-intended studio base (see recipe). |
| [kodak-portra-800-v3](reference-recipes/kodak-portra-800-v3/) | Classic Chrome | **−2** / −0.5 | Highlight softening on a soft top end | Flagged in-recipe: highlights can read milky. Raise Highlight a step first. |
| [ross-sherbet-lemon](reference-recipes/ross-sherbet-lemon/) | Velvia | −1.5 / +1.5 | Softening Velvia's hard highlight end (buys detail) while hardening its already-hard shadow end | **Intentional** — Highlight −1.5 pushes against the base, Shadow +1.5 stacks with it. Expect deep, crushed blacks; the soft-highlight/crushed-shadow split is the "sherbet" signature. Flagged in-recipe. |
| Vision3 [50D](originals/cinema/kodak-vision3-50d/) / [250D](originals/cinema/kodak-vision3-250d/) / [500T](originals/cinema/kodak-vision3-500t/) | Eterna | −2 / 0…+1 | Highlight softening on an already-flat base | **Intentional** — these emulate *ungraded* negative stock, which is genuinely this flat. Eterna is officially "weak as stills… by design." |

---

## The one genuine tension worth naming

**[kodak-gold-200](originals/kodak-gold-200/), Classic Chrome, H −2 / S +0.5.**

On theory this stacks at *both* ends: −2 softens an already-soft highlight end, +0.5 hardens an already-hard shadow end. Theory would predict milky highlights and crushed blacks.

**The recipe stands unchanged**, because it is the most heavily validated in the bank, refined against ~35 real Gold 200 scans across all lighting conditions, and the WB and Clarity values were already revised once on scan evidence. Gold 200 genuinely *is* a soft-highlight, contrasty-shadow film, so the settings are reproducing the emulsion rather than fighting the sim.

This is worth recording precisely because it demonstrates the hierarchy: datasheet + scans > engineering theory > intuition. The curve table predicts where to look; it does not overrule evidence.

---

## Not audited

- [kodak-portra-160-v2](reference-recipes/kodak-portra-160-v2/), Highlight/Shadow are locked by D-Range Priority, so the curve table doesn't apply.
- Recipes without an explicit tone row in the table format (a handful of creative entries carry tone inline in prose).

---

## Actions taken

- Nothing was changed on theory alone. Recipes received in-file pro-notes explaining the stack and the first fix to try ([portra-800-v3](reference-recipes/kodak-portra-800-v3/), [ross-sherbet-lemon](reference-recipes/ross-sherbet-lemon/), [bewaremyvelvia-bold](originals/creative/bewaremyvelvia-bold/), plus the Classic Chrome asymmetry note carried on the flagship originals).
- The per-sim curve table is now the reference for any *new* recipe: check the base's native shape before choosing Highlight/Shadow.

*Last updated: 2026-07-20*
