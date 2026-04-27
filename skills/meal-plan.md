# Meal Plan

*Creates or reviews a rolling two-week meal plan using your day-of-week defaults and Google Calendar. Outputs a printable HTML plan.*

## File Paths

All files live under `~/Documents/MealPlan/`:

| File | Purpose |
|------|---------|
| `patterns.md` | Day-of-week defaults, conditional rules, calendar IDs |
| `recipes.md` | Meals with ingredients, tagged by store |
| `Meal Plan.md` | Active two-week plan (created/updated by this skill) |

## Arguments

- *(none)* — auto-detect: run setup if no config exists, otherwise review or create
- `new` — force create a fresh plan (overwrites existing)
- `review` — review and update the existing plan
- `setup` — re-run the setup interview

---

## Setup (First Run)

If `~/Documents/MealPlan/patterns.md` does not exist, enter setup mode. Walk the user through these questions conversationally — one topic at a time, not a wall of questions.

### Step S1: Create the folder

```bash
mkdir -p ~/Documents/MealPlan/Shopping
```

### Step S2: Calendars

Ask:
> "Which Google Calendar(s) should I check for scheduling conflicts when planning meals? I need the email address associated with each calendar. Most people have at least their own — some households check a partner's or family calendar too."

Collect 1+ calendar email addresses.

### Step S3: Day-of-week defaults

Walk through each day of the week:
> "Let's set up your default meals. These are your go-to dinners for each night — the ones you'd fall back on if you didn't plan anything special. We'll go day by day."

For each day (Monday through Sunday), ask:
> "[Day]: What's the default dinner? (Or 'flexible' if no default.)"

Collect the meal name for each day. Note which days are flexible.

### Step S4: Conditional rules

Ask:
> "Are there any nights where the meal changes based on who's home or what's happening? For example: 'If [person] is out, we do [easy meal]' or 'Fridays someone else cooks.'"

Collect any conditional rules. These are optional.

### Step S5: Household members and preferences

Ask:
> "Who's in the household? I'll use this to track preferences and flag conflicts. Just first names is fine."

Then:
> "Does anyone have dietary restrictions or allergies I should know about? (e.g., vegetarian, gluten-free, nut allergy, dairy-free)"

Then:
> "Are there any meals that specific people won't eat? For example: '[Name] hates tacos' or '[Name] won't eat fish.' I'll flag these on the plan so you can prep an alternative."

Collect:
- Household member names
- Dietary restrictions/allergies (if any)
- Per-person meal dislikes (if any)

### Step S6: Leftovers and cook-once-eat-twice

Ask:
> "Do any of your meals intentionally make enough for leftovers the next day? For example, 'Sunday stir fry → Monday lunch leftovers.' I'll pair these on the plan and scale ingredients."

Collect leftover pairings. These are optional.

### Step S7: Meal display names

Ask:
> "Do you have fun or family names for any of these meals? These show up on the printed plan that goes on the fridge. For example, 'Taco Tuesday' instead of just 'Tacos'. If you just want the plain name, that's fine too."

Collect display names. Default to the plain meal name if none provided.

### Step S8: Weekend lunches

Ask:
> "Do you plan weekend lunches, or just dinners? If you plan lunches, what are the usual options?"

### Step S9: Recipes and ingredients

For each unique meal collected above:
> "Let's capture ingredients for [Meal Name]. List what you need to buy — skip pantry staples you always have on hand. For each item, note which store you'd buy it at (e.g., TJ, Costco, Target) if you have a preference."

Also ask:
> "How many people does this recipe normally serve? (I'll use this to scale up if you're hosting.)"

Format each meal as:

```markdown
## Meal Name
Serves: [number]

- Ingredient 1 [Store]
- Ingredient 2 [Store]
- Ingredient 3
```

Items without a store tag will appear on all store lists.

### Step S10: Save config files

Write `~/Documents/MealPlan/patterns.md`:

```markdown
# Meal Patterns

## Calendars
- primary: [email1]
- [label]: [email2]

## Household

| Name | Restrictions | Won't Eat |
|------|-------------|-----------|
| [name] | [restrictions or none] | [meal dislikes or none] |

## Day-of-Week Defaults

| Day | Default | Display Name |
|-----|---------|--------------|
| Monday | [meal] | [display name] |
| Tuesday | [meal] | [display name] |
| Wednesday | [meal] | [display name] |
| Thursday | [meal] | [display name] |
| Friday | [meal] | [display name] |
| Saturday | [meal or flexible] | [display name] |
| Sunday | [meal or flexible] | [display name] |

## Weekend Lunches
[yes/no, with options if yes]

## Leftovers
- [meal] → [next-day meal] (e.g., "Sunday Stir Fry → Monday lunch leftovers")

## Conditional Rules
- [rule 1]
- [rule 2]

## Notes
- [any additional dietary notes, always-stocked items, or other context]
```

Write `~/Documents/MealPlan/recipes.md` with all the meal/ingredient entries from Step S7.

Confirm:
> "Setup complete! Your config is saved to `~/Documents/MealPlan/`. Run `/meal-plan` anytime to generate a plan. You can edit `patterns.md` or `recipes.md` directly if anything changes."

**Stop here after setup.** Do not automatically generate a plan — let the user invoke `/meal-plan` when they're ready.

---

## Normal Operation

### Step 1: Load context (run in parallel)

Read all config files simultaneously:
1. `patterns.md` — extract day defaults, conditional rules, calendar IDs, household preferences, leftover pairings
2. `recipes.md` — extract meal names and ingredients
3. `Meal Plan.md` — read if it exists (to detect mode)

---

### Step 2: Check calendars

Using the Google Calendar MCP, check all configured calendars for the two-week planning window.

Look for events that affect dinner planning:
- Late meetings or evening commitments → flag that night as "simplify"
- Someone is out for the evening → check conditional rules
- Both adults out → check conditional rules
- Travel, school events, or other disruptions → flag for user to decide

Summarize flags before presenting the plan:
```
Calendar flags:
- Tue May 6: [Person] has 6pm meeting → suggest easy meal
- Thu May 8: [Person] out → [conditional meal]
- Fri May 9: [Flag or question]
```

---

### Step 3: Detect mode

- If `Meal Plan.md` **does not exist** → mode = **CREATE**
- If file exists and today is **Thursday or Friday** → mode = **REVIEW**
- If file exists otherwise → ask: "Review current plan or start fresh?"
- If `new` argument → mode = **CREATE**
- If `review` argument → mode = **REVIEW**

---

### Step 4A: CREATE mode — generate the plan

Apply day-of-week defaults from `patterns.md` as the starting point.

Then apply calendar flags:
- Override any defaulted night if a flag applies
- Move bumped meals to another night in the same week
- Flag any nights that need user input

Then apply household preferences:
- If a meal conflicts with someone's dietary restriction → flag with `⚠️ [Name]: [restriction]`
- If a meal is on someone's "won't eat" list → note `[Name] needs alt`
- If a meal has a leftover pairing → place the leftover in the next day's lunch slot automatically

Then check for guest/scaling:
- If a calendar event looks like hosting (e.g., "dinner party", "guests over") → flag: "Looks like you're hosting [day]. Scale up, or different meal?"

Present the draft plan:
```
Here's a suggested two-week plan:

** Calendar flags: [list any flags] **

Week 1: [dates]
  Mon: [meal]
  Tue: [meal]  [Ollie needs alt]
  Wed: [meal]
  Thu: [meal]  → Fri lunch: leftovers
  Fri: [meal or question] | Lunch: [Thu leftovers]
  Sat: [meal] | Lunch: [?]  ⚠️ hosting — scale up?
  Sun: [meal] | Lunch: [?]

Week 2: [dates]
  ...

Any changes?
```

---

### Step 4B: REVIEW mode — update existing plan

Read the current plan. Identify:
- Unfilled slots
- Which week is now "current" vs "upcoming"
- What new week needs to be planned

Present current state, flag gaps, suggest new week using same defaults + calendar check.

After confirming, roll Week 2 → Week 1 and add the new Week 2.

---

### Step 5: Confirm and save

After user confirms the plan:

1. Save to `~/Documents/MealPlan/Meal Plan.md` in the two-week table format
2. Note any "buy this weekend" items (e.g., proteins that need advance purchase)

---

### Step 6: Generate HTML meal plan

After saving, generate a printable HTML file at:
`~/Documents/MealPlan/meal-plan-current.html`

**Design principles:**
- Clean, attractive, family-friendly — goes on the fridge
- **One week per printed page** — Week 1 on page 1, Week 2 on page 2
- Large font — readable at a glance
- Color-coded by meal type — cheerful, not garish
- **Meal display name only** — no ingredient notes, no planning flags
- Portrait orientation, standard letter size

**HTML structure:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Meal Plan</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: Georgia, 'Times New Roman', serif;
      font-size: 20px;
      color: #2c2c2c;
      padding: 32px 40px;
      max-width: 680px;
      margin: 0 auto;
    }
    h1 {
      font-size: 26px;
      font-weight: normal;
      letter-spacing: 0.03em;
      border-bottom: 2px solid #2c2c2c;
      padding-bottom: 8px;
      margin-bottom: 4px;
    }
    .subtitle {
      font-size: 13px;
      color: #888;
      margin-bottom: 24px;
      font-style: italic;
    }
    .week {
      break-after: page;
    }
    h2 {
      font-size: 15px;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #555;
      margin: 0 0 10px 0;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    td {
      padding: 14px 10px;
      vertical-align: middle;
      border-bottom: 1px solid #e8e8e8;
      line-height: 1.3;
    }
    td.day {
      font-weight: bold;
      white-space: nowrap;
      width: 110px;
      color: #555;
    }
    .dot {
      display: inline-block;
      width: 12px; height: 12px;
      border-radius: 50%;
      margin-right: 8px;
      vertical-align: middle;
    }
    @media print {
      body { padding: 24px 32px; }
    }
  </style>
</head>
<body>

<h1>Meal Plan &mdash; [WEEK1_LABEL] &amp; [WEEK2_LABEL]</h1>
<p class="subtitle">Printed [DATE] &nbsp;|&nbsp; Next review: [REVIEW_DATE]</p>

<div class="week">
  <h2>Week 1 &mdash; [WEEK1_LABEL]</h2>
  <table>
    <tr>
      <td class="day">[Day Date]</td>
      <td><span class="dot" style="background:[color]"></span>[Display Name]</td>
    </tr>
    <!-- repeat for each day -->
  </table>
</div>

<div class="week">
  <h2>Week 2 &mdash; [WEEK2_LABEL]</h2>
  <table>
    <!-- same structure -->
  </table>
</div>

</body>
</html>
```

**Color dots:** Assign each unique meal a distinct color from this palette. Map them during plan generation so the same meal always gets the same color:

| Slot | Color |
|------|-------|
| 1 | `#7dab6e` (green) |
| 2 | `#e8a87c` (warm orange) |
| 3 | `#e8c97c` (yellow) |
| 4 | `#7caae8` (blue) |
| 5 | `#d4b896` (tan) |
| 6 | `#a87ce8` (purple) |
| 7 | `#e87c7c` (red) |
| 8+ | `#bbb` (gray) |

Confirm: "HTML saved to `~/Documents/MealPlan/meal-plan-current.html` — open to print."

---

### Step 7: Offer grocery list

If any nights were marked as "hosting" or scaled up, note: "Ingredients for [night] will be doubled on the grocery list."

Ask:
> "Generate a grocery list now? Say which store (e.g., 'TJ', 'Costco') or 'no' to skip. You can always run `/groceries` later."

---

## Error Handling

| Issue | Response |
|-------|----------|
| `patterns.md` not found | Enter setup mode |
| `recipes.md` not found | Plan by meal name only, skip ingredient detail |
| Google Calendar MCP unavailable | Skip calendar check, ask user to flag disruptions manually |
| `Meal Plan.md` missing | Mode = CREATE |
| HTML write fails | Print HTML to terminal so user can copy-paste |
