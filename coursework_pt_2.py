import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# from sklearn.preprocessing import OneHotEncoder

student_data = pd.read_csv('students.csv')
# student_data.info()

# print(student_data.head())

# Categorical nominal
# Transform 'sex', 'address', 'Mjob', and 'reason' into categorical nominal
# categorical_nominal_cols = ['sex', 'address', 'Mjob', 'reason']
# student_data[categorical_nominal_cols] = student_data[categorical_nominal_cols].astype('category')

# # Check unique values for verification
# for col in categorical_nominal_cols:
#     print(f"{col}: {student_data[col].unique()}")


# Categorical nominal boolean

# Transform binary categorical columns into boolean
# categorical_boolean_cols = ['schoolsup', 'famsup', 'higher', 'internet', 'romantic']
# for col in categorical_boolean_cols:
#     student_data[col] = student_data[col].map({'yes': True, 'no': False})

# # Check transformations
# print(student_data[categorical_boolean_cols].head())

# Categorical ordinal

