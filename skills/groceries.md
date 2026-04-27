# Groceries

*Generates a shopping list from Apple Notes, Apple Reminders, your staples template, and your current meal plan. Saves a clean list for mobile use.*

## File Paths

All files live under `~/Documents/MealPlan/`:

| File | Purpose |
|------|---------|
| `shopping-template.md` | Standing staples list organized by store and category |
| `patterns.md` | Household info, dietary restrictions (shared with `/meal-plan`) |
| `recipes.md` | Meals with ingredients, tagged by store (shared with `/meal-plan`) |
| `Meal Plan.md` | Active two-week plan (shared with `/meal-plan`) |
| `Shopping/[STORE].md` | Output: most recent grocery list per store |

## Arguments

- *(none)* — prompt for store selection
- `tj` or `trader joes` — Trader Joe's
- `costco` — Costco
- `target` — Target
- `general` or `all` — All items from all sources
- `setup` — re-run the setup interview

---

## Setup (First Run)

If `~/Documents/MealPlan/shopping-template.md` does not exist, enter setup mode. Walk the user through these questions conversationally.

### Step S1: Create folders

```bash
mkdir -p ~/Documents/MealPlan/Shopping
```

### Step S2: Stores

Ask:
> "What stores do you regularly grocery shop at? List them all — we'll set up categories for each one."

Collect store names and assign short codes (e.g., "Trader Joe's" → `TJ`, "Costco" → `Costco`).

### Step S3: Categories per store

For each store:
> "How do you organize your list at [Store]? Walk me through the sections you'd group items into — roughly in the order you'd walk through the store. For example: Produce, Dairy, Frozen, Pantry, Bread, Snacks."

Collect category names for each store. Different stores can have different categories.

### Step S4: Apple Reminders setup

Ask:
> "Do you use Apple Reminders to jot down things you need to buy? If so, what's the name of the list? (Some people use 'Shopping', 'Groceries', or have separate lists per store.)"

Collect:
- Whether they use Reminders (yes/no)
- List name(s) and which store each maps to

### Step S5: Apple Notes setup

Ask:
> "Do you keep a running shopping list in Apple Notes? If so, what's the note called? And how is it organized — do you use headers for each store, or is it just a flat list?"

Collect:
- Whether they use Notes (yes/no)
- Note name
- Organization method (store headers vs. flat)

### Step S6: Staple items

Ask:
> "Let's build your staples list — things you buy almost every trip. We'll go store by store and category by category. I'll ask about each category and you can list what usually goes in your cart."

For each store, for each category:
> "[Store] → [Category]: What staples do you usually buy here?"

### Step S7: Save config

Write `~/Documents/MealPlan/shopping-template.md`:

```markdown
# Shopping Template

## [Store 1]

### [Category 1]
- [ ] Staple item 1
- [ ] Staple item 2

### [Category 2]
- [ ] Staple item 3

## [Store 2]

### [Category 1]
- [ ] Staple item 4

## Sources

- **Apple Reminders**: [list name(s) and store mapping]
- **Apple Notes**: [note name and organization]
```

Confirm:
> "Setup complete! Your shopping template is saved to `~/Documents/MealPlan/shopping-template.md`. Run `/groceries` anytime — or `/groceries costco` to skip the store prompt."

**Stop here after setup.**

---

## Normal Operation

### Step 1: Determine store

If store not specified in argument, ask:

```
Which store are you heading to?
1. [Store 1]
2. [Store 2]
3. [Store 3]
4. All stores
```

Store the result as STORE.

---

### Step 2: Fetch Apple Reminders

Read the source config from `shopping-template.md` to get the Reminders list name(s).

Use osascript to pull incomplete reminders from the appropriate list:

```bash
osascript -e '
tell application "Reminders"
  set output to ""
  try
    set targetList to list "[LIST_NAME]"
    repeat with r in (reminders of targetList whose completed is false)
      set output to output & (name of r) & "\n"
    end repeat
  end try
  return output
end tell'
```

Run for each relevant list based on STORE.

If osascript fails or the list is not found, skip this source and note: "Reminders unavailable — if the list has many old completed reminders (1000+), osascript may time out. Fix: open Reminders → Edit → Show Completed → Edit → Delete All Completed."

---

### Step 3: Fetch Apple Notes content

Read the source config from `shopping-template.md` to get the note name.

```bash
osascript -e '
tell application "Notes"
  set targetNote to first note whose name is "[NOTE_NAME]"
  return body of targetNote
end tell'
```

The output is HTML. Strip all HTML tags to get plain text. If the note uses store headers, extract only the section matching STORE. If the note is a flat list or no matching header is found, include all content.

If the note is not found or osascript fails, skip and note "Notes unavailable — confirm '[NOTE_NAME]' note exists in iCloud Notes."

---

### Step 4: Read staples template

Read `~/Documents/MealPlan/shopping-template.md`.

Parse into sections by store. Include only the sections matching STORE (or all sections if STORE = all).

**Preserve category groupings:** The template uses section headers and blank lines to separate categories. Keep those intact in the output — they give visual separation in the store.

---

### Step 4b: Pull meal plan ingredients (if plan exists)

Check for an active meal plan at `~/Documents/MealPlan/Meal Plan.md`.

If it exists:
1. Identify **Week 1** (the current/upcoming week) from the plan
2. Extract all meal names from that week's dinner + weekend lunch slots
3. Skip any slot marked as "leftovers" — these don't need separate ingredients
4. Read `recipes.md` and look up each meal (case-insensitive match on `## Meal Name`)
5. Collect all ingredients tagged `[STORE]` where STORE matches the selected store
6. Items with no store tag go on all lists
7. If a meal is marked as "hosting" or scaled up in the plan, multiply ingredient quantities by the scale factor (guests ÷ normal serves, rounded up)
8. If a meal has a leftover pairing, scale ingredients to 2x normal serves (cook once, eat twice)

If the plan file or `recipes.md` is not found, skip this step silently.
If a meal name is not found in `recipes.md`, skip it silently.

---

### Step 5: Assemble and display the list

Merge ALL sources into a **single unified list** organized by the template's category sections.

**Merge rules:**
1. Use the template's category structure as the skeleton (e.g., ### Produce, ### Dairy, ### Frozen)
2. For each **meal ingredient** (Step 4b): place in the correct category. If an equivalent item is already in the template, it appears **once only** — add a brief meal annotation if helpful (e.g., `*(tacos Wed)*`). Use the larger quantity if both specify one. If the ingredient was scaled (hosting or leftover doubling), note the quantity.
3. For each **Notes/Reminders item** (Steps 2–3): place in the correct category. If it matches a template item, merge.
4. Items that don't fit any template category (non-food, personal care, misc) → brief **"On your list"** section at the top. Omit if empty.
5. Skip any item already checked (`- [x]`) in the template unless the meal plan needs it this week.
6. De-duplicate: same item from multiple sources = one entry.
7. If any household member has a dietary restriction that conflicts with a listed ingredient, add `⚠️` with a note (e.g., `⚠️ check GF version for [Name]`).

**Output format:**
```
# [Store Name] — [Month Day, Year]

## On your list
- [ ] Non-food / misc items

## [Category 1]
- [ ] Item *(for tacos Wed)*
- [ ] Item

## [Category 2]
- [ ] Item
...
```

- Omit "On your list" if empty
- Keep template category names exactly as written
- Meal annotations are brief and optional — only where helpful

After displaying, say:
> "Ready to copy. When you're back, say 'done shopping' and I can mark your Reminders as complete."

---

### Step 5b: Save to MealPlan Shopping folder

After displaying the list:

1. Write the full list to `~/Documents/MealPlan/Shopping/[STORE].md`
   - Use the short store code: `TJ.md`, `Costco.md`, `Target.md`, `General.md`
   - Overwrites the previous list for that store (no date accumulation)
2. Confirm: "Saved to `~/Documents/MealPlan/Shopping/[STORE].md`."

If the write fails, skip silently — the list was already displayed.

---

### Step 6: Clear Reminders after shopping (optional)

If the user says "done shopping" or similar, ask:

> "Mark all [list name] reminders as complete?"

If yes, run:

```bash
osascript -e '
tell application "Reminders"
  set targetList to list "[LIST_NAME]"
  repeat with r in (reminders of targetList whose completed is false)
    set completed of r to true
  end repeat
end tell'
```

Run for each relevant list. Confirm: "Reminders cleared."

---

## Error Handling

| Issue | Response |
|-------|----------|
| `shopping-template.md` not found | Enter setup mode |
| Reminders osascript fails | Skip source, note "Reminders unavailable" |
| Notes not found | Skip source, note "Check that '[NOTE_NAME]' note exists in iCloud Notes" |
| `recipes.md` or `Meal Plan.md` missing | Skip meal ingredients silently |
| Shopping folder write fails | Skip silently — list already displayed |
| All sources fail | Report failures; suggest checking System Settings → Privacy → Automation |
