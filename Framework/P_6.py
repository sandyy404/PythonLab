# Program to Select, Filter, and Sort Data in a Pandas DataFrame
import pandas as pd
data = {
   "name":["Sandeep","Kuldeep","Pradeep"],
   "age":[21,23,20],
   "Subject":["Math","Physics","Art"]
}
df = pd.DataFrame(data)
# print(df)

# Select
print("name:-")
print(df['name'])

#Filter

print("\nage > 22:")
print(df[df['age'] > 22])

#Sort by age

print("\nSorted by Age:")
print(df.sort_values(by='age'))
