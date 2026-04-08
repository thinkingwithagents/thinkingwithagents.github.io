---
type: review/plan
project: uvmecon-ai
status: to-process
date: 2026-04-08
---

# uvmecon-ai: Review and Revision Plan

Two weeks before Session 1 (April 22). The infrastructure is solid. The content needs a voice pass and an audience pass.

---

## Part 1: Review

### What's working

**Infrastructure is clean.** Quarto site + reveal.js slides + GitHub Actions deployment + PDF export via Chrome headless. The render script with four modes (`site`, `slides-html`, `slides-pdf`, `all`) is well-designed. AGENTS.md gives Erkmen (or Codex) a clear working surface. The split between website pages and slide decks is sensible.

**The prep guide is genuinely useful.** The chat-vs-agentic framing is the right distinction for this audience, and the cost summary table is exactly what faculty will want to reference later. The installation steps are clear and correct.

**The session structure is reasonable for a lunch format.** Watch-along is the right call — nobody wants to debug Node.js installs over sandwiches.

---

### Problem 1: The content sounds like AI wrote it

This is the biggest issue. The slides and pages are well-organized but tonally flat. They read like product documentation: every sentence does the same amount of work, the structure is too symmetrical, and the voice is helpful-informative rather than human.

**Specific markers:**

- **Generic framing.** "This is a good AI task because slide drafting is repetitive but still judgment-heavy." That's true but it sounds like a feature description, not something you'd say at lunch.
- **Over-parallel structure.** Every list has 4-5 items of equal weight and similar syntax. Real talks have emphasis — one point matters more, and you say so.
- **Missing your actual experience.** You and Erkmen started using these tools in December/January. The slides mention this once ("we started using these tools in December and January") but never get specific. What did you actually use them for? What surprised you? What went wrong?
- **No dry humor.** Your voice guide says humor should "feel accidental, not crafted." These slides have zero humor. A lunch talk among colleagues should have at least a few honest moments — the time the AI confidently cited a paper that doesn't exist, the time it wrote beautiful Stata code that couldn't run.
- **"We" is doing too much work.** Half the slides use an institutional "we" that sounds like a training manual. In a talk to 15-20 colleagues, you're Emily. Talk like Emily.

**What "your voice" sounds like in these slides vs. what it should sound like:**

Current: "The most useful teaching tasks are usually drafting and revision tasks."
Emily: "The place I've gotten the most out of this for teaching is first drafts — assignment prompts, rubrics, study guides. Things where the hard part is getting something on the page, not getting it right."

Current: "AI makes confident-sounding mistakes. Always review output, especially numbers and citations."
Emily: "It will confidently cite a paper that does not exist. Check everything. I am not exaggerating."

---

### Problem 2: The audience model is too generic

The slides treat the audience as "faculty who haven't tried AI tools." But these are UVM economics faculty — a specific group with specific concerns, work patterns, and skepticism.

**What this audience is actually thinking:**

- "Is this going to make my students cheat more?"
- "I already use ChatGPT sometimes. Why should I bother with a terminal?"
- "I don't have time to learn a new tool. Show me something I could actually use this week."
- "Is this a fad? I've seen a lot of 'transformative' ed-tech."
- "Who's paying for this? Am I supposed to spend $20/month on this?"

**What's missing:**

- **Student AI use.** The elephant in the room. Faculty are already dealing with students using ChatGPT on assignments. The slides never acknowledge this directly. You don't need a policy lecture, but you do need a slide that says: "You're already on the other side of this. Students are using it. Understanding what these tools can and can't do makes your policies better."
- **Economics-specific examples.** The slides describe generic tasks (draft an assignment, build a rubric, explore data). These could be for any department. Use your actual field. Show it working on a Stata do-file, or cleaning CPS data, or drafting a referee report outline, or extracting results from a regression table.
- **Honest cost-benefit.** Faculty are busy. The real pitch isn't "AI is amazing." It's: "Here are the three things where AI saves me actual time, and here are the things where it's not worth the trouble." Be specific about both sides.
- **The "it's wrong" problem.** The current treatment of AI errors is a single bullet: "AI makes confident-sounding mistakes." This audience is trained to be skeptical of claims without evidence. Show them a real failure. The hallucinated citation, the wrong regression specification, the Stata code that uses a function that doesn't exist.

---

### Problem 3: The presentation style is too conference-y

The current setup — multiple reveal.js themes, a breadcrumb navigation widget, CSS badge classes, the four demo templates on the homepage — reads like a tech workshop, not an econ seminar. This audience lives in Beamer. They don't need (or want) slide transitions, section progress dots, or theme showcases.

**Specific issues:**

- **Four demo themes on the homepage.** Why? These are for the presenters to choose a theme, not for the audience. Remove them from the public-facing page.
- **The breadcrumb widget.** It's well-built but it's a distraction. Faculty seminars don't have progress bars. The slide count (`c/t`) is sufficient.
- **Slide titles are too generic.** "Overview," "Tools," "Context," "Safety" — these are section labels, not slide titles. In a seminar, each slide has a takeaway as its title: "The useful distinction is chat vs. file access" or "The context window is why long conversations go sideways."
- **Too many slides per section.** The intro deck alone has ~25+ slides. For a 20-minute joint intro, that's too many. Some slides have 2-3 bullets and could be combined. Others (like the full vocabulary table) should be on the website, not in the talk.
- **The Mermaid diagram.** `Plan → Execute → Review → Clear → Continue` is a fine concept but the rendered Mermaid flowchart looks like a software architecture slide, not something you'd show econ faculty over lunch.

**What seminar-style means here:**

- White or very light background, dark text, no decorations
- One idea per slide, maybe two
- Slide titles that state the point, not the topic
- Tables only when they're doing real work
- No progress widgets, no section navigation
- Simple transitions (none is fine)
- Looks like it was made by someone who had something to say, not someone demonstrating Quarto features

---

### Problem 4: The module/exercise infrastructure is premature

The `modules/`, `lesson_plans/`, and `exercises/` directories are fully templated but completely empty. The CSS has badge classes (time estimates, track levels, difficulty ratings) for a module system that doesn't exist yet. This is scaffolding for a course, but right now you're giving two lunch talks.

**Recommendation:** Don't delete it, but don't link to it from the public site. Move it to a `_future/` directory or just leave it unlinked. The homepage and session pages should only point to things that exist.

---

### Problem 5: Session 2 is overloaded

Session 2 tries to cover four topics in 90 minutes (with lunch): slide creation, teaching applications, a research data pipeline, and Erkmen's web scraping + automated grading demos. That's ambitious even without the watch-along format, where AI processing creates natural pauses.

The research pipeline demo also doesn't have a dataset yet ("TBD — needs to be small, public, relatable"). Two weeks out, this needs to be locked down.

---

### Build system and logging

The build system is in good shape. `render.sh` is clean and correct. The GitHub Actions workflow deploys correctly. One minor issue: `docs/` is in `.gitignore` but GitHub Actions rebuilds from source — this is fine as long as the workflow runs cleanly, but it means you can't preview deployed output locally from a fresh clone without rendering. Not a problem in practice.

There's no changelog or session log, but for a two-session bootcamp this is fine. The git history is the log.

---

## Part 2: Revision Plan

### Priority order

The sessions are April 22 and 27. Erkmen owns his own slides. The plan below covers what *you* can do.

---

### 1. Voice pass on all Emily-authored content

**Scope:** `s1-intro.qmd`, `s1-emily.qmd`, `s2-part1.qmd`, `session1.qmd`, `session2.qmd`, `prep.qmd`, `index.qmd`, `resources.qmd`

**What this means concretely:**

- Read each file aloud (or imagine presenting it). Does it sound like something you'd say at lunch, or something you'd read off a slide? Rewrite the latter.
- Replace generic framing with specific examples from your own experience. "I used Claude Code to extract all the due dates from my syllabus and turn them into a CSV. It took about two minutes. I would have spent twenty."
- Add 2-3 honest failure stories. The hallucinated citation. The beautiful code that didn't run. The time it rewrote something you didn't ask it to change. These are the moments that build credibility with a skeptical audience.
- Cut the institutional "we" where you mean "I." Keep "we" for things you and Erkmen did together.
- Let some slides breathe. Not every bullet needs a parallel structure. Sometimes the point is: "This is the part that matters. The rest is nice but optional."

**Constraint:** Don't rewrite Erkmen's template slides. Add a note for him about tone if you want, but those are his.

---

### 2. Audience reframe: address faculty concerns directly

**Add to Session 1 (s1-intro.qmd or session1.qmd):**

- A slide on student AI use. Frame: "Your students are already using this. Understanding what these tools can and can't do makes your assessment design better. This bootcamp is also about that." 1-2 slides max.
- A slide on honest cost-benefit. "Three things I actually use this for every week: [specific]. Two things I tried that weren't worth it: [specific]."

**Revise the "AI Ladder":** It's a fine concept but feels imposed. Either make it yours (retitle, reframe around what you've observed in your own trajectory) or cut it. "Where are you today?" is a good question. The numbered framework from someone else's substack is less compelling.

**Add economics specificity to Session 2:**

- Pick a real (or realistic) dataset for the research demo. Public-use CPS, FRED macro series, or something from one of your courses. Lock this down now.
- Show the research demo with Stata specifically, since that's what this department uses. The demo script in the comments already suggests this — commit to it.
- For the teaching examples, use an actual econ assignment, not a generic one. "Draft an assignment for an intermediate micro class on price discrimination" is better than "draft an assignment."

---

### 3. Simplify the presentation style

**Slide theme:**

- Standardize on the `simple` theme (white background, dark text, no decorations). This is the Beamer-adjacent look your audience expects.
- Remove the `section-breadcrumb.html` include. Slide numbers (`c/t`) are sufficient.
- Remove the four demo theme links from the homepage. They're presenter tools, not audience content. Keep the demo files in the repo if you want them for reference, but don't feature them.

**Slide structure:**

- Use takeaway titles instead of topic labels. "The useful distinction is chat vs. file access" instead of "Conversational AI vs Agentic AI."
- Cut the full vocabulary table from the slides. Put it on the website (maybe on the prep page). In the talk, define terms as you use them.
- Combine thin slides. If a slide has 2-3 bullets and no image, it probably belongs with the slide before or after it.
- Replace the Mermaid diagram with a plain text sequence or just say it: "Plan, execute, review, clear, repeat."

**Homepage cleanup:**

- Remove the demo theme showcase section.
- Keep: schedule, session materials links, "before you arrive," and the prep/resources links.
- The subtitle "Let's become AI masters" is a little much. Something like "AI tools for teaching and research" or just drop the subtitle.

---

### 4. Tighten Session 2 scope

**Option A (recommended):** Cut the slide-creation section from Session 2. It's the weakest of the four topics and the hardest to demo well. Replace its time with a longer, more careful research demo and a proper Q&A buffer. Session 2 becomes: recap (10 min), research pipeline (35 min), Erkmen (35 min), wrap-up (10 min).

**Option B:** Keep all four but shrink each. Risk: everything feels rushed and nothing lands.

**Lock down the demo dataset** this week. If you want Stata, you need a dataset that works with Stata and that you've actually run through the demo script at least once.

---

### 5. Prep guide and resources: minor polish

These are already the strongest pages. A few tweaks:

- **Prep guide:** Add a "What to expect at the bootcamp" mini-section at the top, since this is where you'll send people beforehand. One paragraph: what it is, what it isn't, what to bring (laptop optional, curiosity required).
- **Resources:** The Paul Goldsmith-Pinkham link has a long tracking URL. Clean it up. Consider adding one or two economics-specific resources if they exist (e.g., an econ-focused AI use case write-up).
- **Both:** Light voice pass — the prep guide especially reads like product docs in places.

---

### 6. Erkmen coordination

Things Erkmen needs from you (or needs to know):

- His two slide decks are still templates. Confirm his timeline for filling them in.
- Share the tone guidance: "Think lunch talk, not conference. Specific examples from your own work. Be honest about what didn't work."
- Agree on the demo theme: if you switch to `simple`, his slides should match.
- For Session 2 grading demo: agree on whether he's using a real rubric from one of your courses or building one from scratch. Real is better.

---

### 7. Things to leave alone

- The build system. It works. Don't touch it.
- The module/lesson/exercise templates. They're fine sitting there for future use. Just don't link to them.
- AGENTS.md. It's accurate and useful.
- The GitHub Actions workflow. It's correct.

---

## Summary: what "as good as possible" means here

It means the slides sound like Emily and Erkmen talking to their colleagues over lunch — specific, honest, a little wry, grounded in real experience. It means the audience sees economics faculty using these tools on economics problems, not a product demo. And it means the visual design gets out of the way so the content does the work.

The infrastructure is already there. The revision is mostly voice, audience, and simplification.

---

## Suggested execution order

| Step | Scope | Time estimate |
|------|-------|------|
| 1 | Lock down Session 2 demo dataset | Now |
| 2 | Slide theme + homepage cleanup | ~1 hour |
| 3 | Voice pass: s1-intro.qmd | ~1–2 hours |
| 4 | Voice pass: s1-emily.qmd | ~30 min |
| 5 | Voice pass: s2-part1.qmd | ~1–2 hours |
| 6 | Session pages (session1, session2) | ~30 min |
| 7 | Prep guide + resources polish | ~30 min |
| 8 | Erkmen check-in | Async |
| 9 | Full dry-run render + link check | ~15 min |
