"""
Campus Placement Data Analysis
Step 4: SQL-based analysis
Loads cleaned data into SQLite and runs SQL queries for the same insights,
demonstrating SQL skills alongside pandas.
"""
import pandas as pd
import sqlite3

df = pd.read_csv('data/placement_cleaned.csv')

# Create an in-memory SQLite database and load the data
conn = sqlite3.connect('data/placement.db')
df.to_sql('students', conn, if_exists='replace', index=False)

print("=" * 60)
print("QUERY 1: Overall placement rate")
print("=" * 60)
q1 = """
SELECT
    status,
    COUNT(*) AS num_students,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM students), 1) AS percentage
FROM students
GROUP BY status;
"""
print(pd.read_sql(q1, conn))

print("\n" + "=" * 60)
print("QUERY 2: Placement rate by specialisation and work experience")
print("=" * 60)
q2 = """
SELECT
    specialisation,
    workex,
    COUNT(*) AS total_students,
    SUM(CASE WHEN status = 'Placed' THEN 1 ELSE 0 END) AS placed_count,
    ROUND(SUM(CASE WHEN status = 'Placed' THEN 1.0 ELSE 0 END) * 100.0 / COUNT(*), 1) AS placement_rate
FROM students
GROUP BY specialisation, workex
ORDER BY placement_rate DESC;
"""
print(pd.read_sql(q2, conn))

print("\n" + "=" * 60)
print("QUERY 3: Average salary by degree type, only placed students")
print("=" * 60)
q3 = """
SELECT
    degree_t,
    COUNT(*) AS placed_students,
    ROUND(AVG(salary), 0) AS avg_salary,
    MAX(salary) AS highest_salary
FROM students
WHERE status = 'Placed'
GROUP BY degree_t
ORDER BY avg_salary DESC;
"""
print(pd.read_sql(q3, conn))

print("\n" + "=" * 60)
print("QUERY 4: Top 5 highest-paid placed students")
print("=" * 60)
q4 = """
SELECT gender, degree_t, specialisation, degree_p, mba_p, salary
FROM students
WHERE status = 'Placed'
ORDER BY salary DESC
LIMIT 5;
"""
print(pd.read_sql(q4, conn))

print("\n" + "=" * 60)
print("QUERY 5: Students with high degree% but NOT placed (interesting outliers)")
print("=" * 60)
q5 = """
SELECT gender, degree_t, specialisation, degree_p, mba_p, etest_p, status
FROM students
WHERE status = 'Not Placed' AND degree_p > 70
ORDER BY degree_p DESC;
"""
print(pd.read_sql(q5, conn))

conn.close()
print("\nDatabase saved to data/placement.db")
