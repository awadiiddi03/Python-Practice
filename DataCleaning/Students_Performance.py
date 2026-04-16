import numpy as np
import pandas as pd

df = pd.read_csv("Student_Performance.csv")

df.duplicated()

df = df.drop_duplicates()

df['gender'] = df['gender'].str.lower()

df['gender'] = df['gender'].replace({
    "m": "male",
    "female": "female",
    "f": "female",
    "male": "male"
})

df = df.replace("?",np.nan)


df = df[(df['age'] >= 15) & (df['age'] <= 30)]
df = df[df['math_score'] <= 100]


df = df.dropna(subset=['attendance'])
df = df.dropna(subset=['science_score'])
df = df.dropna(subset=['gender'])

df['attendance'] = df['attendance'].replace({"-":0})


print(df)

df.to_csv("clean_Student_Performance.csv", index=False)