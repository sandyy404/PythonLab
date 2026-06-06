# Handle missing values in a dataset using Pandas by replacing, dropping, or interpolating null values.

import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Rahul", np.nan, "Priya"],
    "Marks": [85, np.nan, 75, 90]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Drop rows with missing names
df = df.dropna()

print("\nAfter Handling Missing Values:")
print(df)