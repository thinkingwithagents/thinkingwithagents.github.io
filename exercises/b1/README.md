# B1: Terminal Basics — Exercise Files

These files accompany [Module B1: Terminal Basics](../../modules/b1-terminal-basics.qmd).

## Contents

| File | Description |
|---|---|
| `household_survey.csv` | Simulated household survey data (75 observations, 8 variables). Includes realistic patterns, outliers, missing values, and a negative income value for students to discover. |
| `sample_dofile.do` | A simple Stata do-file for search exercises with `grep`. Loads and cleans the household survey data. |
| `scavenger_hunt.md` | Timed exercise (15 min) with 10 questions answered using terminal commands. Includes an answer key. |
| `windows_setup_guide.md` | Setup instructions for Windows students (Git Bash and WSL options). |

## How to Use

1. Download or clone this repository
2. Open your terminal and navigate to this folder (`exercises/b1/`)
3. Work through the scavenger hunt using only terminal commands
4. Windows users: follow `windows_setup_guide.md` first

## Data Description

The `household_survey.csv` contains simulated data from a household survey in Kenya with the following variables:

- `hhid` — Household ID (1001-1075)
- `district` — District name (Nairobi, Mombasa, Kisumu, Nakuru, Eldoret)
- `treatment` — Treatment assignment (0 or 1)
- `income` — Annual household income in KES (includes outliers and one negative value)
- `n_children` — Number of children (0-8)
- `female_head` — Female-headed household (0 or 1)
- `survey_round` — Survey round (1 or 2)
- `consumption` — Annual consumption in KES (some missing values, more in round 2)
