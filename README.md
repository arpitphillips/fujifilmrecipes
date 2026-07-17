# Fujifilm Recipes

A curated, research-backed bank of **Fujifilm film-simulation recipes** for the **X-T5 (X-Trans V)** — plus the reference layer that explains *why* each one works.

A Fujifilm film simulation recipe is a bundle of in-camera JPEG settings — film simulation, white balance shift, dynamic range, tone curve, grain, and a handful of others — that reproduces the look of a specific film stock straight out of the camera, no editing required. This repo is two things at once: a bank of recipes to program into your camera, and a knowledge base grounded in manufacturer datasheets and real film science explaining what each control actually does.

## What makes this different

Most recipe collections are copied settings with a name attached. Every **original** recipe here traces back to something checkable:

- A manufacturer's **technical datasheet** — characteristic curves, RMS granularity or Print Grain Index, colour balance, exposure latitude — archived locally in [`X-T5/_reference-sources/datasheets/`](X-T5/_reference-sources/datasheets/README.md)
- For the top tier, **real film scans** analysed frame-by-frame against the recipe's output
- A **knowledge layer** ([`Knowledge/`](Knowledge/)) explaining the color science and film chemistry behind the settings — not just *what* to dial in, but *why*

See [`Knowledge/validation-methodology.md`](Knowledge/validation-methodology.md) for the full evidence standard, and [`X-T5/VALIDATION-AUDIT.md`](X-T5/VALIDATION-AUDIT.md) for a recipe-by-recipe audit against the datasheet archive.

## Structure

```
Knowledge/           reference layer — film simulations, white balance, dynamic range,
                      grain/detail, color science, film chemistry, validation methodology
X-T5/
├── originals/       independently derived, validated recipes — colour, cinema,
│                    black & white, and creative looks
├── reference-recipes/  recipes from the wider Fujifilm/film community, kept for
│                    testing and comparison, each crediting its original creator
├── _reference-sources/ manufacturer datasheets and scan sources used for validation
└── RANKING.md       the full bank, ranked by aesthetic value and popularity
```

Start at [`Knowledge/README.md`](Knowledge/README.md) for the settings reference, or [`X-T5/README.md`](X-T5/README.md) for the recipe index.

## The recipes

27 validated originals and 34 reference recipes as of this writing (see [`X-T5/RANKING.md`](X-T5/RANKING.md) for the current, full list). A few to start with:

| Recipe | Look | Validation |
|---|---|---|
| [Kodak Gold 200](X-T5/originals/kodak-gold-200/) | Warm sunny nostalgia | Datasheet + **scan-validated** across ~35 real film frames |
| [Kodak Tri-X 400](X-T5/originals/black-and-white/kodak-tri-x-400/) | Gritty, high-contrast photojournalism B&W | Datasheet + characteristic |
| [Fujicolor Superia 400](X-T5/originals/fujicolor-superia-400/) | Cool, green-leaning "Fuji look" | Datasheet + characteristic |
| [Ilford HP5 Plus 400](X-T5/originals/black-and-white/ilford-hp5-plus-400/) | Balanced, forgiving reportage B&W | Datasheet + scan |
| [Kodak Vision3 500T](X-T5/originals/cinema/kodak-vision3-500t/) | Tungsten night cinema | Datasheet + characteristic |
| [Clean Girl](X-T5/originals/creative/clean-girl/) | Bright, airy, luminous-skin — a designed look, not a film emulation | Creative design |

## Using a recipe

Recipes are programmed into one of the camera's **C1–C7 custom presets** (Image Quality menu → Edit/Save Custom Setting). Each recipe folder holds:

- `recipe.md` — the exact settings table
- `knowledge.md` — the grade analysis: the film it emulates and the reasoning behind every setting
- `references/` and `test-shots/` — drop real film scans or your own test shots here to help validate or refine the recipe

Full walkthrough: [How to Program Film Simulation Recipes to Your Fujifilm Camera](https://fujixweekly.com/2024/02/27/how-to-program-film-simulation-recipes-to-your-fujifilm-camera/).

## Attribution

Recipes under `originals/` are independently derived and validated as described above. Recipes under `reference-recipes/` originate with other members of the Fujifilm and film photography community — each carries a `Source` link to the original creator's page. No license is declared for this repository at present; third-party recipes remain the work of their original authors.

## Website

This repo renders into a static knowledge-base site (originals on the homepage, community recipes with full attribution, the knowledge layer, about and contact pages). The generator lives in [`site/`](site/) — `python3 site/build.py` builds it into `_site/` (deps: `pip install markdown jinja2`) — and [`.github/workflows/deploy-site.yml`](.github/workflows/deploy-site.yml) deploys it to GitHub Pages on every push to `main`.

## For contributors (human or AI)

[`CLAUDE.md`](CLAUDE.md) documents the repo's conventions for anyone — human or AI agent — adding to it. [`CHANGELOG.md`](CHANGELOG.md) is the running log of every change and must be updated with each session.
