# Session 1 Slides — Work Log

Tracks open issues, decisions, and next steps for the consolidated Beamer deck.

---

## Open Issues

- [ ] **artemis.jpeg missing** — Erkmen's "productivity" meme slide (slide 36) references `figures/artemis.jpeg` but this file was never pushed to the repo. Get it from Erkmen or replace the slide. PDF compiles but shows a broken image placeholder.
- [ ] **Old slide comment numbers** — Erkmen's original slide comments (after the Emily inserts) still show their original numbering (e.g., `SLIDE 20` for what is now slide 26). Cosmetic only; LaTeX ignores comments. Fix if time permits.
- [ ] **Emily placeholders still generic** — Slides 19–21 use placeholder content from the Quarto originals. Emily to personalize:
  - Slide 19: Add 2–3 specific early experiences (currently generic examples)
  - Slide 20: Confirm the "used it for" list is accurate and complete
  - Slide 21: Review humor items, add/cut as needed

## Decisions Made (2026-04-18)

- Adopted Erkmen's Beamer template for all Session 1 slides (replacing Quarto revealjs)
- One coherent deck, no separate cuts
- Emily slides inserted after Safety (slide 18), before Planning
- Flow: Concepts → Emily personal experience → Voice file demo → Skills/Planning → Erkmen Apps → Wrap-up
- Voice file demo placed early (before skills) because it's simple and relatable
- All Emily content rewritten in Erkmen's framing (third-person, tcolorbox style)
- Site color scheme updated to match slide palette (SlateTeal/UVMGold)

## To Do

- [ ] Get `artemis.jpeg` from Erkmen → `Session1_Slides/figures/`
- [ ] Emily: personalize slides 19–21 with real examples
- [ ] Session 2 slides: build in Erkmen's Beamer template (currently still Quarto placeholders)
- [ ] Update `session2.qmd` links when Session 2 deck is ready

## Completed (2026-04-18)

- [x] Merged Erkmen's slides from `erkmen-update` branch
- [x] Renamed to joint deck (`session_1_slides.tex`)
- [x] Copied Emily screenshots to `Session1_Slides/figures/`
- [x] Inserted 6 Emily slides (19–24): December timeline, used-it-for, zero-time-saved, voice file comparison, creating voice file, using voice file
- [x] Created `custom.scss` with Erkmen palette
- [x] Updated `_quarto.yml`, `styles.css`, `slides/slides.css` colors
- [x] Compiled PDF (44 slides, 63 pages with pauses)
- [x] Rendered Quarto site with new palette
- [x] All committed to `main`
- [x] Updated `session1.qmd` to link consolidated Beamer PDF (was pointing to old Quarto HTML/PDF split)
