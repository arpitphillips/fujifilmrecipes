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

import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = Path(__file__).resolve().parent
OUT = ROOT / "_site"

GITHUB_REPO = "https://github.com/arpitphillips/fujifilmrecipes"
GITHUB_BLOB = GITHUB_REPO + "/blob/main/"
SITE_TITLE = "Fujifilm Recipes"
CONTACT_EMAIL = "arpit.phillips@gmail.com"

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]

# Section files a recipe folder may contain, in page order.
RECIPE_SECTIONS = [
    ("recipe.md", "recipe", "The recipe"),
    ("recipe-video.md", "video", "Movie-mode version"),
    ("knowledge.md", "knowledge", "Grade analysis"),
    ("research.md", "research", "Research"),
    ("validation.md", "validation", "Validation"),
]

ORIGINAL_CATEGORIES = [
    ("", "Colour — negative & slide",
     "Faithful emulations of colour still films, each derived from the "
     "manufacturer's datasheet and, where scans exist, tuned against real frames."),
    ("cinema", "Cinema",
     "Motion-picture stocks — Vision3 negatives, B&W cinema, reversal and the "
     "2383 theatrical print grade. Researched, not just assumed notable."),
    ("black-and-white", "Black & white",
     "Still-photography B&W films on the Acros simulation, grounded in "
     "datasheets and real film scans."),
    ("creative", "Creative / editorial",
     "Original designed looks — not film emulations. Faithfulness here means "
     "faithfulness to an aesthetic reference, not a datasheet."),
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
    return t.strip()


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
    if "scan" in s:
        return "scan", "scan-validated"
    if "characteristic" in s:
        return "char", "datasheet + characteristic"
    if "datasheet" in s:
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
    """Maps repo-relative paths to site URLs; unknown paths fall back to GitHub."""

    def __init__(self):
        self.map: dict[str, str] = {}

    def add(self, repo_path: str, url: str):
        self.map[repo_path.strip("/")] = url

    def resolve(self, src_repo_dir: str, target: str, root: str) -> str:
        if re.match(r"^([a-z]+:|#|//)", target):
            return target
        target, anchor = (target.split("#", 1) + [""])[:2]
        anchor = "#" + anchor if anchor else ""
        resolved = posixpath.normpath(posixpath.join(src_repo_dir, target)).strip("/")
        if resolved in self.map:
            url = self.map[resolved]
            # A mapped URL may carry its own anchor (e.g. research.md → page#research)
            if anchor and "#" in url:
                url = url.split("#")[0]
            return root + url + anchor
        return GITHUB_BLOB + resolved + anchor

    def rewrite(self, md_text: str, src_repo_dir: str, root: str) -> str:
        def sub(m):
            return "](" + self.resolve(src_repo_dir, m.group(1), root) + ")"
        return re.sub(r"\]\(([^)\s]+)\)", sub, md_text)


LINKS = LinkMap()


def render_md(md_text: str, src_repo_dir: str, root: str) -> str:
    rewritten = LINKS.rewrite(md_text, src_repo_dir, root)
    return markdown.markdown(rewritten, extensions=MD_EXTENSIONS)


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
        label = ("Original recipe — " + m.group(1)) if m.group(1) else "Original recipe"
        links.append((label, m.group(2)))
    return credit, links


def creator_for(slug: str, credit: str | None, links) -> str:
    if slug in CREATOR_OVERRIDES:
        return CREATOR_OVERRIDES[slug]
    if credit:
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
            "title": first_h1(text),
            "covers": covers,
            "blurb": first_paragraph(strip_first_h1(text)),
            "text": text,
        })
    return articles


# -------------------------------------------------------------------- build

def build():
    index_meta = parse_recipe_index()
    originals, references = discover_recipes(index_meta)
    articles = load_knowledge_articles()

    # Register every URL in the link map before rendering anything.
    for r in originals + references:
        LINKS.add(r["repo_dir"], r["url"])
        for fname, sec_id, _ in RECIPE_SECTIONS:
            if (Path(ROOT / r["repo_dir"]) / fname).exists():
                LINKS.add(r["repo_dir"] + "/" + fname, r["url"] + "#" + sec_id)
    for a in articles:
        LINKS.add(a["repo_path"], a["url"])
    LINKS.add("Knowledge/README.md", "knowledge/")
    LINKS.add("Knowledge", "knowledge/")
    LINKS.add("X-T5/README.md", "")
    LINKS.add("X-T5", "")
    LINKS.add("X-T5/RANKING.md", "ranking/")
    LINKS.add("README.md", "about/")

    env = Environment(loader=FileSystemLoader(SITE_DIR / "templates"),
                      autoescape=False, trim_blocks=True, lstrip_blocks=True)
    env.globals.update(site_title=SITE_TITLE, github=GITHUB_REPO,
                       email=CONTACT_EMAIL)

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "static").mkdir(parents=True)
    shutil.copy(SITE_DIR / "static" / "style.css", OUT / "static" / "style.css")
    (OUT / ".nojekyll").write_text("")

    def emit(url: str, template: str, **ctx):
        depth = url.rstrip("/").count("/") + 1 if url else 0
        root = "../" * depth
        page_dir = OUT / url
        page_dir.mkdir(parents=True, exist_ok=True)
        html = env.get_template(template).render(root=root, url=url, **ctx)
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    # -- home (originals) --------------------------------------------------
    groups = []
    for cat, label, intro in ORIGINAL_CATEGORIES:
        cards = [r for r in originals if r["category"] == cat]
        groups.append({"label": label, "intro": intro, "cards": cards})
    emit("", "home.html", nav="originals", groups=groups,
         n_originals=len(originals), n_references=len(references),
         n_articles=len(articles),
         meta_description="A research-backed bank of Fujifilm X-T5 film-simulation "
                          "recipes, validated against manufacturer datasheets and real film scans.")

    # -- community ---------------------------------------------------------
    emit("community/", "community.html", nav="community", cards=references,
         meta_description="Film-simulation recipes by the wider Fujifilm community — "
                          "Fuji X Weekly, Ross McConaghy, Luís Costa and more — with full attribution.")

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
        emit(r["url"], "recipe.html",
             nav="originals" if r["tier"] == "original" else "community",
             r=r, sections=rendered_sections,
             meta_description=(r["blurb"] or r["mood"])[:300])

    # -- knowledge ---------------------------------------------------------
    emit("knowledge/", "knowledge_index.html", nav="knowledge", articles=articles,
         meta_description="The knowledge layer: what every Fujifilm setting does, the "
                          "color science of film simulations, film chemistry, and the validation methodology.")
    for a in articles:
        body = demote_headings(strip_first_h1(a["text"]))
        emit(a["url"], "article.html", nav="knowledge", title=a["title"],
             content=render_md(body, "Knowledge", "../../"),
             source_path=a["repo_path"],
             meta_description=a["blurb"][:300])

    # -- ranking -----------------------------------------------------------
    ranking = read(ROOT / "X-T5" / "RANKING.md")
    emit("ranking/", "article.html", nav="originals",
         title=first_h1(ranking),
         content=render_md(demote_headings(strip_first_h1(ranking)), "X-T5", "../"),
         source_path="X-T5/RANKING.md",
         meta_description="The full recipe bank ranked by aesthetic value and real-world popularity.")

    # -- about -------------------------------------------------------------
    about = read(ROOT / "README.md")
    emit("about/", "article.html", nav="about", title="About",
         content=render_md(demote_headings(strip_first_h1(about)), "", "../"),
         source_path="README.md",
         meta_description="What this project is: a validated, research-backed Fujifilm "
                          "recipe bank and the knowledge layer behind it.")

    # -- contact -----------------------------------------------------------
    emit("contact/", "contact.html", nav="contact",
         meta_description="Get in touch — questions, corrections, or film scans to help validate recipes.")

    # -- search index (client-side filter) ---------------------------------
    idx = [{"t": r["title"], "s": r["sim"], "m": r["mood"], "u": r["url"],
            "tier": r["tier"]} for r in originals + references]
    (OUT / "static" / "recipes.json").write_text(json.dumps(idx, ensure_ascii=False))

    n_pages = sum(1 for _ in OUT.rglob("index.html"))
    print(f"Built {n_pages} pages → {OUT}")


if __name__ == "__main__":
    build()
