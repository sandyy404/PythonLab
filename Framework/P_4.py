# Program to Create a Pandas Series and DataFrame.
import pandas as pd
arr = pd.Series([1,2,3,4,5])
print("Panda's array")
print("index value")
print(arr)

data = {
    'Name': ['Sandeep', 'Ritesh', 'Deepak'],
    'Age': [21, 22, 23]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)