#app.py


import streamlit as st

import joblib

import pandas as pd


#loading model

model=joblib.load("fraud_model.pkl")


#website title

st.title("Fraud Detection System")


st.write("Predict whether transaction is fraud or not")


#taking inputs

amount=st.number_input("Transaction Amount")

time=st.number_input("Transaction Time")

transactions=st.number_input("Number of Transactions")


#prediction button

if st.button("Predict"):


    data=[[amount,time,transactions]]

    prediction=model.predict(data)


    if prediction[0]==1:

        st.error("Fraud Transaction Detected")

    else:

        st.success("Normal Transaction")
