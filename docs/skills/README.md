# Shareable Skills: Meal Planning & Groceries

Two Claude Code skills that automate weekly meal planning and grocery list generation. Copy them into your setup, run the setup interview once, and they work from then on.

## What These Do

- **`/meal-plan`** — Generates a rolling two-week dinner plan using your day-of-week defaults and Google Calendar. Produces a printable HTML plan for the fridge.
- **`/groceries`** — Pulls items from Apple Reminders, Apple Notes, and your staples template, merges with meal plan ingredients, and outputs a categorized shopping list for the store you're heading to.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- macOS (Apple Notes and Reminders integration uses `osascript`)
- Google Calendar MCP server configured in Claude Code ([setup guide](https://docs.anthropic.com/en/docs/claude-code/mcp-servers))

## Installation

1. Copy both `.md` files into your Claude Code commands folder:

```bash
cp meal-plan.md ~/.claude/commands/meal-plan.md
cp groceries.md ~/.claude/commands/groceries.md
```

2. The first time you run either skill, it will walk you through a setup interview to learn your meals, stores, calendars, and preferences. Your answers are saved to `~/Documents/MealPlan/` so you only do this once.

## First Run

When you type `/meal-plan` for the first time, the skill will ask you:

- Which Google Calendar(s) to check for scheduling conflicts
- Who's in your household, dietary restrictions, and meal preferences
- Your default meals for each day of the week
- Any conditional rules (e.g., "if I'm out late, make it an easy night")
- Meals that make leftovers for the next day
- Fun/family names for meals (for the fridge printout)
- Recipes, ingredients, and serving sizes for each meal

When you type `/groceries` for the first time, it will ask:

- What stores you shop at
- How you organize items by category/aisle at each store
- Which Apple Reminders list holds your shopping items
- What your Apple Notes shopping note is called
- Staple items that should always appear on the list

## Files Created

After setup, your `~/Documents/MealPlan/` folder will contain:

```
~/Documents/MealPlan/
├── patterns.md           ← Household, day-of-week defaults, dietary restrictions, calendar IDs
├── recipes.md            ← Meals with ingredients tagged by store, serving sizes
├── shopping-template.md  ← Staples list organized by store and category
├── Meal Plan.md          ← Current two-week plan (created on first run)
└── Shopping/
    ├── TJ.md             ← Most recent grocery list by store
    ├── Costco.md
    └── ...
```

## Customizing Later

- Edit `patterns.md` to change your default meals, household members, dietary restrictions, or conditional rules
- Edit `recipes.md` to add new meals or update ingredients
- Edit `shopping-template.md` to change your staples or store categories
- Or just tell the skill what to change — it can update its own config files

## Adapting for Your Household

These skills were designed to be forked. The setup interview collects everything that's household-specific, so the skill files themselves don't need editing. But if you want to change the workflow itself (e.g., one-week plans instead of two, different output format, different data sources), edit the `.md` skill files directly.
