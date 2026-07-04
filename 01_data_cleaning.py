"""
Campus Placement Data Analysis
Step 1: Load and clean the dataset
"""
import pandas as pd

# Load data
df = pd.read_csv('data/Placement_Data_Full_Class.csv')

print("=" * 50)
print("SHAPE:", df.shape)
print("=" * 50)
print("\nCOLUMN INFO:")
print(df.info())

print("\n" + "=" * 50)
print("MISSING VALUES:")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("PLACEMENT STATUS COUNTS:")
print(df['status'].value_counts())

# The only column with missing values is 'salary' — and that's expected,
# because students who were NOT placed have no salary. This isn't
# "missing data" in the bad sense, it's structurally missing.
# We handle it by filling with 0 (no salary earned) rather than dropping rows.
df['salary'] = df['salary'].fillna(0)

# Drop sl_no (serial number) — it's just a row index, no analytical value
df = df.drop(columns=['sl_no'])

# Save cleaned version
df.to_csv('data/placement_cleaned.csv', index=False)
print("\nCleaned data saved to data/placement_cleaned.csv")
print("\nFirst 5 rows after cleaning:")
print(df.head())
