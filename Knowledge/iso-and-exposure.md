# ISO & Exposure, Auto-ISO, exposure compensation, and DR interaction

These aren't part of the colour "grade" per se, but they're specified in every recipe because they affect the *rendered* result and the film feel.

## Auto-ISO ("Auto, up to ISO 6400")

Most recipes cap Auto-ISO at 6400. Reasons:
- Keeps noise within a filmic-but-clean range on the X-T5's 40MP sensor.
- The specified Grain Effect plus the natural high-ISO texture then reads as "film grain" rather than digital noise.
- You can raise the ceiling; the recipe value is a sensible default, not a hard rule.

There is a minimum ISO interaction with Dynamic Range (see below), which is why the *floor* of Auto-ISO effectively rises when DR200/DR400 is used.

## Dynamic Range forces an ISO floor (manual p.130)

This is the most important ISO caveat:

| Dynamic Range | Minimum ISO the camera will use |
|---|---|
| DR100 | base (ISO 125) |
| **DR200** | **ISO 250** |
| **DR400** | **ISO 500** |

So a DR400 recipe can never shoot below ISO 500 even in bright light, the camera raises ISO to buy the highlight headroom. This is intended: the slight extra noise is part of the film-negative latitude look, and it's why DR400 recipes pair naturally with grain.

## Exposure Compensation ("typically…")

Recipes list a suggested exposure-compensation range, e.g. "+1/3 to +1 (typically)". On the X-T5 this is set with the top exposure-comp dial (or the front command dial when the dial is at C, giving ±5 EV).

Essential framing (straight from the recipe authors):
- The suggested value is a starting point, not a rule. It reflects how a given grade tends to want to be exposed (e.g. negative-film emulations are often exposed + to lift shadows and get clean, bright mid-tones the way you'd overexpose colour negative film).
- Judge every scene individually. Highlight-protecting recipes (DR400) tolerate positive exposure comp well; contrasty scenes may want less.
- Some authors (e.g. Reggie's Portra) deliberately give no suggested exposure comp, insisting each frame be metered on its own.

## Why "expose to taste" works here

Because the look is baked into the JPEG, exposure at capture is part of the grade: pushing exposure + brightens and further "fades" a low-contrast recipe; pulling − deepens and saturates it. Treat exposure compensation as the final creative dial that positions the baked-in grade where you want it for the scene.
