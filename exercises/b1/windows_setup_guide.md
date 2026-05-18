# Windows Terminal Setup Guide

This guide helps Windows users get a Unix-like terminal environment so they can follow along with the Terminal Basics module. Mac users can skip this entirely.

---

## Option A: Git Bash (Recommended for This Course)

Git Bash comes bundled with Git for Windows. It gives you a terminal that understands the same commands as Mac/Linux (`ls`, `cd`, `grep`, etc.).

### Installation

1. Download Git for Windows: <https://gitforwindows.org/>
2. Run the installer
3. Accept all default settings (just keep clicking "Next")
   - When asked about the default editor, **Notepad** or **Visual Studio Code** are fine
   - When asked about PATH, choose **"Git from the command line and also from 3rd-party software"** (the default)
4. Click **Install**, then **Finish**

### Opening Git Bash

- **From Start Menu**: Search for "Git Bash" and click it
- **From any folder**: Right-click in File Explorer and select **"Git Bash Here"** (opens the terminal in that folder)

### What you get

Git Bash provides all the commands used in this course: `pwd`, `ls`, `cd`, `cat`, `head`, `tail`, `grep`, `wc`, `sort`, `cut`, `mkdir`, `cp`, `mv`, `rm`, and pipes (`|`, `>`, `>>`). It also includes `git`, which you will need for Module B2.

---

## Option B: WSL (Windows Subsystem for Linux)

WSL runs a full Linux environment inside Windows. It is more powerful but requires more setup. Choose this if you plan to do serious computational work beyond this course.

### Installation

1. Open **PowerShell as Administrator** (right-click Start, select "Windows PowerShell (Admin)")
2. Run:
   ```
   wsl --install
   ```
3. Restart your computer when prompted
4. After restart, a terminal window will open asking you to create a Linux username and password
5. Choose something simple (this is separate from your Windows login)

### Opening WSL

- **From Start Menu**: Search for "Ubuntu" (or whichever Linux distribution was installed)
- **From PowerShell or Command Prompt**: Type `wsl` and press Enter

### When to choose WSL over Git Bash

- You plan to use Python, R, or other tools extensively from the command line
- You want to run Linux-based software
- You are taking additional computational courses

For this course alone, Git Bash is sufficient and simpler.

---

## Key Differences from Mac

| Topic | Mac Terminal | Git Bash (Windows) | WSL (Windows) |
|---|---|---|---|
| Home directory (`~`) | `/Users/yourname` | `/c/Users/yourname` | `/home/yourname` |
| Access Windows files | N/A | `/c/Users/yourname/Documents/` | `/mnt/c/Users/yourname/Documents/` |
| File paths | Forward slashes `/` | Forward slashes `/` | Forward slashes `/` |
| Line endings | LF | May see CRLF issues with Git | LF |

The important thing: all the **commands** (`ls`, `cd`, `grep`, etc.) work the same way. The only difference is how file paths map to your Windows folders.

---

## Test Your Setup

Open your terminal (Git Bash or WSL) and run these three commands:

```bash
pwd
```
You should see a path like `/c/Users/yourname` (Git Bash) or `/home/yourname` (WSL).

```bash
ls
```
You should see a list of files and folders.

```bash
echo "hello"
```
You should see the word `hello` printed back.

If all three commands work, you are ready to go.

---

## Troubleshooting

**"git" is not recognized / command not found**
- Git Bash: Reinstall Git for Windows, making sure to select the PATH option during installation
- WSL: Run `sudo apt update && sudo apt install git`

**I see weird characters or garbled text**
- Make sure your terminal is set to UTF-8 encoding (Git Bash does this by default)

**I cannot find my files**
- In Git Bash, your Windows Desktop is at `/c/Users/yourname/Desktop`
- In WSL, your Windows Desktop is at `/mnt/c/Users/yourname/Desktop`
- Use `ls` to explore and `cd` to navigate to your files

**I am stuck / the terminal is not responding**
- Press `Ctrl + C` to cancel the current command
- Press `q` if you are in a pager (like `less` or `man`)
- Close and reopen the terminal if nothing else works
