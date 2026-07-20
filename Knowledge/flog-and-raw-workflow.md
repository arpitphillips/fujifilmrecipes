# F-Log, F-Log2 & RAW editing: the X-T5 workflow

*Camera specifics verified against the X-T5 Owner's Manual (F-Log/HLG RECORDING p.194, DATA LEVEL SETTING p.195, F-Log VIEW ASSIST p.287, specifications pp.~470+). Claims not from the manual are marked.*

---

## 1. F-Log vs F-Log2: which to shoot

| | **F-Log** | **F-Log2** |
|---|---|---|
| **ISO range (manual)** | **500 – 12800** | **1000 – 12800** |
| Dynamic range | ~12 stops | **13+ stops** *(Fujifilm's claim, not in the manual)* |
| Best for | Most work; easier grade | High-contrast scenes, heavy grading, HDR finish |
| Cost | Slightly less shadow latitude | Noisier shadows; **needs 10-bit and real light control** |

The decision rule: F-Log2 buys latitude you only get to keep if you grade properly and shoot 10-bit. If the footage is going out fast, or lighting is controlled, F-Log is the better tool, less noise, faster grade, fewer ways to go wrong.

> ⚠️ The biggest practical gotcha: the ISO floor. F-Log2 cannot go below ISO 1000. In daylight at 1/50 s and a wide aperture, that is wildly overexposed. You *must* carry ND filters (a variable ND, or fixed 3/6-stop). This single constraint catches more people than anything else in the log workflow. F-Log's floor of ISO 500 is one stop friendlier but still needs ND outdoors.

---

## 2. Shooting settings on the X-T5

- Codec: H.265, 10-bit 4:2:2. Never shoot log in 8-bit, log stretches tonality across fewer code values and banding appears the moment you grade. The X-T5 records 10-bit 4:2:2 internally (H.265, ALL-I or Long GOP, up to 360 Mbps).
  - ALL-I for heavy grading / lots of cuts (bigger files, easier on the timeline).
  - Long GOP for longer takes and smaller files.
- DATA LEVEL SETTING (p.195): the silent killer. Options:
  - `VIDEO RANGE`, 10-bit 64–940 (8-bit 16–235)
  - `FULL RANGE`, 10-bit 0–1023 (8-bit 0–255)

  Pick one and make your NLE agree. A mismatch shows up as crushed blacks and clipped highlights *before you've touched a grade*, and it is very often misdiagnosed as bad exposure. `VIDEO RANGE` is the safer default for a standard Resolve/Premiere workflow.
- F-Log VIEW ASSIST, turn it ON (p.287). It shows a BT.709-corrected preview while recording. Judging exposure on a flat log image is guesswork; this makes the monitor honest. It affects the preview only, never the recording.
- Expose to the right, deliberately. Log protects highlights and hides noise in the shadows. Rate F-Log2 +2/3 to +1 stop over the meter and pull it back in post, shadow noise at ISO 1000+ is the real enemy, not highlight clipping.
- White balance: set it manually. Auto WB drifting shot-to-shot is far more painful to fix in a log grade than a slightly-off fixed value. Use a grey card or a preset K value and stay there.
- Movie mode has no Grain, Color Chrome Effect, Color Chrome FX Blue or Clarity: see [video-mode-settings.md](video-mode-settings.md). All texture work happens in post.

---

## 3. Post workflow: Resolve & Premiere

The correct order of operations. Log grading goes wrong when steps are done out of sequence:

1. Set the project colour management first, before anything else.
   - *Resolve:* Colour Science DaVinci YRGB Color Managed, Input = Fujifilm F-Log / F-Log2 (or apply the input transform per-clip), Timeline = DaVinci WG, Output = Rec.709 Gamma 2.4.
   - *Premiere:* Lumetri → Basic → Input LUT, then grade in the tabs below.
2. Conversion LUT next, as a normalising step, not a look. Ready-made LUTs built from Fujifilm's official transfer functions are in [`luts/`](luts/README.md) (verified against the datasheet's published code-value anchors). Fujifilm also publishes its own official LUTs at [dl.fujifilm-x.com](https://dl.fujifilm-x.com/) if you prefer a vendor-blessed conversion.
3. Balance before you style. Fix exposure and white balance *under* the LUT (in Resolve, a node before it), never on top of it. Correcting above a display transform fights the curve.
4. Then grade the look.
5. Grain last, on the finished image: never before the conversion.

> **Node order in Resolve:** `Input transform → Balance/Exposure → Look → Grain → Output transform`. Getting grain or look ahead of the transform is the most common reason graded Fujifilm footage looks "thin".

Matching a motion-picture stock (Vision3 250D/500T, 2383, Double-X): the grain is the missing ingredient, and it is what the [cinema recipes](../X-T5/originals/cinema/) cannot deliver in-camera because movie mode has no Grain control. Resolve's Film Grain OFX or a scanned 35mm grain plate over the finished grade does more for perceived authenticity than any amount of colour work.

---

## 4. When *not* to shoot log

Eterna is a genuine alternative, not a compromise. Fujifilm states Eterna carries a 12-stop dynamic range, "comparable to F-Log," with "room for post production" ([official design notes](fujifilm-official-design-notes.md)).

So for most work you can shoot Eterna and get near-log latitude with a usable, gradeable image straight off the card, no conversion LUT, no ISO floor, no ND juggling, and the [cinema recipes](../X-T5/originals/cinema/) already do the colour work for you. Reach for F-Log2 when you genuinely need the extra stop and are committed to a full grade.

---

## 5. RAW editing: the part most people get wrong

Lightroom's "film simulation" profiles are Adobe's approximations, not Fujifilm's processing. They are reverse-engineered profiles, not the real conversion. This matters more than it sounds: Fujifilm's Image Design team describes a simulation as *"converting the raw signal while understanding the difference of the spectral sensitivity"*, a spectral-aware conversion of the raw sensor signal. By the time a file has been demosaiced and handed to Lightroom, that step has already happened and cannot be re-run. (See [why film cannot be faked](color-science-why-film-cannot-be-faked.md).)

Three ways to develop a Fujifilm RAW, best first:

1. In-camera RAW conversion: `PLAYBACK MENU → RAW CONVERSION`. Uses the camera's own X-Processor 5. Output is byte-for-byte the real thing, because it *is* the real thing. You can change film simulation, WB, DR, tone, colour, grain, everything, then save a new JPEG.
2. FUJIFILM X RAW Studio (free, desktop), tethers to the camera over USB and uses the camera's processor to render. Same fidelity as in-camera, but with a proper monitor, mouse and file management. This is the single most underused tool for this bank.
3. Lightroom / Capture One: best editing ergonomics, but the film simulation is an approximation. Fine for exposure/crop/retouch work; not a source of truth for how a recipe actually renders.

### The workflow this bank is built around
Shoot FINE + RAW. The JPEG carries the baked recipe, the archival primary. The RAW is your safety net: if a recipe was wrong for the light, re-develop that frame through any other recipe in the bank via in-camera conversion or X RAW Studio, and get a genuine result rather than an emulation.

One shoot, every look in the bank, all authentic. That is the practical payoff of the whole "in-camera JPEG is the primary" philosophy.

> **Pro tip:** X RAW Studio is also the fastest way to *develop* a new recipe. Shoot one RAW of a reference scene, then iterate settings against it on a big screen with instant feedback, instead of re-shooting the scene for every tweak.

---

## 6. RAW video: the maximum-quality cinematic path, and its cost

*Verified against the X-T5 manual, RAW OUTPUT SETTING p.192, and the HDMI specification block.*

The X-T5 can output 12-bit RAW over HDMI to an external recorder:

| Menu option | Recorder | Produces |
|---|---|---|
| `RAW OUTPUT SETTING → ATOMOS` | Atomos (Ninja V+ / Ninja Ultra) | **Apple ProRes RAW** |
| `RAW OUTPUT SETTING → Blackmagic` | Blackmagic Video Assist 12G | **Blackmagic RAW** |

### The asymmetry that matters for this bank

Stills RAW keeps your recipes. Video RAW throws them away.

- A RAF stills file can be re-developed through the camera's own processor ([§5](#5-raw-editing--the-part-most-people-get-wrong)), every recipe in this bank remains available, genuinely, forever.
- RAW video output states plainly: "In-camera image enhancements are not applied to the RAW output." No film simulation. No Eterna. No cinema recipe. The entire recipe bank is bypassed, by design.

That is not a flaw, it is the point of RAW. But it means "cinematic" via RAW video and "cinematic" via this bank are two different projects. RAW video hands you maximum latitude and zero look; the cinema recipes hand you a finished look with less latitude. Choose deliberately.

### The constraints (manual, p.192)

- Frame size is forced to 6.2K.
- Nothing is recorded to the memory card: the external recorder is your only copy. No backup, no safety take.
- ISO is restricted to 800–12800. Same ND-filter problem as F-Log2, one stop worse.
- Focus zoom is unavailable while RAW HDMI output is active, check focus before you roll.
- Disabled in some movie and high-speed modes.
- Fujifilm's own caveat: output quality "varies with device specifications" and may not equal a full post-production result.

### Which RAW, if you use Resolve

Blackmagic RAW is the stronger choice for a Resolve workflow. It decodes natively, plays back far more efficiently, and exposes ISO and white balance as *editable metadata* after the fact. You can genuinely re-rate a shot in post. ProRes RAW is better served in Final Cut and Premiere; Resolve's support for it has long been the weak spot. If you already live in Resolve, the Blackmagic Video Assist path is the less painful one.

### Is it actually worth it?: an honest ladder

| Tier | Shoot | You get | Cost |
|---|---|---|---|
| 1 | **Cinema recipe** (Eterna base) | Finished cinematic look, straight off the card, 12 stops | Baked in — limited regrade |
| 2 | **F-Log2** | ~13 stops, full grading freedom, internal 10-bit | ND filters, ISO 1000 floor, a real grade required |
| 3 | **RAW HDMI** | Maximum latitude, editable ISO/WB, 12-bit 6.2K | External recorder + rig + cables + power, no card backup, ISO 800 floor, no film simulation at all |

The honest recommendation: RAW video only produces a "masterpiece" if the grade is where your craft actually lives. If it isn't, tier 3 buys you a heavier rig and a longer edit for a result that a well-shot Eterna or F-Log2 file would have matched. The [cinema recipes](../X-T5/originals/cinema/) exist precisely because Fujifilm's own colour science is worth more than most people's grading.

Where RAW genuinely wins: mixed or unfixable lighting (editable WB saves the shoot), extreme highlight recovery, heavy VFX/keying work, and any project where a colourist is doing the finishing.

### If you do shoot RAW video

1. Rig for it: recorder, HDMI cable strain relief, external power. HDMI is the fragile link; a knocked cable ends the take with nothing on the card.
2. Shoot a grey card and a colour chart at the head of each setup. Editable WB is RAW's best feature and a chart makes it exact rather than approximate.
3. Expose for the highlights. ISO 800 base with 12-bit depth gives generous shadow recovery; clipped highlights are still gone.
4. Match to your JPEG stills: grade the footage toward the [cinema recipe](../X-T5/originals/cinema/) you would otherwise have shot. Those recipes are, in effect, Fujifilm's own reference grade for the look.
5. Grain last: 6.2K RAW is clinically clean. Motion-picture stocks are not. See [§3](#3-post-workflow--resolve--premiere).


*Last updated: 2026-07-20*
