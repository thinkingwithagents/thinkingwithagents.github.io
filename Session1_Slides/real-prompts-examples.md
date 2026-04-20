# Real Prompts: What Actual Usage Looks Like

These are real prompts Emily has used with Claude Code and Codex — messy, conversational, and effective. They show that **you don't need perfect prompts** to get useful results.

---

## Quick/Simple (< 2 sentences)

**Data orientation:**
> Read this dataset and describe the variables, sample size, missingness, and anything that looks unusual.

**Code generation:**
> Write a Stata do-file that cleans this dataset, labels the variables, and saves a clean version.

**Formatting:**
> Make this output readable in a Markdown viewer.

**Email:**
> Read this draft email and make it shorter, warmer, and more direct.

**Extraction:**
> Extract the deadlines from this document and put them in a table.

**Decision support:**
> Compare these two approaches and recommend the simpler one.

---

## Medium Complexity (A paragraph, clear steps)

**Data download + multi-step workflow:**
> I want to download decennial census data from IPUMS USA using the R package ipumsr. I need the 1% samples for 1970, 1980, 1990, 2000, 2010, and 2020. I need variables on birthplace, education, age, sex, wages, weeks worked, and usual hours. Write an R script that defines the extract, submits it to IPUMS, waits for it to be ready, downloads it, and saves it as a Stata .dta file. My IPUMS API key is in the environment variable IPUMS_API_KEY.

**Exploratory data analysis:**
> Read the .dta file. Tell me how many observations per year, what variables we have, and flag anything that looks weird. Restrict to working-age adults 25–64 and drop anyone with zero or missing wages. Do this in Stata.

**Econometric construction:**
> Now I want to replicate the Borjas (2003) skill-cell approach. Create four education groups: less than high school, high school, some college, and college plus. Create potential experience as age minus years of schooling minus 6, and bin it into 5-year groups from 1–5 through 36–40. Within each education-experience-year cell, compute the share of workers who are foreign-born, weighted by PERWT. Also compute the weighted mean log weekly wage in each cell. Save this as a cell-level dataset.

**Visualization:**
> Make two graphs. First: plot the immigrant share over time, separately for each of the four education groups. Second: show how the total immigrant share has changed by state — pick the top 6 states by immigrant share in 2020 and plot their trends. Make both graphs clean: white background, labeled lines, y-axis as percentage.

---

## Corrections Mid-Stream (Short, direct, factual)

> Check what the correct IPUMS USA sample identifiers are for the 1% decennial samples.

> INCWAGE values of 999998 and 999999 are top-coded. Drop them or cap them.

> In IPUMS, BPL values of 150 and above indicate foreign-born.

> This should be at the cell level — one observation per education-experience-year cell.

> 2010 and 2020 don't have a long-form census. Use the ACS 5-year samples instead.

> Fix the language — this is a replication exercise showing correlations, not a causal estimate.

---

## Follow-Up / Iteration

> Shorter. One page.

> Good structure. Now add: 1. Real-time email validation 2. Password strength indicator 3. Confirm password field with matching validation 4. Accessibility: ARIA labels, keyboard navigation

> Perfect. Final changes: 1. Use our design system components 2. Add loading state during submission 3. Show success message with 2-second auto-dismiss

---

## Complex / Multi-Step

**Grant review:**
> You are helping me review a grant proposal submitted to Project AI Evidence (PAIE), J-PAL's initiative to fund rigorous evidence on the causal impact of AI-based interventions on social outcomes. PAIE funds Full RCTs (up to $200,000) and Pilot Studies (up to $75,000). This is a competitive round with five submissions.

**Grading support:**
> Use local filesystem tools on the folder at `{{ROOT_PATH}}`. The folder may contain one subfolder per student, plus an `index.html` export. Review the annotated bibliographies conservatively and produce a grading-support memo focused on citation reality and evidence of actual engagement with the readings.

**Agentic (meta-prompting):**
> Before writing your score, spawn a research subagent. Search for 2–3 of the most-cited papers referenced in the proposal. For each paper found, summarize: (1) its main finding, and (2) how the proposed study builds on or departs from it.

---

## Key Takeaways

1. **Short often wins.** Half of these are <2 sentences.
2. **Domain knowledge matters.** You include the specific terminology — the AI fills in the code.
3. **Corrections are normal.** You catch mistakes and redirect in 1 sentence.
4. **Iteration is the workflow.** Start simple, refine in layers.
5. **Messy is fine.** No fancy framing needed — just say what you want.
