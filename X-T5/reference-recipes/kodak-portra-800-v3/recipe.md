# Kodak Portra 800 v3 — Fujifilm X-T5 (X-Trans V) · STILLS

**Status:** Reference capture (attributed) — for testing/benchmarking, not yet re-derived as an original.
**Source/credit:** [Fuji X Weekly (Ritchie Roesch)](https://fujixweekly.com/2024/02/14/kodak-portra-800-v3-fujifilm-x-t5-x-trans-v-x-e4-x-trans-iv-film-simulation-recipe/)

Emulates the higher-speed pro portrait negative **Kodak Portra 800** — warmer, grainier, moodier than Portra 400, good in lower/mixed light. Classic Chrome base.

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
- **X-Trans V (X-T5):** as listed (Color Chrome FX Blue **Off**).
- **X-Trans IV** (X-T4, X-S10, X-E4, X-T30 II): set Color Chrome FX Blue **Weak** (V renders Classic Chrome blues deeper — see [x-trans-v-and-conversion](../../../Knowledge/x-trans-v-and-conversion.md)).
- **X-Trans III** (X-Pro3/X100V etc.): set Shadow **0** instead of −0.5.

> **Datasheet check (2026-07-15):** Kodak E-4040 specifies "very fine grain" for Portra 800 — Grain Strong/**Large** overstates the emulsion (reads like a 1600–3200 stock); the soft H−2 highlights and warm balance do match. Deviation consistent with the scanned/pushed look. See [VALIDATION-AUDIT.md](../../VALIDATION-AUDIT.md).
