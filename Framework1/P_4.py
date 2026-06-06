# Create a Pandas DataFrame from a dictionary and display its rows and columns.
import pandas as pd
data = {
    "Name": ["Aman", "Rahul", "Priya"],
    "Age": [20, 21, 19],
    "City": ["Delhi", "Noida", "Gurgaon"]
}
df = pd.DataFrame(data)
print(df)
print("\nRows:")
print(df.index)
print("\nColumns:")
print(df.columns)
