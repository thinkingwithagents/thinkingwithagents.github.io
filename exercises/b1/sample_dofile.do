* ============================================
* Project: Household Survey Analysis
* Author: Research Team
* Date: 2025-06-15
* Purpose: Clean and analyze household data
* ============================================

clear all
set more off

* Set paths
global datadir "./data"
global outdir "./output"

* Load data
import delimited "$datadir/household_survey.csv", clear

* Basic cleaning
destring income consumption, replace force
replace income = . if income < 0
label variable income "Annual household income (KES)"
label variable consumption "Annual consumption (KES)"
label variable treatment "Treatment assignment (0/1)"
label variable female_head "Female-headed household (0/1)"
label variable n_children "Number of children"

* Generate derived variables
gen log_income = ln(income)
gen log_consumption = ln(consumption)
gen income_per_capita = income / (n_children + 1)

* Summary statistics
summarize income consumption n_children if survey_round == 1
summarize income consumption n_children if survey_round == 2

* Treatment effects
reg income treatment female_head n_children, robust
reg consumption treatment female_head n_children, robust

* Export results
esttab using "$outdir/main_results.csv", replace
