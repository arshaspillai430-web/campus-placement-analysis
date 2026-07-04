"""
Campus Placement Data Analysis
Step 3: Visualizations
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
df = pd.read_csv('data/placement_cleaned.csv')

# Chart 1: Placement rate by degree percentage band
df['degree_band'] = pd.cut(df['degree_p'],
                             bins=[0, 55, 65, 75, 100],
                             labels=['Below 55%', '55-65%', '65-75%', 'Above 75%'])
band_placement = df.groupby('degree_band', observed=True)['status'].apply(
    lambda x: (x == 'Placed').mean() * 100
)

plt.figure(figsize=(8, 5))
bars = plt.bar(band_placement.index.astype(str), band_placement.values,
                color=['#e74c3c', '#f39c12', '#3498db', '#2ecc71'])
plt.title('Placement Rate by Degree Percentage Band', fontsize=14, fontweight='bold')
plt.xlabel('Degree Percentage Band')
plt.ylabel('Placement Rate (%)')
plt.ylim(0, 100)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 2, f'{height:.1f}%',
              ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('charts/01_placement_by_degree_band.png', dpi=150)
plt.close()
print("Saved: 01_placement_by_degree_band.png")

# Chart 2: Placement rate by work experience
workex_placement = df.groupby('workex')['status'].apply(
    lambda x: (x == 'Placed').mean() * 100
)
plt.figure(figsize=(6, 5))
bars = plt.bar(workex_placement.index, workex_placement.values,
                color=['#e74c3c', '#2ecc71'])
plt.title('Placement Rate: Work Experience vs No Experience', fontsize=13, fontweight='bold')
plt.ylabel('Placement Rate (%)')
plt.ylim(0, 100)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 2, f'{height:.1f}%',
              ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('charts/02_placement_by_workex.png', dpi=150)
plt.close()
print("Saved: 02_placement_by_workex.png")

# Chart 3: Degree % vs MBA % scatter, colored by placement status
plt.figure(figsize=(8, 6))
colors = df['status'].map({'Placed': '#2ecc71', 'Not Placed': '#e74c3c'})
plt.scatter(df['degree_p'], df['mba_p'], c=colors, alpha=0.7, s=60, edgecolors='white')
plt.title('Degree % vs MBA % (colored by placement status)', fontsize=13, fontweight='bold')
plt.xlabel('Degree Percentage')
plt.ylabel('MBA Percentage')
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=c, markersize=10, label=l)
           for l, c in [('Placed', '#2ecc71'), ('Not Placed', '#e74c3c')]]
plt.legend(handles=handles)
plt.tight_layout()
plt.savefig('charts/03_degree_vs_mba_scatter.png', dpi=150)
plt.close()
print("Saved: 03_degree_vs_mba_scatter.png")

# Chart 4: Average salary by specialisation
placed_df = df[df['status'] == 'Placed']
salary_by_spec = placed_df.groupby('specialisation')['salary'].mean()
plt.figure(figsize=(7, 5))
bars = plt.bar(salary_by_spec.index, salary_by_spec.values, color=['#3498db', '#9b59b6'])
plt.title('Average Salary by Specialisation (Placed Students)', fontsize=13, fontweight='bold')
plt.ylabel('Average Salary (INR)')
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 3000, f'₹{height:,.0f}',
              ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('charts/04_salary_by_specialisation.png', dpi=150)
plt.close()
print("Saved: 04_salary_by_specialisation.png")

print("\nAll charts saved to charts/ folder")
