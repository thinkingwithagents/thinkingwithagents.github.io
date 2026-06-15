# Intake questions & content guidance

Keep intake short — academics are busy. Default aggressively, confirm lightly, and prefer showing them
something to react to over interrogating them. Use the `AskUserQuestion` tool to batch these where possible.

## Questions to ask

1. **CV** (required) — "Point me to your CV (PDF or DOCX)." If it's already in the working directory, just
   confirm you found it.
2. **Existing website** — "Do you have a current site I should pull contact details or links from?" If yes,
   fetch it (WebFetch) and merge email / profile links / any bio you find.
3. **Profile links** (multi-select) — which to include, and the URL for each:
   Google Scholar · ORCID · LinkedIn · X/Twitter · GitHub · NBER/IDEAS-RePEc · personal blog · Bluesky ·
   YouTube · other. These map to `links.*` in `cv-data.json`; only links with a URL render. Email always shows.
4. **Public email** — confirm the contact email (default: the one on the CV).
5. **Bio depth** — Short (2–3 sentences) / Standard (one paragraph) / Extended (with a research narrative).
   Offer to draft it from the CV (see below); set `site.bio_use` to their pick. All three are stored in
   `bio.{short,standard,extended}` so they can switch later.
6. **Photo** — "Have a headshot? Give me the file." If not, the site uses a tasteful initials placeholder;
   they can add one later via `site.photo`. Bold-modern intentionally uses no photo.
7. **Deploy target** — GitHub Pages (recommended free default) / Netlify / Cloudflare Pages / Vercel /
   "just give me the files for now". Details in `deployment.md`.

Do **not** ask which theme they want — build all three and let them choose at the end.

## Drafting the bio

Write in the third person. Lead with field and the core research questions; name 3–4 flagship venues and any
notable press; keep it concrete. Avoid clichés and AI tells — apply the `avoid-ai-writing` skill to the draft.

- **short** → one or two sentences (used as the punchy hero line via `about.lead` if you don't set one).
- **standard** → one paragraph (the default body shown in About / hero).
- **extended** → a fuller narrative for people who want more depth.

Also draft `about.lead` — a single punchy sentence that leads the hero/About (e.g. what the work is really
about, plus the strongest signal of reach: a top venue, major press, or a policy citation).

## Stats (the numeric callouts)

`stats` drives the bold-modern hero strip and the light-academic "Funded research" row. Pick 4 honest,
high-signal numbers, e.g.: peer-reviewed count · working-paper count · total grant funding · "cited by CBO/GAO"
or "featured in NPR, TIME". Keep them true; if a number isn't impressive, choose a different dimension.

## Featured publications

Flag 3–4 publications with `"featured": true` — ideally the highest-venue or most-covered work, with a mix of
topics. Give each a short `venue_short` (e.g. "PNAS", "J. Public Economics") for the card eyebrow, a `year`,
and a `badge` if it has press ("Featured in TIME"). These become the cards at the top of the research section
and seed the bold theme's press ticker.
