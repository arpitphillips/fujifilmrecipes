# Fujifilm X-T5 Film Simulation Recipes

Curated from [Fuji X Weekly](https://fujixweekly.com/fujifilm-x-trans-v-recipes/) — the X-T5 uses the **X-Trans V** sensor/processor, so all recipes in this folder are the X-Trans V versions (or noted as fully compatible). Selected as a well-rounded starter set spanning classic color, punchy/vintage color, moody tones, cinematic night, and black & white.

## Folder structure

This folder is organised in **two tiers**:

- **[`originals/`](originals/)** — validated / research-derived / original-design recipes (the sellable IP), sub-grouped into colour (root), `cinema/`, `black-and-white/`, and `creative/`.
- **[`reference-recipes/`](reference-recipes/)** — attributed recipes from Fuji X Weekly and other sources, kept for testing/benchmarking and as candidates to re-derive as originals.

Plus: `_reference-sources/` (drop-folder for source PDFs/scans used in validation) and the two Fujifilm manuals (below).

Each recipe is its own folder containing:
- **`recipe.md`** — the exact settings to program into the camera.
- **`knowledge.md`** — the grade analysis: what look it produces, the film it emulates, and the reasoning behind every setting.
- **`references/`** and **`test-shots/`** — image drop-folders (see below).

For the settings-based reference (what each control does and how looks are built), see the top-level [Knowledge base](../Knowledge/README.md).

The two Fujifilm PDFs in this folder are the source documents:
- `x-t5_manual_en_s_f.pdf` — the full X-T5 Owner's Manual (Image Quality settings: Ch.6, printed pp.122–132).
- `x-t5_nfg_en_s_f.pdf` — New Features Guide for firmware v4.30 (connectivity/menu changes only; does not affect recipes).

## Recipes

**See [RANKING.md](RANKING.md) for the full bank ranked by aesthetic value × popularity.**

Each recipe folder holds: `recipe.md` (stills), sometimes `recipe-video.md` (movie mode), and `knowledge.md` (grade analysis). Flagship entries also have `research.md` / `validation.md`. Recipes are tagged **original** (research-derived or original design — the clean IP for the bank) or **reference** (attributed captures for testing/benchmarking).

**Every recipe folder also has two drop-folders:**
- `references/` — drop **real film scans** of the look here (Reddit/Flickr/lab finds) to validate & improve the recipe.
- `test-shots/` — drop **your own X-T5 frames** shot with the recipe here to test faithfulness.

(Reddit can't be auto-scraped — it needs login I can't perform — so `references/` is how you feed me good Reddit/Cloudflare-site images.)

### Originals (validated / research-derived — the sellable IP)
| Recipe | Base film sim | Mood | Video? | Validation |
|---|---|---|---|---|
| [kodak-gold-200](originals/kodak-gold-200/) | Classic Chrome | Warm sunny nostalgia | ✅ | datasheet + **scan-validated** |
| [kodak-portra-400](originals/kodak-portra-400/) | Classic Chrome | Emulsion-faithful pro portrait | — | datasheet + scan (partial) |
| [kodak-ektachrome-e100](originals/kodak-ektachrome-e100/) | Provia | Neutral clean slide (E100) | — | datasheet (E-4000 archived) |
| [kodak-ektar-100](originals/kodak-ektar-100/) | Velvia (tamed) | Vivid, sharp, near-invisible grain | — | datasheet + **scan** |
| [fujicolor-pro-400h](originals/fujicolor-pro-400h/) | Pro Neg. Hi | Cool pastel pro portrait | — | datasheet + video-comparison |
| [fujicolor-superia-400](originals/fujicolor-superia-400/) | Classic Negative | Cool green "Fuji look" | ✅ | datasheet + characteristic |
| [cinema/kodak-vision3-50d](originals/cinema/kodak-vision3-50d/) | Eterna | Cleanest daylight cinema (finest grain) | ✅ | datasheet + characteristic + **scan** |
| [cinema/kodak-vision3-250d](originals/cinema/kodak-vision3-250d/) | Eterna | Daylight cinema | ✅ inline | datasheet + characteristic + scan (partial) |
| [cinema/kodak-vision3-500t](originals/cinema/kodak-vision3-500t/) | Eterna | Tungsten night cinema | ✅ inline | datasheet + characteristic |
| [cinema/kodak-double-x-5222](originals/cinema/kodak-double-x-5222/) | Acros | Classic B&W cinema (Raging Bull, Schindler's List) | ✅ | datasheet + characteristic |
| [cinema/kodak-ektachrome-100d](originals/cinema/kodak-ektachrome-100d/) | Provia | Reversal cinema slide (Poor Things) | ✅ | datasheet + characteristic |
| [cinema/kodak-2383-print](originals/cinema/kodak-2383-print/) | Classic Negative | Teal-orange theatrical print | ✅ inline | characteristic |
| [b&w/fujifilm-acros-100](originals/black-and-white/fujifilm-acros-100/) | Acros | Clean fine-grain B&W | ✅ inline | datasheet + **scan** |
| [b&w/ilford-hp5-plus-400](originals/black-and-white/ilford-hp5-plus-400/) | Acros | Balanced reportage B&W | ✅ inline | datasheet + **scan** |
| [b&w/kodak-tri-x-400](originals/black-and-white/kodak-tri-x-400/) | Acros+Ye | Gritty high-contrast B&W | ✅ inline | datasheet + characteristic |
| [b&w/ilford-pan-f-plus-50](originals/black-and-white/ilford-pan-f-plus-50/) | Acros | Slowest, sharpest, contrasty B&W | — | datasheet |
| [b&w/ilford-delta-3200](originals/black-and-white/ilford-delta-3200/) | Acros | Heaviest-grain pushed B&W | — | datasheet + **scan** |
| [mumbai-monsoon](originals/mumbai-monsoon/) | Classic Negative | Overcast/rain cinematic | ✅ | original design |
| [mumbai](originals/mumbai/) | Classic Negative | Warm lively sunny street | ✅ | original design |
| [creative/fashion-editorial-vogue](originals/creative/fashion-editorial-vogue/) | Pro Neg Hi | Polished fashion editorial | inline | creative design |
| [creative/bewaremyvelvia-bold](originals/creative/bewaremyvelvia-bold/) | Velvia | Bold saturated dramatic | inline | creative design |
| [creative/matte-editorial](originals/creative/matte-editorial/) | Eterna | Muted faded lifestyle matte | inline | creative design |
| [creative/pastel-dream](originals/creative/pastel-dream/) | Astia | Soft candy-pastel, bright & airy | inline | creative design |
| [creative/bleach-bypass-noir](originals/creative/bleach-bypass-noir/) | Eterna Bleach Bypass | Silvery high-contrast noir | inline | creative design |
| [creative/golden-hour-glow](originals/creative/golden-hour-glow/) | Astia | Warm honeyed sun-glow | inline | creative design |
| [creative/silent-atlas](originals/creative/silent-atlas/) | Classic Negative | Teal-and-warm cinematic travel documentary | ✅ | creative design (frame study of reference film) |
| [creative/clean-girl](originals/creative/clean-girl/) | Astia | Bright airy white-white, luminous skin | inline | creative design |

See [Knowledge/validation-methodology.md](../Knowledge/validation-methodology.md) for what each validation tier means.

### Reference recipes (attributed captures — for testing/benchmarking, to be re-derived as originals)
| Recipe | Base film sim | Mood | Video? | Status |
|---|---|---|---|---|
| [reggies-portra](reference-recipes/reggies-portra/) | Classic Chrome | Everyday / versatile portraits | — | reference |
| [reggies-superia](reference-recipes/reggies-superia/) | Classic Negative | Portrait interpretation (melanated-skin focus) | — | reference *(added 2026-07-16)* |
| [kodachrome-64](reference-recipes/kodachrome-64/) | Classic Chrome | All-purpose crisp daylight | — | reference |
| [kodak-portra-400-v2](reference-recipes/kodak-portra-400-v2/) | Classic Chrome | Golden-hour portraits | — | reference |
| [kodak-portra-800-v3](reference-recipes/kodak-portra-800-v3/) | Classic Chrome | Moody low-light portraits | — | reference |
| [pacific-blues](reference-recipes/pacific-blues/) | Classic Negative | Cool / moody / coastal | — | reference |
| [reala-ace](reference-recipes/reala-ace/) | Classic Negative | Clean true-to-life (approx.) | — | reference |
| [fujifilm-negative](reference-recipes/fujifilm-negative/) | Reala Ace | Clean true-to-life (native) | — | reference |
| [fujicolor-super-hg-v2](reference-recipes/fujicolor-super-hg-v2/) | Classic Negative | Bright clean everyday | — | reference |
| [luis-costa-classic-negative](reference-recipes/luis-costa-classic-negative/) | Classic Negative | Warm everyday daily-driver | — | reference (other source) |
| [california-summer](reference-recipes/california-summer/) | Nostalgic Neg. | Warm faded summer | — | reference |
| [1976-kodak](reference-recipes/1976-kodak/) | Nostalgic Neg. | Punchy vintage color | — | reference |
| [vintage-kodachrome](reference-recipes/vintage-kodachrome/) | Classic Chrome | Painterly 1st-era Kodachrome | — | reference (III→V port) |
| [cinestill-800t](reference-recipes/cinestill-800t/) | Eterna | Night / neon / cinematic | — | reference |
| [kodak-tri-x-400](reference-recipes/kodak-tri-x-400/) | Acros | Gritty B&W street | — | reference → **superseded** by [b&w original](originals/black-and-white/kodak-tri-x-400/) |
| [acros-red-high-contrast](reference-recipes/acros-red-high-contrast/) | Acros+R | Dramatic high-contrast B&W | — | reference (other source) |
| [provia-positive](reference-recipes/provia-positive/) | Provia | Vintage slide-film standard | — | reference *(added 2026-07-15)* |
| [vivid-velvia](reference-recipes/vivid-velvia/) | Velvia | Bold saturated landscape slide | — | reference *(added 2026-07-15)* |
| [thommys-ektachrome](reference-recipes/thommys-ektachrome/) | Nostalgic Neg. | NatGeo-era Ektachrome documentary | — | reference *(added 2026-07-15)* |
| [kodak-portra-160-v2](reference-recipes/kodak-portra-160-v2/) | Classic Chrome | Warm natural low-ISO portraits | — | reference *(added 2026-07-15)* |
| [kodak-ultramax-400](reference-recipes/kodak-ultramax-400/) | Classic Chrome | Punchy drugstore-film all-rounder | — | reference *(added 2026-07-15)* |
| [fujicolor-natura-1600](reference-recipes/fujicolor-natura-1600/) | Classic Negative | Muted grainy low-light snapshot | — | reference *(added 2026-07-15)* |
| [ilford-fp4-plus-125](reference-recipes/ilford-fp4-plus-125/) | Monochrome | Fine-art low-speed B&W | — | reference *(added 2026-07-15)* |
| [kodak-t-max-p3200](reference-recipes/kodak-t-max-p3200/) | Acros | Pushed high-ISO night B&W | — | reference *(added 2026-07-15)* |
| [cinestill-400d-v2](reference-recipes/cinestill-400d-v2/) | Astia | Daylight CineStill soft tones | — | reference *(added 2026-07-16)* |
| [kodachrome-25](reference-recipes/kodachrome-25/) | Classic Chrome | Sharpest classic Kodachrome | — | reference *(added 2026-07-16)* |
| [kodak-plus-x-125](reference-recipes/kodak-plus-x-125/) | Acros | Classic mid-century pictorial B&W | — | reference *(added 2026-07-16)* |
| [kodak-t-max-100](reference-recipes/kodak-t-max-100/) | Monochrome+G | Modern tabular-grain B&W (Hard/Soft Tone) | — | reference *(added 2026-07-16)* |
| [ross-chrome-fog](reference-recipes/ross-chrome-fog/) | Classic Chrome | Creative: hazy/foggy diffusion-filter look | — | reference (Ross McConaghy) |
| [ross-canned-heat](reference-recipes/ross-canned-heat/) | Classic Negative | Creative: warm sunset teal-orange vibe | — | reference (Ross McConaghy) |
| [ross-fruit-pastel](reference-recipes/ross-fruit-pastel/) | Velvia | Creative: sugared Velvia pastel | — | reference (Ross McConaghy) |
| [ross-sherbet-lemon](reference-recipes/ross-sherbet-lemon/) | Velvia | Creative: bright bold seaside/funfair | — | reference (Ross McConaghy) |
| [ross-pumpkin-soup](reference-recipes/ross-pumpkin-soup/) | Nostalgic Neg. | Creative: warm punchy autumnal | — | reference (Ross McConaghy) |
| [ross-salted-slate](reference-recipes/ross-salted-slate/) | Acros+G | Creative: dark slate-grey grainy B&W | — | reference (Ross McConaghy) |
| [timeless-negative](reference-recipes/timeless-negative/) | Nostalgic Neg. | Faded any-decade print look | — | reference *(added 2026-07-19)* |
| [nostalgia-negative](reference-recipes/nostalgia-negative/) | Nostalgic Neg. | Warm 70s New Color print | — | reference *(added 2026-07-19)* |
| [nostalgic-americana](reference-recipes/nostalgic-americana/) | Nostalgic Neg. | Cool aged shoebox print | — | reference *(added 2026-07-19)* |
| [cine-teal](reference-recipes/cine-teal/) | Eterna | Moody teal cinematic (IV→V port) | — | reference *(added 2026-07-19)* |
| [nostalgic-color](reference-recipes/nostalgic-color/) | Nostalgic Neg. | Video: warm memory-like footage | ✅ | reference *(added 2026-07-19)* |
| [chrome-color](reference-recipes/chrome-color/) | Classic Chrome | Video: documentary editorial | ✅ | reference *(added 2026-07-19)* |
| [vivid-fujichrome](reference-recipes/vivid-fujichrome/) | Velvia | Video: bold postcard slide colour | ✅ | reference *(added 2026-07-19)* |
| [reala-color](reference-recipes/reala-color/) | Reala Ace | Video: clean true-to-life | ✅ | reference *(added 2026-07-19)* |

> **Video recipes** exist for all **originals** (Gold 200 & Mumbai Monsoon as separate `recipe-video.md`; Superia and the cinema sims as inline "Video (movie mode)" sections). Movie mode drops grain/chrome/clarity — see [Knowledge/video-mode-settings.md](../Knowledge/video-mode-settings.md). Video versions of the reference recipes can be generated on request.

## Pro tips (bank-wide, from accumulated research)

- HEIF silently disables Clarity. Any recipe with Clarity away from 0 loses part of its look in HEIF, so shoot JPEG (FINE or FINE+RAW) for the full recipe. Clarity-0 recipes (Gold 200, Portra 400, Superia 400, Clean Girl, all the cinema stills) are HEIF-safe.
- Clarity away from 0 also slows shot-to-shot saving. For street or burst work, favour the Clarity-0 recipes or accept the buffer pause (Kodachrome 64 at +3, Tri-X at +3, UltraMax at +3, Pan F at +2).
- Shoot FINE + RAW. The JPEG carries the baked look, and the RAW lets you re-develop any other recipe later, in-camera or via Fujifilm X RAW Studio. One shoot, every look in the bank.
- On Acros-based recipes, ISO is a real grain control: Fujifilm's own design notes state the grain engine scales with ISO and concentrates in shadows. For more grit, raise ISO and expose slightly down; high-key frames always render cleaner because highlight grain stays fine by design.
- The X-T5 remembers a WB Shift per C-slot, so program all seven slots without shifts bleeding across recipes.
- Classic Neg highlights lean magenta by design (official). If highlights look too pink on 2383, Silent Atlas or Mumbai, reduce Red in the WB shift rather than adding Blue.
- Nostalgic Neg's shadow amber can't be neutralised by WB (official). Pick a different base if you need neutral shadows; conversely it is the best base for portraits in shade.

See [fujifilm-official-design-notes](../Knowledge/fujifilm-official-design-notes.md) for the first-party sources behind the "official" items.

## General notes
- Store recipes in the **C1–C7 custom presets** (Image Quality → Edit/Save Custom Setting). See [How to Program Film Simulation Recipes to Your Fujifilm Camera](https://fujixweekly.com/2024/02/27/how-to-program-film-simulation-recipes-to-your-fujifilm-camera/).
- "Exposure Compensation: typically" is a starting suggestion, not a rule — judge each scene.
- The X-T5 remembers a **White Balance Shift per C-preset** (X-Pro3-and-newer feature), so each recipe keeps its own shift.
- **X-Trans V blue note:** many of these are ports of X-Trans IV recipes with Color Chrome FX Blue dropped one notch. To run a recipe on an X-Trans IV body, raise CCFXB one notch (Off→Weak, Weak→Strong). Full detail in [x-trans-v-and-conversion.md](../Knowledge/x-trans-v-and-conversion.md).
