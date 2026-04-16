import pandas as pd

df = pd.read_csv("dirty_cafe_sales.csv")

#Identify Duplicates
df.duplicated()

#Remove Duplicates
df = df.drop_duplicates()

# convert numeric columns first

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['PricePerUnit'] = pd.to_numeric(df['PricePerUnit'], errors='coerce')
df['TotalSpent'] = pd.to_numeric(df['TotalSpent'], errors='coerce')

# fix TotalSpent, PricePreUnit and Quantity before removing the rows
mask = df['TotalSpent'].isna()
df.loc[mask, 'TotalSpent'] = df['Quantity'] * df['PricePerUnit']

mask = df['PricePerUnit'].isna()
df.loc[mask, 'PricePerUnit'] = df['TotalSpent'] / df['Quantity']

mask = df['Quantity'].isna()
df.loc[mask, 'Quantity'] = df['TotalSpent'] / df['PricePerUnit']

df = df[~df.isin(["UNKNOWN","ERROR"]).any(axis=1)]

print(df.to_string())

df.to_csv("clean_cafe_sales.csv", index=False)