"""
Campus Placement Data Analysis
Step 2: Exploratory analysis - what factors relate to placement?
"""
import pandas as pd

df = pd.read_csv('data/placement_cleaned.csv')

def pct(series):
    return round(series, 1)

print("=" * 60)
print("1. OVERALL PLACEMENT RATE")
print("=" * 60)
total = len(df)
placed = (df['status'] == 'Placed').sum()
print(f"Total students: {total}")
print(f"Placed: {placed} ({pct(placed/total*100)}%)")
print(f"Not Placed: {total-placed} ({pct((total-placed)/total*100)}%)")

print("\n" + "=" * 60)
print("2. PLACEMENT RATE BY GENDER")
print("=" * 60)
gender_placement = df.groupby('gender')['status'].apply(
    lambda x: (x == 'Placed').mean() * 100
).round(1)
print(gender_placement)

print("\n" + "=" * 60)
print("3. PLACEMENT RATE BY WORK EXPERIENCE")
print("=" * 60)
workex_placement = df.groupby('workex')['status'].apply(
    lambda x: (x == 'Placed').mean() * 100
).round(1)
print(workex_placement)

print("\n" + "=" * 60)
print("4. PLACEMENT RATE BY SPECIALISATION")
print("=" * 60)
spec_placement = df.groupby('specialisation')['status'].apply(
    lambda x: (x == 'Placed').mean() * 100
).round(1)
print(spec_placement)

print("\n" + "=" * 60)
print("5. PLACEMENT RATE BY DEGREE TYPE")
print("=" * 60)
degree_placement = df.groupby('degree_t')['status'].apply(
    lambda x: (x == 'Placed').mean() * 100
).round(1)
print(degree_placement)

print("\n" + "=" * 60)
print("6. AVERAGE ACADEMIC SCORES: PLACED vs NOT PLACED")
print("=" * 60)
score_cols = ['ssc_p', 'hsc_p', 'degree_p', 'etest_p', 'mba_p']
comparison = df.groupby('status')[score_cols].mean().round(2)
print(comparison)

print("\n" + "=" * 60)
print("7. CGPA BAND vs PLACEMENT RATE (using degree_p as proxy)")
print("=" * 60)
df['degree_band'] = pd.cut(df['degree_p'],
                             bins=[0, 55, 65, 75, 100],
                             labels=['Below 55%', '55-65%', '65-75%', 'Above 75%'])
band_placement = df.groupby('degree_band', observed=True)['status'].apply(
    lambda x: (x == 'Placed').mean() * 100
).round(1)
print(band_placement)

print("\n" + "=" * 60)
print("8. AVERAGE SALARY BY SPECIALISATION (placed students only)")
print("=" * 60)
placed_df = df[df['status'] == 'Placed']
salary_by_spec = placed_df.groupby('specialisation')['salary'].mean().round(0)
print(salary_by_spec)

print("\n" + "=" * 60)
print("9. HIGHEST PAYING DEGREE TYPE (placed students only)")
print("=" * 60)
salary_by_degree = placed_df.groupby('degree_t')['salary'].mean().round(0)
print(salary_by_degree)
