# Your academic website

This folder is your whole website. It's plain HTML — no accounts, no frameworks, nothing to install beyond
Python (which you already have). Everything you see on the site comes from **one file: `cv-data.json`**.

## Files

- **`cv-data.json`** — all your content (name, bio, publications, teaching, links). Edit this.
- **`build.py`** — regenerates the site. Run it after editing `cv-data.json`.
- **`index.html`** — your live site (the design you chose). This is the page you publish.
- **`preview.html`** — shows all three designs side by side, so you can switch any time.
- **`site-*.html`** — the three designs (minimal dark, light academic, bold modern).
- **`templates/`**, **`CV/`** — the design templates and your CV download. Leave `templates/` alone unless
  you want to tweak a design.

## Update your site in three steps

1. Open `cv-data.json` in any text editor.
2. Make your change (examples below).
3. Run this in a terminal from this folder:
   ```
   python build.py
   ```
   Then refresh your browser — or push to your host to publish.

### Common edits

- **Add a publication:** in the `"publications"` list, copy a nearby `{ ... }` block, paste it, and update
  the title, authors, venue, and year. Set `"type"` to one of: `peer_reviewed`, `working_paper`,
  `under_revision`, `in_progress`, `policy_report`.
- **Change your design:** set `"theme"` (top of the file) to `minimal-dark`, `light-academic`, or
  `bold-modern`, then rebuild.
- **Add your photo:** drop the image in this folder and set `"photo": "your-photo.jpg"` under `"site"`.
- **Add a link (Scholar, ORCID, LinkedIn, X…):** fill in the matching field under `"links"`. Blank ones
  stay hidden.
- **Fix a typo anywhere:** find the text in `cv-data.json`, change it, rebuild.

### Got a freshly updated CV?

You don't have to re-type anything. Open this folder with Claude Code and say *"update my website from my new
CV"* — it will refresh `cv-data.json` for you (keeping your design, photo, and links) and rebuild.

## Publish it

See your setup notes, or: put these files in a GitHub repo and turn on **Settings → Pages**, or drag the
folder onto **Netlify** / **Cloudflare Pages**. All free, all with HTTPS. The site works offline too —
just open `index.html`.
