# Kodak Tri-X 400 — Grade Analysis

> Original (research-derived). See [`recipe.md`](recipe.md), the [B&W README](../README.md), and the [Knowledge base](../../../../Knowledge/README.md).

## The film
Kodak Tri-X 400 is the most iconic B&W film in history — the stock of classic photojournalism and street photography. Its signature is **dark, rich contrast, deep blacks, a wide tonal range, and a heavy, distinctive (love-it-or-hate-it) grain**, with huge exposure latitude and legendary push tolerance.

## The look in one line
**Gritty, high-contrast, deep-black reportage B&W** with heavy characterful grain and mid-tone bite.

## How it's built
- **Acros+Ye base** — Acros gives the richest tonality; the yellow filter adds Tri-X's slight contrast and darker skies.
- **DR200 + Highlight +1 + Shadow +2** — punchy contrast with deep rich blacks (Tri-X renders greys darker and blacks deeper than HP5).
- **Grain Strong, Large** — the heavy, clumpy Tri-X grain.
- **Clarity +3** — the crucial move: Tri-X's tactile, gritty mid-tone bite. This overrides the Clarity-0 default *because faithfulness demands it* (Tri-X without grit isn't Tri-X).
- **High ISO** — pushes the grain and grit; Tri-X lives at 400–1600+.

## Datasheet confirmation & an honest nuance (Kodak F-4017, fetched & extracted)
The F-4017 datasheet confirms: **fine grain for its speed, wide exposure latitude, "rich tonality"** — and a development aim of **contrast index 0.56** (i.e. box-speed Tri-X, normally developed, is actually *moderate* contrast). The sheet also documents that **pushing raises contrast and graininess and sinks shadow detail** — which is exactly the point: the iconic "Tri-X look" (deep blacks, heavy grit) is substantially a product of **push-processing and printing choices**, not the base curve.

**Design decision (documented honestly):** this recipe targets the **iconic pushed/reportage rendering** — the Tri-X people mean when they say "Tri-X" — not box-speed-normal-dev. Hence Shadow +2 / Highlight +1 / Clarity +3 / Strong-Large grain / high ISO. A faithful *box-speed* variant would be: Highlight 0, Shadow +1, Clarity +1, Grain Strong/Small, ISO ≤ 1600.

## Validation tier
**Datasheet (extracted) + characteristic.** **Scan-fetch pending:** open sources (Wikimedia) lacked accessible Tri-X pictorials this pass; drop a Tri-X reference PDF into `_reference-sources/` or `references/` to reach the full scan tier (the Gold 200 workflow).

## vs the other B&W originals
- **[Acros 100](../fujifilm-acros-100/knowledge.md):** the clean/fine opposite — smooth, fine grain, Clarity 0.
- **[HP5 Plus 400](../ilford-hp5-plus-400/knowledge.md):** the middle ground — even grain, balanced contrast, deep-but-natural shadows, Clarity 0. Tri-X is grittier and more contrasty than HP5.
