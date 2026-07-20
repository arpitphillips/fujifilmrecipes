#!/usr/bin/env python3
"""Static site generator for the Fujifilm Recipes knowledge base.

Reads the repo's markdown (X-T5 recipe bank + Knowledge layer) and renders a
static site into _site/. No content is duplicated: the markdown files remain
the single source of truth.

Usage:  python3 site/build.py
Deps:   pip install markdown jinja2
"""

import json
import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import quote

import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = Path(__file__).resolve().parent
OUT = ROOT / "_site"

SITE_TITLE = "Fujifilm Recipes"
BASE_URL = "https://arpitphillips.github.io/fujifilmrecipes/"
AUTHOR = "Arpit Phillips"
CONTACT_EMAIL = "arpit.phillips@gmail.com"
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]

# Section files a recipe folder may contain, in page order.
RECIPE_SECTIONS = [
    ("recipe.md", "recipe", "The recipe"),
    ("recipe-video.md", "video", "Movie-mode version"),
    ("knowledge.md", "knowledge", "Grade analysis"),
    ("research.md", "research", "Research"),
    ("validation.md", "validation", "Validation"),
]

# How internal file names read on the site (the site never shows repo paths).
SECTION_INLINE_NAMES = {
    "recipe": "the recipe",
    "video": "the movie-mode version",
    "knowledge": "the grade analysis",
    "research": "the research notes",
    "validation": "the validation report",
}

# Prose cleanup: internal file/folder mentions → friendly wording.
PROSE_CLEANUP = [
    (r"`X-T5/<recipe>/recipe-video\.md`", "the movie-mode version"),
    (r"`(?:X-T5/)?_reference-sources/[\w./-]*`", "the source archive"),
    (r"(?<![/(])`?\brecipe-video\.md\b`?", "the movie-mode version"),
    (r"(?<![/(])`?\brecipe\.md\b`?", "the recipe"),
    (r"(?<![/(])`?\bknowledge\.md\b`?", "the grade analysis"),
    (r"(?<![/(])`?\bresearch\.md\b`?", "the research notes"),
    (r"(?<![/(])`?\bvalidation\.md\b`?", "the validation report"),
    (r"(?<![/(])`?\bRANKING\.md\b`?", "the ranking"),
    (r"(?<![/(])`?\bCHANGELOG\.md\b`?", "the project log"),
    (r"(?<![/(])`?\bCLAUDE\.md\b`?", "the project notes"),
    (r"\bCHANGELOG\b", "the project log"),
    (r"(?<![/(])`?(?:X-T5/)?x-t5_manual_en_s_f\.pdf`?", "the X-T5 Owner's Manual"),
    (r"(?<![/(])`?(?:X-T5/)?x-t5_nfg_en_s_f\.pdf`?", "the X-T5 New Features Guide"),
    (r"(?<![/(])`?(?:X-T5/)?README\.md\b`?", "the recipe index"),
    (r"(?<![/(])`?\b_reference-sources/`?", "the source archive"),
    (r"(?<![/(])`?\breferences/`?", "the reference-scan collection"),
    (r"(?<![/(])`?\btest-shots/`?", "the sample gallery"),
]


ORIGINAL_CATEGORIES = [
    ("", "Colour film",
     "Kodak Gold for sunny afternoons, Superia for that cool Fuji green. Each "
     "one rebuilt from the manufacturer's own published numbers."),
    ("cinema", "Cinema",
     "The Vision3 negatives are here, along with the black and white stock "
     "Scorsese and Spielberg shot, and the 2383 print film behind twenty years "
     "of teal shadows at the movies."),
    ("black-and-white", "Black & white",
     "Six films, six personalities. Pan F etches, Tri-X punches, and Delta "
     "3200 turns grain into the whole point."),
    ("creative", "Creative looks",
     "These aren't emulations of anything. I designed them from scratch and "
     "kept tuning until they felt right."),
]

SIM_COLORS = [
    ("classic neg", "#7a9a5a"),
    ("nostalgic", "#c08a4f"),
    ("classic chrome", "#b0885a"),
    ("velvia", "#c05a6a"),
    ("astia", "#d09aa8"),
    ("provia", "#7a95b8"),
    ("reala", "#5aa898"),
    ("pro neg", "#c8a08a"),
    ("eterna bleach", "#9aa0ac"),
    ("eterna", "#6a86a0"),
    ("acros", "#9a9a9a"),
    ("monochrome", "#c0c0c0"),
]

CREATOR_OVERRIDES = {
    "reggies-portra": "Reggie Ballesteros · via Fuji X Weekly",
    "reggies-superia": "Reggie Ballesteros · via Fuji X Weekly",
    "thommys-ektachrome": "Thomas Schwab · via Fuji X Weekly",
    "fujicolor-super-hg-v2": "Ritchie Roesch with Thomas Schwab · Fuji X Weekly",
}

DOMAIN_CREATORS = [
    ("fujixweekly.com", "Fuji X Weekly · Ritchie Roesch"),
    ("rossandhisjpegs.com", "Ross McConaghy"),
    ("lifeunintended.com", "Luís Costa · Life, Unintended"),
]


# ---------------------------------------------------------------- utilities

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_h1(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def strip_first_h1(text: str) -> str:
    return re.sub(r"^#\s+.+\n+", "", text, count=1, flags=re.M)


def display_title(raw: str) -> str:
    """'Kodak Gold 200 — Fujifilm X-T5 (X-Trans V) · STILLS' → 'Kodak Gold 200'."""
    t = re.sub(r"\s*—\s*Fujifilm X-T5.*$", "", raw)
    return t.strip().replace(" — ", ": ")


def plain_text(md_text: str) -> str:
    """Markdown → rough plain text (for card blurbs / meta descriptions)."""
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md_text)
    t = re.sub(r"[*_`>#]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def first_paragraph(body: str) -> str:
    """First non-heading, non-table paragraph of a markdown body."""
    for block in re.split(r"\n\s*\n", body):
        b = block.strip()
        if not b or b.startswith(("#", "|", ">", "!", "```", "---")):
            continue
        return plain_text(b)
    return ""


def demote_headings(text: str) -> str:
    """Push all headings down one level (outside fenced code blocks)."""
    out, in_code = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
        if not in_code and re.match(r"^#{1,5}\s", line):
            line = "#" + line
        out.append(line)
    return "\n".join(out)


def sim_color(sim: str) -> str:
    s = sim.lower()
    for key, color in SIM_COLORS:
        if key in s:
            return color
    return "#8a8a8a"


def validation_badge(status: str) -> tuple[str, str]:
    """→ (css class, short label) for a validation/status cell."""
    s = status.lower()
    if "characteristic only" in s or ("characteristic" in s and "no datasheet" in s):
        return "ref", "characteristic only"
    if "scan" in s and "no scan" not in s:
        return "scan", "scan-validated"
    if "characteristic" in s:
        return "char", "datasheet + characteristic"
    if "datasheet" in s and "no datasheet" not in s:
        return "data", "datasheet-derived"
    if "frame study" in s:
        return "creative", "frame-study design"
    if "creative" in s or "original design" in s:
        return "creative", "original design"
    if "superseded" in s:
        return "ref", "superseded by original"
    return "ref", "reference"


# ------------------------------------------------------------ link rewriting

class LinkMap:
    """Maps repo-relative paths to site URLs.

    Links the site can serve become site links (with human link text — never a
    file name); links to anything internal (PDFs, drop folders, project files)
    are unlinked so no repo path ever surfaces on the site.
    """

    def __init__(self):
        self.map: dict[str, str] = {}
        self.names: dict[str, str] = {}

    def add(self, repo_path: str, url: str, name: str = ""):
        self.map[repo_path.strip("/")] = url
        if name:
            self.names.setdefault(url, name)

    def resolve(self, src_repo_dir: str, target: str):
        """→ (url-with-anchor or None, canonical url or None)."""
        target, anchor = (target.split("#", 1) + [""])[:2]
        anchor = "#" + anchor if anchor else ""
        resolved = posixpath.normpath(posixpath.join(src_repo_dir, target)).strip("/")
        if resolved in self.map:
            url = self.map[resolved]
            if anchor and "#" in url:
                url = url.split("#")[0]
            return url + anchor, url
        return None, None

    def rewrite(self, md_text: str, src_repo_dir: str, root: str) -> str:
        looks_internal = re.compile(r"(\.(md|pdf)\b|^`|/$)")

        def sub(m):
            bang, text, target = m.group(1), m.group(2), m.group(3)
            if re.match(r"^([a-z]+:|#|//)", target):
                return m.group(0)
            if bang:  # image reference — leave untouched
                return m.group(0)
            url, canonical = self.resolve(src_repo_dir, target)
            if url is None:
                # Internal-only target: drop the link, keep readable text.
                return humanize(text)
            if looks_internal.search(text.strip()):
                text = self.names.get(url, self.names.get(canonical, humanize(text)))
            return f"[{text}]({root}{url})"

        return re.sub(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)", sub, md_text)


def humanize(text: str) -> str:
    """'`kodak-gold-200/`' → 'kodak gold 200' — last-resort de-filing of link text."""
    t = text.strip().strip("`").rstrip("/")
    t = re.sub(r"\.(md|pdf)$", "", t)
    t = t.split("/")[-1].replace("-", " ").replace("_", " ")
    return t or text


LINKS = LinkMap()


def clean_prose(md_text: str) -> str:
    for pattern, replacement in PROSE_CLEANUP:
        md_text = re.sub(pattern, replacement, md_text)
    return md_text


def render_md(md_text: str, src_repo_dir: str, root: str) -> str:
    rewritten = LINKS.rewrite(md_text, src_repo_dir, root)
    return markdown.markdown(clean_prose(rewritten), extensions=MD_EXTENSIONS)


# ----------------------------------------------------------------- data load

def parse_recipe_index() -> dict[str, dict]:
    """Metadata (sim, mood, video, status) per recipe folder from X-T5/README.md."""
    text = read(ROOT / "X-T5" / "README.md")
    meta = {}
    row = re.compile(
        r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|\n]*)\|",
        re.M,
    )
    for m in row.finditer(text):
        _, target, sim, mood, video, status = (g.strip() for g in m.groups())
        path = posixpath.normpath(posixpath.join("X-T5", target)).strip("/")
        meta[path] = {
            "sim": re.sub(r"\*+", "", sim),
            "mood": plain_text(mood),
            "video": ("✅" in video) or ("inline" in video),
            "status": plain_text(status),
        }
    return meta


def parse_sources(md_text: str):
    """→ (creator_credit_text or None, [ (label, url), ... ])."""
    links = []
    credit = None
    for m in re.finditer(
        r"\*\*(?:Original )?[Ss]ource/credit:\*\*\s*\[([^\]]+)\]\((https?://[^)\s]+)\)",
        md_text,
    ):
        credit = m.group(1).strip()
        links.append(("Original recipe", m.group(2)))
    for m in re.finditer(r"\[Source(?::\s*([^\]]+))?\]\((https?://[^)\s]+)\)", md_text):
        label = ("Original recipe: " + m.group(1)) if m.group(1) else "Original recipe"
        links.append((label, m.group(2)))
    return credit, links


def creator_for(slug: str, credit: str | None, links) -> str:
    if slug in CREATOR_OVERRIDES:
        return CREATOR_OVERRIDES[slug]
    if credit:
        credit = credit.replace(" — ", " · ")
        return re.sub(r"\s*\(", " · ", credit.replace(")", ""), count=1)
    for _, url in links:
        for domain, name in DOMAIN_CREATORS:
            if domain in url:
                return name
    return "see source"


def load_recipe(folder: Path, tier: str, category: str, index_meta: dict) -> dict:
    repo_dir = folder.relative_to(ROOT).as_posix()
    slug = folder.name
    if tier == "original":
        url = ("originals/" + (category + "/" if category else "") + slug + "/")
    else:
        url = "community/" + slug + "/"

    sections = []
    for fname, sec_id, sec_title in RECIPE_SECTIONS:
        f = folder / fname
        if f.exists():
            sections.append({"id": sec_id, "title": sec_title, "path": f})

    recipe_md = read(folder / "recipe.md")
    meta = index_meta.get(repo_dir, {})
    credit, source_links = parse_sources(recipe_md)

    # Real sample frames, if the photographer has dropped any in test-shots/.
    shots = sorted(
        f for f in (folder / "test-shots").glob("*")
        if f.suffix.lower() in IMAGE_EXTS
    ) if (folder / "test-shots").is_dir() else []

    badge_class, badge_label = validation_badge(
        meta.get("status", "reference" if tier == "reference" else "")
    )
    return {
        "slug": slug,
        "tier": tier,
        "category": category,
        "repo_dir": repo_dir,
        "url": url,
        "title": display_title(first_h1(recipe_md)),
        "blurb": first_paragraph(strip_first_h1(recipe_md)),
        "sim": meta.get("sim", ""),
        "sim_color": sim_color(meta.get("sim", "")),
        "mood": meta.get("mood", ""),
        "video": meta.get("video", False) or (folder / "recipe-video.md").exists(),
        "status": meta.get("status", ""),
        "badge_class": badge_class,
        "badge_label": badge_label,
        "creator": creator_for(slug, credit, source_links) if tier == "reference" else None,
        "source_links": source_links,
        "sections": sections,
        "shot_files": shots,
        "shots": ["shots/" + quote(f.name) for f in shots],
    }


def discover_recipes(index_meta: dict):
    # Keep the curated order of the X-T5/README.md index tables; recipes not
    # yet indexed there sort alphabetically at the end of their group.
    index_order = {path: i for i, path in enumerate(index_meta)}

    def order_key(recipe):
        return (index_order.get(recipe["repo_dir"], len(index_order)), recipe["slug"])

    originals, references = [], []
    base = ROOT / "X-T5" / "originals"
    for cat, _, _ in ORIGINAL_CATEGORIES:
        cat_dir = base / cat if cat else base
        cards = [
            load_recipe(child, "original", cat, index_meta)
            for child in cat_dir.iterdir()
            if child.is_dir() and (child / "recipe.md").exists()
            and (cat or child.parent == base)
        ]
        originals.extend(sorted(cards, key=order_key))
    references = sorted(
        (load_recipe(child, "reference", "", index_meta)
         for child in (ROOT / "X-T5" / "reference-recipes").iterdir()
         if child.is_dir() and (child / "recipe.md").exists()),
        key=order_key,
    )
    return originals, references


def load_knowledge_articles():
    """Ordered per the curated table in Knowledge/README.md."""
    readme = read(ROOT / "Knowledge" / "README.md")
    ordered = []
    for m in re.finditer(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|([^|\n]+)\|", readme, re.M):
        fname, covers = m.group(2).strip(), plain_text(m.group(3))
        path = ROOT / "Knowledge" / fname
        if path.exists():
            ordered.append((path, covers))
    seen = {p.name for p, _ in ordered}
    for f in sorted((ROOT / "Knowledge").glob("*.md")):
        if f.name not in seen and f.name != "README.md":
            ordered.append((f, ""))
    articles = []
    for path, covers in ordered:
        text = read(path)
        articles.append({
            "slug": path.stem,
            "url": "knowledge/" + path.stem + "/",
            "repo_path": path.relative_to(ROOT).as_posix(),
            "title": first_h1(text).replace(" — ", ": "),
            "covers": covers.replace(" — ", ", "),
            "blurb": first_paragraph(strip_first_h1(text)),
            "text": text,
        })
    return articles


# -------------------------------------------------------------------- build

def build():
    index_meta = parse_recipe_index()
    originals, references = discover_recipes(index_meta)
    articles = load_knowledge_articles()

    # Register every URL (and its human name) in the link map before rendering.
    for r in originals + references:
        LINKS.add(r["repo_dir"], r["url"], r["title"])
        for fname, sec_id, _ in RECIPE_SECTIONS:
            if (Path(ROOT / r["repo_dir"]) / fname).exists():
                LINKS.add(r["repo_dir"] + "/" + fname,
                          r["url"] + "#" + sec_id,
                          SECTION_INLINE_NAMES[sec_id])
    for a in articles:
        LINKS.add(a["repo_path"], a["url"], a["title"])
    LINKS.add("Knowledge/README.md", "knowledge/", "the knowledge base")
    LINKS.add("Knowledge", "knowledge/", "the knowledge base")
    LINKS.add("X-T5/README.md", "", "the recipe bank")
    LINKS.add("X-T5", "", "the recipe bank")
    LINKS.add("X-T5/RANKING.md", "ranking/", "the full ranking")
    LINKS.add("README.md", "about/", "about this project")

    env = Environment(loader=FileSystemLoader(SITE_DIR / "templates"),
                      autoescape=False, trim_blocks=True, lstrip_blocks=True)
    env.globals.update(site_title=SITE_TITLE, email=CONTACT_EMAIL)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "static").mkdir(parents=True)
    shutil.copy(SITE_DIR / "static" / "style.css", OUT / "static" / "style.css")
    (OUT / ".nojekyll").write_text("")

    emitted_urls = []

    def emit(url: str, template: str, jsonld: dict | None = None, **ctx):
        depth = url.rstrip("/").count("/") + 1 if url else 0
        root = "../" * depth
        page_dir = OUT / url
        page_dir.mkdir(parents=True, exist_ok=True)
        html = env.get_template(template).render(
            root=root, url=url, canonical=BASE_URL + url,
            jsonld=json.dumps(jsonld, ensure_ascii=False) if jsonld else None,
            **ctx)
        (page_dir / "index.html").write_text(html, encoding="utf-8")
        emitted_urls.append(url)

    def article_jsonld(headline: str, url: str, description: str) -> dict:
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": headline,
            "description": description,
            "url": BASE_URL + url,
            "author": {"@type": "Person", "name": AUTHOR},
            "publisher": {"@type": "Organization", "name": SITE_TITLE},
        }

    # -- home (originals) --------------------------------------------------
    groups = []
    for cat, label, intro in ORIGINAL_CATEGORIES:
        cards = [r for r in originals if r["category"] == cat]
        groups.append({"label": label, "intro": intro, "cards": cards})
    emit("", "home.html", nav="originals", groups=groups,
         n_originals=len(originals), n_references=len(references),
         n_articles=len(articles),
         page_title="Fujifilm X-T5 film simulation recipes, built from film datasheets",
         meta_description="Film simulation recipes for the Fujifilm X-T5, worked out "
                          "from manufacturer datasheets and checked against real film "
                          "scans. Kodak, Fuji, Ilford and cinema looks, straight out of camera.",
         jsonld={
             "@context": "https://schema.org",
             "@type": "WebSite",
             "name": SITE_TITLE,
             "url": BASE_URL,
             "description": "Research-backed film simulation recipes for the Fujifilm X-T5.",
             "author": {"@type": "Person", "name": AUTHOR},
         })

    # -- community ---------------------------------------------------------
    emit("community/", "community.html", nav="community", cards=references,
         page_title="Community film simulation recipes for the Fujifilm X-T5",
         meta_description="Fujifilm X-T5 recipes from creators across the community, "
                          "including Fuji X Weekly, Ross McConaghy and Luís Costa. Every "
                          "recipe is credited and linked to its original page.")

    # -- recipe pages ------------------------------------------------------
    for r in originals + references:
        depth_root = "../" * (r["url"].rstrip("/").count("/") + 1)
        rendered_sections = []
        for s in r["sections"]:
            body = demote_headings(strip_first_h1(read(s["path"])))
            rendered_sections.append({
                "id": s["id"], "title": s["title"],
                "html": render_md(body, r["repo_dir"], depth_root),
            })
        if r["shot_files"]:
            shots_dir = OUT / r["url"] / "shots"
            shots_dir.mkdir(parents=True, exist_ok=True)
            for f in r["shot_files"]:
                shutil.copy(f, shots_dir / f.name)
        mood = r["mood"].rstrip(".")
        desc = (f"Exact Fujifilm X-T5 settings for the {r['title']} look"
                + (f", built on {r['sim']}" if r["sim"] else "")
                + (f": {mood[0].lower()}{mood[1:]}." if mood else ".")
                + " With the reasoning behind every setting.")
        emit(r["url"], "recipe.html",
             nav="originals" if r["tier"] == "original" else "community",
             r=r, sections=rendered_sections,
             page_title=f"{r['title']} film simulation recipe for the Fujifilm X-T5",
             meta_description=desc,
             jsonld=article_jsonld(
                 f"{r['title']} film simulation recipe for the Fujifilm X-T5",
                 r["url"], desc))

    # -- knowledge ---------------------------------------------------------
    emit("knowledge/", "knowledge_index.html", nav="knowledge", articles=articles,
         page_title="Fujifilm settings and film science, explained",
         meta_description="What every Fujifilm X-T5 image quality setting does and how "
                          "settings combine into a look. Film simulation bases, white "
                          "balance shift, grain, colour science and film chemistry.")
    for a in articles:
        body = demote_headings(strip_first_h1(a["text"]))
        emit(a["url"], "article.html", nav="knowledge", title=a["title"],
             page_title=f"{a['title']} (Fujifilm X-T5 guide)",
             content=render_md(body, "Knowledge", "../../"),
             meta_description=(a["covers"] or a["blurb"])[:300],
             jsonld=article_jsonld(a["title"], a["url"],
                                   (a["covers"] or a["blurb"])[:300]))

    # -- ranking -----------------------------------------------------------
    ranking = read(ROOT / "X-T5" / "RANKING.md")
    emit("ranking/", "article.html", nav="originals",
         title=first_h1(ranking),
         page_title="Every recipe in the bank, ranked",
         content=render_md(demote_headings(strip_first_h1(ranking)), "X-T5", "../"),
         meta_description="All the Fujifilm X-T5 recipes on this site ranked by how "
                          "good they look and how much people actually use them.")

    # -- about -------------------------------------------------------------
    emit("about/", "about.html", nav="about",
         n_originals=len(originals), n_references=len(references),
         page_title="About Fujifilm Recipes",
         meta_description="Why this recipe bank starts from film datasheets instead of "
                          "guesswork, and what the validation badges on each recipe mean.")

    # -- contact -----------------------------------------------------------
    emit("contact/", "contact.html", nav="contact",
         page_title="Contact Fujifilm Recipes",
         meta_description="Questions, corrections, recipe requests, or sample frames "
                          "and film scans you want to share.")

    # -- search index (client-side filter) ---------------------------------
    idx = [{"t": r["title"], "s": r["sim"], "m": r["mood"], "u": r["url"],
            "tier": r["tier"]} for r in originals + references]
    (OUT / "static" / "recipes.json").write_text(json.dumps(idx, ensure_ascii=False))

    # -- sitemap + robots --------------------------------------------------
    entries = "\n".join(
        f"  <url><loc>{BASE_URL}{u}</loc></url>" for u in sorted(emitted_urls))
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n</urlset>\n")
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}sitemap.xml\n")

    n_pages = sum(1 for _ in OUT.rglob("index.html"))
    print(f"Built {n_pages} pages → {OUT}")


if __name__ == "__main__":
    build()
