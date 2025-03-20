import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
model = joblib.load('rf_model.pkl')
st.title("Accident Severity Prediction")
start_lat = st.number_input("Start Latitude")
start_lng = st.number_input("Start Longitude")
distance = st.number_input("Distance (mi)")
temperature = st.number_input("Temperature (F)")
humidity = st.number_input("Humidity (%)")
visibility = st.number_input("Visibility (mi)")
wind_speed = st.number_input("Wind Speed (mph)")
precipitation = st.number_input("Precipitation (in)")
traffic_signal = st.selectbox("Traffic Signal", [0, 1])
junction = st.selectbox("Junction", [0, 1])
railway = st.selectbox("Railway", [0, 1])
nautical_twilight = st.selectbox("Nautical Twilight", [0, 1])
input_data = pd.DataFrame({
    'Start_Lat': [start_lat],
    'Start_Lng': [start_lng],
    'Distance(mi)': [distance],
    'Temperature(F)': [temperature],
    'Humidity(%)': [humidity],
    'Visibility(mi)': [visibility],
    'Wind_Speed(mph)': [wind_speed],
    'Precipitation(in)': [precipitation],
    'Traffic_Signal': [traffic_signal],
    'Junction': [junction],
    'Railway': [railway],
    'Nautical_Twilight': [nautical_twilight]
})
if st.button("Predict Severity"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Severity: {prediction[0]}")