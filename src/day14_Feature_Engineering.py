# Task !
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures,OneHotEncoder
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data={
      'Name':["A","B","C","D","E","F"],
      'Transmission':['Automatic','Automatic','Manual','Manual','Manual','Automatic'],
      'Color':['Red','Blue','Red','Green','Blue','Green']
      }
df=pd.DataFrame(data)
le=LabelEncoder()
df["Transmission"]=le.fit_transform(df["Transmission"])
df= pd.get_dummies(df,columns=["Color"],drop_first=True)


# Task 2
d = {
        "Age":[35,29,26,33,39,25,30],
        "Salary":[30000,25000,27000,30000,35000,25000,33000]
        }
d2=pd.DataFrame(d)
plt.subplot(1, 2, 1)
plt.hist(x=d2["Age"])
plt.title("Age histograam")
plt.show()
plt.subplot(1, 2, 2)
plt.hist(x=d2["Salary"])
plt.title("Salary histogram")
plt.tight_layout()
plt.show()

scaler1 = StandardScaler()
scaled_features = scaler1.fit_transform(d2[['Age', 'Salary']])

plt.hist(x=scaled_features)
plt.title("Standard Scaled histograam")
plt.show()

scaler2 = MinMaxScaler()
d2[['Age', 'Salary']] = scaler2.fit_transform(d2[['Age', 'Salary']])
print("Scaled DataFrame (Min-Max Scaling):")
print(d2)

plt.subplot(1, 2, 1)
plt.hist(x=d2["Age"])
plt.title("Min max Age histogram")
plt.show()
plt.subplot(1, 2, 2)
plt.hist(x=d2["Salary"])
plt.title("Min max Salary histogram")
plt.tight_layout()
plt.show()


#Task 3

df=pd.read_csv("gdp.csv")
X_train,X_test,y_train,y_test = train_test_split(df[['Year']],df[['Value']],test_size=0.2,random_state=42)


model=LinearRegression()
model.fit(X_train,y_train)
baseline_pred=model.predict(X_test)
baseline_score=r2_score(y_test, baseline_pred)

print(baseline_score)


poly=PolynomialFeatures(degree=2,include_bias=False)

X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)

poly_model=LinearRegression()
poly_model.fit(X_train_poly,y_train)
poly_pred=poly_model.predict(X_test_poly)
poly_score=r2_score(y_test, poly_pred)
print(poly_score)