import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/titanic.csv")    # <-- change the path here with your own file path


print("Shape of Dataset: ")
print(df.shape)

print("\nFirst 5 Rows: ")
print(df.head())

print("\nLast 5 Rows: ")
print(df.tail())

print("\nSample Entries: ")
print(df.sample(5))


print("\nData Types and Non-Null Values: ")
df.info()


print("\nStatistical Description: ")
print(df.describe())


print("\nDuplicate Values: ")
print(df.duplicated().sum())


print("\nNULL Values: ")
print(df.isnull().sum())


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex")
plt.title("Gender Count")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Pclass")
plt.title("Passenger Class Count")
plt.show()


df["Sex"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

df["Pclass"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Passenger Class Distribution")
plt.ylabel("")
plt.show()


df["Age"].hist()
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


df.boxplot(column="Age")
plt.title("Age Box Plot")
plt.show()
