# Session Log — Cash Transfers & School Attendance (Kenya)

> ⓘ This is a **fictional sample** for the Thinking with Agents webinar (June 2026).
> Pairs with **`sample-HUB.md`**. The HUB holds the *current state*; this log holds the
> *running history* — what each work session did, why, and where to pick up next.
>
> Newest entry on top. Each entry: what we tackled, decisions (with the *why*), files
> touched, and a "Start here next time" handoff.

---

## 2026-06-12 · Session 4 — Heterogeneity by poverty

**Goal:** Start the heterogeneity analysis now that the main spec is settled.

**What happened:**
- Confirmed the balance table still passes after the midline merge (no differential attrition flags).
- Ran the main attendance regression interacted with a baseline poverty index (PCA of asset ownership).
- First pass: the attendance effect looks roughly twice as large in the poorest tercile, but CIs overlap — needs the endline data before we lean on it.

**Decisions:**
- Use the **baseline** poverty index for heterogeneity, not midline — midline poverty is post-treatment and would be a bad control. *(Why: avoids conditioning on an outcome.)*

**Files touched:**
- `code/04_heterogeneity.do` (new)
- `03_output/f3_het_poverty.png` (new, draft figure)

**Start here next time:**
- Don't finalize heterogeneity numbers until the transfer-student recode is resolved (see open question in HUB) — it shifts the denominator.

---

## 2026-06-05 · Session 3 — Main spec + SE clustering

**Goal:** Lock down the main attendance regression so results are stable.

**What happened:**
- Specified the primary model: attendance rate on treatment, school strata fixed effects, baseline controls.
- Reviewed whether to cluster at school or household.

**Decisions:**
- **Cluster SEs at the school level** — that's the unit of randomization. *(Why: clustering below the randomization unit understates SEs.)* Recorded in HUB "Key Decisions."

**Files touched:**
- `code/03_main_results.do`
- `03_output/t2_attendance.tex`

**Start here next time:**
- Begin heterogeneity by poverty. Build the baseline poverty index first.

---

## 2026-05-28 · Session 2 — Clean and merge midline

**Goal:** Get midline into a usable analysis file.

**What happened:**
- Cleaned the midline attendance roster; fixed 14 duplicate student IDs (kept the most recent record).
- Merged midline to baseline on `student_id`; 3% unmatched, all explained by students who left the sample area.

**Decisions:**
- All cleaning writes to `02_working/`; `01_raw/` stays untouched. *(Why: reproducibility — raw must always regenerate the same working file.)*

**Files touched:**
- `code/02_clean_midline.do`
- `02_working/midline_clean.dta`

**Start here next time:**
- Specify the main attendance regression and settle SE clustering.

---

## 2026-05-20 · Session 1 — Project setup

**Goal:** Stand up the project so future sessions have context.

**What happened:**
- Created the project HUB (`sample-HUB.md`): mapped where data, code, and the draft live; listed the team and what each person is waiting on.
- Confirmed IRB and pre-registration IDs and recorded them in the HUB.

**Files touched:**
- `sample-HUB.md` (new)

**Start here next time:**
- Clean and merge the midline data.
