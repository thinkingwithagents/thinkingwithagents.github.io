#!/usr/bin/env python3
"""Academic website builder — build engine.

This is the piece that makes the site easy to keep up to date. Everything on the
website comes from one file, `cv-data.json`. Edit that file (add a paper, change
your title, fix a typo) and run this script — the whole site rebuilds in a second.
No frameworks, no install step: just Python 3.8+ and the template files next to
this script.

Typical use
-----------
    python build.py                      # rebuild the site from ./cv-data.json
    python build.py --data other.json    # use a different data file
    python build.py --theme bold-modern  # force the live theme (overrides cv-data)

What it writes (all in the site folder, so relative links to CV/ and your photo
just work):
    index.html                 -> your chosen theme (this is the page you deploy)
    site-minimal-dark.html     -> the three themes, always rebuilt so you can
    site-light-academic.html      compare them or switch any time
    site-bold-modern.html
    preview.html               -> a chooser page that shows all three side by side

To switch the live theme later, change "theme" in cv-data.json (or pass --theme)
and rebuild. To refresh from a brand-new CV, have Claude re-extract it into
cv-data.json (keeping your links/photo/theme settings), then rebuild.
"""
import argparse
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_templates():
    # Works both in the deployed site (templates/ next to this script) and in
    # the skill source tree (scripts/build.py with assets/templates/).
    for cand in (os.path.join(HERE, "templates"), os.path.join(HERE, "..", "assets", "templates")):
        if os.path.isdir(cand):
            return os.path.abspath(cand)
    return os.path.join(HERE, "templates")


TEMPLATE_DIR = _find_templates()
THEMES = ["minimal-dark", "light-academic", "bold-modern"]


# --------------------------------------------------------------------------
# Tiny template engine: {{var}}, {{{raw}}}, {{#each list}}…{{/each}},
# {{#if key}}…{{/if}}, {{#unless key}}…{{/unless}}. One level of looping is
# enough because the data is pre-grouped into flat lists below. Values are
# HTML-escaped by default; use {{{triple}}} only for trusted pre-built HTML.
# CSS/JS in the templates use single braces, so they never collide with {{ }}.
# --------------------------------------------------------------------------
EACH_RE = re.compile(r"\{\{#each\s+([\w.]+)\}\}(.*?)\{\{/each\}\}", re.S)
IF_RE = re.compile(r"\{\{#if\s+([\w.]+)\}\}(.*?)\{\{/if\}\}", re.S)
UNLESS_RE = re.compile(r"\{\{#unless\s+([\w.]+)\}\}(.*?)\{\{/unless\}\}", re.S)
RAW_RE = re.compile(r"\{\{\{\s*([\w.]+)\s*\}\}\}")
VAR_RE = re.compile(r"\{\{\s*([\w.]+)\s*\}\}")


def _resolve(path, ctx, root):
    """Look up a dotted path in the current loop item, then fall back to root."""
    if path in (".", "this"):
        return ctx if not isinstance(ctx, (dict, list)) else ""
    for source in (ctx, root):
        cur = source
        ok = True
        for part in path.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                ok = False
                break
        if ok and cur is not None:
            return cur
    return ""


def _truthy(v):
    if isinstance(v, (list, dict)):
        return len(v) > 0
    if isinstance(v, str):
        return v.strip() != ""
    return bool(v)


def render(tpl, ctx, root):
    def each_sub(m):
        items = _resolve(m.group(1), ctx, root)
        if not isinstance(items, list):
            return ""
        return "".join(render(m.group(2), it, root) for it in items)

    tpl = EACH_RE.sub(each_sub, tpl)
    tpl = UNLESS_RE.sub(
        lambda m: "" if _truthy(_resolve(m.group(1), ctx, root)) else render(m.group(2), ctx, root),
        tpl,
    )
    tpl = IF_RE.sub(
        lambda m: render(m.group(2), ctx, root) if _truthy(_resolve(m.group(1), ctx, root)) else "",
        tpl,
    )
    tpl = RAW_RE.sub(lambda m: str(_resolve(m.group(1), ctx, root)), tpl)
    tpl = VAR_RE.sub(lambda m: html.escape(str(_resolve(m.group(1), ctx, root)), quote=True), tpl)
    return tpl


# --------------------------------------------------------------------------
# Turn the user-facing cv-data.json into a render context: group publications,
# resolve the active bio, derive a few theme-specific bits so the data file
# itself stays clean and easy to edit.
# --------------------------------------------------------------------------
def prepare_context(raw):
    d = dict(raw)
    site = raw.get("site", {}) or {}
    d["cv_file"] = site.get("cv_file", "")
    d["footer_year"] = str(site.get("footer_year", ""))
    d["photo"] = site.get("photo", "")
    d["photo_alt"] = "%s, %s" % (raw.get("name", ""), raw.get("title", ""))
    d["has_photo"] = _truthy(site.get("photo", ""))
    d["goatcounter"] = site.get("goatcounter", "")
    d["institution_short"] = raw.get("institution_short") or raw.get("institution", "")
    d["since"] = str(raw.get("since", ""))

    parts = [p for p in raw.get("name", "").split() if p]
    d["initials"] = "".join(p[0] for p in parts[:3]).upper()

    bio = raw.get("bio", {}) or {}
    use = site.get("bio_use", "standard")
    d["bio_text"] = bio.get(use) or bio.get("standard") or bio.get("short") or ""

    about = raw.get("about", {}) or {}
    d["about_lead"] = about.get("lead") or bio.get("short") or d["bio_text"]
    d["about_where_heading"] = about.get("where_heading", "Where the work lands")
    d["about_where_body"] = about.get("where_body") or d["bio_text"]
    d["research_intro"] = (
        raw.get("research_intro")
        or about.get("research_intro")
        or ("Selected research across %s." % (raw.get("fields") or raw.get("tagline") or "economics"))
    )

    links = raw.get("links", {}) or {}
    d["links"] = links
    d["has_any_link"] = any(_truthy(v) for v in links.values())
    link_labels = [
        ("scholar", "Google Scholar"), ("orcid", "ORCID"), ("linkedin", "LinkedIn"),
        ("x", "X"), ("github", "GitHub"), ("website", "Website"), ("nber", "NBER"),
        ("bluesky", "Bluesky"), ("youtube", "YouTube"),
    ]
    d["social_links"] = [
        {"label": label, "url": links[key]} for key, label in link_labels if _truthy(links.get(key))
    ]

    pubs = raw.get("publications", []) or []
    by_type = lambda t: [p for p in pubs if p.get("type") == t]
    d["under_revision"] = by_type("under_revision")
    d["peer_reviewed"] = by_type("peer_reviewed")
    d["working_papers"] = by_type("working_paper")
    d["in_progress"] = by_type("in_progress")
    d["policy_reports"] = by_type("policy_report")

    featured = [p for p in pubs if p.get("featured")][:4]
    for i, p in enumerate(featured):
        p["num"] = "0%d" % (i + 1)
    d["featured"] = featured

    # Marquee for the bold theme: flagship venues + press outlets, de-duplicated.
    seen, ticker = set(), []
    for p in featured:
        vs = p.get("venue_short", "")
        if vs and vs not in seen:
            seen.add(vs)
            ticker.append(vs)
    for m in raw.get("media", []) or []:
        o = m.get("outlet", "")
        if o and o not in seen:
            seen.add(o)
            ticker.append(o)
    d["ticker_items"] = ticker

    d["count_under_revision"] = str(len(d["under_revision"]))
    d["count_peer_reviewed"] = str(len(d["peer_reviewed"]))
    d["count_working_papers"] = str(len(d["working_papers"]))
    d["count_in_progress"] = str(len(d["in_progress"]))
    d["count_policy_reports"] = str(len(d["policy_reports"]))
    nber = sum(
        1 for p in d["working_papers"]
        if "nber" in (str(p.get("venue", "")) + str(p.get("marker", "")) + str(p.get("note", ""))).lower()
    )
    d["count_wp_nber"] = str(nber)
    # Precompute the working-papers count label so templates need no nested {{#if}}
    # (the template engine intentionally supports only one level of conditionals).
    d["wp_count_label"] = d["count_working_papers"] + ((" · %d NBER" % nber) if nber else "")

    # Bold theme "fact list" — derived so the data file needs no theme-specific keys.
    edu = raw.get("education", []) or []
    facts = []
    fields = raw.get("fields") or raw.get("tagline", "")
    if fields:
        facts.append({"k": "Fields", "v": fields})
    if edu:
        e0 = edu[0]
        spec = e0.get("degree", "")
        spec = spec.split(",")[-1].strip() if "," in spec else spec
        v = "%s, %s" % (spec, e0.get("institution", ""))
        if e0.get("year"):
            v += " (%s)" % e0["year"]
        if e0.get("note"):
            v += " — %s" % e0["note"]
        facts.append({"k": "Ph.D.", "v": v})
        d["edu_primary"] = "%s, %s" % (
            e0.get("degree", "").split(",")[0].strip(), e0.get("institution", ""),
        )
    else:
        d["edu_primary"] = ""
    at = "%s since %s" % (raw.get("title", ""), d["since"]) if d["since"] else raw.get("title", "")
    facts.append({"k": "At " + d["institution_short"], "v": at})
    affs = raw.get("affiliations", []) or []
    if affs:
        facts.append({"k": "Networks", "v": " · ".join(affs)})
    d["bold_facts"] = facts

    d["stats"] = raw.get("stats", []) or []
    return d


def build_one(theme, ctx):
    with open(os.path.join(TEMPLATE_DIR, theme + ".html"), encoding="utf-8") as fh:
        return render(fh.read(), ctx, ctx)


def main():
    ap = argparse.ArgumentParser(description="Build the academic website from cv-data.json")
    ap.add_argument("--data", default="cv-data.json", help="path to the data file")
    ap.add_argument("--out", default=".", help="output folder (defaults to current folder)")
    ap.add_argument("--theme", choices=THEMES, help="override the live theme")
    args = ap.parse_args()

    if not os.path.exists(args.data):
        sys.exit("error: %s not found. Run this from your site folder, or pass --data." % args.data)

    with open(args.data, encoding="utf-8") as fh:
        raw = json.load(fh)
    ctx = prepare_context(raw)

    chosen = args.theme or (raw.get("site", {}) or {}).get("theme", "light-academic")
    if chosen not in THEMES:
        print("warning: unknown theme %r, falling back to light-academic" % chosen)
        chosen = "light-academic"

    os.makedirs(args.out, exist_ok=True)
    rendered = {}
    for theme in THEMES:
        rendered[theme] = build_one(theme, ctx)
        with open(os.path.join(args.out, "site-%s.html" % theme), "w", encoding="utf-8") as fh:
            fh.write(rendered[theme])

    with open(os.path.join(args.out, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(rendered[chosen])

    with open(os.path.join(TEMPLATE_DIR, "chooser.html"), encoding="utf-8") as fh:
        chooser = render(fh.read(), ctx, ctx)
    with open(os.path.join(args.out, "preview.html"), "w", encoding="utf-8") as fh:
        fh.write(chooser)

    print("Built %s" % os.path.abspath(args.out))
    print("  index.html        <- live site (theme: %s)" % chosen)
    print("  preview.html      <- compare all three themes")
    for theme in THEMES:
        print("  site-%s.html" % theme)


if __name__ == "__main__":
    main()
