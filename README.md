# Campus Placement Data Analysis

## Overview
This project analyzes a dataset of 215 MBA students to identify the factors most
strongly associated with campus placement outcomes and salary. It combines Python
(pandas) for data cleaning and exploration, SQL (SQLite) for structured querying,
and Matplotlib/Seaborn for visualization.

**Dataset:** [Campus Recruitment Dataset](https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement) (Kaggle, by Ben Roshan)

## Problem Statement
What academic and demographic factors most influence whether a student gets
placed, and how much they earn if placed?

## Approach
1. **Data Cleaning** (`01_data_cleaning.py`)
   - Loaded 215 records, 15 columns
   - Identified that `salary` was the only column with missing values — expected,
     since unplaced students have no salary. Filled with 0 rather than dropping rows.
   - Dropped the serial number column (no analytical value).

2. **Exploratory Analysis with Pandas** (`02_analysis.py`)
   - Grouped and compared placement rate across gender, work experience,
     specialisation, and degree type.
   - Bucketed degree percentage into bands to check for a threshold effect.

3. **SQL Analysis with SQLite** (`04_sql_analysis.py`)
   - Loaded the cleaned data into a SQLite database.
   - Wrote SQL queries to cross-tabulate specialisation and work experience,
     find top earners, and surface outliers (high scorers who weren't placed).

4. **Visualization** (`03_visualizations.py`)
   - Bar charts for placement rate by degree band and work experience.
   - Scatter plot of degree % vs MBA % colored by placement status.
   - Bar chart of average salary by specialisation.

## Key Findings

| Finding | Detail |
|---|---|
| Overall placement rate | 68.8% (148 of 215 students) |
| Degree % is the strongest single predictor | Below 55% → 0% placed. Above 75% → 92% placed. |
| Work experience matters a lot | 86.5% placement rate with experience vs 59.6% without |
| Specialisation affects both placement and pay | Mkt&Fin: 79.2% placed, avg salary ₹2.99L. Mkt&HR: 55.8% placed, avg salary ₹2.70L |
| Sci&Tech grads earn the most on average | ₹3.15L average salary, higher than Comm&Mgmt or Others despite similar placement rate |
| Notable outlier group | Several students with degree% above 70 were *not* placed — 5 of 6 such cases in this dataset were women, worth further investigation with a larger dataset |

## Tech Stack
- Python 3, pandas
- SQLite (via Python's `sqlite3` module)
- Matplotlib, Seaborn

## How to Run
```bash
pip install pandas matplotlib seaborn
python 01_data_cleaning.py
python 02_analysis.py
python 03_visualizations.py
python 04_sql_analysis.py
```

## Files
```
placement_project/
├── data/
│   ├── Placement_Data_Full_Class.csv   # raw data
│   ├── placement_cleaned.csv           # cleaned data
│   └── placement.db                    # SQLite database
├── charts/
│   ├── 01_placement_by_degree_band.png
│   ├── 02_placement_by_workex.png
│   ├── 03_degree_vs_mba_scatter.png
│   └── 04_salary_by_specialisation.png
├── 01_data_cleaning.py
├── 02_analysis.py
├── 03_visualizations.py
├── 04_sql_analysis.py
└── README.md
```
