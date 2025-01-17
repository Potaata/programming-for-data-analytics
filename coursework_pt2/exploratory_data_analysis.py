import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

student_data = pd.read_csv('students.csv')



# EXPLORATORY DATA ANALYSIS

# Total Grades for Each Student Across Subjects

# Adding a new column for total grades (sum of G1, G2, and G3)
student_data['total_grades'] = student_data['G1'] + student_data['G2'] + student_data['G3']

# Visualizing the total grades distribution
plt.figure(figsize=(8, 6))
sns.histplot(student_data['total_grades'], kde=True, color='lightblue')
plt.title('Distribution of Total Grades')
plt.xlabel('Total Grades')
plt.ylabel('Number of Students')
plt.show()


# Average Study Time per Student Grouped by Gender

# Define mapping for 'studytime' 
studytime_mapping = {
    '<2 hours': 1,
    '2 to 5 hours': 2,
    '5 to 10 hours': 3,
    '>10 hours': 4
}

# Map the 'studytime' strings to numeric values
student_data['studytime'] = student_data['studytime'].map(studytime_mapping)

# Ensure the 'studytime' column is now numeric
avg_studytime_gender = student_data.groupby('sex')['studytime'].mean()

# Visualizing the average study time by gender
plt.figure(figsize=(8, 6))
sns.barplot(x=avg_studytime_gender.index, y=avg_studytime_gender.values, palette='Set1')
plt.title('Average Study Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Study Time')
plt.show()

# Top 10 students with the highest grades

# Adding a column for total grades
student_data['total_grades'] = student_data['G1'] + student_data['G2'] + student_data['G3']

# Sorting the dataset by total grades in descending order
top_students = student_data.sort_values(by='total_grades', ascending=False).head(10)

# Displaying the top 10 students details
print("Top 10 Students with the Highest Total Grades:")
print(top_students[['school', 'sex', 'G1', 'G2', 'G3', 'total_grades']])


# Relationship Between Absences and Study Time

# Custom color palette for gender
custom_palette = {'M': 'blue', 'F': 'pink'}

# Scatter plot with custom colors for gender
plt.figure(figsize=(8, 6))
sns.scatterplot(x='studytime', y='absences', data=student_data, hue='sex', palette=custom_palette)
plt.title('Relationship Between Study Time and Absences')
plt.xlabel('Study Time')
plt.ylabel('Absences')
plt.show()

# Analysis of Failures in Relation to Study Time

# Visualizing the relationship between number of failures and study time
plt.figure(figsize=(8, 6))
sns.boxplot(x='failures', y='studytime', data=student_data, palette='Set2')
plt.title('Study Time Based on Number of Failures')
plt.xlabel('Number of Failures')
plt.ylabel('Study Time')
plt.show()


# Average grades based on internet access

# Calculating average grades based on internet access
avg_grades_internet = student_data.groupby('internet')[['G1', 'G2', 'G3']].mean()

# Plotting the bar chart
plt.figure(figsize=(10, 6))
avg_grades_internet.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average Grades (G1, G2, G3) Based on Internet Access')
plt.xlabel('Internet Access')
plt.ylabel('Average Grades')
plt.xticks(rotation=0)
plt.legend(title='Grades', loc='upper left')
plt.show()