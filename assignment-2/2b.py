import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv("/content/synthetic_dataset.csv")  # <-- change the path here wit

print("Raw data")
print(df.head(10))

print("\nReplace Empty Set")
mean_filling = df["Rating"].fillna(df["Rating"].mean())
mode_filling = df["Stock"].fillna(df["Stock"].mode().iloc[0])
median_filling = df["Discount"].fillna(df["Discount"].median())
df["Rating"] = mean_filling
df["Stock"] = mode_filling
df["Discount"] = median_filling

median_filling = df["Price"].fillna(df["Price"].median())
mode_filling = df["Category"].fillna(df["Category"].mode().iloc[0])
df["Price"] = median_filling
df["Category"] = mode_filling

print(df.head(10))

print("\nWrong Data")
for x in df.index:
    if df.loc[x, "Discount"] > 30:
        df.loc[x, "Discount"] = 25
print(df.head(10))

print("\nNull Values")
nulls_column = df.isnull().sum()
print(nulls_column)

df.duplicated()
df.drop_duplicates(inplace=True)

print("\nInterquartile Range (IQR)")
print(df.describe())

Q1 = df.Price.quantile(0.25)
Q3 = df.Price.quantile(0.75)
IQR = Q3 - Q1
print("IQR :", IQR)
lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

print("Lower Limit :", lower_limit)
print("Upper Limit :", upper_limit)

print("\nLabel Encoder")
le = LabelEncoder()
df["Category"] = le.fit_transform(df["Category"])
print(df.head())

print("\nOne Hot Encoder")
one = OneHotEncoder(sparse_output=False)
Stock = ["In Stock", "Stock"]
df["Stock"] = one.fit_transform(df[["Stock"]])
print(df.head())
