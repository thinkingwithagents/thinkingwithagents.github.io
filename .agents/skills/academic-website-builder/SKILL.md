---
name: academic-website-builder
description: >-
  Build a clean, modern, CV-driven academic website for a researcher, professor, postdoc, or grad
  student. Generates three distinct design mock-ups (minimal dark, light academic, bold modern) from
  a CV, lets the person preview all three and modify any of them, then has them pick one — producing a
  self-contained site that is genuinely easy to keep updated (edit one data file, or drop in a new CV,
  and re-run one build command). Use this whenever someone wants to create, build, design, generate,
  refresh, or deploy an academic or faculty website, a researcher/scholar personal homepage, a "website
  from my CV/resume", a professor or lab landing page, or wants to update a site previously built with
  this skill. Trigger even when they don't say "skill" — e.g. "make me a personal academic site",
  "turn my CV into a website", "I need a faculty page", "update my academic website with my new papers".
---

# Academic Website Builder

Most academics have no time and no interest in fighting with web tooling. This skill turns a CV into a
polished personal website and — crucially — leaves behind something they can keep current themselves by
editing **one plain data file** (or dropping in a fresh CV) and running **one command**. No frameworks,
no build pipeline to learn, no servers required.

## What it produces

A self-contained site folder the person owns and can deploy anywhere:

```
<site>/
  cv-data.json      <- the single source of truth (everything on the site lives here)
  build.py          <- run `python build.py` to (re)generate the site; no dependencies
  templates/        <- the three theme templates (edit these to change a design)
  CV/               <- the source CV (PDF), linked as a download
  index.html        <- the LIVE site: the chosen theme (this is what you deploy)
  preview.html      <- a chooser page showing all three themes side by side
  site-minimal-dark.html  site-light-academic.html  site-bold-modern.html
  README.md         <- plain-language "how to update & deploy" for the academic
```

The three themes are real, distinct visual identities, not recolors of one template:
- **minimal-dark** — twilight charcoal + iris accent; research as a typed "ledger". Restrained, design-forward.
- **light-academic** — cool paper + pine green, literary serif, card-based. Scholarly, à la Chetty.
- **bold-modern** — full-width bands, oversized display type, a press "ticker". High-impact, public-facing.

## The core idea (why updates are easy)

`build.py` reads `cv-data.json` and renders **all three themes** plus the chooser. The academic never
edits HTML to change content. Adding a paper = adding one object to a JSON list; fixing a title = editing
one string; switching the whole design = changing `"theme"`. Then `python build.py` rebuilds in a second.
A whole-CV refresh means re-extracting the new CV into `cv-data.json` (Claude does this) and rebuilding.

**Always generate all three themes and let the person choose at the end** — seeing the real options beside
their own content is far more useful than picking a theme up front. Let them request changes to any one.

## Workflow

### 1 — Gather inputs (keep it short; academics are busy)
- Locate the CV (PDF/DOCX) in the working directory or ask for the path. Read it.
- Ask the small set of intake questions in `references/intake.md` (profile links, public email, bio depth,
  photo, deploy target). Do **not** ask which theme up front — all three get built.
- If they mention an existing website, offer to fetch it (WebFetch) and merge contact details/links.

### 2 — Extract the CV into `cv-data.json`
- Read `references/cv-data-schema.md` for the field-by-field shape, and `assets/cv-data.example.json` for a
  complete worked example (a fictional but realistic economist's CV — use it as the pattern, not the content).
- Extract faithfully: exact titles, venues, coauthors, years; classify each publication into one of
  `under_revision`, `peer_reviewed`, `working_paper`, `in_progress`, `policy_report`; flag 3–4 as
  `featured`; capture press notes as `badge`/`tag`. Draft the bio (see `references/intake.md`); apply the
  `avoid-ai-writing` skill so it doesn't read as AI prose.
- Show the person the key extracted facts (name, title, counts, featured picks, bio) and let them correct
  before building. LLM extraction is reliable but not perfect — a quick human confirm is worth it.

### 3 — Scaffold the site folder
Copy the engine and templates next to the new `cv-data.json` so the site is portable and self-contained:
```
# from the chosen <site> folder
cp "<skill>/scripts/build.py" build.py
mkdir -p templates && cp "<skill>/assets/templates/"*.html templates/
mkdir -p CV && cp "<the CV>" CV/      # match site.cv_file in cv-data.json
cp "<skill>/assets/README.template.md" README.md
```
Write the extracted `cv-data.json` into `<site>/cv-data.json`.

### 4 — Build all three and review
Run `python build.py`. Open `preview.html` to show all three themes side by side (the chooser embeds live
previews). Walk through each. If a preview tool is available, screenshot each for a quick visual check.

### 5 — Let them modify any theme
- **Content** (any theme): edit `cv-data.json`, rebuild. This covers ~90% of requests.
- **Design** of a specific theme: edit `templates/<theme>.html` (colors live in the `:root` CSS variables
  near the top; layout is plain HTML). Keep the template's `{{tokens}}` intact — see the engine note below.
- Treat the three themes as strong starting points, not constraints. For substantive redesigns, apply the
  `frontend-design` skill's principles and make deliberate choices for *this* person rather than templated
  defaults.

### 6 — Choose the live theme
Set `"theme"` in `cv-data.json` to their pick (or pass `--theme`), rebuild. `index.html` is now their site.

### 7 — Deploy
Walk them through `references/deployment.md` (GitHub Pages is the recommended free default; Netlify /
Cloudflare Pages are easy alternatives; reuse an existing domain if they have one).

### 8 — Updating later (the promise of this skill)
Point them to `README.md` and `references/updating.md`. Two paths: (a) edit `cv-data.json` + `python
build.py`; (b) hand Claude a new CV → re-extract into `cv-data.json` (preserving `site`, `links`, `photo`)
→ rebuild. Switching theme, adding a photo (`site.photo`), and adding profile links are all one-line edits.

## How the templates work (template engine)

`build.py` includes a tiny, dependency-free template engine. Templates use:
`{{ field }}` (HTML-escaped value), `{{{ field }}}` (raw), `{{#each list}}…{{/each}}`,
`{{#if key}}…{{/if}}`, `{{#unless key}}…{{/unless}}`. It supports **one level of `{{#each}}` and no nested
`{{#if}}`** — keep conditionals flat (precompute combined values in `build.py`'s `prepare_context` if you
need a conditional inside a conditional). CSS/JS use single braces and never collide with `{{ }}`. The
fields available to templates are exactly what `prepare_context` builds; read it before adding a new token.

## Reference files
- `references/intake.md` — the intake questions, bio-drafting guidance, profile-link and deploy options.
- `references/cv-data-schema.md` — every `cv-data.json` field, with the publication `type` taxonomy.
- `references/deployment.md` — GitHub Pages / Netlify / Cloudflare Pages, custom domains, analytics.
- `references/updating.md` — the edit-and-rebuild loop, theme switching, photos, links, new-CV refresh.
- `assets/cv-data.example.json` — a full, worked example (use as the extraction pattern).
- `assets/README.template.md` — plain-language guide that ships inside the generated site.
- `scripts/build.py` — the build engine; read `prepare_context` to see all template fields.
