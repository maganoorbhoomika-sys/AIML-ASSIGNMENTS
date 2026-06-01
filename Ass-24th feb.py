###Assignment Name : Dataset Detective

###Load a dataset, display top rows, find highest value column, count missing values, share 5 insights.


import pandas as pd

# Load dataset (example CSV file)
df = pd.read_csv(r"C:\Users\DELL\Downloads\admission.csv" )

# 1. Display top rows
print("Top 5 Rows:")
print(df.head())

# 2. Find highest value in each column
print("\nHighest Value in Each Column:")
print(df.max(numeric_only=True))

# 3. Column with the overall highest value 
highest_column = df.max(numeric_only=True).idxmax()
print("\nColumn with Highest Value:", highest_column)

# 4. Count missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# 5. Basic dataset info
print("\nDataset Info:")
print(df.info())

