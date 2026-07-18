# Fujicolor Pro 400H — Fujifilm X-T5 (X-Trans V) · STILLS

Research-backed original, derived from the Fujifilm Pro 400H datasheet (archived: [`_reference-sources/datasheets/fujifilm/fujicolor-pro-400h.pdf`](../../_reference-sources/datasheets/README.md)) and a [dedicated video comparison of real Pro 400H scans vs the PRO Neg. Hi simulation](../../../Knowledge/pro400h-vs-proneghi-analog-comparison.md). Reproduces the discontinued (2021/2022) wedding-photographer favourite: extraordinarily fine grain, cool-to-neutral skin, controlled shadow saturation with a distinctive cyan-green cast, and one of the longest highlight shoulders of any colour negative. Derivation in [`knowledge.md`](knowledge.md).

| Setting | Value |
|---|---|
| Film Simulation | PRO Neg. Hi |
| Grain Effect | Weak, Small |
| Color Chrome Effect | Off |
| Color Chrome FX Blue | Weak |
| White Balance | Daylight, −1 Red & +2 Blue |
| Dynamic Range | DR400 |
| Highlight (Tone Curve) | −2 |
| Shadow (Tone Curve) | −1 |
| Color | 0 |
| Sharpness | −1 |
| High ISO NR | −4 |
| Clarity | 0 |
| ISO | Auto, up to ISO 6400 |
| Exposure Compensation | 0 to +1/3 (typically) |

### Why these values (short)
- PRO Neg. Hi base: the closest built-in match to Pro 400H's reduced-contrast, neutral-to-cool skin register (confirmed against real Pro 400H scans in the linked comparison).
- Grain Weak/Small: datasheet: diffuse RMS granularity 4, the finest grain of *any* film in this bank (finer even than Ektar or Acros).
- WB Daylight −1R/+2B: the comparison found Pro Neg. Hi reads slightly warmer/more neutral than the real film's blue-green shadow cast; this shift pulls it cooler to compensate.
- CCFXB Weak (not Off), adds back the cyan-green depth in shadows/greens that the base simulation lacks natively; this is the single biggest correction identified by the video comparison.
- DR400 + Highlight −2: models "one of the longest shoulder curves in professional colour negative film", highlights hold detail far beyond typical negative stocks.
- Shadow −1: natural lift; Pro 400H never crushes blacks.
- Color 0, CCE Off: datasheet: "appropriately controlled color saturation in the shadows" for a three-dimensional feel, not a saturated film.
- Sharpness −1: softer acuity than digital, per the comparison.
- Clarity 0: per quality standard; nothing calls for grit.

### Handling
- Best for portraits, weddings, overcast/mixed light: this was the wedding-industry standard for a reason: forgiving, cool-neutral, flattering without being punchy.
- Wide real-world latitude (often rated 200–320 by film shooters for smoother gradation), slight overexposure is safe.

Validation tier: Datasheet-validated (RMS 4, controlled shadow saturation, wide latitude, archived PDF) + characteristic-validated against an existing side-by-side video analysis of real film vs the Fuji simulation (see [pro400h-vs-proneghi-analog-comparison.md](../../../Knowledge/pro400h-vs-proneghi-analog-comparison.md)), the strongest non-scan evidence base in the bank, since it's a direct film-vs-simulation study rather than film alone. Scan-validation (additional independent scans) still pending; drop scans into [`references/`](references/).
