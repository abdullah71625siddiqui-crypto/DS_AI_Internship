# Task 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
df=pd.read_csv("Housing.csv")
plt.figure()
sns.histplot(x=df["price"],kde=True)
plt.title("Price Histogram")
plt.show()

print("Skewnwess:",df["price"].skew())
print("Kurtosis:",df["price"].kurt())
sns.countplot(x="furnishingstatus",data=df)
plt.show()


# Task 2
sns.scatterplot(x="area",y="price",data=df)
plt.show()

sns.boxplot(x=df["furnishingstatus"],y=df["price"])
plt.show()
plt.title("furnishingstatus X price")
plt.show()


# Task 3
corr=df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, annot=True)
plt.title("Heatmap")
plt.show()

sns.boxplot(x=df["price"])
plt.title("Outliers in price")
plt.show()
