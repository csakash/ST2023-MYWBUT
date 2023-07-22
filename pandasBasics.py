import pandas as pd

data = {
    "apple": [4, 6, 2, 8],
    "banana": [5, 2, 8, 5]
}

index = ["Anuska", "Aditya", "Rahul", "Tanmoy"]
df = pd.DataFrame(data, index=index)
print(df, type(df))

print(df.loc['Rahul'])