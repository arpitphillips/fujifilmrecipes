# Thommy's Ektachrome — Fujifilm X-T5 (X-Trans V)

Nostalgic Neg. base. Emulates Kodak Ektachrome slide film, specifically the look of National Geographic photographs from before Ektachrome's 2013 discontinuation (pre-2018 revival). Created by Thomas Schwab, who was originally just building a portrait recipe on Nostalgic Neg. and landed on this aesthetic. Fills the bank's Ektachrome gap.

[Source](https://fujixweekly.com/2023/03/24/thommys-ektachrome-fujifilm-x-t5-x-trans-v-film-simulation-recipe/)

| Setting | Value |
|---|---|
| Film Simulation | Nostalgic Neg. |
| Grain Effect | Weak, Small |
| Color Chrome Effect | Weak |
| Color Chrome FX Blue | Off |
| White Balance | 5000K, -1 Red & +3 Blue |
| Dynamic Range | DR100 |
| Highlight | +1.5 |
| Shadow | +1.5 |
| Color | +1 |
| Sharpness | -1 |
| High ISO NR | -4 |
| Clarity | -2 |
| ISO | Auto, up to ISO 6400 |
| Exposure Comp | 0 to +1/3 (typically) |

Notes
- Good for portraits *and* landscapes; strongest in sunny daylight, acceptable in overcast/shade/indoor natural light.
- Requires Nostalgic Neg. → X-Trans V only (no IV port possible).

> **Datasheet check (2026-07-15):** Kodak E-4000 specifies a "low contrast tone scale" for E100, H+1.5/S+1.5 renders contrastier than the transparency itself. This recipe emulates the *printed NatGeo page*, not the film. Grain Weak/Small (matching the RMS 8 figure) and the cool-neutral WB do match the sheet. See [VALIDATION-AUDIT.md](../../VALIDATION-AUDIT.md); a datasheet-faithful original lives at [originals/kodak-ektachrome-e100](../../originals/kodak-ektachrome-e100/).

> **Official design note:** Fujifilm's Nostalgic Neg. page confirms the sim's amber warmth is anchored in the shadows, where negative film normally goes cool, and "does not change easily when adjusted via white balance alone". Don't try to cool this recipe via WB shifts; if you need neutral shadows, switch base sims instead. The flip side: portraits in shadow are a native strength of this base, since skin keeps its richness in shade. See [fujifilm-official-design-notes](../../../Knowledge/fujifilm-official-design-notes.md).
