# Request #1: "Grand Tour" · European Travel Editorial

**Client brief:** *"Could anyone suggest recipes for these colours"*, 7 reference frames.
**Body:** Fujifilm X-T5 (X-Trans V) · Stills, SOOC JPEG
**Status:** Design derived from reference analysis, field-test pending (drop frames in [`test-shots/`](test-shots/)).
**Date:** 2026-07-20

---

## 1. What the references actually are

| # | Scene | Light | Source file |
|---|---|---|---|
| 1 | Bellagio / Lake Como aerial | Late-afternoon sun, hazy | `…14noq2r9kbeh1` |
| 2 | Grand-hotel room, desk at window | Strong backlight through sheers | `…6metw1r9kbeh1` |
| 3 | Tuscan villa pool, woman + spritz | Golden hour, low raking sun | `…c0wd53r9kbeh1` |
| 4 | Lake Como, palms + Riva runabout | Bright midday, hazy | `…cm0s31r9kbeh1` |
| 5 | Glass-roof atrium bar | Flat cool daylight, huge DR | `…el022ar9kbeh1` |
| 6 | Wine bar, tiled counter | Soft flat ambient | `…jzuda7r9kbeh1` |
| 7 | Mid-century hotel lobby | Dim warm tungsten | `…zxyke5r9kbeh1` |

All seven are Instagram carousel screenshots (`10/10`, `1/5`, `1/7`, `1/10`, `3/10`, `1/7` badges), so they come from at least four different posts, likely more than one photographer, and they are heavily re-compressed. What the client is responding to is therefore a genre look, not one person's single preset. That is good news: a genre look is exactly what a film-simulation recipe reproduces well.

---

## 2. Can one recipe do all seven?: Yes.

The seven frames span golden hour, harsh midday, extreme backlight, flat cool daylight and dim tungsten. That sounds like it needs several recipes, but it doesn't, because **what unifies them is a colour *response*, not a colour *cast***. Every frame does the same five things:

1. Saturation is compressed, not reduced. Neutrals stay clean, but anything strongly coloured gets pulled back, the Riva's mahogany (4), the bar stools' red (6) and the croton plant (7) all land as terracotta/brick rather than red. Nothing in any frame is vivid.
2. Greens go olive. Hillsides (1), palms (4), cypress (3), foliage (7) all sit yellow-shifted and darkened. This is the single most identifiable fingerprint in the set.
3. Blues go pale and hazy, but dark water stays deep teal. Skies in 1, 3 and 4 are washed-out cyan with almost no saturation, while the lake and pool hold a deep blue-green. So blues are *desaturated*, not *deepened*.
4. Highlights roll, they never clip hard. The window in 2, the skylight in 5, the white loungers in 3 and the cream wall in 6 all retain texture at the top end.
5. Shadows are deep but open and slightly warm. The lobby corners in 7, the hillside in 1 and the room shadows in 2 all hold detail with a brown/amber lean, never inky neutral black.

Plus a consistent warm-mid / cool-neutral split: wood, brass, skin and stone read golden, while whites and greys stay honest (cream in 2 and 6, genuinely cool in 5). That split is what makes the look feel expensive rather than filtered.

**Why one recipe works:** the white balance has to *move* between these scenes, that's Auto WB's job, while the tone curve, saturation compression and hue shifts stay fixed. That's precisely how a Fujifilm recipe is built.

**Where one recipe is honestly stretched:** frame 5 sits noticeably cooler than the rest and frame 7 noticeably warmer/moodier. §5 gives a ±1 WB-shift variant for each; the base recipe lands both acceptably, and the variants land them exactly.

---

## 3. Base simulation: why Classic Chrome

| Candidate | Verdict |
|---|---|
| **Classic Chrome** | ✅ **Chosen.** Muted saturation with warm mid-tones intact, olive-shifted greens, restrained reds that fall to terracotta, deep neutral shadows. Every fingerprint in §2 is native behaviour. |
| Classic Negative | ❌ Fujifilm's own design notes describe it as biased **cyan-green in shadows and magenta in highlights**. The references have *warm* highlights and *warm* shadows — the exact opposite. |
| Reala Ace | ⚠️ Close on saturation compression (its documented "the more saturated the subject, the more muted the colour"), but it keeps greens natural rather than olive, and its native contrast is harder than these frames. |
| Eterna | ❌ Right softness, wrong colour — flattens to grey-green and drains the golden richness in 1, 2, 3, 7. |
| Nostalgic Neg. | ❌ Its amber is anchored in the *shadows* and cannot be tuned out with WB. Great for 7, wrong for the crisp lake frames. |

Classic Chrome's one mismatch is that its shadows run slightly cool-green where the references run warm, corrected below with the WB shift and a Shadow lift.

> **First-party backing (Fujifilm's own design page):** Classic Chrome is officially "more subdued with suppressed magenta and cool shadows" versus Provia, aiming at an "assured, composed look." Both halves of that sentence land on these references: *suppressed magenta* is why every red in the set falls to terracotta rather than staying red, and *cool shadows* is the one trait we have to correct (hence +2 Red). Fujifilm also explicitly recommends this simulation for "fashion, interior, and product photography", four of the seven references are interiors.
>
> **The two fingerprints in §2 are officially designed in.** Fujifilm's development story for this simulation states the mode **"controls the saturation *and hue* of reds and greens to produce a unique chromatic balance" — that is first-party confirmation of exactly the two traits identified in your references: greens shifting olive, reds falling to terracotta. The team also says they deliberately "removed the magenta component"** from skies, where conventional colour design *adds* it — which is precisely why the skies in frames 1, 3 and 4 read pale and hazy, and why Color Chrome FX Blue is switched Off in this recipe rather than merely turned down. Turning it on would fight a deliberate design decision.
>
> One more, and it explains the Clarity/Sharpness choices: Fujifilm "worked to create a mode that looks like a print when viewed on an LCD screen." The base is already doing print-emulation work at the tone level, so adding micro-contrast on top double-processes it.
>
> Worth knowing: Classic Chrome is based on no analog film at all. Fujifilm describes it as "an imaginary film" modelling 20th-century photojournalism magazines, the golden age of print. That is precisely why it suits this brief: the client's references have the colour restraint of a printed magazine page, not of a film stock. See [official design notes](../../Knowledge/fujifilm-official-design-notes.md).

---

## 4. The recipe

| Setting | Value |
|---|---|
| **Film Simulation** | **Classic Chrome** |
| Grain Effect | **Weak, Small** |
| Color Chrome Effect | **Strong** |
| Color Chrome FX Blue | **Off** |
| White Balance | **Auto**, **+2 Red / −2 Blue** |
| Dynamic Range | **DR400** |
| Tone Curve — Highlight | **−1** |
| Tone Curve — Shadow | **−1** |
| Color | **+1** |
| Sharpness | **−1** |
| High ISO NR | **−4** |
| **Clarity** | **0** |
| ISO | Auto, **500–6400** |
| Exposure Compensation | **0 to +1/3** outdoors · **−1/3 to 0** for dim interiors |

### Why each setting

- Classic Chrome + Color +1: the base supplies the muted palette; +1 stops it from going drab, so wood, brass and mustard keep the body they have in frames 5–7. Still far quieter than Provia.
- Color Chrome Effect Strong: adds density and gradation *inside* already-saturated colours rather than adding overall saturation. This is what makes the mahogany hull (4), the marble counter (6) and the amber chairs (7) look rich while the frame stays restrained. It is the single most important setting in this recipe.
- Color Chrome FX Blue Off: the references' skies are pale and hazy (1, 3, 4). FX Blue *deepens* blue; switching it on would immediately break the most fragile part of the look. The deep water in 3 and 4 comes from the water being dark, not from blue enhancement. See §5 for the water-forward variant.
- Auto WB +2R/−2B: Auto is mandatory here: the set runs from golden hour to tungsten, and any fixed WB that suits frame 3 turns frame 7 orange and frame 5 blue. The +2 Red restores the warm shadows Classic Chrome renders slightly cool; the −2 Blue yellows the greens toward the olive of frames 1 and 4 and keeps skies hazy rather than blue.
- DR400: frames 2 and 5 have brutal dynamic range (backlit window, glass roof) and both hold. DR400 protects the top end without a hard shoulder. It pins ISO ≥ 500; see the pro-tips.
- Highlight −1: the gentle roll on the white loungers (3), the cream wall (6) and the sheer curtains (2). With DR400 already protecting, −1 is enough; −2 goes limp.
- Shadow −1: opens the blacks just enough to match the detailed lobby corners (7) and hillside (1) while Classic Chrome's native depth keeps the frame from looking flat.
- Sharpness −1, Clarity 0: the references are smooth and editorial, never crunchy. Nothing here needs added micro-contrast, so Clarity stays at 0 per the [bank's standing rule](../../Knowledge/validation-methodology.md), which also keeps this recipe HEIF-safe and fast-saving.
- Grain Weak/Small: a whisper of texture so 40MP files don't read clinically. Invisible at normal viewing size.

---

## 5. Per-scene variants

Same recipe, one setting moved. Program the base in a C-slot; these are 5-second field tweaks.

| Reference frame | Change | Why |
|---|---|---|
| **5** — cool flat interiors, marble/grey stone | WB shift → **+1R / −1B** | Keeps greys honestly cool instead of creamy. |
| **7** — dim tungsten, moody | WB shift → **+1R / 0B**, EC **−1/3** | Auto WB already warms; less push avoids going orange. Underexposing keeps the depth. |
| **3** — golden hour | WB shift → **+3R / −3B** | Leans into the low-sun warmth without touching anything else. |
| **4** — water/sea-forward | Color Chrome FX Blue → **Weak** | Adds depth to large water areas. Only when little sky is in frame. |
| **2** — heavy backlight | EC **+2/3 to +1** | Protects the interior; DR400 handles the window. |
| Softer, glowier interior look | Clarity **−1** | Optional. Costs shot-to-shot speed — see pro-tips. |

---

## 6. Pro tips

- DR400 pins ISO at 500 minimum. In bright sun that means stopping down or a fast shutter. On the X-T5 use the electronic shutter or a 3-stop ND for wide-open work; don't try to force ISO 125. You lose the highlight roll-off that defines the look.
- This recipe is HEIF-safe. Clarity is 0, so nothing is lost shooting HEIF. If you take the Clarity −1 variant, shoot JPEG instead, HEIF silently disables Clarity, and non-zero Clarity also slows shot-to-shot saving.
- Shoot FINE + RAW. The JPEG carries the look; the RAW lets you re-run any other recipe later in-camera or in X RAW Studio.
- The look lives on warm materials. Wood, brass, terracotta, linen, stone, skin. It rewards hotel interiors, old towns, boats and golden hour, and does very little for grey cityscapes or overcast greenery.
- Expose for the highlights, trust the shadows. Every reference frame protects the top end and lets the bottom end sit dark-but-open. Shadow −1 plus DR400 gives more room down there than you expect.
- The X-T5 stores WB Shift per C-slot: you can program the base and the cool-interior variant in two slots without them interfering.

---

## 7. Movie-mode translation

Movie mode has no Grain, no Color Chrome Effect, no Color Chrome FX Blue and no Clarity ([details](../../Knowledge/video-mode-settings.md)), so the Color Chrome Effect that carries this look is unavailable, compensate with Color.

| Setting | Value | vs stills |
|---|---|---|
| Film Simulation | Classic Chrome | same |
| White Balance | Auto, **+2R / −2B** | same |
| Dynamic Range | DR400 | same (no Auto DR in movie mode) |
| Highlight | −1 | same |
| Shadow | −1 | same |
| **Color** | **+2** | **+1 vs stills**, to offset the lost Color Chrome Effect |
| Sharpness | −1 | same |
| High ISO NR | −4 | same |
| Interframe NR | Auto | movie-only |
| ISO | Auto, 500–6400 | same |

Grain must be added in post if you want the texture.

---

## 8. Honest caveats for the client

1. These are graded photographs, not SOOC frames. They were almost certainly shot RAW and finished per-image in Lightroom, with per-scene control no in-camera recipe can match. This recipe reproduces the *shared colour signature*, expect a very close family resemblance, not a pixel match on any single frame.
2. The sources are compressed Instagram screenshots. Hue relationships are trustworthy; absolute saturation and grain are not. Settings here are anchored on hue behaviour and tone shape, which survive compression.
3. More than one photographer is represented (four-plus separate carousels), so no single preset produced all seven to begin with.
4. Not yet field-tested. This is a first-pass design from reference analysis. Shoot the recipe, drop frames into [`test-shots/`](test-shots/) next to the client's references, and it can be tuned, the WB shift and Color are the two dials most likely to move.

---

### Related work in the bank
- [Classic Chrome behaviour](../../Knowledge/film-simulations.md) · [WB shift grid](../../Knowledge/white-balance.md) · [DR & tone](../../Knowledge/dynamic-range-and-tone.md) · [Colour & chrome effects](../../Knowledge/color-and-chrome.md)
- Nearest existing recipes: [Kodak Gold 200](../../X-T5/originals/kodak-gold-200/recipe.md) (warmer, more nostalgic) · [Matte Editorial](../../X-T5/originals/creative/matte-editorial/recipe.md) (flatter, cooler) · [Golden Hour Glow](../../X-T5/originals/creative/golden-hour-glow/recipe.md) (warmer, less muted)
