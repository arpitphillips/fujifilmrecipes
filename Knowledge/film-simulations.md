# Film Simulations — the base profiles

The Film Simulation is the **master colour/contrast profile**. Every other setting is a modifier layered on top of it, so the base you pick determines the fundamental character of the grade. Fujifilm's own one-line descriptions (from the X-T5 manual, p.122–123) are given first, then the practical grading character.

> **Deep dives:** the per-simulation spectral behaviour, the 2003–2020 history of the simulations, and why they can't be recreated in Photoshop live in [color-science-why-film-cannot-be-faked.md](color-science-why-film-cannot-be-faked.md); the underlying film chemistry is in [film-chemistry-fundamentals.md](film-chemistry-fundamentals.md).

## The colour bases

### PROVIA / STANDARD
- **Manual:** "Ideal for a wide range of subjects."
- **Character:** The neutral reference. Medium contrast, medium saturation, accurate-but-pleasing colour. Everything else is best understood as a departure from Provia.

### Velvia / VIVID
- **Manual:** "Vibrant reproduction, ideal for landscape and nature."
- **Character:** High saturation + high contrast slide-film look (named after Fuji's Velvia transparency film). Punchy blues and greens, deep shadows. Can overwhelm skin tones. In recipes it's used for bold, saturated grades — often tamed with negative Color.

### ASTIA / SOFT
- **Manual:** "Softer color and contrast for a more subdued look."
- **Character:** Gentle contrast, restrained saturation, especially flattering, soft skin tones. A good base for calm, muted, or pastel grades.

### CLASSIC CHROME
- **Manual:** "Soft color and enhanced shadow contrast for a calm look."
- **Character:** The workhorse of the recipe world. Muted, slightly desaturated colour with a distinctive **shadow contrast bump** and a documentary/editorial (Kodachrome-ish) feel. Skews colours subtly — reds go brick, blues go muted. This is the base for the majority of Kodak-branded colour recipes (Kodachrome, Portra, Gold). See how many recipes lean on it.

### PRO Neg. Hi
- **Manual:** "Ideal for portrait with slightly enhanced contrast."
- **Character:** A colour-negative portrait profile with a touch more contrast/pop than Pro Neg Std. Studio/portrait oriented.

### PRO Neg. Std
- **Manual:** "Ideal for portrait with soft gradations and skin tones."
- **Character:** The flattest, most forgiving portrait profile. Very smooth tonal gradations, natural skin. A base for neutral, low-contrast looks.

### CLASSIC Neg.
- **Manual:** "Enhanced color with hard tonality to increase image depth."
- **Character:** Modelled on Fujicolor Superia consumer negative film. Punchy but "crunchy" — hard tonality, colour separation that shifts hues (notably cyan-leaning blues/greens and amber reds). Loved for a nostalgic snapshot look. Base for Pacific Blues, Reala Ace, Fujicolor recipes.

### NOSTALGIC Neg.
- **Manual:** "Amber tinted highlights and rich shadow tone for printed photo look."
- **Character:** Warm amber highlights + deep, rich shadows — the look of an old printed photo / 1970s American New-Color aesthetic. Base for California Summer, 1976 Kodak, etc.

### ETERNA / CINEMA
- **Manual:** "Soft color and rich shadow tone suitable for film look movie."
- **Character:** Low-contrast, low-saturation cine profile with lifted, rich shadows. Muted and moody. Base for cinematic and CineStill-style recipes.

### ETERNA BLEACH BYPASS
- **Manual:** "Unique color with low saturation and high contrast. Suitable for still and movie."
- **Character:** Simulates the bleach-bypass film process — very desaturated but *high* contrast, silvery and gritty. Dramatic, editorial.

## The monochrome bases

### ACROS
- **Manual:** "Shoot in Black and White in rich details with sharpness." Available as **ACROS**, **ACROS+Ye**, **ACROS+R**, **ACROS+G**.
- **Character:** The premium B&W profile — richer tonality, finer perceived grain structure, and better detail than plain Monochrome. The colour-filter suffix mimics shooting B&W film through a coloured filter:
  - **+Ye (Yellow):** slightly more contrast, darkens skies a little. The classic all-rounder.
  - **+R (Red):** strong contrast, dramatically darkened skies, lightened reds.
  - **+G (Green):** flatters skin tones in portraits.

### MONOCHROME
- **Manual:** same filter options as Acros (+Ye/+R/+G) but without Acros's advanced grain/tonality processing. A cleaner, flatter B&W.

### SEPIA
- **Manual:** "Shoots in sepia tone." Fixed warm monochrome.

> Both Acros and Monochrome can take a **Monochromatic Color** tint (warm/cool + green/magenta) — see [color-and-chrome.md](color-and-chrome.md).

## Which base → which family of looks

| Base | Typical grade family |
|---|---|
| Classic Chrome | Kodak slide/negative emulations (Kodachrome, Portra, Gold), muted editorial |
| Classic Neg. | Fujicolor/Superia, punchy nostalgic snapshots (Pacific Blues, Reala Ace) |
| Nostalgic Neg. | Warm vintage / 70s printed-photo looks |
| Eterna | Cinematic, moody, CineStill-style |
| Velvia | Bold saturated landscapes |
| Astia / Pro Neg Std | Soft portraits, pastel/muted grades |
| Acros | All serious black & white |

> **Note on Reala Ace:** The X-T5 (X-Trans V) has an *actual* film simulation called **Reala Ace** in some recipes. Where a recipe predates that film sim's arrival on X-series, "Reala Ace" is instead *approximated* on a Classic Negative base — the recipe file will state which base it uses.
