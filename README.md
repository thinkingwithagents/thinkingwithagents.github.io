# uvmecon-ai

Quarto website and slide decks for the UVM Economics AI bootcamp.

## Repo structure

- website pages live in the repo root:
  - `index.qmd`
  - `prep.qmd`
  - `resources.qmd`
  - `session1.qmd`
  - `session2.qmd`
- slide source lives in `slides/`
- rendered output lives in `docs/`

Edit source files, not generated files in `docs/`.

## Local render commands

From the repo root:

```bash
cd /Users/ebeam/Dropbox/GitHub/uvmecon-ai
```

Render the website only:

```bash
./render.sh site
```

Render slide HTML only:

```bash
./render.sh slides-html
```

Render slide PDFs from already-built HTML:

```bash
./render.sh slides-pdf
```

Render everything:

```bash
./render.sh all
```

If you changed `resources.qmd`, `session1.qmd`, `session2.qmd`, or other website pages, `./render.sh site` is usually enough.

If you changed files in `slides/`, the safest pre-push command is usually:

```bash
./render.sh all
```

## Deployment

This repo now includes a GitHub Actions workflow:

- `.github/workflows/deploy-pages.yml`

On push to `main`, GitHub Actions will:

1. install Quarto
2. detect Chrome or Chromium
3. run `./render.sh all`
4. deploy the generated `docs/` directory to GitHub Pages

You can also run the workflow manually from the GitHub Actions tab.

## Required GitHub Pages setting

In the GitHub repository settings, set:

- **Pages** -> **Build and deployment** -> **Source** -> `GitHub Actions`

If Pages is still configured to deploy from a branch, the workflow will run but the site will not deploy the way this repo expects.

## PDF rendering note

Slide PDFs are generated from reveal.js HTML using headless Chrome or Chromium.

The helper script:

- `slides/render_pdf.sh`

now works both:

- locally on macOS with Google Chrome
- in GitHub Actions on Linux with Chrome or Chromium

If PDF rendering fails locally, check that a browser is installed and available.

## Suggested pre-push workflow

1. Edit source `.qmd` files.
2. Run the smallest relevant render command locally.
3. Check source changes and generated `docs/` output.
4. Commit source and any intended generated output.
5. Push to `main`.
6. Let GitHub Actions rebuild and deploy the site.

## Notes

- `render.sh` is the canonical build entry point for this repo.
- Do not edit `docs/` by hand.
- If local rendering is flaky but source changes are correct, GitHub Actions can still serve as the clean deployment path once pushed.
