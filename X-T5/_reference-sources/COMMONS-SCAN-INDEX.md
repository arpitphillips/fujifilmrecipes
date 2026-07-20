# Open-source scan index: what genuine film scans exist on Wikimedia Commons

**Swept 2026-07-20.** A systematic search of Wikimedia Commons for real photographs shot on each film stock in the bank, not box shots, not product photography, not software presets.

**Why this file exists:** every scan-validation pass so far has started by re-discovering what's available. This is the standing answer, so future passes start from a list instead of a search.

---

## How to read it

| Mark | Meaning |
|---|---|
| ✅ | Genuine scans confirmed — description explicitly names the stock |
| ⚠️ | Hits exist but attribution is unverified or the stock is ambiguous |
| ❌ | Nothing genuine — only box/product shots, or no results |

**The verification rule that matters:** Commons search matches *filenames and descriptions*, so a search for a film name returns box photographs, camera photos with the film mentioned in passing, and unrelated words. **Always confirm the description says the photo was *shot on* the stock before analysing it.** Traps caught so far:

- "Ektachrome ELITE 100 5045 EB": a different 1990s consumer film, not the 2018 E100 reissue.
- "Frozen Laundry (Slide film)": categorised as film, but tagged Nikon D750, a digital body.
- "Kodak Ektar 100 - DXO PhotoLab" / "Ilford Pan F Plus 50 - DXO PhotoLab", software simulations of the film, not the film. Rejected previously and again here.
- "Kodachrome 25"-labelled frames returned by a Kodachrome 64 search, right family, wrong emulsion.
- "Fortia": returns *Fortià*, a Catalan town. Zero film results.

---

## Findings by stock

### ✅ Confirmed genuine scans available

| Stock | What's there | Used? |
|---|---|---|
| **Fujifilm Acros 100** | A **Cospuden lake series** (Canon EOS 300, Neopan Acros 100) — several frames, one photographer, varied subjects | 2 used earlier; **more available** |
| **Ilford Delta 3200** | Multiple photographers: Holga 120 frames (RNC St Paul), *Locarno Festival* (Leica), *New Orchardfield* (Ricoh GR1) | 2 used — **best multi-photographer coverage in the bank** |
| **Fujicolor Pro 400H** | *Leaf* (Rolleiflex SLX) — overcast, foliage, neutral rail | ✅ used 2026-07-20 (first ever pixel evidence) |
| **Kodak Vision3 50D** | *Новое Село Раменский район 2020-05* — explicitly "Kodak Vision3 50D" | 2 used earlier |
| **Kodak Vision3 (unspecified)** | **RZD Vesyegonsk 2020-12 series** — 5+ frames "at kodak vision 3", stock variant not specified | ⚠️ unused — variant unknown |
| **Kodak Gold 200** | *Kukës on 35mm film, November 2021* ×2 (Zenith 11, expired Gold 200) | not needed — already ~35-scan validated |
| **Kodak Portra 800** | Bangalore frames (*Majestic bus terminal* daylight, *Marathalli Bridge* night), 120 **toy fisheye** | ❌ **examined 2026-07-20 and rejected** — see below |
| **Kodak Ektachrome E100** | *Maasvlakte at blue hour*, *Oberschloss Kranichfeld* | 2 used 2026-07-20 |
| **Kodak Portra 400** | *Ikarus 250 coach* | 1 used earlier |
| **Kodak Tri-X 400** | HABS panoramic architectural survey frames on Tri-X; expired-stock frames | ⚠️ unused — mostly archival/technical subjects |

### ⚠️ Thin or ambiguous

| Stock | Situation |
|---|---|
| **Ilford HP5 Plus** | Mostly box shots. One converted negative (*ILFORD HP5 PLUS SAFETY FILM*) — usable but atypical |
| **Ilford Pan F Plus 50** | **No genuine scans.** Top hits are box shots and a **DXO software preset** |
| **Ilford FP4 Plus** | Box/packaging shots only |
| **Kodak T-Max** | Box shots dominate |
| **Kodak UltraMax 400** | Box shots dominate; a few candidate frames unverified |
| **Kodachrome 64** | Family results only — K25, K40A, K200, Kodachrome II. **Careful: verify the exact emulsion** |
| **Velvia / Provia** | Packaging photos dominate the results |

### ❌ Nothing usable

| Stock | Situation |
|---|---|
| **Fujichrome Fortia SP** | Zero. Search returns *Fortià*, a Catalan town. Japan-only limited run, 2004–07 |
| **Kodak Double-X 5222** | No frame-grabs — real motion-picture footage isn't Commons material |
| **Kodak Ektachrome 100D** | Same — cinema stock, no Commons frames |
| **Kodak 2383 print** | Same — a print stock, seen only in projection |

---

---

## A third trap: genuine scans that are still bad evidence

Verifying the *stock* is only half the job. A frame can be provably shot on the right film and still be useless, because something other than the emulsion is driving the image.

**Worked example, Kodak Portra 800, examined and rejected 2026-07-20.** Both Commons frames were confirmed Portra 800 (the rebate edge-markings "KODAK PORTRA 800" are visible in the scan itself, the strongest attribution available). They were still set aside:

- Both were shot on a toy fisheye, heavy vignetting, soft corners, probable light leaks.
- The night frame is drowned in uncorrected sodium-vapour street lighting, which swamps everything in yellow-green.

Neither tells you what Portra 800 does; they tell you what a plastic lens and a sodium lamp do. Counting them would have been fitting to an artifact, and would have "upgraded" the recipe's status on evidence that means nothing.

**The check to run on every candidate, after attribution:**
1. Lens: toy/plastic/expired-adapted optics impose vignetting, softness and flare that read as film character.
2. Light source: uncorrected sodium, mercury or mixed lighting overwhelms the emulsion's own colour.
3. Process: cross-processing, heavy expiry, or push/pull changes the result more than the stock does.
4. Scan: the scanner and operator shift colour as much as the film. Prefer frames where the pipeline is stated.

**A frame that fails any of these is worth recording as *seen and rejected*, not silently ignored**, otherwise the next pass re-finds it and has to re-reason about it.

---

## Where to look next (Commons is now largely exhausted)

Commons skews toward European, daytime, architectural and technical subjects, by a small number of prolific film photographers. That produces two systematic gaps across the whole bank:

1. Almost no skin tones or portraits: the single most valuable missing evidence, and the hardest thing to judge in a recipe.
2. Little golden hour, little tungsten/night, little tropical or high-UV light: which is why the Mumbai recipes could never be Commons-validated.

Better sources for those, in rough order of value:
- Flickr: vast film-photography community, EXIF and tags often name the stock; static URLs are directly fetchable.
- User drops into each recipe's `references/` folder: still the highest-quality path, and the only one that can supply portraits.
- Lab galleries (film labs publish scans organised by stock).
- Reddit r/analog, excellent material, but blocked in this environment (403 on API and WebFetch; needs OAuth).

---

*Last updated: 2026-07-20*
