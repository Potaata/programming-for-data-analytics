import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

student_data = pd.read_csv('students.csv')


# FURTHER ANALYSIS

# Analyzing the Impact of Family Support on Grades

# Grouping data by family support and calculating average grades
family_support_grades = student_data.groupby('famsup')[['G1', 'G2', 'G3']].mean()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
family_support_grades.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'lightgreen', 'pink'])
plt.title('Impact of Family Support on Grades')
plt.xlabel('Family Support')
plt.ylabel('Average Grades')
plt.xticks(rotation=0)
plt.legend(title='Grades', loc='upper right')
plt.show()

# Exploring the Effect of Alcohol Consumption on Grades

# Grouping data by alcohol consumption and calculating average grades
weekend_alcohol_grades = student_data.groupby('Walc')[['G1', 'G2', 'G3']].mean().mean(axis=1)
weekday_alcohol_grades = student_data.groupby('Dalc')[['G1', 'G2', 'G3']].mean().mean(axis=1)

# Combining weekend and weekday alcohol consumption data into a single DataFrame
combined_alcohol_grades = pd.DataFrame({
    'Weekend (Walc)': weekend_alcohol_grades,
    'Weekday (Dalc)': weekday_alcohol_grades
})

# Plotting the data
plt.figure(figsize=(10, 6))
combined_alcohol_grades.plot(kind='bar', figsize=(10, 6), color=['coral', 'skyblue'], width=0.7)
plt.title('Effect of Alcohol Consumption on Average Grades')
plt.xlabel('Alcohol Consumption Level (1=Low, 5=High)')
plt.ylabel('Average Grades')
plt.xticks(rotation=0)
plt.legend(title='Alcohol Consumption', loc='upper right')
plt.show()

# Gender-Based Preferences for Higher Education

# Splitting data by gender
male_higher_education = student_data[student_data['sex'] == 'M']['higher'].value_counts()
female_higher_education = student_data[student_data['sex'] == 'F']['higher'].value_counts()

# Creating subplots for two pie charts
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart for males
axes[0].pie(
    male_higher_education, 
    labels=male_higher_education.index, 
    autopct='%1.1f%%', 
    colors=['lightblue', 'orange'], 
    startangle=90
)
axes[0].set_title('Higher Education Aspiration (Male)')

# Pie chart for females
axes[1].pie(
    female_higher_education, 
    labels=female_higher_education.index, 
    autopct='%1.1f%%', 
    colors=['pink', 'purple'], 
    startangle=90
)
axes[1].set_title('Higher Education Aspiration (Female)')

# Displaying the charts
plt.tight_layout()
plt.show()

# Relationship Between Parents’ Education and Student Performance

# Grouping data by parents' education levels and calculating average grades
parent_education_grades = student_data.groupby(['Medu', 'Fedu'])[['G1', 'G2', 'G3']].mean().reset_index()

# Creating a heatmap of average grades
parent_education_pivot = parent_education_grades.pivot(index='Medu', columns='Fedu', values='G3')

plt.figure(figsize=(8, 6))

# Create the heatmap
sns.heatmap(parent_education_pivot, annot=True, cmap='YlGnBu', fmt=".2f", 
            annot_kws={'size': 8})  # Adjust annotation size

# Adjust title, labels, and tick sizes
plt.title('Relationship Between Parents’ Education and Average Grade (G3)', fontsize=10)
plt.xlabel('Father’s Education Level', fontsize=8)
plt.ylabel('Mother’s Education Level', fontsize=8)

# Adjust tick label size
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Tight layout to remove extra gap
plt.tight_layout()

plt.show()
