# Film Stocks Master List — the Canon of Top Stocks & Recipe Coverage

The reference canon of the most important film stocks per manufacturer, with this bank's coverage status. Use this to decide what to emulate next.

> **Datasheets:** official technical datasheets for nearly every stock below (46 PDFs — characteristic curves, spectral sensitivity, granularity) are archived in [`X-T5/_reference-sources/datasheets/`](../X-T5/_reference-sources/datasheets/README.md), organised by manufacturer. Gaps are listed in that folder's README.

**Coverage legend:**
- ✅ **original** — validated/research-derived recipe in `X-T5/originals/`
- 📗 **reference** — attributed recipe in `X-T5/reference-recipes/`
- 🔎 **available** — a known X-Trans V recipe exists (Fuji X Weekly unless noted) but isn't in the bank yet
- 🔶 **IV-only** — only an X-Trans IV recipe exists; needs porting (raise CCFXB one notch — see [x-trans-v-and-conversion.md](x-trans-v-and-conversion.md))
- ❌ **gap** — no known faithful recipe; original-derivation candidate

---

## Fujifilm

| Stock | Type | ISO | Signature look | Coverage |
|---|---|---|---|---|
| **Velvia 50** | Slide | 50 | Extreme saturation, royal-blue skies, landscape king (1991) | 📗 [vivid-velvia](../X-T5/reference-recipes/vivid-velvia/) |
| **Provia 100F** | Slide | 100 | Balanced pro slide standard | 📗 [provia-positive](../X-T5/reference-recipes/provia-positive/) |
| **Astia 100F** | Slide | 100 | Soft skin-optimised slide (discont. 2012) | 🔶 (FXW Astia recipes are IV-era) |
| **Pro 400H** | C-neg | 400 | Cool cyan-green pastel, wedding classic (discont. 2021) | ✅ [fujicolor-pro-400h](../X-T5/originals/fujicolor-pro-400h/) |
| **Superia X-TRA 400** | C-neg | 400 | The green-leaning consumer "Fuji look" | ✅ [fujicolor-superia-400](../X-T5/originals/fujicolor-superia-400/) |
| **Superia 100** | C-neg | 100 | Basis of Classic Neg. itself | 🔎 "Fujicolor Superia 100" |
| **Fujicolor C200** | C-neg | 200 | Budget everyday Fuji colour | 🔎 ("Fujicolor 100 Industrial" is the nearest V recipe) |
| **Reala 100 / Reala Ace** | C-neg | 100 | 4th cyan layer, true-to-life colour | 📗 [reala-ace](../X-T5/reference-recipes/reala-ace/) + [fujifilm-negative](../X-T5/reference-recipes/fujifilm-negative/) |
| **Fujicolor Super HG** | C-neg | var | Bright clean 90s consumer colour | 📗 [fujicolor-super-hg-v2](../X-T5/reference-recipes/fujicolor-super-hg-v2/) |
| **Natura 1600** | C-neg | 1600 | Japan-only low-light legend (2003–2017) | 📗 [fujicolor-natura-1600](../X-T5/reference-recipes/fujicolor-natura-1600/) |
| **Neopan Acros 100 (II)** | B&W | 100 | Ultra-fine grain, rich blacks | ✅ [fujifilm-acros-100](../X-T5/originals/black-and-white/fujifilm-acros-100/) |
| **Neopan 1600** | B&W | 1600 | High-speed gritty B&W (discont.) | ❌ |
| **Eterna cine stocks** | Cine | var | The Eterna sim's source family | ✅ covered indirectly via cinema originals + Eterna-based recipes |

## Kodak

| Stock | Type | ISO | Signature look | Coverage |
|---|---|---|---|---|
| **Portra 160** | C-neg | 160 | Warm-natural low-ISO portrait | 📗 [kodak-portra-160-v2](../X-T5/reference-recipes/kodak-portra-160-v2/) |
| **Portra 400** | C-neg | 400 | The modern portrait standard | ✅ [kodak-portra-400](../X-T5/originals/kodak-portra-400/) (+ 📗 [v2](../X-T5/reference-recipes/kodak-portra-400-v2/), [reggies](../X-T5/reference-recipes/reggies-portra/)) |
| **Portra 800** | C-neg | 800 | Low-light portrait warmth | 📗 [kodak-portra-800-v3](../X-T5/reference-recipes/kodak-portra-800-v3/) |
| **Ektar 100** | C-neg | 100 | Sharpest, most saturated C-neg — "digital-like" | ✅ [kodak-ektar-100](../X-T5/originals/kodak-ektar-100/) |
| **Gold 200** | C-neg | 200 | Warm sunny nostalgia (film demand #4) | ✅ [kodak-gold-200](../X-T5/originals/kodak-gold-200/) |
| **UltraMax 400** | C-neg | 400 | Punchy drugstore all-rounder | 📗 [kodak-ultramax-400](../X-T5/reference-recipes/kodak-ultramax-400/) |
| **ColorPlus 200** | C-neg | 200 | Budget vintage-leaning colour | ❌ (V recipe not confirmed) |
| **Kodachrome 25** | Slide | 25 | Finest-grain classic Kodachrome | 📗 [kodachrome-25](../X-T5/reference-recipes/kodachrome-25/) |
| **Kodachrome 64** | Slide | 64 | THE 20th-century documentary slide | 📗 [kodachrome-64](../X-T5/reference-recipes/kodachrome-64/) (+ [vintage-kodachrome](../X-T5/reference-recipes/vintage-kodachrome/) for the 1st era) |
| **Ektachrome E100** | Slide | 100 | Cooler, cleaner NatGeo slide (revived 2018) | ✅ [kodak-ektachrome-e100](../X-T5/originals/kodak-ektachrome-e100/) (+ 📗 [thommys](../X-T5/reference-recipes/thommys-ektachrome/)) |
| **Tri-X 400** | B&W | 400 | THE gritty photojournalism B&W | ✅ [kodak-tri-x-400](../X-T5/originals/black-and-white/kodak-tri-x-400/) |
| **T-Max 100** | B&W | 100 | Modern tabular-grain, clean & sharp | 📗 [kodak-t-max-100](../X-T5/reference-recipes/kodak-t-max-100/) (Hard Tone & Soft Tone) |
| **T-Max 400** | B&W | 400 | Modern tabular-grain, medium speed | ❌ |
| **T-Max P3200** | B&W | 800–3200+ | Push-process news film | 📗 [kodak-t-max-p3200](../X-T5/reference-recipes/kodak-t-max-p3200/) |
| **Plus-X 125** | B&W | 125 | Classic mid-century pictorial B&W | 📗 [kodak-plus-x-125](../X-T5/reference-recipes/kodak-plus-x-125/) |
| **Vision3 50D** | Cine | 50 | Cleanest, finest-grain daylight cinema negative | ✅ [kodak-vision3-50d](../X-T5/originals/cinema/kodak-vision3-50d/) |
| **Vision3 250D** | Cine | 250 | Daylight cinema negative, everyday use | ✅ [kodak-vision3-250d](../X-T5/originals/cinema/kodak-vision3-250d/) |
| **Vision3 200T** | Cine | 200 | Tungsten cinema negative, medium speed | ❌ |
| **Vision3 500T** | Cine | 500 | Tungsten cinema negative, night/interior | ✅ [kodak-vision3-500t](../X-T5/originals/cinema/kodak-vision3-500t/) |
| **Ektachrome 100D (cine)** | Cine reversal | 100 | Slide-film cinema; used in *Poor Things* (2023) | ✅ [kodak-ektachrome-100d](../X-T5/originals/cinema/kodak-ektachrome-100d/) |
| **Double-X 5222** | Cine B&W | 250/200 | THE classic B&W cinema stock (1959–present); *Raging Bull*, *Schindler's List* | ✅ [kodak-double-x-5222](../X-T5/originals/cinema/kodak-double-x-5222/) |
| **2383 Print Film** | Cine print | — | Teal-orange theatrical projection look | ✅ [kodak-2383-print](../X-T5/originals/cinema/kodak-2383-print/) |
| **Vericolor III 160** | C-neg | 160 | 80s pro portrait neg (Portra's ancestor) | 🔎 "Kodak Vericolor III 160" |

## Ilford

| Stock | Type | ISO | Signature look | Coverage |
|---|---|---|---|---|
| **HP5 Plus 400** | B&W | 400 | Balanced, forgiving reportage | ✅ [ilford-hp5-plus-400](../X-T5/originals/black-and-white/ilford-hp5-plus-400/) |
| **FP4 Plus 125** | B&W | 125 | Fine-art mid-speed, luminous shadows | 📗 [ilford-fp4-plus-125](../X-T5/reference-recipes/ilford-fp4-plus-125/) |
| **Delta 100 / 400** | B&W | 100/400 | Modern tabular-grain precision | ❌ (datasheets archived; derivation candidates) |
| **Delta 3200** | B&W | 3200 | Grainy available-light B&W | ✅ [ilford-delta-3200](../X-T5/originals/black-and-white/ilford-delta-3200/) |
| **Pan F Plus 50** | B&W | 50 | Ultra-fine slow B&W, deep contrast | ✅ [ilford-pan-f-plus-50](../X-T5/originals/black-and-white/ilford-pan-f-plus-50/) |
| **XP2 Super 400** | B&W (C-41) | 400 | Smooth chromogenic B&W | ❌ |
| **SFX 200** | B&W infrared-ish | 200 | Near-IR drama | ❌ (Acros+R approximates) |

## CineStill (repackaged Kodak cine stock, remjet removed)

| Stock | Type | ISO | Signature look | Coverage |
|---|---|---|---|---|
| **800T** | C-neg (tungsten) | 800 | Neon night, red halation | 📗 [cinestill-800t](../X-T5/reference-recipes/cinestill-800t/) (+ 🔎 "Pushed CineStill 800T") |
| **400D** | C-neg | 400 | Soft daylight cine colour | 📗 [cinestill-400d-v2](../X-T5/reference-recipes/cinestill-400d-v2/) (+ 🔎 v1) |
| **50D** | C-neg | 50 | Finest-grain daylight cine | ❌ (V recipe not confirmed) |

## Agfa / others

| Stock | Type | ISO | Signature look | Coverage |
|---|---|---|---|---|
| **Agfa Ultra 100** | C-neg | 100 | Hyper-saturated cult colour | 🔎 "Agfa Ultra 100 v2" |
| **Agfa Scala 200** | B&W slide | 200 | Silvery B&W transparency | 🔎 "Agfa Scala" |
| **Agfa APX 100/400** | B&W | 100/400 | Classic European B&W | ❌ |
| **Ferrania P30** | B&W | 80 | Italian cinema B&W, deep blacks | ❌ |
| **Fomapan 100/400** | B&W | 100/400 | Budget Czech B&W, vintage curve | ❌ |
| **Lomography 800** | C-neg | 800 | Saturated toy-camera colour | ❌ |
| **Konica Centuria** | C-neg | var | 90s Japanese consumer colour | ❌ |

---

## Priority queue — ✅ closed 2026-07-16

All six 2026-07-15 priority items are now covered: **Ektar 100** and **Pro 400H** as datasheet-derived originals; **CineStill 400D v2**, **Kodachrome 25**, **Plus-X 125**, and **T-Max 100** (Hard/Soft Tone) as attributed reference recipes; **Delta 3200** and **Pan F Plus 50** as datasheet-derived originals (the two ❌ derivation candidates). See [CHANGELOG.md](../CHANGELOG.md) for details.

## Next tier of gaps (candidates for a future pass)

1. **Astia 100F** 🔶 — port an X-Trans IV Astia recipe (CCFXB one notch up).
2. **Superia 100 / Fujicolor C200** 🔎 — fetch FXW recipes to round out the Fuji consumer-negative family.
3. **Vericolor III 160** 🔎 — Portra's direct ancestor; fetch FXW recipe.
4. **Ilford Delta 100 / 400** ❌ — datasheets already archived; derivation candidates (Delta 3200's precedent shows the approach).
5. **Agfa Ultra 100 / Scala 200** 🔎 — fetch FXW recipes; Agfa datasheets (APX, Scala) already archived.
6. **CineStill 50D** ❌ — no confirmed X-Trans V recipe found yet.
7. **XP2 Super 400 / SFX 200** ❌ — Ilford datasheets already archived; chromogenic-B&W and near-IR derivation candidates.

> **Additional recipe source — [Ross McConaghy (rossandhisjpegs.com)](https://www.rossandhisjpegs.com/fujifilm-recipes):** 6 of his **creative** looks are now in `reference-recipes/` (ross-chrome-fog, -canned-heat, -fruit-pastel, -sherbet-lemon, -pumpkin-soup, -salted-slate). His site *also* has film-emulation recipes that map to open gaps above and could be fetched next: **Ultramax Electro** (UltraMax 400, Provia base), **XP2 Electro** (Ilford XP2 Super, Acros+R), **Fujipop Trio 1–3** (Fujicolor C200, three bases), **Lomo800 Electro** (Lomography 800). Note: several of his recipes were published without a stated sensor generation — apply the CCFXB IV→V check where the base is Classic Chrome/Neg/Eterna.

*Sources: [Fuji X Weekly X-Trans V index](https://fujixweekly.com/fujifilm-x-trans-v-recipes/) (fetched 2026-07-15/16), [Ross McConaghy recipes](https://www.rossandhisjpegs.com/fujifilm-recipes) (fetched 2026-07-16), existing bank contents, manufacturer datasheets.*

*Last updated: 2026-07-16*
