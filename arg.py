import pandas as pd
df=pd.read_csv("cars.csv",index_col="Brand")
# print(df)

# print(df.loc["Chevrolet"]
print(df.loc["Honda"])


# print(df.count(numeric_only=True))
# print()

# print(df.mean(numeric_only=True))
# print()

# print(df.sum(numeric_only=True))
# print()

# print(df.min(numeric_only=True))
# print()

# print(df.max(numeric_only=True))
# print()

# print(df["Transmission"].sum())


# b=df.groupby("Model")
# print(b["Engine "].sum())