# Read a CSV file using Pandas and generate descriptive statistics of the dataset.

import pandas as pd  # type: ignore

df = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\PythonLab\Framework1\students.csv")

print(df)

print("\nDescriptive Statistics:")
print(df.describe())