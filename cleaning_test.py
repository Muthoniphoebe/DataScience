import pandas as pd
pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')
print(df)
new_df = df.dropna()

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.info())

print(df.duplicated())

df.drop_duplicates(inplace = True)
print(df.duplicated())
