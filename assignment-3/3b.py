import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")


print(df.head())


sns.scatterplot(data=df, x="sepal_length", y="sepal_width")
plt.title("Sepal Length vs Sepal Width")
plt.show()


sns.lineplot(data=df, x="petal_length", y="petal_width")
plt.title("Petal Length vs Petal Width")
plt.show()


sns.histplot(data=df, x="petal_length")
plt.title("Petal Length Distribution")
plt.show()


sns.barplot(data=df, x="species", y="petal_length")
plt.title("Average Petal Length by Species")
plt.show()


sns.boxplot(data=df, x="species", y="petal_length")
plt.title("Petal Length by Species")
plt.show()


sns.scatterplot(data=df, x="petal_length", y="petal_width")
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.title("Petal Length vs Petal Width")
plt.show()


sns.pairplot(df)
plt.show()


g = sns.FacetGrid(df, col="species")
g.map(sns.scatterplot, "petal_length", "petal_width")
plt.show()


plt.scatter(df["petal_length"], df["petal_width"])
plt.title("Petal Length vs Petal Width")
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.show()


plt.hist(df["petal_length"])
plt.title("Petal Length Distribution")
plt.xlabel("petal_length")
plt.ylabel("Frequency")
plt.show()


avg_petal_length = df.groupby("species")["petal_length"].mean()

plt.bar(
    avg_petal_length.index,
    avg_petal_length.values
)
plt.title("Average Petal Length by Species")
plt.xlabel("species")
plt.ylabel("Average Petal Length")
plt.show()


plt.boxplot(
    [df[df["species"] == species]["petal_length"] for species in df["species"].unique()],
    tick_labels=df["species"].unique()
)
plt.title("Petal Length Distribution by Species")
plt.xlabel("species")
plt.ylabel("petal length")
plt.show()
