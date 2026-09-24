import pandas as pd

df=pd.read_csv("department.csv")
print(df)

print(df["Name"])
print(df.iloc[0:,1:3].to_string())

print()
print(df[df["Name"].str.startswith('A')])
print(df[df.iloc[0:,1:]["Name"].str.startswith('A')])

