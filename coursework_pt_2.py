import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

student_data = pd.read_csv('students.csv')
student_data.info()

print(student_data.head())

# # Categorical nominal
# # Transforming 'sex', 'address', 'Mjob', and 'reason' into categorical nominal
# categorical_nominal_cols = ['sex', 'address', 'Mjob', 'reason']
# student_data[categorical_nominal_cols] = student_data[categorical_nominal_cols].astype('category')

# # Checking unique values for verification
# for col in categorical_nominal_cols:
#     print(f"{col}: {student_data[col].unique()}")


# # Categorical nominal boolean

# # Transforming binary categorical columns into boolean
# categorical_boolean_cols = ['schoolsup', 'famsup', 'higher', 'internet', 'romantic']
# for col in categorical_boolean_cols:
#     student_data[col] = student_data[col].map({'yes': True, 'no': False})

# # Displaying transformations
# print(student_data[categorical_boolean_cols].head())


# # Categorical ordinal

# # mapping for ordinal transformation
# ordinal_mappings = {
#     'studytime': {
#         '<2 hours': 1,
#         '2 to 5 hours': 2,
#         '5 to 10 hours': 3,
#         '>10 hours': 4
#     },
#     'famrel': {
#         'very bad': 1,
#         'bad': 2,
#         'good': 3,
#         'very good': 4,
#         'excellent': 5
#     },
#     'health': {
#         'very bad': 1,
#         'bad': 2,
#         'good': 3,
#         'very good': 4,
#         'excellent': 5
#     }
# }

# # Mapping descriptive strings to numeric values
# for col, mapping in ordinal_mappings.items():
#     if col in student_data.columns:  # Ensure the column exists
#         student_data[col] = student_data[col].map(mapping)

# # Transforming into Categorical Ordinal
# for col, mapping in ordinal_mappings.items():
#     if col in student_data.columns:  # Ensure the column exists
#         student_data[col] = pd.Categorical(
#             student_data[col], 
#             categories=list(mapping.values()), 
#             ordered=True
#         )

# # Displaying the transformed data
# print("Transformed Data (First 5 Rows):")
# print(student_data[['studytime', 'famrel', 'health']].head())


# # Categorical time interval

# # Defining map for 'traveltime'
# traveltime_mapping = {
#     '<15 min.': 1,
#     '15 to 30 min.': 2,
#     '30 min. to 1 hour': 3,
#     '>1 hour': 4
# }

# # Mapping descriptive strings to numeric values
# student_data['traveltime'] = student_data['traveltime'].map(traveltime_mapping)

# # Transforming into Categorical Ordinal
# traveltime_categories = [1, 2, 3, 4]  # Define the category order
# student_data['traveltime'] = pd.Categorical(
#     student_data['traveltime'],
#     categories=traveltime_categories,
#     ordered=True
# )

# # Displaying the output
# print("Transformed 'traveltime':")
# print(student_data['traveltime'].head())


# # total students passed  in all 3 subjects and determining the co-relation between students attending the lecture and passing
# # Defining the pass marks
# pass_marks = 8

# # Checking if student passed each subject (G1, G2, G3)
# student_data['pass_G1'] = student_data['G1'] >= pass_marks
# student_data['pass_G2'] = student_data['G2'] >= pass_marks
# student_data['pass_G3'] = student_data['G3'] >= pass_marks

# # Creating a new column to check if the student passed all 3 subjects
# student_data['pass_all_subjects'] = student_data['pass_G1'] & student_data['pass_G2'] & student_data['pass_G3']

# # Calculate the number of students who passed all 3 subjects
# num_passed_all = student_data['pass_all_subjects'].sum()
# print(f"Total students who passed all 3 subjects: {num_passed_all}")

# # Displaying the records of students who passed all subjects
# passed_students = student_data[student_data['pass_all_subjects']]
# print("\nDetails of astudents who passed all 3 subjects:")
# print(passed_students[['G1', 'G2', 'G3', 'pass_all_subjects']])

# # Explore the correlation between attendance and passing
# attendance_column = 'absences'  # Assuming absences is the attendance proxy
# attendance_pass_corr = student_data[attendance_column].corr(student_data['pass_all_subjects'])
# print(f"\nCorrelation between absences and passing all subjects: {attendance_pass_corr:.2f}")


# # EXPLORATORY DATA ANALYSIS

# # Total Grades for Each Student Across Subjects

# # Adding a new column for total grades (sum of G1, G2, and G3)
# student_data['total_grades'] = student_data['G1'] + student_data['G2'] + student_data['G3']

# # Visualizing the total grades distribution
# plt.figure(figsize=(8, 6))
# sns.histplot(student_data['total_grades'], kde=True, color='lightblue')
# plt.title('Distribution of Total Grades')
# plt.xlabel('Total Grades')
# plt.ylabel('Number of Students')
# plt.show()


# # Average Study Time per Student Grouped by Gender

# # Define mapping for 'studytime' 
# studytime_mapping = {
#     '<2 hours': 1,
#     '2 to 5 hours': 2,
#     '5 to 10 hours': 3,
#     '>10 hours': 4
# }

# # Map the 'studytime' strings to numeric values
# student_data['studytime'] = student_data['studytime'].map(studytime_mapping)

# # Ensure the 'studytime' column is now numeric
# avg_studytime_gender = student_data.groupby('sex')['studytime'].mean()

# # Visualizing the average study time by gender
# plt.figure(figsize=(8, 6))
# sns.barplot(x=avg_studytime_gender.index, y=avg_studytime_gender.values, palette='Set1')
# plt.title('Average Study Time by Gender')
# plt.xlabel('Gender')
# plt.ylabel('Average Study Time')
# plt.show()

# # Top 10 students with the highest grades

# # Adding a column for total grades
# student_data['total_grades'] = student_data['G1'] + student_data['G2'] + student_data['G3']

# # Sorting the dataset by total grades in descending order
# top_students = student_data.sort_values(by='total_grades', ascending=False).head(10)

# # Displaying the top 10 students details
# print("Top 10 Students with the Highest Total Grades:")
# print(top_students[['school', 'sex', 'G1', 'G2', 'G3', 'total_grades']])


# # Relationship Between Absences and Study Time

# # Custom color palette for gender
# custom_palette = {'M': 'blue', 'F': 'pink'}

# # Scatter plot with custom colors for gender
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='studytime', y='absences', data=student_data, hue='sex', palette=custom_palette)
# plt.title('Relationship Between Study Time and Absences')
# plt.xlabel('Study Time')
# plt.ylabel('Absences')
# plt.show()

# # Analysis of Failures in Relation to Study Time

# # Visualizing the relationship between number of failures and study time
# plt.figure(figsize=(8, 6))
# sns.boxplot(x='failures', y='studytime', data=student_data, palette='Set2')
# plt.title('Study Time Based on Number of Failures')
# plt.xlabel('Number of Failures')
# plt.ylabel('Study Time')
# plt.show()


# # Average grades based on internet access

# # Calculating average grades based on internet access
# avg_grades_internet = student_data.groupby('internet')[['G1', 'G2', 'G3']].mean()

# # Plotting the bar chart
# plt.figure(figsize=(10, 6))
# avg_grades_internet.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'lightgreen', 'salmon'])
# plt.title('Average Grades (G1, G2, G3) Based on Internet Access')
# plt.xlabel('Internet Access')
# plt.ylabel('Average Grades')
# plt.xticks(rotation=0)
# plt.legend(title='Grades', loc='upper left')
# plt.show()


# # FURTHER ANALYSIS

# # Analyzing the Impact of Family Support on Grades

# # Grouping data by family support and calculating average grades
# family_support_grades = student_data.groupby('famsup')[['G1', 'G2', 'G3']].mean()

# # Plotting the bar chart
# plt.figure(figsize=(10, 6))
# family_support_grades.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'lightgreen', 'pink'])
# plt.title('Impact of Family Support on Grades')
# plt.xlabel('Family Support')
# plt.ylabel('Average Grades')
# plt.xticks(rotation=0)
# plt.legend(title='Grades', loc='upper right')
# plt.show()

# # Exploring the Effect of Alcohol Consumption on Grades

# # Grouping data by alcohol consumption and calculating average grades
# weekend_alcohol_grades = student_data.groupby('Walc')[['G1', 'G2', 'G3']].mean().mean(axis=1)
# weekday_alcohol_grades = student_data.groupby('Dalc')[['G1', 'G2', 'G3']].mean().mean(axis=1)

# # Combining weekend and weekday alcohol consumption data into a single DataFrame
# combined_alcohol_grades = pd.DataFrame({
#     'Weekend (Walc)': weekend_alcohol_grades,
#     'Weekday (Dalc)': weekday_alcohol_grades
# })

# # Plotting the data
# plt.figure(figsize=(10, 6))
# combined_alcohol_grades.plot(kind='bar', figsize=(10, 6), color=['coral', 'skyblue'], width=0.7)
# plt.title('Effect of Alcohol Consumption on Average Grades')
# plt.xlabel('Alcohol Consumption Level (1=Low, 5=High)')
# plt.ylabel('Average Grades')
# plt.xticks(rotation=0)
# plt.legend(title='Alcohol Consumption', loc='upper right')
# plt.show()

# # Gender-Based Preferences for Higher Education

# # Splitting data by gender
# male_higher_education = student_data[student_data['sex'] == 'M']['higher'].value_counts()
# female_higher_education = student_data[student_data['sex'] == 'F']['higher'].value_counts()

# # Creating subplots for two pie charts
# fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# # Pie chart for males
# axes[0].pie(
#     male_higher_education, 
#     labels=male_higher_education.index, 
#     autopct='%1.1f%%', 
#     colors=['lightblue', 'orange'], 
#     startangle=90
# )
# axes[0].set_title('Higher Education Aspiration (Male)')

# # Pie chart for females
# axes[1].pie(
#     female_higher_education, 
#     labels=female_higher_education.index, 
#     autopct='%1.1f%%', 
#     colors=['pink', 'purple'], 
#     startangle=90
# )
# axes[1].set_title('Higher Education Aspiration (Female)')

# # Displaying the charts
# plt.tight_layout()
# plt.show()

# # Relationship Between Parents’ Education and Student Performance

# # Grouping data by parents' education levels and calculating average grades
# parent_education_grades = student_data.groupby(['Medu', 'Fedu'])[['G1', 'G2', 'G3']].mean().reset_index()

# # Creating a heatmap of average grades
# parent_education_pivot = parent_education_grades.pivot(index='Medu', columns='Fedu', values='G3')

# plt.figure(figsize=(8, 6))

# # Create the heatmap
# sns.heatmap(parent_education_pivot, annot=True, cmap='YlGnBu', fmt=".2f", 
#             annot_kws={'size': 8})  # Adjust annotation size

# # Adjust title, labels, and tick sizes
# plt.title('Relationship Between Parents’ Education and Average Grade (G3)', fontsize=10)
# plt.xlabel('Father’s Education Level', fontsize=8)
# plt.ylabel('Mother’s Education Level', fontsize=8)

# # Adjust tick label size
# plt.xticks(fontsize=8)
# plt.yticks(fontsize=8)

# # Tight layout to remove extra gap
# plt.tight_layout()

# plt.show()











