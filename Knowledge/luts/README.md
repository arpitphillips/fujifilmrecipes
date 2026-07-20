# F-Log / F-Log2 → Rec.709 conversion LUTs

Two ready-to-use 33³ `.cube` LUTs, generated from Fujifilm's official published transfer functions:

| File | Use with |
|---|---|
| [`FLog_to_Rec709.cube`](FLog_to_Rec709.cube) | Footage shot in **F-Log** |
| [`FLog2_to_Rec709.cube`](FLog2_to_Rec709.cube) | Footage shot in **F-Log2** |

Regenerate or tweak with [`make-flog-luts.ps1`](make-flog-luts.ps1):
```
powershell -ExecutionPolicy Bypass -File make-flog-luts.ps1
```

---

## What's exact, and what's a judgement call

Be clear about which parts of a conversion LUT are *physics* and which are *taste*. In this one:

| Stage | Source | Status |
|---|---|---|
| 1. Log → scene-linear | Fujifilm datasheets ([F-Log Ver.1.2](https://dl.fujifilm-x.com/technical-data/F-Log_DataSheet_E_Ver.1.2.pdf), [F-Log2 Ver.1.1](https://dl.fujifilm-x.com/technical-data/F-Log2_DataSheet_E_Ver.1.1.pdf)), section 2-3 | ✅ **Exact** — official constants, verbatim |
| 2. F-Gamut → Rec.709 | Standard BT.2020→BT.709 matrix, D65 | ✅ Exact *(assumes F-Gamut = BT.2020 primaries — see caveat)* |
| 3. Scene-linear → display | Extended-Reinhard shoulder, W = 8, 18% grey preserved | ⚠️ **My choice** — the one creative step |
| 4. Rec.709 OETF | ITU-R BT.709 | ✅ Exact |

**Official constants used** (from the datasheets, not from memory or a third-party page):

```
F-Log   a=0.555556  b=0.009468  c=0.344676  d=0.790453  e=8.735631  f=0.092864  cut2=0.100537775223865
F-Log2  a=5.555556  b=0.064829  c=0.245281  d=0.384316  e=8.799461  f=0.092864  cut2=0.100686685370811
```

Decode (datasheet, "log → scene linear reflection"):
```
out = (10^((in - d) / c)) / a - b / a     ( in >= cut2 )
out = (in - f) / e                        ( in <  cut2 )
```

> Worth noting: a web search returned `a = 0.555556` for F-Log2. That is wrong, it's F-Log's value. The official PDF gives 5.555556. Constants here were taken from the PDFs directly for exactly this reason.

---

## Verification

Checked against the anchor points Fujifilm publishes in the datasheet (F-Log2, section 2-2):

| Input reflection | Datasheet 10-bit code | LUT input | LUT output | Expected |
|---|---|---|---|---|
| 0 % | 95 | 0.0929 | **0.0005** | ~0 (black) ✅ |
| 18 % | 400 | 0.3910 | **0.4093** | 0.4090 ✅ |
| 90 % | 570 | 0.5572 | 0.7275 | see below |

- 18% grey lands within 0.0003 of the Rec.709 target. Exposure is correct, a properly-exposed grey card comes out as a properly-exposed grey card.
- Black point is right: the LUT reaches zero at input ≈0.093, precisely the datasheet's code value 95 for 0% reflection.
- 90% white sits at 0.73, not 0.95: this is the tone-map shoulder doing its job, not an error. Fujifilm's log holds ~8 stops above grey; a straight linear→709 mapping would clip all of it. The shoulder trades a slightly darker diffuse white for highlights that roll instead of clipping.

**Want brighter whites?** Raise `$W` / `W = 8.0` in the script (try 12–16) for a gentler shoulder and a higher diffuse white. Lower it (4–6) for a stronger filmic rolloff. Grey stays at 18% either way, the script re-solves the gain automatically.

---

## How to use

**DaVinci Resolve**
1. Copy the `.cube` files to `%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\LUT\` (or *Project Settings → Color Management → Open LUT Folder*), then Update Lists.
2. Colour node tree: `Balance/Exposure → [LUT node] → Look → Grain`.
3. Right-click a node → *LUTs* → pick the file. **Correct exposure and WB on a node *before* the LUT**, never after.

**Premiere Pro**
- Lumetri → *Basic Correction* → Input LUT → Browse. Grade in the panels *below* it.
- Do not load it under *Creative → Look*, that applies it after your corrections, which is the wrong order.

**Important:** match your DATA LEVEL SETTING on the camera (p.195) to your NLE's interpretation. A range mismatch crushes blacks and clips highlights before the LUT even runs, and is routinely misdiagnosed as bad exposure. See [flog-and-raw-workflow.md](../flog-and-raw-workflow.md).

---

## Caveats

- F-Gamut primaries are assumed to be BT.2020. The datasheet names the gamut "F-Gamut" and shows it plotted against BT.709/DCI-P3/ACES, but the primary coordinates are in a figure rather than machine-readable text, so I could not extract them. BT.2020 is the widely-documented equivalence and the plot is consistent with it, but it is an assumption, not something I verified from the PDF.
- Fujifilm publishes its own official LUTs at [dl.fujifilm-x.com](https://dl.fujifilm-x.com/) (support → LUT). If you want a vendor-blessed conversion, use theirs. These exist so you have a transparent, adjustable, documented alternative, and so the maths is in the repo rather than in a black box.
- These are technical conversions, not looks. They normalise log footage to Rec.709. The film look comes afterwards, from the grade, or from shooting the [cinema recipes](../../X-T5/originals/cinema/) in the first place.
- 33³ is the standard resolution and is plenty for a smooth transform. Raise `$N` in the script if you want 65³.

*Last updated: 2026-07-20*
