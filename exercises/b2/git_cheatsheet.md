# Git Cheat Sheet for Economists

A one-page reference for the commands you will use most often.

---

## Setup (One-Time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@uvm.edu"
```

---

## Starting a Project

| What You Want | Command |
|---|---|
| Create a new repo from scratch | `git init` |
| Download an existing repo | `git clone <url>` |

---

## Daily Workflow

This is the sequence you will repeat constantly:

```
[edit files] → git status → git add <files> → git commit -m "message" → git push
```

| Command | What It Does |
|---|---|
| `git status` | Show what has changed since the last commit |
| `git add <file>` | Stage a file (mark it for the next commit) |
| `git add .` | Stage all changes (use cautiously — check status first) |
| `git commit -m "message"` | Save a snapshot with a descriptive message |
| `git push` | Upload your commits to GitHub |
| `git pull` | Download your collaborator's commits from GitHub |

---

## Inspecting History

| Command | What It Does |
|---|---|
| `git log --oneline` | Show commit history (compact) |
| `git log` | Show commit history (full detail) |
| `git diff` | Show unstaged changes (what you have edited but not yet added) |
| `git diff --staged` | Show staged changes (what will be in the next commit) |
| `git show <hash>` | Show what a specific commit changed |
| `git show <hash>:<file>` | Show a file as it existed at a specific commit |

---

## Undoing Things

| Situation | Command |
|---|---|
| Unstage a file (undo `git add`) | `git restore --staged <file>` |
| Discard uncommitted edits to a file | `git restore <file>` |
| Undo the last commit (keep changes staged) | `git reset --soft HEAD~1` |
| See what a file used to look like | `git show <hash>:<file>` |

---

## Key Concepts

**Repository (repo)**: A project folder tracked by Git.

**Commit**: A snapshot of your project at a point in time. Each commit has a unique hash (like `a3b8f2d`), a message, an author, and a timestamp.

**Staging area**: A holding zone between your working files and a commit. You choose which changes go into each commit.

**Remote**: A copy of your repo on GitHub (or another server). `push` sends your commits there; `pull` brings commits from there.

**HEAD**: A pointer to your most recent commit. `HEAD~1` means "one commit before the current one."

---

## When Things Go Wrong

**"I do not know what is going on"**
```bash
git status
```
Read the output carefully. Git usually tells you what to do next.

**"I committed a file I should not have (and have not pushed yet)"**
```bash
git reset --soft HEAD~1
git restore --staged <unwanted-file>
git commit -m "Same message as before"
```

**"I want to see what the file looked like before I changed it"**
```bash
git log --oneline <file>
git show <hash>:<file>
```

**"My collaborator and I edited the same file"**
Run `git pull`. If Git reports a merge conflict, open the file — Git marks the conflicting sections with `<<<<<<<`, `=======`, and `>>>>>>>`. Edit the file to keep what you want, then `git add` and `git commit`.

**"I accidentally ran git init in the wrong folder"**
```bash
rm -rf .git
```
This removes the Git repository (not your files). The folder becomes a regular folder again.

---

## Files to Ignore

Use a `.gitignore` file to tell Git which files to skip. Common entries for economics projects:

```
*.dta          # Stata data
*.csv          # CSV data
*.log          # Stata logs
.DS_Store      # macOS system file
```

See `econ_gitignore` in this folder for a complete template.
