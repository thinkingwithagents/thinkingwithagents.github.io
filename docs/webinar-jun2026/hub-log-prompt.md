# Prompt: Create & maintain your own project HUB + session log

> ⓘ Copy this into your agent (Claude Code, Claude, ChatGPT — anything that can read your
> project folder). It builds a **HUB** and a **session log** for *your* project, modeled on the
> webinar sample files, then keeps them current. Edit the bracketed bits first.

---

## Step 1 — Create the two files (run once)

```
You're helping me set up persistent context for a research project so that you (and future
sessions) can pick up where we left off without me re-explaining everything.

My project: [one or two sentences — what it is and the deliverable].
Project folder: [path, e.g. ~/Dropbox/GitHub/my-project/ — or describe where things live].

Please create two Markdown files in [folder]:

1. HUB.md — the standing state of the project. Include:
   - Status / stage / last-updated / owner
   - A "Where Everything Lives" table (data, code, draft, IRB, pre-registration — whatever applies)
   - Team & human dependencies (who's waiting on what, with dates)
   - Current state (done / in progress / blocked)
   - Next 3 steps, each concrete enough to act on
   - Key decisions & open questions
   - A status log table at the bottom

2. session-log.md — a running, newest-on-top history. For each work session, record:
   - Date and a one-line goal
   - What happened
   - Decisions made, each with the *why*
   - Files touched
   - A "Start here next time" handoff line

Before you write anything, look through my project folder and ask me up to 5 questions about
anything you can't infer (team, deadlines, where the data lives, open decisions). Then draft both
files and show them to me for edits.
```

## Step 2 — Keep them current (use at the end of each session)

```
Before we stop: update HUB.md and session-log.md to reflect today's work.
- Add a new session-log entry on top (goal, what happened, decisions + why, files touched,
  and a "Start here next time" line).
- Update the HUB's current-state, next-3-steps, open-questions, and status-log so they match reality.
Keep it concise — these are working notes, not a report.
```

## Step 3 — Start of a later session (rehydrate context)

```
Read HUB.md and session-log.md before we begin, then tell me in 3–4 bullets where the project
stands and what the "start here next time" note said. Then we'll pick the next step.
```

---

### Tips

- **Keep it short.** A HUB that's painful to maintain won't get maintained. Aim for a page.
- **Record the *why* behind decisions**, not just the decision — that's the part your future self forgets.
- **One source of truth.** The HUB holds *current* state; the log holds *history*. Don't duplicate.
- See the worked examples: **`sample-HUB.md`** and **`sample-session-log.md`**.
