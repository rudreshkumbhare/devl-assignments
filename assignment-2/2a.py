import pandas as pd
import altair as alt

column_names = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

df = pd.read_csv("iris.data", names=column_names)   # <-- change the path here with your own file path

print("Complete DataFrame")
print(df.to_string())

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nDataFrame Information")
print(df.info())

print("\nShape of DataFrame")
print(df.shape)

print("\nStatistical Summary")
print(df.describe())

print("\nUnique Species")
print(df["species"].unique())

print("\nSpecies Count")
print(df["species"].value_counts())

# Access row using iloc
print("\nRow at Index 10")
print(df.iloc[10])

# Access specific value
print("\nValue at Row 0, Column 2")
print(df.iloc[0, 2])

# Access using loc
print("\nRow using loc")
print(df.loc[0])

# Remove missing values
df = df.dropna()

print("\nAverage Measurements by Species")
summary_by_group = df.groupby("species").mean()
print(summary_by_group)

df.to_csv("iris_cleaned.csv", index=False)
summary_by_group.to_json("summary.json")

print("\nFiles Saved Successfully!")
