# Keeping the site up to date

This is the whole point of the skill: the academic should be able to maintain the site without touching HTML.
Everything flows from `cv-data.json` → `python build.py` → regenerated pages.

## Path A — edit the data file (the common case)

For any content change — a new paper, a fixed title, a new course, updated stats:

1. Open `cv-data.json`.
2. Make the edit. To add a publication, copy an existing object in the `publications` list and change its
   fields (`type`, `marker`, `title`, `authors`, `venue`, etc. — see `cv-data-schema.md`).
3. Run `python build.py`.
4. Refresh the browser (or commit/push to redeploy).

Common one-line edits:
- **Switch the live design:** change `site.theme` to `minimal-dark` / `light-academic` / `bold-modern`.
- **Add a headshot:** put the file in the folder and set `site.photo` (e.g. `assets/photo.jpg`).
- **Add a profile link:** fill in `links.scholar` / `links.orcid` / `links.linkedin` / `links.x` / etc.
  Empty links stay hidden; filled ones appear in the contact area.
- **Change which papers are featured:** set `"featured": true/false` on publications (keep it to ~4).

## Path B — drop in a brand-new CV (Claude does the parsing)

When the CV has changed a lot, hand the new CV to Claude and ask it to refresh the site. Claude will
re-extract the CV into `cv-data.json` — **preserving** the `site` block, `links`, `photo`, and `theme`
choice — then run `python build.py`. Review the diff (or the rebuilt pages) before deploying.

## Optional: rebuild automatically on push

If the site lives in a GitHub repo, a small GitHub Action can run `python build.py` on every push and commit
the regenerated HTML, so editing `cv-data.json` and pushing is all that's ever needed. See `deployment.md`.

## If something looks off

- A `{{token}}` showing up literally on the page means a template references a field that isn't being set —
  check `prepare_context` in `build.py` and the field name in `cv-data.json`.
- `python build.py` errors with "cv-data.json not found" → run it from inside the site folder.
- A publication in the wrong section → fix its `type` (`peer_reviewed`, `working_paper`, etc.).
