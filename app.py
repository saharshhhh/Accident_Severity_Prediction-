import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('gb_model.pkl')

# Set up Streamlit page config
st.set_page_config(page_title="Accident Severity Prediction", layout="wide")

# Custom styling
st.markdown("""
    <style>
        .main { background-color: #f4f4f4; }
        h1 { color: #1E88E5; text-align: center; }
        div.stButton > button { background-color: #1E88E5; color: white; font-size: 18px; padding: 10px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar with instructions
st.sidebar.header("ℹ️ How to Use This App")
st.sidebar.write("""
1. Enter the accident details in the fields provided.  
2. Click **Predict Severity** to get the result.  
3. The model will predict severity based on the inputs.
""")

# Title
st.title("🚦 Accident Severity Prediction")

# Use columns for a better layout
col1, col2 = st.columns(2)

# Left column inputs
with col1:
    st.subheader("📍 Location Details")
    start_lat = st.number_input("🌍 Start Latitude", format="%.6f")
    start_lng = st.number_input("🌍 Start Longitude", format="%.6f")
    distance = st.slider("📏 Distance (mi)", 0.0, 50.0, 1.0)

    st.subheader("🌦️ Weather Conditions")
    temperature = st.slider("🌡️ Temperature (°F)", -30, 120, 70)
    humidity = st.slider("💧 Humidity (%)", 0, 100, 50)
    visibility = st.slider("👀 Visibility (mi)", 0.0, 10.0, 5.0)
    wind_speed = st.slider("💨 Wind Speed (mph)", 0.0, 50.0, 10.0)

# Right column inputs
with col2:
    st.subheader("🚧 Road & Traffic Conditions")
    precipitation = st.slider("🌧️ Precipitation (in)", 0.0, 5.0, 0.0)
    traffic_signal = st.radio("🚦 Traffic Signal", ["No", "Yes"])
    junction = st.radio("🔀 Junction", ["No", "Yes"])
    railway = st.radio("🚂 Railway", ["No", "Yes"])
    nautical_twilight = st.radio("🌙 Nautical Twilight", ["No", "Yes"])

# Convert categorical inputs
traffic_signal = 1 if traffic_signal == "Yes" else 0
junction = 1 if junction == "Yes" else 0
railway = 1 if railway == "Yes" else 0
nautical_twilight = 1 if nautical_twilight == "Yes" else 0

# Create a DataFrame for input data
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

# Predict severity
if st.button("🔮 Predict Severity"):
    prediction = model.predict(input_data)
    severity_levels = {
        0: "🟢 Low Severity",
        1: "🟡 Moderate Severity",
        2: "🔴 High Severity"
    }
    st.success(f"Predicted Severity: {severity_levels.get(prediction[0], 'Unknown')}")
