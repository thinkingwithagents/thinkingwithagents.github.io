# `cv-data.json` schema

One JSON file is the single source of truth for the whole site. `build.py` reads it, groups the
publications, derives a few values, and renders every theme. See `assets/cv-data.example.json` for a
complete worked example — copy its shape. All fields are plain strings unless noted. The `&` character is
fine in values (it's HTML-escaped automatically); do not put HTML tags in values.

## Top-level fields

| Field | What it is |
|---|---|
| `site.theme` | live theme for `index.html`: `minimal-dark` \| `light-academic` \| `bold-modern` |
| `site.photo` | path to a headshot (e.g. `assets/photo.jpg`); empty → initials placeholder |
| `site.cv_file` | path to the CV download (e.g. `CV/Name_CV.pdf`) |
| `site.footer_year` | year shown in the footer |
| `site.bio_use` | which bio to show: `short` \| `standard` \| `extended` |
| `site.goatcounter` | optional GoatCounter code (the `code` in `https://code.goatcounter.com`) — adds privacy-friendly visitor analytics to every page; empty → no tracking script |
| `name`, `first_name`, `last_name` | full name and its parts (parts drive the hero line break + brand) |
| `title` | e.g. "Assistant Professor of Economics" |
| `institution`, `institution_short` | e.g. "University of Vermont" / "UVM" |
| `since` | year they joined `institution` (used in the light theme photo caption) |
| `email` | public contact email (always shown) |
| `tagline` | short field line, e.g. "Health · Labor · Public Economics" |
| `fields` | longer field list (used in the bold theme's fact list) |
| `address_line1`, `address_line2` | department + street address for the contact section |
| `affiliations` | list of strings → the hero "chips" |
| `links` | object: `scholar, orcid, linkedin, x, github, website, nber, bluesky, youtube` — only non-empty ones render |
| `bio` | object with `short`, `standard`, `extended` strings |
| `about.lead` | one punchy sentence leading the hero/About |
| `about.where_heading`, `about.where_body` | the dark theme's "Where the work lands" column |
| `research_intro` | one sentence introducing the research section (light & bold themes); falls back to a line built from `fields` |
| `education` | list of `{degree, institution, year, note}` |
| `stats` | list of `{value, label}` — the 4 numeric callouts (bold hero strip, light grants row) |
| `publications` | list — see below |
| `teaching` | list of `{course, terms}` |
| `advising` | list of `{name, detail, note}` |
| `media` | list of `{outlet, headline, date, url}` |

## Publication objects

Each entry in `publications`:

| Field | What it is |
|---|---|
| `type` | one of `under_revision`, `peer_reviewed`, `working_paper`, `in_progress`, `policy_report` |
| `marker` | the left-column label in the list (e.g. a year `2024`, `NBER`, an NBER number, `JEL`, or `·`) |
| `title` | exact paper title |
| `authors` | author line, e.g. "with J. Currie & E. Tekin" or "sole author" or a first-author list |
| `note` | optional non-italic trailing info before the venue, e.g. "NBER WP 34245 · R&R" |
| `venue` | optional journal/venue (rendered italic), e.g. "PNAS, 123(21)" |
| `tag` | optional small badge in the list, e.g. "TIME", "Policy Impacts Library" |
| `url` | optional link for the title; empty → plain text (don't invent links) |
| `featured` | `true` for the 3–4 cards at the top of the research section |
| `venue_short` | short venue for a featured card's eyebrow (featured items only) |
| `year` | year shown on a featured card (featured items only) |
| `badge` | press line on a featured card, e.g. "Featured in TIME" (featured items only) |

`build.py` derives the rest (counts, the working-paper "· N NBER" suffix, the bold theme's fact list and
press ticker, the photo initials, the social-link list). To see exactly what a template can reference,
read `prepare_context` in `scripts/build.py` — every key it sets is available as a `{{token}}`.

## Publication `type` taxonomy

- `under_revision` — submitted / R&R at a journal (often with an NBER number).
- `peer_reviewed` — published articles, law reviews, forthcoming. The `featured` flags live here.
- `working_paper` — circulating but not yet under review / accepted.
- `in_progress` — early-stage; usually no venue and no link.
- `policy_report` — reports, briefs, non-refereed outlets.
