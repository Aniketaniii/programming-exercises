#train_model.py

import pandas as pd

import joblib

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier


#reading dataset

df=pd.read_csv("fraud.csv")


#input

x=df.drop("Fraud",axis=1)


#output

y=df["Fraud"]


#splitting data

x_train,x_test,y_train,y_test=train_test_split(
x,y,
test_size=0.2,
random_state=42
)


#creating model

model=RandomForestClassifier()

model.fit(x_train,y_train)


#saving model

joblib.dump(model,"fraud_model.pkl")


print("Model Saved Successfully")