---
type: plan
project: uvmecon-ai
status: to-process
date: 2026-04-08
---

# Session 2 Research Demo: Prep Guide

## The demo concept

Emily tells Claude Code what to do — zero code from her. Claude writes an R script to download decennial census data from IPUMS USA, then writes Stata code to analyze it. The topic is **immigration and wages across census decades** — inspired by Borjas (2003, QJE), "The Labor Demand Curve is Downward Sloping."

**Verify the cite before putting it in slides.** The paper uses Census 1960–2000 and constructs skill cells (education × potential experience) to estimate the wage effect of immigration. We'll replicate the spirit of it with 1970–2020 data.

**Two-run design:**

1. **Dry run (before the session):** Run the full workflow from scratch. Save all prompts, outputs, and the final report. Note every place you intervened.
2. **Live run (during the session):** Do it again in front of the audience. Compare the two runs — what came out different, where you had to step in.

The comparison is the pedagogical payoff: the AI is useful but not deterministic, and your judgment matters at every step.

---

## Prerequisites (do these before the dry run)

### 1. IPUMS API key

You said you have one. Verify it's set as an environment variable:

```bash
echo $IPUMS_API_KEY
```

If not set, add to your `~/.zshrc`:

```bash
export IPUMS_API_KEY="your-key-here"
```

Then `source ~/.zshrc`.

If you need a new key: [account.ipums.org/api_keys](https://account.ipums.org/api_keys) (free, instant).

### 2. R packages

Claude Code will try to install these, but pre-install to avoid mid-demo delays:

```r
install.packages(c("ipumsr", "httr", "jsonlite", "tidyverse", "haven"))
```

`ipumsr` handles the IPUMS API. `haven` writes `.dta` files for Stata.

### 3. Stata

Needs to be callable from the command line. Verify:

```bash
which stata-se   # or stata-mp, or stata
```

If it's not on the PATH, Claude Code can't run it. On Mac, you may need to add the Stata directory to your PATH, or tell Claude Code the full path (e.g., `/Applications/Stata/StataSE.app/Contents/MacOS/stata-se`).

### 4. Demo project folder

```bash
mkdir -p ~/Dropbox/Github/uvmecon-ai/demo
cd ~/Dropbox/Github/uvmecon-ai/demo
```

Start Claude Code from this directory. It should have nothing in it except this prep file and the CLAUDE.md.

### 5. CLAUDE.md for the demo

Create this in the demo folder so the audience can see what a project file looks like. This is also a teaching moment.

```markdown
# Demo: Immigration and Wages (Decennial Census)

## What this project is
A demo of a research workflow for the UVM Economics AI Bootcamp.
Inspired by Borjas (2003, QJE) — skill-cell approach to immigration and wages.

## Rules
- Use R for data download (IPUMS USA API via ipumsr package)
- Use Stata for all analysis
- Save all intermediate outputs as files
- Write a short report at the end as a markdown file
- Use PERWT as person weight throughout
```

---

## Data: IPUMS USA Decennial Census, 1970–2020

**Why decennial census:** Six waves (1970, 1980, 1990, 2000, 2010, 2020) with nice gaps between them. Large samples. The Borjas (2003) paper uses 1960–2000. We extend to 2020.

**Note on 2010 and 2020:** The decennial census long form was replaced by the ACS starting in 2010. IPUMS USA includes ACS samples for these years. The 2010 and 2020 "census" data are actually ACS 5-year samples. Claude Code may or may not know this — a good moment to explain if it comes up.

**Variables to request from IPUMS USA:**

| Variable | Purpose |
|----------|---------|
| `YEAR` | Census year (1970, 1980, 1990, 2000, 2010, 2020) |
| `STATEFIP` | State identifier |
| `PERWT` | Person weight |
| `AGE` | For restricting to working age (25–64) and computing potential experience |
| `SEX` | Control variable |
| `BPL` | Birthplace — for classifying native vs. foreign-born |
| `EDUCD` | Education (detailed) — for constructing Borjas-style education groups |
| `INCWAGE` | Wage and salary income |
| `WKSWORK2` | Weeks worked last year (interval-coded) |
| `UHRSWORK` | Usual hours worked per week |

**Claude Code will likely propose its own variable list.** The point is for you to review and adjust. If it misses something (e.g., `WKSWORK2`), that's an intervention moment.

**Sample sizes will be large** (~1-5 million per decade for the 1% or 5% samples). If the download is too slow or the file too big, tell Claude Code to use the 1% sample for each year.

---

## The Borjas (2003) approach in brief

For context — you know this, but having it written down helps you narrate during the demo.

1. **Skill cells:** Divide workers into groups by education (4 groups: <HS, HS, some college, college+) and potential experience (8 five-year bins: 1–5, 6–10, ..., 36–40). That gives 32 cells per year.

2. **Immigrant share:** Within each cell-year, compute the fraction of the workforce that is foreign-born (weighted by PERWT).

3. **Mean log wage:** Within each cell-year, compute mean log weekly wage (weighted).

4. **Regression:** Regress mean log wage on immigrant share, with cell fixed effects and year fixed effects. The coefficient is the estimated wage effect of a change in immigrant supply within a skill group.

The punchline of Borjas (2003): a 10% increase in immigrant share in a skill cell reduces wages by 3–4%. Card and others dispute this, arguing that local labor markets adjust. The debate is the fun part — you don't need to resolve it.

---

## Prompt sequence (what you say to Claude Code)

This is the approximate script. You don't need to memorize it — the whole point is that it's conversational. But having the sequence in mind prevents dead air.

### Step 1: Download the data (~8 min including IPUMS processing)

> "I want to download decennial census data from IPUMS USA using the R package ipumsr. I need the 1% samples for 1970, 1980, 1990, 2000, 2010, and 2020. I need variables on birthplace, education, age, sex, wages, weeks worked, and usual hours. Write an R script that defines the extract, submits it to IPUMS, waits for it to be ready, downloads it, and saves it as a Stata .dta file. My IPUMS API key is in the environment variable IPUMS_API_KEY."

**What Claude Code should do:** Write an R script using `ipumsr::define_extract_usa()` with the right sample IDs and variable names, submit via `submit_extract()`, wait with `wait_for_extract()`, download with `download_extract()`, read with `read_ipums_micro()`, and save as `.dta` via `haven::write_dta()`.

**Where it might go wrong:**

- **Sample IDs:** IPUMS USA sample IDs are specific (e.g., `us1970a` for the 1970 1% Form 1 State sample). Claude may get these wrong or not know them. You may need to say: "Check what the correct IPUMS USA sample identifiers are for the 1% decennial samples."
- **2010 and 2020:** These are ACS, not census. Claude may not know this. If it tries to request a decennial sample for 2020 and it doesn't exist, you say: "2010 and 2020 don't have a long-form census. Use the ACS 5-year samples instead."
- **Extract processing time:** IPUMS extracts typically take 1–10 minutes. While it processes, show a slide about the Borjas paper or the workflow concept. This is built-in presentation time, not dead air.
- **Variable names:** IPUMS is picky. `INCWAGE` not `WAGE`, `EDUCD` not `EDUC_DETAILED`, etc. Claude may guess wrong.

**Intervention opportunities:**
- "It forgot to include UHRSWORK — I need that for hourly wages. Add it."
- "The 2020 sample ID looks wrong. Let's check."

### Step 2: Describe the data (~5 min)

> "Read the .dta file. Tell me how many observations per year, what variables we have, and flag anything that looks weird. Restrict to working-age adults 25–64 and drop anyone with zero or missing wages. Do this in Stata."

**What Claude Code should do:** Write a Stata do-file that loads the data, runs `tab year`, `describe`, `summarize`, applies sample restrictions, and saves the cleaned dataset.

**Where it might go wrong:**
- May try to do this in R. Redirect: "Use Stata for all analysis from here."
- May not handle IPUMS coding conventions. `INCWAGE` has top-coded values (999998, 999999) and a code for N/A (0). Claude may not know this. If it doesn't drop them, say: "INCWAGE values of 999998 and 999999 are top-coded. Drop them or cap them."
- May forget person weights. Prompt: "Use PERWT as the person weight."

### Step 3: Construct skill cells and immigrant shares (~8 min)

> "Now I want to replicate the Borjas (2003) skill-cell approach. Create four education groups: less than high school, high school, some college, and college plus. Create potential experience as age minus years of schooling minus 6, and bin it into 5-year groups from 1–5 through 36–40. Within each education-experience-year cell, compute the share of workers who are foreign-born, weighted by PERWT. Also compute the weighted mean log weekly wage in each cell. Save this as a cell-level dataset."

**What Claude Code should do:** Write Stata code to:
1. Recode `EDUCD` into 4 education groups
2. Map education groups to years of schooling (e.g., <HS = 10, HS = 12, some college = 14, college+ = 16)
3. Compute potential experience = age - years of schooling - 6
4. Create 5-year experience bins
5. Compute weekly wage = INCWAGE / (WKSWORK2 midpoints × 1) — or just annual wages divided by weeks
6. `collapse (mean) lnwage immig_share [pw=PERWT], by(educ_group exp_group year)`

**Where it might go wrong:**
- **WKSWORK2 is interval-coded**, not continuous. Values are 1–6 representing intervals (1–13, 14–26, 27–39, 40–47, 48–49, 50–52). Claude probably won't know this. This is a great intervention: "WKSWORK2 is interval-coded — you need to convert to midpoints first."
- **Education recoding from EDUCD** is nontrivial — EDUCD has dozens of values. Claude may get the cutpoints wrong. Review carefully.
- **Potential experience** can go negative for young, highly-educated people. Need to drop or floor at zero.
- **The foreign-born classification from BPL**: values ≥ 150 are foreign-born in IPUMS. Claude may not know the cutpoint. If it gets it wrong: "In IPUMS, BPL values of 150 and above indicate foreign-born."

**This step has the most intervention potential.** That's a feature — it shows the audience that domain knowledge matters.

### Step 4: The visuals (~8 min)

> "Make two graphs. First: plot the immigrant share over time, separately for each of the four education groups. Second: show how the total immigrant share has changed by state — pick the top 6 states by immigrant share in 2020 and plot their trends. Make both graphs clean: white background, labeled lines, y-axis as percentage."

**What Claude Code should do:** Two Stata graphs using `twoway line` or `twoway connected`, with appropriate labels and formatting.

**Where it might go wrong:**
- Stata graph defaults are ugly. You will almost certainly need to ask for formatting fixes.
- May try to plot all 50 states. "Just the top 6 by 2020 immigrant share."
- Line labels may overlap. "Add a legend instead of line labels."

**This is the visual payoff.** The trend graph showing immigrant shares rising in different education groups at different rates is the classic Borjas figure. It tells a story without a regression.

### Step 5: Regression (~5 min)

> "Run the Borjas-style regression: regress mean log weekly wage on immigrant share in the cell, with skill-cell fixed effects and year fixed effects. Weight by cell size. Show me the results and interpret the coefficient."

**What Claude Code should do:** A regression at the cell level. Something like:
```
reghdfe lnwage immig_share [aw=cell_n], absorb(cell_id year)
```
or the equivalent with `areg` or manual dummies.

**Where it might go wrong:**
- May run a micro-level regression instead of a cell-level one. Redirect: "This should be at the cell level — one observation per education-experience-year cell."
- May use the wrong weight. Cell-level regression should weight by cell size (number of workers in the cell).
- May interpret the coefficient causally. "That's a correlation within skill cells over time. It's not a causal estimate — what else is changing between 1970 and 2020 within these cells?"

### Step 6: Write a report (~3 min)

> "Write a one-page markdown report summarizing what we found. Include both graphs, the regression results in a table, and a paragraph explaining why this is descriptive, not causal — reference the Borjas vs. Card debate. Save it as report.md."

**What Claude Code should do:** Draft a short report with findings, embedded figures, formatted table, and limitations.

**Where it might go wrong:**
- May overclaim causality. "Fix the language — this is a replication exercise showing correlations, not a causal estimate."
- May hallucinate citations. "Check that citation — does that paper actually exist?"
- May write too much. "Shorter. One page."

---

## What to capture during the dry run

Save everything:

```
demo/
├── CLAUDE.md                    # Project instructions
├── download_census.R            # R script Claude wrote
├── census_1970_2020.dta         # Downloaded data
├── 01_describe.do               # Stata: data description
├── 02_skill_cells.do            # Stata: construct cells + immigrant shares
├── 03_graphs.do                 # Stata: trend graphs
├── 04_regression.do             # Stata: Borjas-style regression
├── immig_share_by_educ.png      # Graph: immigrant share by education group
├── immig_share_by_state.png     # Graph: top states over time
├── report.md                    # Final report
└── DRY_RUN_LOG.md               # ← You write this
```

**DRY_RUN_LOG.md** should capture:

- Each prompt you gave (copy-paste from the session)
- Where Claude Code got it right on the first try
- Where you had to intervene and what you said
- Any errors or weird behavior
- Total time from start to finish
- Total number of prompts

This log is your cheat sheet for the live demo AND the comparison artifact you show the audience.

---

## Live demo plan (April 27)

**Time budget:** ~35 minutes total

| Segment | Time | What happens |
|---------|------|-------------|
| Setup and context | 3 min | Show the empty folder, show CLAUDE.md, explain: "We're going to replicate the spirit of Borjas (2003) from scratch." |
| Download data | 8 min | Step 1. While IPUMS processes, show a slide about the paper and the skill-cell idea. |
| Describe + clean | 5 min | Step 2. Quick Stata summary. Flag the IPUMS coding issues. |
| Skill cells + shares | 8 min | Step 3. This is where domain knowledge matters most. |
| Graphs | 6 min | Step 4. The visual payoff — immigrant shares by education group across decades. |
| Regression + report | 3 min | Steps 5–6. Quick regression, quick report, open in Typora. |
| Comparison | 2 min | Show DRY_RUN_LOG.md. Where did the two runs differ? Where did you step in? |

**If something breaks live:** That's fine. It's the point. Say: "This is exactly what I mean — you have to check the work." Fix it and move on.

**If IPUMS is slow:** Have the dry-run `.dta` file as a backup. "The API is slow right now — let me use the version I downloaded yesterday." Continue from Step 2.

---

## Backup plan

If the IPUMS API is down or painfully slow during the live demo:

1. Start from the pre-downloaded `.dta` file from the dry run
2. Say: "I downloaded this yesterday using the same workflow. Let me show you the R script it wrote." Show the script briefly.
3. Continue from Step 2 (Stata analysis) live

The audience still sees the full workflow. They just don't wait for the download.

---

## Things that make this demo good for this audience

- **They know the Borjas paper** (or should). Instant credibility — you're not doing a toy example.
- **Decennial gaps are visually fun.** Six dots across 50 years, not a smooth line. Looks like real research.
- **The skill-cell construction requires domain knowledge.** Claude Code won't get WKSWORK2 interval coding or BPL cutpoints right on its own. You step in. This is the point.
- **R → Stata handoff is realistic.** This is how people actually work (download in one language, analyze in another).
- **The Borjas/Card debate is intellectually interesting.** You can end with: "This is descriptive. Whether this is causal is the whole debate. Borjas says yes, Card says no. The AI doesn't know the difference."

---

## Before the dry run: checklist

- [ ] Verify Borjas (2003) cite — "The Labor Demand Curve is Downward Sloping," QJE
- [ ] IPUMS API key is set as `IPUMS_API_KEY` environment variable
- [ ] R packages installed: `ipumsr`, `httr`, `jsonlite`, `tidyverse`, `haven`
- [ ] Stata is callable from the terminal (check `which stata-se`)
- [ ] Demo folder created and clean: `~/Dropbox/Github/uvmecon-ai/demo/`
- [ ] `CLAUDE.md` created in demo folder
- [ ] Typora or another Markdown viewer available to show the final report
- [ ] ~45 minutes of uninterrupted time for the dry run
- [ ] Do the dry run at least 3–4 days before April 27 so you have time to adjust
