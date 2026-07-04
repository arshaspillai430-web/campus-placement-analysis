# Campus Placement Data Analysis & Prediction App

## Overview
This project analyzes a dataset of 215 MBA students to identify the factors most
strongly associated with campus placement outcomes and salary, then goes a step
further by training a machine learning model to predict placement and wrapping
it in an interactive Streamlit app.

**Dataset:** [Campus Recruitment Dataset](https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement) (Kaggle, by Ben Roshan)

## Problem Statement
What academic and demographic factors most influence whether a student gets
placed, and can we build a model that predicts placement outcome for a new student?

## Approach
1. **Data Cleaning** (`01_data_cleaning.py`)
   - Loaded 215 records, 15 columns
   - Handled the only missing-value column (`salary`) — expected, since
     unplaced students have no salary. Filled with 0 rather than dropping rows.
   - Dropped the serial number column (no analytical value).

2. **Exploratory Analysis with Pandas** (`02_analysis.py`)
   - Compared placement rate across gender, work experience, specialisation, and degree type.
   - Bucketed degree percentage into bands to check for a threshold effect.

3. **SQL Analysis with SQLite** (`04_sql_analysis.py`)
   - Loaded cleaned data into a SQLite database.
   - Wrote SQL queries to cross-tabulate specialisation and work experience,
     find top earners, and surface outliers.

4. **Visualization** (`03_visualizations.py`)
   - Bar charts for placement rate by degree band and work experience.
   - Scatter plot of degree % vs MBA % colored by placement status.
   - Bar chart of average salary by specialisation.

5. **Model Training** (`05_model_training.py`)
   - Trained a classification model on the cleaned dataset to predict
     placement status (Placed / Not Placed) based on academic scores,
     work experience, and specialisation.
   - Saved the trained model for reuse in the app.

6. **Interactive Prediction App** (`06_app.py`)
   - Built with Streamlit.
   - Lets a user enter a student's details (SSC%, HSC%, degree%, work
     experience, specialisation, etc.) and get a live placement prediction
     from the trained model.

## Key Findings

| Finding | Detail |
|---|---|
| Overall placement rate | 68.8% (148 of 215 students) |
| Degree % is the strongest single predictor | Below 55% → 0% placed. Above 75% → 92% placed. |
| Work experience matters a lot | 86.5% placement rate with experience vs 59.6% without |
| Specialisation affects both placement and pay | Mkt&Fin: 79.2% placed, avg salary ₹2.99L. Mkt&HR: 55.8% placed, avg salary ₹2.70L |
| Sci&Tech grads earn the most on average | ₹3.15L average salary, higher than Comm&Mgmt or Others |
| Notable outlier group | Several high-scoring students weren't placed — worth further investigation with a larger dataset |

## Tech Stack
- Python 3, pandas
- SQLite (via Python's `sqlite3` module)
- Matplotlib, Seaborn
- scikit-learn (model training)
- Streamlit (interactive app)

## How to Run
```bash
pip install pandas matplotlib seaborn scikit-learn streamlit
python 01_data_cleaning.py
python 02_analysis.py
python 03_visualizations.py
python 04_sql_analysis.py
python model_training.py
streamlit run app.py
```

## Files
```
campus-placement-analysis/
├── 01_data_cleaning.py
├── 02_analysis.py
├── 03_visualizations.py
├── 04_sql_analysis.py
├── 05_model_training.py
├── 06_app.py
├── README.md
└── charts/
    ├── 01_placement_by_degree_band.png
    ├── 02_placement_by_workex.png
    ├── 03_degree_vs_mba_scatter.png
    └── 04_salary_by_specialisation.png
```
