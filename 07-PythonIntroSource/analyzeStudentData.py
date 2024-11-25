import pandas as pd

# Load the Excel file into a DataFrame
excel_file_path = '/07-PythonIntroSource/student_data.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(excel_file_path)

# Display all data
print("All Student Data:")
print(df)

# Display basic information about the data
print("Basic Information about the Data:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Sort students by GPA in descending order
df_sorted_gpa = df.sort_values(by='GPA', ascending=False)
print("\nStudents sorted by GPA in descending order:")
print(df_sorted_gpa)

# Sort students by last name and then by first name in ascending order
df_sorted_name = df.sort_values(by=['Last Name', 'First Name'])
print("\nStudents sorted by last name and then by first name in ascending order:")
print(df_sorted_name)

# Filter students with GPA greater than a certain value
gpa_threshold = 3.5
high_gpa_students = df[df['GPA'] > gpa_threshold]
print(f"\nStudents with GPA greater than {gpa_threshold}:")
print(high_gpa_students)

# Filter students whose names start with a certain letter
name_starts_with = 'A'
a_students = df[df['First Name'].str.startswith(name_starts_with, na=False) | df['Last Name'].str.startswith(name_starts_with, na=False)]
print(f"\nStudents whose names start with '{name_starts_with}':")
print(a_students)

# Filter students with Student ID less than a certain value
id_threshold = 'S008'
low_id_students = df[df['Student ID'] < id_threshold]
print(f"\nStudents with Student ID less than {id_threshold}:")
print(low_id_students)
