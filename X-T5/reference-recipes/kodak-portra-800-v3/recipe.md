# Kodak Portra 800 v3 — Fujifilm X-T5 (X-Trans V) · STILLS

Status: Reference capture (attributed), for testing/benchmarking, not yet re-derived as an original.
Source/credit: [Fuji X Weekly (Ritchie Roesch)](https://fujixweekly.com/2024/02/14/kodak-portra-800-v3-fujifilm-x-t5-x-trans-v-x-e4-x-trans-iv-film-simulation-recipe/)

Emulates the higher-speed pro portrait negative Kodak Portra 800, warmer, grainier, moodier than Portra 400, good in lower/mixed light. Classic Chrome base.

| Setting | Value |
|---|---|
| Film Simulation | Classic Chrome |
| Grain Effect | Strong, Large |
| Color Chrome Effect | Strong |
| Color Chrome FX Blue | Off |
| White Balance | 6600K, −1 Red & −3 Blue |
| Dynamic Range | DR400 |
| Highlight | −2 |
| Shadow | −0.5 |
| Color | +3 |
| Sharpness | −2 |
| High ISO NR | −4 |
| Clarity | −3 |
| ISO | Auto, up to ISO 6400 |
| Exposure Compensation | +1/3 to +1⅓ (typically) |

### Sensor-generation translation (from source)
- X-Trans V (X-T5): as listed (Color Chrome FX Blue Off).
- X-Trans IV (X-T4, X-S10, X-E4, X-T30 II): set Color Chrome FX Blue Weak (V renders Classic Chrome blues deeper; see [x-trans-v-and-conversion](../../../Knowledge/x-trans-v-and-conversion.md)).
- X-Trans III (X-Pro3/X100V etc.): set Shadow 0 instead of −0.5.

> **Datasheet check (2026-07-15):** Kodak E-4040 specifies "very fine grain" for Portra 800, Grain Strong/Large overstates the emulsion (reads like a 1600–3200 stock); the soft H−2 highlights and warm balance do match. Deviation consistent with the scanned/pushed look. See [VALIDATION-AUDIT.md](../../VALIDATION-AUDIT.md).

> **Pro note (official, 2026-07-20):** Fujifilm states Classic Chrome's curve is asymmetric, "the shadow end is hard, but the tonality is soft on the highlight end." This recipe's strongly negative Highlight is therefore added softness on an end that is already soft, which is why highlights here can read flat or milky in bright scenes. If that happens, raise Highlight by a step before touching anything else; you will lose less than you expect. The hard shadow end is conversely why the low Shadow values still hold detail. See [TONE-CURVE-AUDIT.md](../../TONE-CURVE-AUDIT.md).

> **Scan pass attempted 2026-07-20, evidence found but judged not usable.** Two genuine Portra 800 frames were located and analysed (Wikimedia Commons, analysis-only; the stock confirmed by the rebate edge-markings visible in the scan itself): a Bangalore bus terminal in flat daylight, and a Marathalli Bridge night long-exposure. Both were set aside, because both were shot on a toy fisheye (heavy vignetting, soft corners, likely light leaks) and the night frame is dominated by uncorrected sodium-vapour lighting that swamps everything in yellow-green. The lens and the light overwhelm the film's own signature, so counting either would be fitting to an artifact. Recorded as seen, deliberately not counted; this recipe remains unvalidated by scan. See the [Commons scan index](../../_reference-sources/COMMONS-SCAN-INDEX.md).
