import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

student_data = pd.read_csv('students.csv')
student_data.info()

print(student_data.head())


# Categorical nominal
# Transforming 'sex', 'address', 'Mjob', and 'reason' into categorical nominal
categorical_nominal_cols = ['sex', 'address', 'Mjob', 'reason']
student_data[categorical_nominal_cols] = student_data[categorical_nominal_cols].astype('category')

# Checking unique values for verification
for col in categorical_nominal_cols:
    print(f"{col}: {student_data[col].unique()}")


# Categorical nominal boolean

# Transforming binary categorical columns into boolean
categorical_boolean_cols = ['schoolsup', 'famsup', 'higher', 'internet', 'romantic']
for col in categorical_boolean_cols:
    student_data[col] = student_data[col].map({'yes': True, 'no': False})

# Displaying transformations
print(student_data[categorical_boolean_cols].head())


# Categorical ordinal

# mapping for ordinal transformation
ordinal_mappings = {
    'studytime': {
        '<2 hours': 1,
        '2 to 5 hours': 2,
        '5 to 10 hours': 3,
        '>10 hours': 4
    },
    'famrel': {
        'very bad': 1,
        'bad': 2,
        'good': 3,
        'very good': 4,
        'excellent': 5
    },
    'health': {
        'very bad': 1,
        'bad': 2,
        'good': 3,
        'very good': 4,
        'excellent': 5
    }
}

# Mapping descriptive strings to numeric values
for col, mapping in ordinal_mappings.items():
    if col in student_data.columns:  # Ensure the column exists
        student_data[col] = student_data[col].map(mapping)

# Transforming into Categorical Ordinal
for col, mapping in ordinal_mappings.items():
    if col in student_data.columns:  # Ensure the column exists
        student_data[col] = pd.Categorical(
            student_data[col], 
            categories=list(mapping.values()), 
            ordered=True
        )

# Displaying the transformed data
print("Transformed Data (First 5 Rows):")
print(student_data[['studytime', 'famrel', 'health']].head())


# Categorical time interval

# Defining map for 'traveltime'
traveltime_mapping = {
    '<15 min.': 1,
    '15 to 30 min.': 2,
    '30 min. to 1 hour': 3,
    '>1 hour': 4
}

# Mapping descriptive strings to numeric values
student_data['traveltime'] = student_data['traveltime'].map(traveltime_mapping)

# Transforming into Categorical Ordinal
traveltime_categories = [1, 2, 3, 4]  # Define the category order
student_data['traveltime'] = pd.Categorical(
    student_data['traveltime'],
    categories=traveltime_categories,
    ordered=True
)

# Displaying the output
print("Transformed 'traveltime':")
print(student_data['traveltime'].head())