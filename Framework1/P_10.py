# Analyze a CSV dataset using Pandas and visualize the results using Matplotlib (e.g., plot average marks, sales trends, or population growth).

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\PythonLab\Framework1\student2.csv')

print("Dataset:")
print(df)

average = df["Marks"].mean()

print("\nAverage Marks:", average)

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()