# Kodak Vision3 500T — Grade Analysis

> Original (research-backed). See [`recipe.md`](recipe.md), the [cinema README](../README.md), and the [Knowledge base](../../../../Knowledge/README.md).

## The stock
Kodak Vision3 500T (5219/7219) is the **tungsten-balanced (3200K), high-speed (EI 500)** ECN-2 motion-picture negative — the workhorse of night and interior cinematography. Outstanding skin tones, fine grain for its speed, wide dynamic range, and reduced grain in shadows. In daylight it's rated 320 with an 85 filter (and goes blue without one).

## The grade in one line
**Clean, cool, low-contrast tungsten night cinema** — natural warm practicals, cinematic cool-blue daylight/shadows, soft highlights, fine grain.

## The CineStill relationship (important)
**CineStill 800T *is* Vision3 500T** with the anti-halation *remjet* layer removed (so bright lights bloom red) and pushed to ISO 800. So:
- This recipe = the clean, accurate 500T: Incandescent WB, fine grain, Clarity 0, no exaggerated glow.
- [CineStill 800T](../../../reference-recipes/cinestill-800t/knowledge.md) = the stylised version: Fluorescent-3 WB (stronger cool cast), Strong/Large grain, Clarity −5 (glow standing in for halation).
Having both lets the user choose accurate vs stylised for night work.

## How it's built
Eterna + DR400 + Highlight −2 give the wide-latitude soft-highlight cine base. Incandescent WB matches the tungsten balance (warm light neutral, daylight cool). Shadow +1 adds night density over Eterna's clean shadows. Color +2 + CCE Strong lift saturation so practicals/neon read richly. Fine grain + Clarity 0 keep it a *clean* motion-picture rendering.

## Real-image validation (via CineStill proxy)
Analysed a real **CineStill night frame** (Reading Terminal Market neon, Wikimedia Commons — CineStill *is* 5219 with remjet removed, so it's a valid proxy for the emulsion's colour/tonality): confirmed **deep clean blacks that retain stone texture, natural warm rendering under tungsten-matched light, saturated reds around signage** → validates the Incandescent WB + Shadow +1 + clean-texture choices here. The frame's dramatic **red halation bloom** around lights is the *remjet-removed* CineStill artifact — correctly **absent** from this clean 500T recipe and **present** (via Clarity −5/glow) in the stylised [CineStill 800T](../../../reference-recipes/cinestill-800t/knowledge.md). The split between the two recipes is exactly what the real frame shows.

## vs the other cinema recipes
- **[Vision3 250D](../kodak-vision3-250d/knowledge.md):** the daylight sibling — neutral, clean, natural.
- **[2383 Print](../kodak-2383-print/knowledge.md):** the graded theatrical print look (teal-orange).
