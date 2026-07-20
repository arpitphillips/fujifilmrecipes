# Cinema Film Sims — the most notable and pleasing motion-picture stocks

Motion-picture film emulations for the X-T5. Selection isn't arbitrary — each stock was chosen because independent research (cinematographer commentary, published BSC praise, or a specific well-documented production) confirms it's genuinely notable and pleasing, not just "a Kodak stock that exists." See [`Knowledge/film-stocks-master-list.md`](../../../Knowledge/film-stocks-master-list.md) for the full research trail.

## Bases
Fujifilm's **Eterna** film simulation is a cine profile (low contrast, low saturation, rich/lifted shadow tone) built to mimic **negative** motion-picture stocks — the faithful base for the Vision3 camera negatives (**50D**, **250D**, **500T**).
The **2383 print** look needs teal shadows + print contrast + saturation, so it uses **Classic Negative** instead (native teal shadows) — the negative is Eterna, the *print* is Classic Neg.
**Ektachrome 100D** is a *reversal* (positive/slide) stock, not a negative — it uses **Provia** (Fuji's balanced-slide profile), the structurally correct analogue.
**Double-X** is B&W — it uses **Acros**, same as the bank's still-photo B&W family, but lives here because it's a cinema stock with cinema-specific grain/contrast targets, not a still-photography one.

## The stocks (grounded in Kodak technical data + verified critical consensus)

**The Vision3 family — clean modern negatives:**
- **[Vision3 50D](kodak-vision3-50d/)** (5203/7203) — *daylight-balanced (5500K)*, EI 50. Kodak's own **finest-grain** cinema stock — the cleanest image in the whole collection. Used on Sean Baker's *Red Rocket*; Vanessa Whyte BSC has publicly praised the family's highlight latitude (3–4 stops over, outdoors, and still holds).
- **[Vision3 250D](kodak-vision3-250d/)** (5207/7207) — daylight-balanced, EI 250. Clean, natural, everyday daylight cinema. Sub-Micron tech = **2 stops extended highlight latitude**; Dye Layering = reduced shadow grain. ECN-2.
- **[Vision3 500T](kodak-vision3-500t/)** (5219/7219) — tungsten-balanced (3200K), EI 500T/320D. The high-speed night/interior stock; outstanding skin, fine grain, wide DR. ECN-2. **CineStill 800T is this film with the remjet removed** (adds red halation glow, pushed to 800) — our [CineStill 800T](../../reference-recipes/cinestill-800t/) reference recipe is the *stylised* version; this Vision3 500T original is the *clean/accurate* version.

**The specialists — a reversal stock and a B&W classic:**
- **[Kodak Ektachrome 100D](kodak-ektachrome-100d/)** (5294/7294) — daylight-balanced, EI 100, **reversal** (E-6, slide-film process, not negative). "Moderately enhanced" saturation with accurate flesh tones and sharpness Kodak calls "unsurpassed by any other 100-speed reversal film." Used in **Poor Things (2023)** for its elevated, sensory colour.
- **[Kodak Double-X 5222](kodak-double-x-5222/)** — B&W negative, in continuous production since **1959**. *The* classic cinema black-and-white — *Raging Bull*, *Schindler's List*, *Manhattan*. RMS granularity 14 (moderately heavy), moderate contrast (control gamma 0.65–0.70), fast enough for dim available light.

**The print stock:**
- **[Kodak 2383 Print](kodak-2383-print/)** — the film **print stock** most theatrical release prints are struck on; the source of the classic "Hollywood" **teal-shadow / warm-skin** graded look. Very popular, very aesthetic.

## Validation status
- **Datasheet-validated:** ✅ all six, against archived official Kodak technical data sheets (balance, EI, latitude, grain/RMS, contrast/gamma, sharpness).
- **Characteristic-validated:** ✅ against **specific, named, independently-verifiable productions and cinematographer statements** (Red Rocket, Vanessa Whyte BSC, Raging Bull, Schindler's List, Manhattan, Poor Things) — a stronger evidence class than generic review consensus.
- **Real-scan validation:** ✅ Vision3 50D (2 real Wikimedia Commons scans, daylight + overcast). ⏳ Pending for the rest — actual cinema footage isn't Commons material (it's mostly copyrighted studio content), so real-footage validation for 250D/500T/Double-X/Ektachrome 100D/2383 needs a user-supplied reference frame (a shot from one of the cited films, or your own test footage) dropped into the relevant `references/` folder.

## Note on stills vs video
Cinema looks are most-used in **video** — but movie mode drops Grain, Color Chrome Effect, Color Chrome FX Blue, and Clarity (see [video-mode-settings](../../../Knowledge/video-mode-settings.md)). Each recipe has its own **stills** `recipe.md` and a separate **`recipe-video.md`**. Double-X loses the most in translation — its identity is substantially about heavy grain, which video mode can't render at all.

## Sources
- [Kodak Vision3 50D 5203/7203 technical data (PDF, archived)](../../../_reference-sources/datasheets/kodak-motion/vision3-50d-5203.pdf)
- [Kodak Vision3 250D 5207/7207 technical data (PDF)](https://www.kodak.com/content/products-brochures/Film/VISION3-250D-Technical-Data-EN.pdf)
- [Kodak Vision3 500T 5219/7219 technical data (PDF)](https://www.kodak.com/content/products-brochures/Film/VISION3_5219_7219_Technical-data.pdf)
- [Eastman Double-X 5222/7222 technical data (PDF, archived)](../../../_reference-sources/datasheets/kodak-motion/double-x_5222.pdf)
- [Kodak Ektachrome 100D 5294/7294 technical data (PDF, archived)](../../../_reference-sources/datasheets/kodak-motion/ektachrome-100d_5294.pdf)
- Characteristic research: [The Hollywood History of Iconic Kodak Film Stocks](https://www.filmmakersacademy.com/blog-hollywood-kodak-film-stocks/), reporting on *Red Rocket*, Vanessa Whyte BSC, *Raging Bull*, *Schindler's List*, and *Poor Things* (fetched 2026-07-16).

> **Officially confirmed:** Fujifilm's own Eterna page states the sim deliberately looks "weak" as isolated stills. It is an ungraded cinema canvas meant for a finishing layer, "opening the door" to post-production. That is first-party validation of this family's approach: the Color lifts, CCE Strong and tone shaping in these recipes are the finishing grade. See [fujifilm-official-design-notes](../../../Knowledge/fujifilm-official-design-notes.md).
