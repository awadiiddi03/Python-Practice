import pandas as pd

# Load a manually downloaded CSV file
file_path = "airbnb_ct_listings.csv"
print(file_path)

df = pd.read_csv(file_path)

# Show the raw column names (usually messy)
print(df.columns)


# Display the first few rows
print(df.head())


# Display the last few rows
print(df.tail())



#Display rows 10 - 30
print(df[10:31])




