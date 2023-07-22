import pandas as pd
import numpy as np

df = pd.read_csv("./kohli.csv")

# # print(df.columns)

# print(df.head(10))

# # print(df.info())

# # print(df.shape)

# # print(df.describe())

# runs_col = df["Runs"]
# print(runs_col)

# cols = df[["Runs", "4s", "6s", "BF"]]
# print(cols)

# print(df.iloc[50:59])

# Find out the matches he played against austrailia
aus_df = df[df["SR"] >= 70]
print(aus_df)
print(aus_df.describe())

def find_centuries(x):
    if x >= 100:
        return "OG"
    else:
        return "NOOB"
    
df["centuries"] = df["Runs"].apply(find_centuries)
print(df)