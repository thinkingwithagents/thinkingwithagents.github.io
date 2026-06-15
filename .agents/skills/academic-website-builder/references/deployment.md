# Deployment

The site is plain static files (`index.html` + the `site-*.html` pages + `CV/` + any photo). It can be
hosted free, with HTTPS, in minutes. Recommend **GitHub Pages** as the default; the others are equally fine.

## Option A — GitHub Pages (recommended, free)

Best when the academic is OK with a GitHub account; supports a custom domain and free HTTPS.

1. Create a repo (e.g. `lastname.github.io` for a user site, or any name for a project site).
2. Commit the site folder contents (including `index.html`, `CV/`, the photo, and — so they can rebuild
   later — `cv-data.json`, `build.py`, and `templates/`).
3. Repo **Settings → Pages → Build and deployment → Deploy from a branch**, pick `main` / root.
4. The site is live at `https://<user>.github.io/<repo>/` within a minute.

Optional auto-rebuild on push: add a GitHub Action that runs `python build.py` and commits the output, so
the academic only ever edits `cv-data.json` and pushes. Offer this only if they're comfortable with Actions.

## Option B — Netlify or Cloudflare Pages (free, drag-and-drop or git)

- Netlify: drag the site folder onto the dashboard, or connect the repo. Instant deploy + rollbacks.
  Netlify Forms can give a working contact form with no backend.
- Cloudflare Pages: connect the repo, set build command to `python build.py` and output dir to the folder
  (or "no build" and serve as-is). Generous free tier, fast global CDN.

## Option C — Vercel (free)

Connect the repo; for a no-build static site, set the framework preset to "Other" and output to the folder.

## Custom domain

If they already own a domain (e.g. `name.com`), point it at the host:
- GitHub Pages: add a `CNAME` file with the domain and set DNS (CNAME to `<user>.github.io`, or A records
  to GitHub's IPs). Enable "Enforce HTTPS".
- Netlify/Cloudflare/Vercel: add the domain in the dashboard and follow the DNS prompts.

No domain yet? Cloudflare Registrar (at-cost, ~$10/yr), Porkbun, or Namecheap are cheap and reliable.

## Analytics (optional, privacy-friendly)

**GoatCounter is built in** (free, open source, no cookies — so no consent banner needed): have them
sign up at goatcounter.com, pick a site code, and set `site.goatcounter` to that code in `cv-data.json`,
then rebuild. Every page then reports pageviews to their private dashboard at
`https://<code>.goatcounter.com` (iframe loads, e.g. preview.html's embedded themes, are not counted).

Alternatives, if they prefer (one-line snippet in the templates' `<head>`):
- **Cloudflare Web Analytics** — free, no cookies.
- **Umami** — self-host for free, or hosted.

## "Just give me the files"

Perfectly valid. Zip the folder; they can open `index.html` locally and host it whenever they like. Everything
works offline except the Google Fonts `<link>` (which degrades gracefully to system fonts).
