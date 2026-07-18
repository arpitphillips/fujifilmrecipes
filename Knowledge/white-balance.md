# White Balance & WB Shift, the colour-cast control

White Balance (WB) sets the overall colour temperature/tint of the image, and the WB Shift grid nudges it precisely. In recipes, WB + shift is the single most important control for the *colour cast* of the grade (warm/cool, green/magenta).

## WB base options (manual p.126)

| Option | Manual description / use |
|---|---|
| **AUTO WHITE PRIORITY** | Auto WB tuned for *whiter* whites under incandescent light (removes warmth) |
| **AUTO** | Standard automatic white balance |
| **AUTO AMBIENCE PRIORITY** | Auto WB that *keeps* warmth under incandescent light |
| **CUSTOM 1–3** | Measure a manual WB value from a grey/white reference |
| **COLOR TEMPERATURE (K)** | Pick an explicit Kelvin value (e.g. 5200K, 5800K) |
| **DAYLIGHT** | Fixed for direct sunlight (~5500K) |
| **SHADE** | Fixed for shade (warmer) |
| **FLUORESCENT 1/2/3** | "Daylight", "warm white", "cool white" fluorescent |
| **INCANDESCENT** | For tungsten/incandescent lighting |
| **UNDERWATER** | Reduces underwater blue cast |

### Fixed vs Auto in recipes
- A fixed WB (Daylight, a Kelvin value, or a Fluorescent preset) gives a *consistent, repeatable* cast shot-to-shot, essential when the grade depends on a specific colour balance (most Kodak recipes use Daylight or a Kelvin value).
- Auto WB adapts per scene, so the cast floats with the light. Chosen when versatility matters more than repeatability (e.g. Reggie's Portra, Reala Ace).
- Fluorescent presets are used *creatively*, not literally, e.g. CineStill 800T uses Fluorescent 3 to push a cool tungsten-night cast, not because the scene is fluorescent-lit.

## WB Shift (manual p.127)

After choosing a WB option, pressing MENU/OK opens the WB SHIFT grid with two axes:

- R (Red) axis: positive = warmer/redder, negative = cooler/cyan.
- B (Blue) axis: positive = bluer/cooler, negative = warmer/yellow.

Recipes write this as e.g. "Daylight, +2 Red & -5 Blue" → warm it up on the red axis (+2R) *and* remove blue / add yellow (-5B). The two axes together place the cast anywhere in the red–cyan / blue–yellow plane.

### Reading a shift
- +R and −B together → strong warm/golden cast (classic Kodak-negative warmth). Example: Kodak Gold 200 uses Daylight +4R / −5B.
- −R and +B → cool, cyan-blue cast (e.g. an overcast/"Pacific" look).
- Small values (±1–2) fine-tune; larger values (±5 to ±9) are a deliberate strong tint.

> The grid is limited to ±9 on each axis. On monochrome bases the shift still applies a *toning* direction but has little effect on the grey tones themselves; some B&W recipes carry a large shift mostly as a carry-over/toning nuance.

## Why WB matters more than "Color" for a grade

Saturation (Color) changes *how intense* colours are; WB shift changes *what colour everything leans toward*. A grade's identity, "warm faded Kodak", "cool moody blue", "amber vintage", is set primarily by the WB base + shift, then reinforced by the film-sim base and the Chrome effects. See [color-and-chrome.md](color-and-chrome.md).
