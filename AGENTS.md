# AGENTS.md

Repo-local instructions for collaborators working on `uvmecon-ai`.

## Purpose

This repo supports a small Quarto website plus separately rendered reveal.js slide decks for the UVM Econ-AI bootcamp.

The main goal is to keep edits fast and safe:

- edit source files, not generated output
- use the smallest render that matches the change
- avoid broken slide links or accidental LaTeX builds

## Source of truth

Edit these files:

- website pages in the repo root: `index.qmd`, `prep.qmd`, `resources.qmd`, `session1.qmd`, `session2.qmd`
- slide sources in `slides/*.qmd`
- site config in `_quarto.yml`
- slide config in `slides/_quarto.yml`

Do **not** edit generated files in `docs/` by hand.

## Canonical build commands

Use the repo script instead of ad hoc render commands.

- `./render.sh site`
  Rebuild the main website only. Use this for most text and navigation edits.

- `./render.sh slides-html`
  Rebuild slide HTML only. Use this after editing slide source `.qmd` files.

- `./render.sh slides-pdf`
  Rebuild slide PDFs from already-rendered slide HTML using Chrome headless.

- `./render.sh all`
  Rebuild the website plus slide HTML plus slide PDFs.

## Default workflow

For normal website edits:

1. Edit the source `.qmd` file.
2. Run `./render.sh site`.
3. Check the changed source and generated `docs/` output.

For slide edits:

1. Edit the source file in `slides/`.
2. Run `./render.sh slides-html`.
3. Run `./render.sh slides-pdf` only if the downloadable PDFs need updating.

## Known pitfalls

- Do not rely on stale file names like `slides/session1.qmd` or `slides/session2.qmd`. The current slide files are split by section.
- Do not edit `docs/slides/` directly.
- Do not use Beamer/LaTeX for slide PDFs here. This repo uses reveal.js HTML plus Chrome headless PDF output.
- If a render is interrupted, rerun the relevant `./render.sh ...` command rather than trying to clean up generated files manually.

## Current slide source files

- `slides/demo-title.qmd`
- `slides/demo-columns.qmd`
- `slides/demo-table.qmd`
- `slides/s1-intro.qmd`
- `slides/s1-emily.qmd`
- `slides/s1-erkmen.qmd`
- `slides/s2-part1.qmd`
- `slides/s2-part2.qmd`

## Collaboration notes

- Emily is using Codex and Claude.
- Erkmen may also use Codex while collaborating.
- Keep comments and instructions plain-language. Avoid unnecessary software jargon for faculty-facing text.
- When revising the prep guide, prefer the distinction:
  - `chat-based tools`
  - `agentic tools`
  rather than browser/app distinctions.

## High-value habits

- If you change navigation or page names, run `./render.sh site` before stopping.
- If you change slide file names or links, rebuild slide HTML before stopping.
- Keep placeholders explicit when collaborator content is still missing.
