# Terminal Scavenger Hunt

**Time limit**: 15 minutes
**Rules**: Use ONLY terminal commands. No Finder, no Excel, no Stata.
**Setup**: Open your terminal and navigate to the folder containing `household_survey.csv` and `sample_dofile.do`.

For each question, write (a) the command you used and (b) the answer.

---

## Questions

**1. How many lines are in `household_survey.csv` (including the header)?**

Command: _______________________________________________
Answer: ________________________________________________

**2. What are the column headers (variable names)?**

Command: _______________________________________________
Answer: ________________________________________________

**3. How many households are in the treatment group (treatment = 1)?**

Command: _______________________________________________
Answer: ________________________________________________

**4. Which districts appear in the data?**

Command: _______________________________________________
Answer: ________________________________________________

**5. How many households are in Nairobi?**

Command: _______________________________________________
Answer: ________________________________________________

**6. What is the last household ID in the file?**

Command: _______________________________________________
Answer: ________________________________________________

**7. Find all lines in the do-file that mention "income".**

Command: _______________________________________________
Answer (how many lines?): ______________________________

**8. How many comment lines (lines starting with `*`) are in the do-file?**

Command: _______________________________________________
Answer: ________________________________________________

**9. Find the household with negative income.**

Command: _______________________________________________
Answer (which hhid?): __________________________________

**10. Save all Nairobi observations to a new file called `nairobi_only.csv` (with the header row).**

Command(s): ____________________________________________

---

## Bonus (if you finish early)

**11.** How many households have missing consumption data (empty cells)?

**12.** What is the most common number of children? (Hint: `cut`, `sort`, `uniq -c`, and `sort -rn` piped together.)

---

<details>
<summary><strong>Answer Key</strong> (click to expand)</summary>

**1. Line count**
```bash
wc -l household_survey.csv
```
Answer: 76 (75 data rows + 1 header)

**2. Column headers**
```bash
head -1 household_survey.csv
```
Answer: hhid,district,treatment,income,n_children,female_head,survey_round,consumption

**3. Treatment group count**
```bash
cut -d',' -f3 household_survey.csv | grep -c "^1$"
```
Answer: 36

Alternative (slightly less precise but works here):
```bash
awk -F',' 'NR>1 && $3==1' household_survey.csv | wc -l
```

Note: `grep ",1," household_survey.csv | wc -l` would overcount because it also matches 1s in other columns like `female_head` and `survey_round`. This is a good lesson in being precise with CSV data on the command line.

**4. Districts**
```bash
cut -d',' -f2 household_survey.csv | sort -u
```
Answer: Eldoret, Kisumu, Mombasa, Nairobi, Nakuru (plus "district" from the header)

To skip the header:
```bash
tail -n +2 household_survey.csv | cut -d',' -f2 | sort -u
```

**5. Nairobi count**
```bash
grep "Nairobi" household_survey.csv | wc -l
```
Answer: 22

**6. Last household ID**
```bash
tail -1 household_survey.csv
```
Answer: 1075 (the full row is: 1075,Nairobi,1,139949,1,0,1,92179)

To get just the ID:
```bash
tail -1 household_survey.csv | cut -d',' -f1
```

**7. Lines mentioning "income" in the do-file**
```bash
grep "income" sample_dofile.do
```
Answer: 8 lines match. To count:
```bash
grep -c "income" sample_dofile.do
```

**8. Comment lines in the do-file**
```bash
grep "^\*" sample_dofile.do | wc -l
```
Answer: 13 (lines beginning with `*`)

Note: This counts lines that start with `*`. Some Stata comments use `//` or `/* */`, but in this file all comments start with `*`.

**9. Negative income**
```bash
grep ",-" household_survey.csv
```
Answer: hhid 1038 (row: 1038,Eldoret,0,-500,5,0,2,109564)

**10. Save Nairobi observations**
```bash
head -1 household_survey.csv > nairobi_only.csv
grep "Nairobi" household_survey.csv >> nairobi_only.csv
```
This first writes the header, then appends all Nairobi rows.

**Bonus 11. Missing consumption**
```bash
grep ",$" household_survey.csv | wc -l
```
Answer: 5 households have missing consumption.

Note: Consumption is the last column, so missing values appear as lines ending in a comma. If the missing column were in the middle of the row, you would look for `,,` (two consecutive commas) instead.

**Bonus 12. Most common number of children**
```bash
tail -n +2 household_survey.csv | cut -d',' -f5 | sort | uniq -c | sort -rn
```
This skips the header, extracts the n_children column, sorts it, counts unique values, then sorts by frequency (highest first).

</details>
