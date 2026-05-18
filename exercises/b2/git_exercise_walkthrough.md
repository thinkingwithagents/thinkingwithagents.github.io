# Git Exercise: Your First Repository

In this exercise, you will create your own Git repository from scratch, make commits, inspect history, and (optionally) push to GitHub. Every step includes the exact commands to type and what you should see.

**Prerequisites**: Git installed, terminal open, comfortable with `cd`, `ls`, `mkdir`.

---

## Part 1: Create and Initialize

### Step 1: Create a project folder

```bash
mkdir ~/my-econ-project
cd ~/my-econ-project
```

**What you should see**: No output (that is normal). Verify with:

```bash
pwd
```

```
/Users/yourname/my-econ-project
```

### Step 2: Initialize a Git repository

```bash
git init
```

**What you should see**:

```
Initialized empty Git repository in /Users/yourname/my-econ-project/.git/
```

This creates a hidden `.git/` folder that stores all version history. Your project folder looks the same, but Git is now watching it.

### Step 3: Check status

```bash
git status
```

**What you should see**:

```
On branch main
No commits yet
nothing to commit (create/copy files and use "git add" to track)
```

Git is ready and waiting. There are no files to track yet.

### Step 4: Create an analysis file

Open a text editor and create a file called `analysis.do` in the `my-econ-project` folder. Paste the following:

```stata
* ============================================
* Project: Practice Analysis
* Author: [Your Name]
* Date: [Today's Date]
* Purpose: Demonstrate version control workflow
* ============================================

clear all
set more off

* Load sample data
sysuse auto, clear

* Summary statistics
summarize price mpg weight
```

Save the file. (If you prefer R, create `analysis.R` with equivalent content.)

Alternatively, create it from the terminal:

```bash
cat > analysis.do << 'EOF'
* ============================================
* Project: Practice Analysis
* Author: Student
* Date: 2025-01-15
* Purpose: Demonstrate version control workflow
* ============================================

clear all
set more off

* Load sample data
sysuse auto, clear

* Summary statistics
summarize price mpg weight
EOF
```

### Step 5: Verify Git sees the new file

```bash
git status
```

**What you should see**:

```
On branch main
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        analysis.do

nothing added to commit but untracked files present (use "git add" to track)
```

Git sees the file but is not tracking it yet. It is "untracked."

---

## Part 2: First Commit

### Step 6: Stage the file

```bash
git add analysis.do
```

**What you should see**: No output (that is normal).

Check status again:

```bash
git status
```

**What you should see**:

```
On branch main
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   analysis.do
```

The file has moved from "untracked" to "staged" (ready to commit).

### Step 7: Commit with a descriptive message

```bash
git commit -m "Add initial analysis script with summary statistics"
```

**What you should see**:

```
[main (root-commit) 7a3b2c1] Add initial analysis script with summary statistics
 1 file changed, 14 insertions(+)
 create mode 100644 analysis.do
```

The exact hash (`7a3b2c1`) will be different for you. That is your commit's unique ID.

### Step 8: Verify

```bash
git status
```

**What you should see**:

```
On branch main
nothing to commit, working tree clean
```

Everything is saved. Your project has one snapshot.

```bash
git log --oneline
```

**What you should see**:

```
7a3b2c1 Add initial analysis script with summary statistics
```

---

## Part 3: Make Changes and Commit Again

### Step 9: Edit the file

Open `analysis.do` and add these lines at the bottom:

```stata

* Regression analysis
reg price mpg weight, robust
```

Save the file.

### Step 10: See the diff

```bash
git diff
```

**What you should see**:

```diff
diff --git a/analysis.do b/analysis.do
index 1234567..abcdefg 100644
--- a/analysis.do
+++ b/analysis.do
@@ -13,3 +13,6 @@

 * Summary statistics
 summarize price mpg weight
+
+* Regression analysis
+reg price mpg weight, robust
```

Lines with `+` are new additions. This is exactly what changed since your last commit.

### Step 11: Stage and commit

```bash
git add analysis.do
git commit -m "Add price regression on mpg and weight"
```

**What you should see**:

```
[main b4c5d6e] Add price regression on mpg and weight
 1 file changed, 3 insertions(+)
```

### Step 12: Check your history

```bash
git log --oneline
```

**What you should see**:

```
b4c5d6e Add price regression on mpg and weight
7a3b2c1 Add initial analysis script with summary statistics
```

You now have two snapshots. You can go back to either one at any time.

---

## Part 4: Time Travel

### Step 13: View the full log

```bash
git log
```

**What you should see** (something like):

```
commit b4c5d6e... (HEAD -> main)
Author: Your Name <your.email@uvm.edu>
Date:   Wed Jan 15 10:30:00 2025 -0500

    Add price regression on mpg and weight

commit 7a3b2c1...
Author: Your Name <your.email@uvm.edu>
Date:   Wed Jan 15 10:15:00 2025 -0500

    Add initial analysis script with summary statistics
```

### Step 14: View a file at a previous commit

Copy the hash of your first commit (the shorter version from `git log --oneline`), then:

```bash
git show 7a3b2c1:analysis.do
```

**What you should see**: The file as it existed at that commit (without the regression lines). Your current file is unchanged.

### Step 15: Compare two commits

```bash
git diff 7a3b2c1 b4c5d6e
```

This shows everything that changed between the two commits. Use your actual hashes.

---

## Part 5: Push to GitHub (Optional)

This part requires a GitHub account. If you do not have one, skip this section — everything you have done so far is tracked locally.

### Step 16: Create a repository on GitHub

1. Go to <https://github.com/new>
2. Name the repository `my-econ-project`
3. Leave it **empty** (do NOT add a README, .gitignore, or license)
4. Click **Create repository**

GitHub will show you a set of commands. Use the ones under **"push an existing repository from the command line"**.

### Step 17: Connect your local repo to GitHub

```bash
git remote add origin https://github.com/YOUR-USERNAME/my-econ-project.git
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### Step 18: Push your commits

```bash
git push -u origin main
```

**What you should see**:

```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 612 bytes | 612.00 KiB/s, done.
Total 6 (delta 1), reused 0 (delta 0)
To https://github.com/YOUR-USERNAME/my-econ-project.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

Your code is now on GitHub. Visit `https://github.com/YOUR-USERNAME/my-econ-project` to see it.

---

## What You Just Did

1. Created a project folder and initialized Git (`git init`)
2. Created a file and made your first commit (`git add` + `git commit`)
3. Made changes, viewed the diff, and committed again
4. Inspected your history and viewed files at previous commits
5. (Optionally) Connected to GitHub and pushed your history online

This is the core Git workflow. Everything else — branches, pull requests, merge conflicts — builds on these exact steps.

---

## Common Issues

**"fatal: not a git repository"**
You are not inside a folder that has been initialized with `git init`. Use `cd` to navigate to the right folder and try again.

**"nothing to commit, working tree clean"**
You have not made any changes since the last commit, or you forgot to save the file.

**"Please tell me who you are"**
You need to configure Git with your name and email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@uvm.edu"
```

**Authentication failed when pushing**
You may need to set up a personal access token or SSH key. See GitHub's documentation: <https://docs.github.com/en/authentication>
