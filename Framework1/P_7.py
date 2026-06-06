# Perform data filtering and grouping using Pandas to analyze student marks or sales records.
import pandas as pd

data = {
    "Student": ["Aman", "Rahul", "Priya", "Aman", "Rahul"],
    "Subject": ["Math", "Math", "Math", "Science", "Science"],
    "Marks": [85, 90, 88, 80, 92]
}

df = pd.DataFrame(data)

# Filter
print("Marks greater than 85:")
print(df[df["Marks"] > 85])

# Group By
print("\nAverage Marks:")
print(df.groupby("Student")["Marks"].mean())