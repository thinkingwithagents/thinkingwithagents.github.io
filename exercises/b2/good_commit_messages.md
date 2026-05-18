# Writing Good Commit Messages

Your commit messages are a research log. Future you will read them when you are trying to remember why you changed something six months ago. Your co-authors will read them when they are trying to understand what you did. Journal referees may read them in your replication package.

Make them count.

---

## The Template

```
[Action verb] [what changed] [why, if not obvious]
```

Start with a verb. Be specific about what changed. Add context if someone reading just the message would not understand the purpose.

---

## Bad vs. Good Commit Messages

### Bad messages

| Message | Why It Is Bad |
|---|---|
| `update` | Update what? Which file? Why? |
| `changes` | This says nothing. |
| `fixed stuff` | What stuff? What was broken? |
| `final` | It is never final. |
| `final v2` | Proof that it was not final. |
| `asdfg` | You will regret this. |
| `WIP` | Acceptable as a temporary save, but clean it up before sharing. |

### Good messages

| Message | Why It Works |
|---|---|
| `Add income variable construction from raw survey data` | Clear action, specific variable, identifies the data source. |
| `Fix merge error: duplicate household IDs in round 2` | Identifies the bug (duplicates), the location (round 2), and the action (fix). |
| `Add district fixed effects to main regression specification` | Specific about which specification changed and what was added. |
| `Drop top 1% income outliers per referee suggestion` | Documents the change and the reason (referee request). |
| `Clean occupation codes: harmonize across 2015-2020 ACS waves` | Specific about what was cleaned and the scope. |
| `Add robustness table: results with and without state controls` | Clear about what was added and its purpose. |
| `Remove unused helper functions from 01_clean_data.do` | Specific about what was removed and where. |
| `Update README with data access instructions for replication` | Clear scope and purpose. |

---

## A Real-World Example

Imagine you are working on a project studying the effect of a job training program on earnings. Here is what a clean commit history might look like:

```
f3a21b8  Add heterogeneity analysis by gender and education level
c9e12d4  Fix top-coding of earnings at 99th percentile (was 95th)
a8b34c1  Add district fixed effects to main specification
7d2e9f0  Restrict sample to working-age adults (18-65)
5c1a8b3  Merge baseline and endline survey data on household ID
2e7d4a6  Clean income variable: convert to real KES using CPI
1a3b5c7  Import raw household survey data
```

Reading from bottom to top, you can reconstruct the entire analysis pipeline. Each commit is a meaningful, recoverable step. If the top-coding threshold needs to change again, you know exactly which commit to look at.

---

## Guidelines

1. **Start with a verb**: Add, Fix, Update, Remove, Refactor, Clean, Merge, Restrict, Drop
2. **Be specific**: "Fix bug" is useless. "Fix duplicate observations caused by m:m merge on hhid" is actionable.
3. **Keep the first line under 72 characters**: This is the summary that appears in `git log --oneline`.
4. **If you need more detail, add a body**: Leave a blank line after the summary, then write a longer explanation.

```bash
git commit -m "Restrict sample to working-age adults (18-65)

Previous analysis included all ages. Referee 2 noted that including
children and retirees biases the earnings estimates downward.
Affects Tables 2-4 and Figure 3."
```

5. **Commit one logical change at a time**: If you fixed a bug AND added a new table, make two commits. This makes your history readable and individual changes easy to undo.

---

## Quick Self-Test

Before you commit, ask yourself: "If I read this message in six months with no other context, would I understand what changed and why?"

If the answer is no, rewrite it.
