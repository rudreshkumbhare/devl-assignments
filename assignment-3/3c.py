import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

path = kagglehub.dataset_download("syedfaizanalii/car-price-dataset-cleaned")
df=pd.read_csv(f"{path}/Car_price_cleaned.csv")

print(df.info())
print(df.describe())
print(df.head())

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(df["highwaympg_squared"], bins=10, kde=True, ax=axes[0])
axes[0].set_title("Distribution of highwaympg_squared")
sns.histplot(df["drivewheel"], bins=10, kde=True, ax=axes[1])
axes[1].set_title("Distribution of drivewheel")
sns.histplot(df["citympg_squared"], bins=10, kde=True, ax=axes[2])
axes[2].set_title("Distribution of citympg_squared")
plt.tight_layout()
plt.show()

print("Mean:", df["horsepower_squared"].mean())
print("Median:", df["horsepower_squared"].median())
print("Mode:", df["horsepower_squared"].mode()[0])
print("Variance:", df["horsepower_squared"].var())
print("Std Dev:", df["horsepower_squared"].std())

sns.boxplot(x=df["compressionratio_squared"])
plt.title("Box plot of compressionratio_squared")
plt.show()

plt.scatter(df["car_ID"], df["citympg_squared"], alpha=0.7, marker="o")
plt.xlabel("car_ID")
plt.ylabel("citympg_squared")
plt.title("Scatter plot: citympg_squared vs car_ID")
plt.show()

new_df = df.head(3)
numeric_df = new_df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(24, 18))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Heatmap (First 3 Rows)")
plt.tight_layout()
plt.show()

print(
    "Correlation between log_enginesize and enginesize_squared:",
    df["log_enginesize"].corr(df["enginesize_squared"]),
)
print(
    "Correlation between log_enginesize and car_ID:",
    df["log_enginesize"].corr(df["car_ID"]),
)

sns.boxplot(
    data=df.iloc[:25],
    x="symboling",
    y="compressionratio_squared",
    hue="fueltype",
)
plt.title(
    "Boxplot: compressionratio_squared by Symboling and Fuel Type (First 25"
    " Cars)"
)
plt.show()

df["drivewheel"].value_counts().plot.pie(
    autopct="%1.1f%%", labels=df["drivewheel"].unique()
)
plt.title("Drive Wheel Distribution")
plt.ylabel("")
plt.show()

plt.figure(figsize=(10, 5))
sns.violinplot(data=df.tail(50), x='enginesize_squared', y='price')
plt.xticks(rotation=45)
plt.title("Violin Plot: Price vs enginesize_squared (Binned)")
plt.show()
