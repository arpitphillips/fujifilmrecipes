# System Changelog

**Every Claude agent (and human) working in this repo must log their changes here.** Newest entries at the top. This is the repo's memory — read the recent entries before making changes so you don't undo or duplicate prior work.

## Entry template

```markdown
## YYYY-MM-DD — short title (author: Claude session / user)
**What changed:** bullet list of files/folders added, edited, moved, deleted.
**Why:** one or two lines.
**Follow-ups:** anything left pending (or "none").
```

---

## 2026-07-21 — Fourth snapshot merged: rebuilt RANKING, evidence-state summary, colour-science + Commons additions (author: Claude session)
**What changed:** merged the newest diverged snapshot (upload `2eae9f2e`). Its markdown was otherwise a subset of this copy, so only four genuinely-newer items were pulled in and humanised to the audit-clean style. Site rebuilt: 92 pages, audit 0 sitewide, 0 broken links.
- **`X-T5/RANKING.md` fully rebuilt** — the old "full bank" table covered only 17 of 61 recipes and was flagged stale. Replaced with the snapshot's tiered ranking (Tier S/A/B/C by aesthetic × real-world popularity, with a "false precision" caveat and honest reading of the `n/a` popularity signal). The snapshot's rebuild predated this copy's 8 recent community recipes, so I added them back as an explicit "Recent reference additions, not yet re-scored" block (the four FXW video recipes + the three Nostalgic Neg. stills + Cine Teal); bank count updated 62 → 70. Medal emoji stripped from tier headings for the published page.
- **`Knowledge/validation-methodology.md`** gained the "Evidence state of the bank at a glance" summary table (9 film-based originals now carry real pixel evidence, up from 3) and the "Which remaining gaps are actually closable" triage (which stocks are structurally blocked on Commons vs closable, and the two highest-value human contributions).
- **`Knowledge/color-science-why-film-cannot-be-faked.md`** gained a "Fujifilm's own words for this argument" section putting the Image Design team's raw-signal-conversion quote where the cannot-be-faked thesis lives.
- **`X-T5/_reference-sources/COMMONS-SCAN-INDEX.md`** gained the "confounders cluster on exactly what the bank lacks" analysis (night/tungsten/interior colour frames are abundant but light-contaminated; B&W is exempt; three colour frames rejected for light-source contamination).
- Not ported: everything else in the snapshot was an older or identical state of files this copy already leads on (its recipe set lacks the 8 community recipes, the datasheet MANIFEST, and the nerd guide); the Requests screenshots were already handled and stay gitignored.

## 2026-07-20 — Third-machine snapshot merged: F-Log/RAW workflow, Fortia SP, tone-curve audit, expanded design notes (author: Claude session)
**What changed:** integrated another diverged repo snapshot (uploaded), merging its genuinely-new work into this canonical copy and humanising all ported prose to the audit-clean house style. New site now 92 pages (was 90), audit 0 sitewide, 0 broken links.
- **New knowledge article `Knowledge/flog-and-raw-workflow.md`** (F-Log vs F-Log2, the ISO-floor and DATA-LEVEL traps, Resolve/Premiere node order, in-camera RAW conversion + X RAW Studio, RAW-video cost ladder), plus **`Knowledge/luts/`** (two datasheet-derived F-Log→Rec709 `.cube` LUTs + generator script + README). Indexed in `Knowledge/README.md`. Renders on the site.
- **New original `X-T5/originals/fujifilm-fortia-sp/`** — Fujifilm's most-saturated emulsion, a deliberate Velvia+CCE-Strong rule-break; filed as **characteristic-only** (no datasheet, no scans) with an honest evidence banner. Indexed in `X-T5/README.md`; added to the validation ledger.
- **`Knowledge/fujifilm-official-design-notes.md` greatly expanded** — added the official design stories for Classic Chrome (×3 depth levels), Astia, Provia, Velvia (+dev story), Pro Neg Hi/Std, the cross-simulation blue/sky axis, the Image Design team's philosophy, the Color Chrome Effect origin (modelled on Fortia), the Eterna X-H1 development story (12-stop, F-Log-comparable, cyan sky shift), and a coverage-status footer. All humanised.
- **New audit `X-T5/TONE-CURVE-AUDIT.md`** (every recipe's Highlight/Shadow vs its base sim's native curve) and **`X-T5/_reference-sources/COMMONS-SCAN-INDEX.md`** (standing record of which stocks have genuine Commons scans + mislabelling traps). Referenced from `X-T5/README.md` and the validation methodology.
- **Merged sections into shared files:** the per-sim curve table into `dynamic-range-and-tone.md`; the CCE origin/mechanism into `color-and-chrome.md`; a Fujifilm-style **blind-evaluation** section + the Commons-index cross-ref + a Fortia ledger row into `validation-methodology.md`; seven new official-design pro-tips + the Fortia index row + the tone-curve-audit link into `X-T5/README.md`; tone-curve pro-notes on `bewaremyvelvia-bold`, `kodak-portra-800-v3`, `ross-sherbet-lemon`.
- **New `Requests/1/`** — a worked "design from client references" example (European travel editorial, Classic Chrome). Repo-only, not published; the third-party Instagram reference screenshots are gitignored (analysis-only), a README documents the folder.
- **Corrections made during merge, not propagated blindly:** the snapshot mis-classified `ross-sherbet-lemon` as Classic Chrome in the tone-curve audit and its pro-note (it's Velvia) — fixed the audit row and wrote a correct Velvia note instead. Fixed a `validation_badge` bug where a "no scans" status matched the scan check (Fortia had wrongly shown "scan-validated"); it now reads "characteristic only". Restored recipe/article H1 title conventions that the em-dash→comma humanisation had broken.
- **Not ported:** everything else in the snapshot was an older state of files already improved here (it lacked the 8 recipes, the datasheet MANIFEST, and the nerd guide this copy already has); its `.claude/` settings and macOS cruft were ignored.

## 2026-07-20 — Second-machine copy merged: official design notes, pro-tips, scan passes (author: Claude session)
**What changed:**
- User uploaded the second machine's repo copy (the diverged `D:\Fujifilm Recipes`); its four unmerged sessions (2026-07-16 through 2026-07-20, logged below) are now integrated into this canonical copy. All ported prose was restyled to this copy's human-written standard; facts, official quotes and settings kept intact.
- **New `Knowledge/fujifilm-official-design-notes.md`** — first-party design statements from Fujifilm's X Stories/product pages for Acros, Classic Neg., Eterna, Nostalgic Neg. and Reala Ace, each mapped to recipe implications. Indexed in `Knowledge/README.md`.
- **Bank-wide "Pro tips" section added to `X-T5/README.md`** (HEIF disables Clarity; Clarity save-speed cost; FINE+RAW re-development workflow; ISO-as-grain-control on Acros; per-C-slot WB memory; Classic Neg magenta-highlight tuning rule; Nostalgic Neg shadow-amber rule).
- **Per-recipe notes ported (13 files):** pro tips on Tri-X, Gold 200, CineStill 800T; Nostalgic Neg. official note on california-summer, 1976-kodak, thommys-ektachrome, ross-pumpkin-soup; Reala Ace saturation-compression note on reala-ace, fujifilm-negative; Eterna ungraded-canvas confirmation in `originals/cinema/README.md`; scan-validation first-pass notes on **kodak-portra-400** and **kodak-vision3-250d** (both now datasheet + scan (partial) in the index and ledger) and **kodachrome-25**.
- **New CLAUDE.md rule 9:** the standing continuous pro-tip enrichment directive from the second machine now lives in the repo rules, where both copies' agents will honour it.
- Not ported: everything else in the upload was an older snapshot of files already improved here (the delta-3200 comparison and pastel-dream variant were already present); the upload's `.claude/` settings and macOS cruft were ignored.

## 2026-07-20 — Standing directive added: continuous pro-tip enrichment (author: Claude session, second machine; merged 2026-07-20)
**What changed:** every research iteration must convert findings into practical pro-tips on the recipe listings themselves. Immediate enrichment pass: bank-wide Pro tips section in `X-T5/README.md`; per-recipe tips for Tri-X, Gold 200, CineStill 800T.
**Why:** user directive: "keep making edits to recipe listings: pro-tips, pro-notes, top tips, suggestions, recommendations as you keep finding information."

## 2026-07-20 — Loop iteration 4: scan-validation pass, Portra 400 / Vision3 250D / Kodachrome 25 (author: Claude session, second machine; merged 2026-07-20)
**What changed:** real Wikimedia Commons scans analysed (analysis-only) for recipes lacking pixel evidence; validation notes appended and ledger updated. Portra 400 and Vision3 250D move to Scan (partial); the Kodachrome 25 reference's headline Sharpness +3 / Grain Off / Color +1 choices confirmed against a dated May-1980 K25 scan. A fourth candidate (a slide labelled only "Dia") was discarded for lacking stock attribution rather than counted as Ektachrome evidence.
**Follow-ups:** E100 scan pass still open; Tri-X and 2383 remain the least scan-covered; partials want 5-scan spreads per methodology.

## 2026-07-20 — Loop iterations 2–3: remaining official sim pages mined, insights applied (author: Claude session, second machine; merged 2026-07-20)
**What changed:** mined the Eterna, Nostalgic Neg. and Reala Ace official pages into `fujifilm-official-design-notes.md` (Eterna as deliberately ungraded canvas; Nostalgic Neg's WB-immovable shadow amber; Reala Ace's nonlinear saturation compression), then applied the insights as notes on the affected recipe files.
**Follow-ups:** remaining official pages (Provia, Velvia, Astia, Classic Chrome, Pro Neg) for a future pass.

## 2026-07-16 — Loop iteration 1: Fujifilm official design notes mined (author: Claude session, second machine; merged 2026-07-20)
**What changed:** first version of `fujifilm-official-design-notes.md` with the Acros engineering story (10-year development; core-level, tone-differentiated, ISO-scaling grain) and Classic Neg's official signature (cyan-green shadows, magenta highlights, aged-consumer-film intent), each mapped to recipe implications, including the new tuning rule: too-pink Classic Neg highlights want less Red, not more Blue.

## 2026-07-19 — 8 famous recipes added (incl. video wing); datasheet manifest; the nerd guide (author: Claude session)
**What changed:**
- **8 new attributed reference recipes** (each `recipe.md` + drop-folders, indexed in `X-T5/README.md`), researched from the most-popular / Instagram-known / YouTube-cinematic space. All by Ritchie Roesch (Fuji X Weekly), all with Source links:
  - Stills: **timeless-negative** (NN, one of FXW's most popular V recipes), **nostalgia-negative** (Ritchie's first X-T5 recipe), **nostalgic-americana** (cool aged-print NN).
  - **Video wing** (FXW's May 2026 video-recipe series, the "cinematic YouTube" category): **nostalgic-color** (NN, memory-toned), **chrome-color** (CC documentary), **vivid-fujichrome** (Velvia postcard), **reala-color** (Reala Ace true-to-life).
  - **cine-teal** (Eterna, the famous moody teal look) — an X-Trans IV recipe, ported with the documented CCFXB Strong→Weak drop and the port noted in the file.
  - Research method note: FXW and most recipe sites are Cloudflare-blocked from this environment, so settings were transcribed from search-index snippets of the source pages, complete for every recipe added; recipes whose full settings couldn't be verified (Roman Fox's five, Shuttergroove's movie recipes, Ross's four film-emulation looks) were left out rather than guessed.
- **Datasheet archive: manifest + fetch script.** This environment's network policy blocks arbitrary downloads (proxy CONNECT 403), so instead of PDFs: **`datasheets/MANIFEST.md`** now catalogues every film-stock datasheet known to exist (~50 pending beyond the 48 archived, across Kodak still/motion, Fujifilm, Ilford, Agfa, Foma, Adox, Rollei, Bergger, Ferrania, and a none-exists list), and **`datasheets/fetch-datasheets.sh`** downloads all pending sheets into the right folders when run with open network. README points to both.
- **New Knowledge article: `nerd-guide-datasheet-to-recipe.md`** ("The nerd guide") — how to read a characteristic curve, granularity scales (RMS vs PGI), spectral sensitivity; the full measurement-to-menu mapping table; the four judgment calls no sheet can settle; a Gold 200 worked example; and a recipe-skepticism checklist. Indexed in `Knowledge/README.md`; renders on the site.
- Site rebuilt: 89 pages (was 80), audit score still 0 sitewide, 0 broken links, sitemap updated.

**Why:** User asked for more famous/popular/cinematic recipes, every findable datasheet, enriched knowledge, and a guide for nerds.
**Follow-ups:** Run `fetch-datasheets.sh` on an unrestricted machine, then flip MANIFEST statuses and log. Candidates left on the table for a future pass (full settings unobtainable this session): Roman Fox's 5 street recipes (snapsbyfox.com), Shuttergroove's movie recipes (In The Mood For Teal, Super 8), Ross's Ultramax/XP2/Fujipop/Lomo800 film emulations.

## 2026-07-18 — Site v3 final iteration: audit reaches zero across all 80 pages (author: Claude session)
**What changed:**
- **Bulk prose passes across all rendered recipe files + Knowledge articles:** debolded 752 prose spans (blockquote callout keys and all table content kept), converted 138 em dashes with connective continuations to commas/semicolons, then the ~355 residual prose em dashes to commas, protecting any line where the dash sits inside a quotation.
- **Repairs from reviewing that pass:** restored 103 H1 title dashes the comma pass had broken (recipe titles were showing their "— Fujifilm X-T5" suffixes on the site), and hand-fixed 19 run-on sentences it created, including a meaning inversion in validation-methodology ("don't fight it, switch hosts…" read as a negated list).
- **Individual residue fixes:** two "reflecting…" participle tails, two "not just/not merely" parallelisms, "crucial" ×2 and "vibrant" ×1 in our own prose (Fujifilm's quoted manual wording kept verbatim), ✓-glyphs in two datasheet-check notes rewritten as words, and the recipe-page source-link label "Original recipe — X" → "Original recipe: X".
- **`site/audit.py`:** vocabulary matches inside double-quoted spans are now exempt (quotations aren't our authorship).
- **Final state: audit score 0 on all 80 pages** (from 2,593 at the start of the loop); 0 broken internal links; sitemap covers all 80 pages; screenshots verified in both colour schemes.

**Why:** Completes the user's /loop task: entire site copy humanized per the humanizer skill, SEO layer complete.
**Follow-ups:** none for copy. The audit gate (`python3 site/audit.py`) can run in CI or before any future content merge to keep new copy clean.

## 2026-07-17 — Site v3 iteration 5: bulk bullet-key transform + knowledge articles (author: Claude session)
**What changed:**
- **Mechanical repo-wide transform** across all rendered recipe files, Knowledge articles and RANKING.md (207 lines in 50 files): `- **Key** — explanation` list items became `- Key: explanation`, and `## Heading — subtitle` became `## Heading: subtitle`. Applied only outside tables and code fences; diff sampled and verified readable. This is the single most common machine-styling pattern in the bank.
- **`Knowledge/film-chemistry-fundamentals.md`** and **`Knowledge/film-simulations.md`** hand-humanized: prose em dashes and bold removed (chemical equations debolded but untouched in content; Fujifilm's own quoted manual descriptions kept verbatim, including the quoted word "vibrant" — quotations are not our copy).
- Sitewide audit score 1,295 → 822; template pages remain 0.

**Why:** Loop continues; the bulk transform safely cleared the long tail's dominant pattern.
**Follow-ups:** Remaining ~70 pages average ~11 points (light em dash/bold residue). Next: validation-methodology, ektar-100, vision3-50d, pro-400h, pro400h-comparison, grain-and-detail, double-x, video-mode-settings.

## 2026-07-17 — Site v3 iteration 4: content humanization batch 3 (author: Claude session)
**What changed:**
- **`originals/mumbai/`** (all 3 files), **`originals/mumbai-monsoon/`** (all 3 files), **`originals/cinema/kodak-ektachrome-100d/`** (recipe.md + knowledge.md): prose humanized — em dashes, "**Key** — explanation" bullet scaffolding and remaining "vibrant" vocabulary removed; all settings, variants, study evidence and citations preserved.
- **Two more stale-value fixes found and corrected in mumbai-monsoon:** knowledge.md's design-response table and recipe-video.md's compensation notes both still said "Clarity −1" from before the Clarity-0 quality standard; both now match the recipe's actual Clarity 0.
- Sitewide audit score 1,462 → 1,295; 7 pages fully clean; template pages remain 0.

**Why:** Loop continues toward fully human-reading site copy.
**Follow-ups:** Next: film-chemistry-fundamentals (56), kodak-ektar-100 (53), fujicolor-pro-400h (52), validation-methodology (50), kodak-double-x-5222 (49), kodak-ektachrome-e100 (45), then the ~40-and-below tail (~60 pages).

## 2026-07-17 — Site v3 iteration 3: content humanization batch 2 (author: Claude session)
**What changed:**
- **`Knowledge/color-science-why-film-cannot-be-faked.md` fully rewritten for prose style** (largest offender: 59 prose em dashes): headings de-title-cased, "**Key** — explanation" bullet scaffolding converted to sentences, em dashes replaced with natural punctuation. Every fact, figure, table, citation and cross-link preserved; footer date bumped.
- **`originals/creative/silent-atlas/`** (recipe.md, recipe-video.md, knowledge.md): same prose treatment, including the ✓-mark verification summary rewritten as sentences. All settings, the −3B→−2B correction record, and verification history intact.
- **`originals/fujicolor-superia-400/`** (all 4 files): same treatment; datasheet claims, validation status and caveats preserved verbatim in meaning.
- Sitewide audit score 1,720 → 1,462; template pages remain clean.

**Why:** Loop continues toward fully human-reading site copy.
**Follow-ups:** Next batch: mumbai (61, has 2 vocab hits), kodak-ektachrome-100d (57, 1 -ing tail), mumbai-monsoon (57), film-chemistry-fundamentals (56), kodak-ektar-100 (53), fujicolor-pro-400h (52), then the ~40-point tier.

## 2026-07-17 — Site v3 iteration 2: content humanization batch 1 (author: Claude session)
**What changed:**
- **Audit refinement (`site/audit.py`):** style tells (em dash, curly quotes, bold) are now measured on prose only, with `<table>` content excluded, and coverage/status glyphs (✅📗🔎🔶❌⚠️) exempted — tables legitimately use em dashes as empty-value markers, bold as row keys, and glyphs as data notation. Sitewide score dropped 2,593 → 1,848 from measurement fairness alone.
- **`originals/kodak-gold-200/` (all 5 files) humanized:** prose em dashes and bold removed, sentences rewritten to read naturally. Settings, links, sources and tables untouched. Also fixed three **stale-value references** that predated the scan-validation pass: knowledge.md cited "Highlight −1.5 + Clarity −2" and "+4R" (validated recipe is Highlight −2, Clarity 0, +3R); research.md's derivation table cited "Clarity −2"; recipe-video.md's compensation notes referenced stills Clarity −2. Recipe values themselves unchanged.
- **`Knowledge/film-stocks-master-list.md` prose humanized:** H1 de-title-cased, legend/priority-queue/Ross-note em dashes and bold-key patterns rewritten as plain sentences. All tables and coverage data untouched.
- Sitewide audit score now 1,720 (was 2,593); 6 pages fully clean; template pages still 0.

**Why:** Loop iterations toward the user's goal: the whole site reading as human-written.
**Follow-ups:** Next batches: color-science article (59 prose em dashes), silent-atlas, fujicolor-superia-400, mumbai ×2, ektachrome-100d, then the long tail of ~70 pages scoring 10–50.

## 2026-07-17 — Site v3 iteration 1: copy humanized, SEO layer, AI-tell audit (author: Claude session)
**What changed:**
- **All site-authored copy rewritten** per the humanizer skill (Wikipedia "Signs of AI writing"): removed em dashes, negative parallelisms, tailing-negation fragments, rule-of-three padding, emoji-decorated headings/bullets, and promotional vocabulary from every template (home, community, knowledge index, about, contact, footer, category intros). Site voice is now first-person (the owner's), with varied rhythm and plain copulas.
- **SEO layer in `site/build.py` + `base.html`:** per-page unique `<title>` and hand-written meta descriptions (recipe pages get generated but natural ones), canonical URLs against the Pages base URL, Open Graph/Twitter meta, JSON-LD (WebSite on home; Article with author on recipe and knowledge pages), `sitemap.xml`, `robots.txt`.
- **New `site/audit.py`** — scans built pages for AI-writing tells (em dash counts, AI vocabulary, negative parallelisms, participle tails, curly quotes, emoji, bold density), prints worst pages, exits non-zero if template pages aren't clean. Template pages now score 0; markdown-driven pages carry a total score of ~2,590 to work down in subsequent passes.
- Display transforms: knowledge titles and recipe display titles render " — " as ": "; creator credits normalised.
- **Index wording edit:** `X-T5/README.md` + `RANKING.md` Mumbai mood cell "Warm vibrant sunny street" → "Warm lively sunny street" ("vibrant" is a flagged AI-vocabulary word surfacing on the homepage).

**Why:** User asked for the entire site copy redone with the humanizer skill + SEO best practices so the site reads as human-written, iterating in a loop until clean.
**Follow-ups:** Loop continues: humanize the rendered markdown prose (knowledge articles and recipe files) in batches, preserving all settings, facts and sources — worst pages first. Decide whether table status glyphs (✅/❌) should stay exempt in the audit.

## 2026-07-17 — Site v2: internal references scrubbed, light/dark, image-led design (author: Claude session)
**What changed (all in `site/`):**
- **No internal-document references anywhere on the site.** Removed the per-page "Source file" footers and all GitHub links from the chrome. The link rewriter now *unlinks* anything that isn't a site page (instead of falling back to a GitHub URL), rewrites file-name link texts to human wording ("the research notes", "the grade analysis"), and a prose-cleanup pass rewrites remaining file/folder mentions (`recipe.md`, `_reference-sources/`, CHANGELOG, the manual PDFs…). Verified by scanner: 0 `.md`/`.pdf`/path mentions and 0 repo links across all 80 pages.
- **About page rewritten** as site-native content (was the rendered root README, which is full of repo structure); Contact page rewritten without the GitHub card, adding "send a sample frame" and "send film scans" cards.
- **Light/dark theming** via `prefers-color-scheme` — warm-paper light palette, darkroom-charcoal dark palette, all colors tokenised.
- **Image-led layout:** every recipe card and page now has a photo slot. The generator publishes images found in a recipe's `test-shots/` folder (cover on the card + gallery on the page); until real frames exist it renders film-frame placeholders tinted with the recipe's base-sim colour, and each empty gallery invites readers to submit a frame via the contact page. Also: hero film-strip of the flagship looks' sim colours, per-article emoji on the knowledge index, punchier copy throughout ("Your X-T5 already shoots film.").

**Why:** User feedback on site v1 — remove internal-doc references, make it fun, follow system light/dark, and design image-heavy with space for sample images.
**Follow-ups:** Drop real JPEGs into any recipe's `test-shots/` and rebuild — they'll appear automatically. `references/` scans stay unpublished by design (third-party material, analysis-only).

## 2026-07-17 — Static knowledge-base website added (author: Claude session)
**What changed:**
- New **`site/`** — a static site generator (`build.py` + Jinja2 templates + `static/style.css`) that renders the whole repo into a browsable website (`_site/`, gitignored). No content is duplicated: the markdown stays the single source of truth, and every page footer links back to its source file on GitHub.
- Site structure per the user's spec: **Originals** as the homepage (card grid grouped Colour / Cinema / B&W / Creative, ordered per the curated `X-T5/README.md` tables, with base-sim chips and validation-tier badges), **Community recipes** tab (every card names its creator; every page links to the original publication, plus an attribution-and-takedown note on the contact page), **Knowledge** (all 13 articles + index), **About** (rendered root README), **Contact**, plus a `/ranking/` page from `RANKING.md`. Client-side filter box on both recipe grids.
- Relative-link rewriting: recipe↔knowledge↔Knowledge-article links resolve to site pages (per-recipe files become section anchors on one combined page — recipe / movie-mode / grade analysis / research / validation); anything outside the site (PDFs, CLAUDE.md, drop-folders) falls back to a GitHub link. Verified 0 broken internal links across the 80 built pages, and visually via screenshots.
- New **`.github/workflows/deploy-site.yml`** — builds and deploys to **GitHub Pages** on push to `main` (also runnable manually via workflow_dispatch). `.gitignore` now excludes `_site/`.
- Root `README.md` gained a short Website section.

**Why:** User asked to turn the repo itself into a website — originals on the homepage, others' recipes with proper attribution, about and contact pages.
**Follow-ups:** Enable Pages once merged to `main` (repo Settings → Pages → Source: **GitHub Actions**); site will publish at `arpitphillips.github.io/fujifilmrecipes`. The contact page currently shows the user's Gmail address — swap for an alias if spam becomes a concern. Recipe pages have no images yet; when `test-shots/` folders gain real frames, the generator could surface them as galleries.

## 2026-07-17 — Version control established; Gumroad go-to-market research; Higgsfield validation experiment (author: Claude session)
**What changed:**
- Initialized git for the repo, added `.gitignore` (excludes macOS `._*`/`.DS_Store` cruft and the personal `.claude/settings.local.json`), made the initial commit (302 files), added the GitHub remote (`github.com/arpitphillips/fujifilmrecipes`, **public**), and pushed `main`. The repo is under version control for the first time.
- Root `README.md` exists only as GitHub's auto-generated placeholder (`# fujifilmrecipes`), merged in from the remote during setup — not yet written.
- Researched the Gumroad monetization landscape for this bank against three live comparisons (a pay-what-you-want 70-recipe aggregator pack, Reggie Ballesteros's ~$11 single-recipe listing, Fuji X Weekly's $19.99/yr Patron tier) and produced a go-to-market strategy memo. Published as a private Claude Artifact — **not** committed to this repo.
- Ran an experiment generating an AI test image (CSMT, Mumbai) styled after the Kodak Tri-X 400 recipe via Higgsfield/GPT Image 2, to gauge whether AI image generation can previsualize a recipe's look before shooting film. Result is an external CDN URL, not saved into the repo.

**Why:** Bringing the changelog up to date with a session's work, in lieu of syncing the raw session transcript (a 6MB internal JSONL log) — not appropriate content for a public repo.
**Follow-ups:** Write a real root `README.md` (currently just the GitHub placeholder). Decide whether the Gumroad strategy memo should be adapted into a repo doc (e.g. a `business/` folder) if the user wants it version-controlled.

## 2026-07-16 — Clean Girl creative original added (author: Claude session)
**What changed:**
- New creative original **`originals/creative/clean-girl/`** (recipe.md + drop-folders): the bright/airy/white-white/luminous-skin "clean girl" aesthetic. Astia base; the design hinge is **Auto White Priority WB** (Fujifilm's keep-whites-white AWB mode) with a +1R/−1B whisper for skin, DR400 + Highlight −1.5 for high-key headroom, Shadow −1 (lifted but not matte), Color +1/CCE Weak/CCFXB Off, **Grain Off** (the defining clean choice — only Grain-Off recipe in the bank besides Kodachrome 25), Sharpness −1, Clarity 0, ISO capped 1600, EC +2/3…+1⅓. Golden-hour and PRO-Neg-Hi studio variants + inline movie-mode section (translates near-1:1 since Grain/Clarity were already off/0). Comparison table vs Pastel Dream / Matte Editorial / Golden Hour Glow documents the distinct niche (neutral-white luminous pole).
- Indexed in `creative/README.md`, `X-T5/README.md`, `RANKING.md`.

**Why:** User asked for a maximally aesthetic "white-white, clean look, clean girl aesthetics" stills recipe.
**Follow-ups:** Tune against user-dropped reference images in `clean-girl/references/` (Pinterest/IG saves welcome — analysis-only).

## 2026-07-16 — Silent Atlas frame-verified independently; WB corrected (author: Claude session)
**What changed:**
- Ran a **second, independent frame-verification pass** on the Silent Atlas reference video (user request: "watch the video and double check and fine tune"). YouTube's player blocks browser screenshots in this environment, so used YouTube's **auto-generated real frame stills** (i.ytimg.com sd1/sd2/sd3 = ~25/50/75% points + maxresdefault hero frame) — 4 frames spanning mist landscape, portrait, clear sky, and the hero shot.
- **Confirmed** the ported grade on every axis except one: warm golden skin/earth ✓, deep held shadows ✓, soft bloomed highlights ✓, muted saturation ✓, fine grain in mist ✓ (supports the stills Weak/Large grain choice).
- **Corrected from the evidence: WB Blue shift −3 → −2** in both `recipe.md` and `recipe-video.md` — all 4 frames show skies/mist landing *teal-cyan*; −3B would strip too much blue and yellow the atmosphere toward khaki, while −2B preserves enough blue for Classic Negative's native cyan lean to render it teal. Knowledge.md gained a "Frame verification — second independent pass" section with the full observation table; the 2383-comparison table updated to match.
- Method caveat documented: YouTube auto-frames are heavily compressed → hue relationships treated as reliable evidence, absolute saturation only loosely.

**Why:** Core principle — verify with real images, not inherited notes; the second pass caught a real mis-tune.
**Follow-ups:** none — the i.ytimg.com auto-frame strategy was added to validation-methodology.md fetch strategies same day.

## 2026-07-16 — Silent Atlas ported from second-machine copy + stills companion added (author: Claude session)
**What changed:**
- Discovered the two repo copies have **diverged**: `D:\Fujifilm Recipes` (worked on by a session on the user's other machine) contained `originals/creative/silent-atlas/` (recipe-video.md + knowledge.md, derived 2026-07-15 from a frame-by-frame study of Merlin Krumme's *The Silent Atlas* YouTube film), which was absent from this copy — and this copy has ~13 recipes the D: copy lacks.
- **Ported** `silent-atlas/` D:→C: unchanged (crediting the original session in knowledge.md's footer), added the standard `references/`/`test-shots/` drop-folders.
- **Added `recipe.md` (stills companion)** — the D: version was video-only. Same grade (Classic Neg, Daylight +3R/−3B, DR200, H−1/S+2, Sharpness −1); stills build uses the movie-mode-unavailable controls instead of saturation compensation: Color +2 (not +3) with **CCE Strong** carrying warm-tone depth, **CCFXB Weak** for teal shadow depth, **Grain Weak/Large** for subtle cine texture, Clarity 0 per standard (physical Glimmerglass/mist filter recommended; Clarity −2 documented as the no-filter variant).
- Updated knowledge.md (video-first section now points to the stills build), `creative/README.md`, `X-T5/README.md`, `RANKING.md`.
- **Did not write to the D: copy** (it's the other session's working copy; one-way port only).

**Why:** User asked for the grade + sim for the same YouTube reference on this machine; the prior work existed only in the unsynced D: copy.
**Follow-ups:** The two repo copies need reconciling — this C: copy is ahead by ~13 recipes (Ektar, Pro 400H, Delta 3200, Pan F, 4 FXW references, 6 Ross creatives, Reggie's Superia, 3 cinema stocks) and D: had silent-atlas. Recommend picking one copy as canonical.

## 2026-07-16 — Researched and added the most notable cinema stocks (author: Claude session)
**What changed:**
- Researched (not assumed) which cinema film stocks cinematographers/critics rate most highly, beyond the existing Vision3 250D/500T/2383: web search surfaced **Vision3 50D** (Kodak's own "finest grain" cinema stock; used on Sean Baker's *Red Rocket*; Vanessa Whyte BSC has published praise for the family's highlight latitude), **Kodak Double-X 5222** (B&W cinema negative in continuous production since 1959 — *Raging Bull*, *Schindler's List*, *Manhattan*), and **Kodak Ektachrome 100D** (reversal/slide cinema stock used in *Poor Things*, 2023).
- Added 3 new **datasheet-derived cinema originals**, each with `recipe.md` + `recipe-video.md` + `knowledge.md`:
  - **`originals/cinema/kodak-vision3-50d/`** — Eterna base, Weak/Small grain, neutral WB. Validated against 2 real Commons scans (daylight + overcast) confirming near-invisible grain.
  - **`originals/cinema/kodak-double-x-5222/`** — **placed in `cinema/`, not `black-and-white/`** (a cinema stock with cinema-specific grain/contrast targets, distinct from the still-photo B&W family). Acros base, Strong/Large grain (datasheet RMS 14), Clarity +1 (third B&W-family recipe to deviate from the Clarity-0 default, after Tri-X and Delta 3200).
  - **`originals/cinema/kodak-ektachrome-100d/`** — the one cinema recipe on **Provia, not Eterna**, since it's a *reversal* stock (E-6, slide-film logic) rather than a negative — same base-choice logic as the still Ektachrome E100 original.
- Fetched and archived 2 new official Kodak datasheets not previously in the collection: `kodak-motion/double-x_5222.pdf`, `kodak-motion/ektachrome-100d_5294.pdf` (corrected from an initial misfile into `kodak-still/` — Double-X is a motion-picture stock).
- Rewrote `originals/cinema/README.md` to explain the research-driven selection and the now-6-stock family (was 3).
- Updated `X-T5/README.md`, `X-T5/RANKING.md`, `Knowledge/film-stocks-master-list.md` (added Double-X and Ektachrome-100D-cine as new rows, distinguished from the existing still-photo Ektachrome E100 row; flipped Vision3 50D's flag), and `Knowledge/validation-methodology.md` ledger.

**Why:** User asked for research into the most notable/pleasing cinema stocks beyond Vision3, sourced from official/authentic/reliable sources.
**Follow-ups:** No Wikimedia Commons frame-grabs exist for Double-X, Ektachrome 100D, 250D, 500T, or 2383 (real movie footage isn't Commons' domain) — real-footage scan-validation for those needs a user-supplied reference (a still from one of the cited films, or the user's own test footage) dropped into each recipe's `references/` folder. Vision3 200T remains an open gap (❌, no recipe yet).

## 2026-07-16 — Added Ross McConaghy creative recipes + Reggie's Superia (author: Claude session)
**What changed:**
- 6 new **creative** attributed reference recipes from [rossandhisjpegs.com](https://www.rossandhisjpegs.com/fujifilm-recipes), each with recipe.md + drop-folders + source link: **`ross-chrome-fog`** (Classic Chrome, Clarity −5 diffusion-filter/fog look — a genuinely new niche), **`ross-canned-heat`** (Classic Neg, +6R/−7B extreme-warm teal-orange), **`ross-fruit-pastel`** (Velvia pastel — the Velvia counterpart to our Astia Pastel Dream), **`ross-sherbet-lemon`** (Velvia bright seaside), **`ross-pumpkin-soup`** (Nostalgic Neg, Underwater-WB autumnal), **`ross-salted-slate`** (Acros+G dark slate B&W).
- Added **`reference-recipes/reggies-superia/`** (Classic Negative; Reggie Ballesteros's deliberately heavy-handed, moody, grain-forward portrait recipe for melanated skin — the philosophical *opposite* of Reggie's Portra despite the shared author).
- Corrected an earlier mischaracterisation: Reggie's Superia had been described as "versatile like Reggie's Portra" — a timestamped video breakdown showed it's intentionally heavy-handed/moody; recipe.md and the Superia-original comparison updated. WB Blue shift updated −3 → −4 (video's on-screen reading; discrepancy with the article text documented, not silently resolved).
- Wrote full settings-diff comparison tables into `originals/kodak-portra-400/knowledge.md` and `originals/fujicolor-superia-400/knowledge.md` covering original (emulsion-faithful) vs Reggie's (purpose-faithful) for both Portra and Superia.
- Updated `X-T5/README.md` reference table (7 new rows) and `Knowledge/film-stocks-master-list.md` (added Ross as a source + noted his film-emulation recipes that map to open gaps: UltraMax/XP2/C200/Lomography).

**Why:** User supplied rossandhisjpegs.com as a creative-look source and asked to compare the bank's Portra/Superia originals against Reggie's versions.
**Sensor-generation verification (same day):** Ross's pages don't state a sensor gen, so verified it independently — his **Pumpkin Soup** uses **Nostalgic Neg.**, a sim that exists only on X-Processor 5 / X-Trans V-category bodies (and on *no* X-Trans IV camera). This proves his whole current recipe set is X-Trans V category = the X-T5's blue-rendering generation, so **all 6 are correct as-published; no IV→V Color Chrome FX Blue translation needed.** Recorded the verified finding in each of the 6 recipe files (replacing the earlier hedged "unknown gen" notes). The 4 non-blue-affected bases (Velvia ×2, Acros B&W, and Nostalgic Neg itself) are doubly safe.
**Follow-ups:** Ross's site has film-emulation recipes (Ultramax Electro, XP2 Electro, Fujipop Trio = C200, Lomo800) that would close several master-list gaps — candidates for a future pass.

## 2026-07-16 — Closed all 6 priority-queue gaps (author: Claude session)
**What changed:**
- 4 new **datasheet-derived originals** (all datasheets already in the archive; extracted via pdftotext):
  - **`originals/kodak-ektar-100/`** — Velvia base (tamed toward negative-film rolloff), Weak/Small grain (PGI<25), near-neutral WB. Validated against 2 real scans (saturated autumn street + night long-exposure, Wikimedia Commons).
  - **`originals/fujicolor-pro-400h/`** — PRO Neg. Hi base, CCFXB Weak + cool WB to add the film's cyan-green shadow cast. Grounded in the datasheet (RMS 4) **and** the existing `pro400h-vs-proneghi-analog-comparison.md` (a real-film-vs-simulation video study) — the strongest non-scan evidence base in the bank.
  - **`originals/black-and-white/ilford-delta-3200/`** — Acros base, Strong/Large grain, Clarity +1. Datasheet reveals true ISO is 1000 (not 3200) — designed for EI-3200 push development. Validated against 1 real scan.
  - **`originals/black-and-white/ilford-pan-f-plus-50/`** — Acros base, Sharpness +2 / Clarity +2 (highest of any B&W in the bank — datasheet calls out "edge contrast"). A found "reference" image turned out to be a synthetic DXO FilmPack preset, not real film — **correctly discarded** rather than used; flagged as scan-pending.
- 4 new **attributed reference recipes** fetched from Fuji X Weekly: **`reference-recipes/cinestill-400d-v2/`**, **`kodachrome-25/`**, **`kodak-plus-x-125/`**, **`kodak-t-max-100/`** (Hard Tone + Soft Tone in one file). Datasheet-check notes added where sheets exist.
- Updated `Knowledge/film-stocks-master-list.md` — flipped coverage flags for all 8 stocks (🔶/🔎/❌ → ✅/📗); replaced the closed priority queue with a new "next tier of gaps" list (Astia 100F, Superia 100/C200, Vericolor III 160, Delta 100/400, Agfa Ultra/Scala, CineStill 50D, XP2 Super/SFX 200).
- Updated `X-T5/README.md` (both tables) and `X-T5/RANKING.md` ("Validated originals" table) with all 8 new recipes; flagged the older "Full bank" ranking table in RANKING.md as stale/needing a full rebuild (it predates several recent expansions).
- Updated `Knowledge/validation-methodology.md` ledger with the 4 new originals' validation tiers.
- Updated `X-T5/originals/black-and-white/README.md` — expanded the B&W family comparison from 3 to 6 stocks (added Pan F Plus 50 as the slow/sharp pole, Delta 3200 as the heaviest-grain pole); documented Pan F's Clarity +2 as a third justified deviation from the Clarity-0 default (after Tri-X, now also Delta 3200 at +1).

**Why:** User asked to "fix all identified gaps" — the six-item priority queue from the 2026-07-15 master-list entry.
**Follow-ups:** New "next tier of gaps" list above. Both new datasheet originals with only partial/no scan coverage (Pan F Plus 50 has none yet) need real scans dropped into their `references/` folders. The stale RANKING.md "Full bank" table needs a full rebuild across all ~49 recipes.

## 2026-07-15 — Datasheet validation audit of all recipes (author: Claude session)
**What changed:**
- Added **`X-T5/VALIDATION-AUDIT.md`** — every recipe with a corresponding datasheet checked against the archived PDF (granularity/RMS, contrast/tone scale, balance, latitude, speed). No recipe settings changed.
- Results: all 8 film-based **originals pass** ✅. Reference recipes: 6 flagged ⚠️ (provia-positive & thommys-ektachrome & ultramax-400 & portra-400/800 & fp4-plus — each renders the *remembered artifact* (print/aged slide/pushed roll) rather than the emulsion spec; FP4's Weak/Large grain is the only combination with no datasheet support). Kodachrome RMS ladder (9/10/16) and grain-size↔RMS anchors documented.

**Why:** User asked to validate all recipes against the new datasheet archive.
**Follow-ups (approved & executed same day):**
- **A ✅** Datasheet-check notes added to the 6 flagged reference recipes.
- **B ✅** Two new datasheet-derived originals: **`originals/kodak-portra-400/`** (Classic Chrome, Weak/Small grain per PGI 37, DR400 + H−1.5, Daylight +2R/−4B) and **`originals/kodak-ektachrome-e100/`** (Provia, Weak/Small grain per RMS 8, cool-neutral WB, H−1/S−0.5). Each with recipe.md + knowledge.md (trait→setting derivation) + drop-folders; curve pages of both sheets read visually (pymupdf render). Scan-validation pending. Indexed in README, RANKING, master list.
- **C ✅** Validation ledger updated (archive-PDF-verified datasheet tier + 2 new rows).

## 2026-07-15 — Datasheet archive for all master-list stocks (author: Claude session)
**What changed:**
- Created **`X-T5/_reference-sources/datasheets/`** with **46 official technical datasheet PDFs (~25 MB)** organised by manufacturer: `fujifilm/` (10 — Velvia 50/100, Provia 100F, Astia 100F, Pro 400H, Superia X-TRA 400/100/Reala, Neopan Acros 100, Neopan 1600), `kodak-still/` (15 — Portra trio, Ektar, Gold, UltraMax, Ektachrome E100/E100VS, Kodachrome E-55, Tri-X, T-Max 100/400/P3200, Plus-X, Vericolor III), `kodak-motion/` (5 — Vision3 50D/250D/200T/500T, 2383 print), `ilford/` (11 — all current stocks + Kentmere), `agfa/` (3), `foma/` (2).
- All files validated as real PDFs; index at `datasheets/README.md` with per-file sources, recipe cross-links, the CineStill→Vision3 equivalence note, and the gap list (Natura 1600, C200, ColorPlus 200, Ferrania P30, Lomography/Konica).
- Master list now points to the archive.

**Why:** User asked for datasheets for all stocks; they are the datasheet evidence tier of the validation methodology.
**Follow-ups:** Gaps above; Ektar 100 + Pro 400H sheets now unblock the two top items in the master-list priority queue.

## 2026-07-15 — Repo restructure, agent docs, stock-gap research (author: Claude session)
**What changed:**
- Moved the 15 flat attributed-recipe folders from `X-T5/` root into **`X-T5/reference-recipes/`** — the X-T5 root now shows only README, RANKING, manuals, `_reference-sources/`, `originals/`, `reference-recipes/`. Rewrote all relative links across ~26 files; link check passes with 0 broken links.
- Added root **`CLAUDE.md`** (agent orientation: structure map, conventions, rules) and this **`CHANGELOG.md`**.
- Updated `X-T5/README.md` folder-structure section to describe the two-tier layout.
- Added **`Knowledge/film-stocks-master-list.md`** — top film stocks per manufacturer (Fujifilm/Kodak/Ilford/CineStill/others) with recipe-coverage status.
- Added 8 new reference recipes under `X-T5/reference-recipes/` for top missing stocks (all from Fuji X Weekly, X-Trans V versions): **provia-positive** (Provia 100F slide), **vivid-velvia** (Velvia), **thommys-ektachrome** (Ektachrome, Nostalgic Neg. base), **kodak-portra-160-v2**, **kodak-ultramax-400**, **fujicolor-natura-1600**, **ilford-fp4-plus-125** (Monochrome base, negative EC convention), **kodak-t-max-p3200** (pushed B&W, ISO up to 12800). Each has recipe.md + standard references/ + test-shots/ drop-folders; all added to the X-T5 README reference table.

**Why:** User asked for a self-orienting repo any agent can pick up, a logical structure, and coverage research for missing top film stocks.
**Follow-ups:** New reference recipes need field test-shots; candidates for re-derivation as originals per validation methodology.

## 2026-07-15 — Knowledge-base integration of chemistry + full Imaging Resource guide (author: Claude session)
**What changed:**
- New `Knowledge/film-chemistry-fundamentals.md` from the UW–Eau Claire chemistry-of-photography reference (silver halide chemistry, latent image, development/stop/fix, grain-speed-contrast coupling, sepia chemistry).
- Major enrichment of `Knowledge/color-science-why-film-cannot-be-faked.md` from the full Imaging Resource definitive guide (retrieved via Wayback Machine — live site blocks bots): simulation history timeline 2003–2020, colour-film layer/dye physics with the Provia-vs-Velvia dye-purity case study, new Eterna Bleach Bypass entry, ACROS grain-model section, Ye/R/G filters + B&W Adjust, per-simulation additions.
- Cross-references added in `Knowledge/grain-and-detail.md` and `Knowledge/film-simulations.md`; `Knowledge/README.md` index updated.

**Why:** User requested integration of three sources (Imaging Resource guide — most important, chemistry page, YouTube comparisons); the two YouTube videos were already integrated in a prior session (`color-science-…` + `pro400h-vs-proneghi-analog-comparison.md`).
**Follow-ups:** Nostalgic Neg. and REALA ACE postdate the Aug-2020 guide — no spectral data for them yet; add if a comparable source appears.

## Baseline (pre-changelog state, reconstructed)
- `Knowledge/` reference layer (11 files) grounded in the X-T5 manual + Fuji X Weekly.
- `X-T5/` recipe bank: 16 originals (colour, cinema, B&W, creative) + 15 attributed reference recipes, RANKING.md, validation methodology, per-recipe references/ + test-shots/ drop-folders.
