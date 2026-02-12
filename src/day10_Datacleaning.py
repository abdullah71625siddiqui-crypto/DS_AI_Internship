# Task 1
import pandas as pd
df= pd.read_csv("customer_orderst.csv")
print(df.shape)
print(df.isna().sum())
df=df.drop_duplicates()

df["Name"]=df["Name"].fillna("Unknown")
df["Price"]=df["Price"].fillna(df["Price"].median())
df["Payment"]=df["Payment"].fillna(df["Payment"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])
df["Cust_ID"]=df["Cust_ID"].fillna(0)

print(df)
print(df.shape)


# Task 2
data=pd.read_csv("customer.csv")
print(data.dtypes)

data["Price"]=data["Price"].str.replace("$",'')
data["Price"]=data["Price"].str.replace(",",'')
print(data)
print(data["Price"].astype(float))
pd.to_datetime(data["Date"])


# Task 3
d=pd.read_csv("customer.csv")
d["Location"]=d["Location"].str.strip()
d["Location"]=d["Location"].str.lower()
unique= d["Location"].unique()
print(unique)
