
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

student_data = pd.read_csv('students.csv')

# total students passed  in all 3 subjects and determining the co-relation between students attending the lecture and passing
# Defining the pass marks
pass_marks = 8

# Checking if student passed each subject (G1, G2, G3)
student_data['pass_G1'] = student_data['G1'] >= pass_marks
student_data['pass_G2'] = student_data['G2'] >= pass_marks
student_data['pass_G3'] = student_data['G3'] >= pass_marks

# Creating a new column to check if the student passed all 3 subjects
student_data['pass_all_subjects'] = student_data['pass_G1'] & student_data['pass_G2'] & student_data['pass_G3']

# Calculate the number of students who passed all 3 subjects
num_passed_all = student_data['pass_all_subjects'].sum()
print(f"Total students who passed all 3 subjects: {num_passed_all}")

# Displaying the records of students who passed all subjects
passed_students = student_data[student_data['pass_all_subjects']]
print("\nDetails of astudents who passed all 3 subjects:")
print(passed_students[['G1', 'G2', 'G3', 'pass_all_subjects']])

# Explore the correlation between attendance and passing
attendance_column = 'absences'  # Assuming absences is the attendance proxy
attendance_pass_corr = student_data[attendance_column].corr(student_data['pass_all_subjects'])
print(f"\nCorrelation between absences and passing all subjects: {attendance_pass_corr:.2f}")