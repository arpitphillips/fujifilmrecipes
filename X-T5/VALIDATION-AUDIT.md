# Datasheet Validation Audit — 2026-07-15

Every recipe with a corresponding manufacturer datasheet in [`_reference-sources/datasheets/`](_reference-sources/datasheets/README.md) checked against that sheet's objective data (granularity, contrast/tone scale, colour balance, latitude, speed). Method per [validation-methodology](../Knowledge/validation-methodology.md). **No recipe settings were changed in this audit** — findings and proposals only.

**Verdicts:** ✅ consistent with datasheet · ⚠️ deviation (explained or flaggable) · 📋 datasheet not applicable / no sheet

---

## Originals (the product) — all pass

| Recipe | Datasheet | Verdict | Key checks |
|---|---|---|---|
| [kodak-gold-200](originals/kodak-gold-200/) | gold-200_e7022 | ✅ | "Outstanding colour saturation, fine grain, high sharpness; latitude −2/+3 stops" → Color +3 ✓, Grain Strong/**Small** ✓ (visible consumer grain, fine structure), EC +2/3…+1 exploits the overexposure latitude ✓. Recipe was *derived from this sheet* and scan-validated; still holds. |
| [fujicolor-superia-400](originals/fujicolor-superia-400/) | fujicolor-superia-xtra-400 | ✅ | Sheet: fine grain, excellent sharpness, "naturally depicted skin," neutral balance → Grain Weak/Small ✓, Sharpness 0 ✓, whisper-cool WB −1R/+1B ✓ consistent with Superia's cool consumer palette. |
| [cinema/kodak-vision3-250d](originals/cinema/kodak-vision3-250d/) | vision3-250d-5207 | ✅ | Sheet: daylight 5500K balance, **2 stops extended highlight latitude**, reduced shadow grain → Daylight WB ✓, DR400 + Highlight −2 ✓ (direct model of the extended shoulder), Shadow 0 (open shadows) ✓. |
| [cinema/kodak-vision3-500t](originals/cinema/kodak-vision3-500t/) | vision3-500t-5219 | ✅ | Sheet: tungsten **3200K** balance, EI 500, 2-stop highlight latitude → Incandescent WB ✓, DR400 + Highlight −2 ✓, ISO to 12800 appropriate for a 500-speed night stock ✓. |
| [cinema/kodak-2383-print](originals/cinema/kodak-2383-print/) | vision-print-2383-3383 | ✅ | Sheet: "rich blacks and more neutral highlights," high print-stock contrast → Shadow +2 (rich blacks) ✓, Highlight 0 (controlled, neutral highlights) ✓, added saturation vs negative stock ✓. |
| [b&w/fujifilm-acros-100](originals/black-and-white/fujifilm-acros-100/) | neopan-acros-100 | ✅ | RMS 7 (finest of any 100-speed B&W, per prior extraction) → Grain Weak/Small ✓, ISO cap 3200 preserves the clean look ✓, Clarity 0 ✓ (smooth stock). |
| [b&w/ilford-hp5-plus-400](originals/black-and-white/ilford-hp5-plus-400/) | hp5-plus | ✅ | Sheet: best at EI 400, good to **EI 3200** with push development, medium contrast → Strong/Small grain ✓ (prominent but even), Highlight 0/Shadow +2 medium-contrast-with-deep-shadows ✓, ISO to 12800 mirrors push tolerance ✓. |
| [b&w/kodak-tri-x-400](originals/black-and-white/kodak-tri-x-400/) | tri-x-320-400_f4017 | ✅ with documented intent | Sheet aims at contrast index **0.56** (moderate!) with "brilliant highlights" — box-speed Tri-X is *less* contrasty than its reputation. The recipe deliberately targets the **pushed reportage look** (H+1/S+2, Clarity +3, Strong/Large) and documents this. Faithful to Tri-X *as commonly shot*, not to box-speed processing — already stated in its knowledge.md ✓. |

**Mumbai / Mumbai Monsoon / all creative looks:** 📋 original designs, no film target — datasheet validation not applicable.

---

## Reference recipes — checks & flags

These are **attributed captures** — per methodology they stay as-published for benchmarking; deviations are flagged here, not edited into them.

| Recipe | Datasheet | Verdict | Finding |
|---|---|---|---|
| [provia-positive](reference-recipes/provia-positive/) | provia-100f | ⚠️ deliberate | Sheet: **RMS 8**, "vivid *and faithful*, well-balanced gradation." Grain **Strong**/Small overstates an RMS-8 film — but the author explicitly targets *aged vintage slides*, not fresh Provia (documented in recipe). Color +4 pushes past "faithful" toward the vintage look. Fine as a reference; a *faithful fresh Provia* original would use Grain Weak/Small, Color +2. |
| [vivid-velvia](reference-recipes/vivid-velvia/) | velvia-50 | ✅ | Sheet: highest saturation class, superb granularity, vivid-but-fine → Grain Weak/Small ✓, Color +4 ✓. H−1/S−1 tames the Velvia sim's already-hard S-curve rather than doubling it — consistent. |
| [thommys-ektachrome](reference-recipes/thommys-ektachrome/) | ektachrome-e100_e4000 | ⚠️ | Sheet: RMS 8 ✓ (Grain Weak/Small ✓), neutral-to-cool balance ✓ (WB −1R/+3B ✓), **but "low contrast tone scale"** vs recipe **H+1.5/S+1.5** on Nostalgic Neg. The recipe reads contrastier than the film's spec; it emulates the *printed NatGeo page*, not the transparency. Keep as reference; a datasheet-faithful E100 original would run H0/S0 or lower. |
| [kodachrome-64](reference-recipes/kodachrome-64/) | kodachrome-25-64-200_e55 | ✅ | Sheet: K64 **RMS 10** → Grain Weak/Small ✓; moderate saturation/contrast → Color +2, H0/S+0.5 ✓. (K25 = RMS 9, K200 = RMS 16 — future recipes should scale grain accordingly.) |
| [vintage-kodachrome](reference-recipes/vintage-kodachrome/) | (E-55 K-14 era) | 📋 | Targets 1935–60 first-era Kodachrome; the E-55 sheet covers the later K-14 films — not directly applicable. Underexposure convention & painterly high-contrast are consistent with period accounts. |
| [kodak-portra-160-v2](reference-recipes/kodak-portra-160-v2/) | portra-160_e4051 | ✅ | Sheet: "significantly finer grain," neutral skin, optimized sharpness → Grain Weak/Small ✓, Color 0 ✓, DR-P Auto low-contrast ✓. Strongest datasheet match of the Portra set. |
| [kodak-portra-400-v2](reference-recipes/kodak-portra-400-v2/) | portra-400_e4050 | ⚠️ minor | Sheet: "**world's finest grain** high-speed film" → Grain **Strong**/Small slightly overstates (Weak/Small would match the spec; Strong matches *scanned* Portra as commonly seen). Low-contrast S−2 ✓, warm 5200K/−6B ✓. |
| [kodak-portra-800-v3](reference-recipes/kodak-portra-800-v3/) | portra-800_e4040 | ⚠️ minor | Sheet: "very fine grain, best-in-class underexposure latitude" → Grain Strong/**Large** overstates the spec (Large reads as a 1600-3200 stock). H−2 soft highlights ✓, warm 6600K ✓. |
| [kodak-ultramax-400](reference-recipes/kodak-ultramax-400/) | ultramax-400_e7023 | ⚠️ minor | Sheet: "excellent sharpness and **fine grain**" (T-GRAIN) → Grain Strong/**Large** + Clarity +3 renders it grittier/punchier than spec; consistent with the *drugstore print* memory, not the emulsion. |
| [ilford-fp4-plus-125](reference-recipes/ilford-fp4-plus-125/) | fp4-plus | ⚠️ minor | Sheet: "**exceptionally fine grain**," EI 50–200 range → Grain Weak/**Large** contradicts "fine" on size (Weak/Small would match). Negative-EC convention ✓ (sheet: best at 125, latitude tight above EI 200 — protecting highlights is right). |
| [kodak-t-max-p3200](reference-recipes/kodak-t-max-p3200/) | t-max-p3200_f4001 | ✅ | Sheet: **nominal EI 800–1000**, push-designed to 3200–6400, better shadow separation than pushed 400 stocks → recipe's ISO-as-creative-control (640 ≈ unpushed, 3200–12800 ≈ pushed) mirrors the sheet's push table precisely ✓. Strong/Large grain, H+1/S+3 ✓ for pushed rendering. |
| [cinestill-800t](reference-recipes/cinestill-800t/) | vision3-500t-5219 (same emulsion) | ✅ stylised | 800T = 5219 minus remjet. Recipe's deviations from our clean 500T original (Fluorescent WB, Strong/Large grain, Clarity −5 glow, Color +4) all model the *remjet-removal* consequences (halation, one-stop push, scan saturation) — the split is deliberate and documented in both files ✓. |
| [reala-ace](reference-recipes/reala-ace/) + [fujifilm-negative](reference-recipes/fujifilm-negative/) | fujicolor-superia-reala | ✅ | Sheet: "superb granularity, **soft gradations**," 4th-layer colour accuracy → Grain Weak/Small ✓, soft tone curves (H−1.5/S−2 and H−1/S−0.5) ✓, moderate Color +2 ✓. |
| [reggies-portra](reference-recipes/reggies-portra/) | portra-400_e4050 | 📋 | An *interpretation* of the Portra palette, not an emulation (author's framing) — datasheet conformity not its goal. Soft H−1/S−1 + warm AWB are directionally Portra ✓. |
| [kodak-tri-x-400 (reference)](reference-recipes/kodak-tri-x-400/) | f4017 | 📋 | Superseded by the B&W original; not re-audited. |
| [acros-red-high-contrast](reference-recipes/acros-red-high-contrast/) | neopan-acros-100 | 📋 | Creative filter look (Acros+R, H+3/S+4) — deliberately departs from the Acros stock; not a film emulation. |
| fujicolor-super-hg-v2, luis-costa, pacific-blues, california-summer, 1976-kodak | — | 📋 | No datasheet exists / no specific film target. |

---

## Cross-cutting observations

1. **The originals hold up.** All 8 film-based originals are consistent with their sheets — expected, since they were derived from them, but now re-verified against the archived PDFs.
2. **A recurring, legitimate tension:** datasheets describe the *emulsion*; several reference recipes emulate the *artifact people remember* (drugstore prints, aged slides, pushed rolls, magazine pages). UltraMax, Provia Positive, Thommy's Ektachrome and Portra 400/800 v2/v3 all sit on the "memory" side. This mirrors Fujifilm's own memory-colour philosophy ([color-science](../Knowledge/color-science-why-film-cannot-be-faked.md)) — but for *sellable originals* the bank should state which target each recipe aims at: **emulsion-faithful** or **artifact-faithful**.
3. **Grain-size language now has datasheet anchors:** RMS 7 (Acros) → Weak/Small … RMS 8–10 (Provia, E100, K64, Velvia) → Weak/Small … consumer 200–400 (Gold, UltraMax, Superia) → Strong/Small … pushed/1600+ (P3200, Natura, K200 RMS 16) → Strong/Large. FP4's Weak/Large is the one combination no datasheet supports.
4. **Kodachrome grain scaling:** E-55 gives RMS 9/10/16 for K25/K64/K200 — a ready-made ladder for future Kodachrome-era recipes.

## Actions taken (approved by user 2026-07-15)

**A. ✅ Done** — "Datasheet check (2026-07-15)" notes added to all six flagged reference recipes (provia-positive, thommys-ektachrome, portra-400-v2, portra-800-v3, ultramax-400, fp4-plus-125).

**B. ✅ Done** — two datasheet-faithful originals derived (settings built from the archived sheets, curve pages read visually):
   1. [originals/kodak-ektachrome-e100](originals/kodak-ektachrome-e100/) — Provia base, Weak/Small grain (RMS 8), cool-neutral WB, H−1/S−0.5 (low-contrast tone scale per E-4000).
   2. [originals/kodak-portra-400](originals/kodak-portra-400/) — Classic Chrome base, Weak/Small grain (PGI 37@4×6), warm-neutral fixed WB, DR400 + H−1.5 (latitude/shoulder per E-4050).
   Both marked **scan-validation pending**; the existing reference recipes remain untouched as benchmarks.

**C. ✅ Done** — validation ledger updated: datasheet tier for all film-based originals marked archive-PDF-verified; two new ledger rows added.

*Audit performed against the 46-PDF datasheet archive; extraction via pypdf, key pages spot-checked. Author: Claude session, 2026-07-15.*
