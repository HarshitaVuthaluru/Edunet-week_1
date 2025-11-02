import streamlit as st
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Title
st.title("🌿 Air Quality Prediction App")
st.write("Enter pollutant levels to predict Air Quality Category")

# Input fields
pm25 = st.number_input("PM2.5", min_value=0.0, max_value=1000.0, value=50.0)
pm10 = st.number_input("PM10", min_value=0.0, max_value=1000.0, value=80.0)
no2 = st.number_input("NO2", min_value=0.0, max_value=500.0, value=25.0)
so2 = st.number_input("SO2", min_value=0.0, max_value=500.0, value=15.0)
co = st.number_input("CO", min_value=0.0, max_value=10.0, value=1.0)
o3 = st.number_input("O3", min_value=0.0, max_value=500.0, value=30.0)

# Load trained model (make sure to have your .pkl file)
try:
    with open("air_quality_classifier.pkl", "rb") as file:
        model = pickle.load(file)
except:
    st.warning("⚠️ Model file not found! Please train and save it first.")

# Predict button
if st.button("🌤️ Predict AQI Category"):
    data = np.array([[pm25, pm10, no2, so2, co, o3]])
    prediction = model.predict(data)[0]
    categories = ['Good', 'Moderate', 'Poor', 'Very Poor', 'Severe']

    # Show prediction result
    if prediction < len(categories):
        st.success(f"✅ Predicted Air Quality: **{categories[prediction]}**")
    else:
        st.error("Unexpected output. Please check the model.")

    # --- Bar Chart for Pollutant Contribution ---
    import matplotlib.pyplot as plt

    st.subheader("📊 Pollutant Contribution Visualization")

    pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    values = [pm25, pm10, no2, so2, co, o3]

    fig, ax = plt.subplots()
    bars = ax.bar(pollutants, values)
    ax.set_xlabel("Pollutants")
    ax.set_ylabel("Concentration (µg/m³)")
    ax.set_title("Pollutant Levels Entered")

    # Color bars based on concentration level
    for bar, val in zip(bars, values):
        if val < 50:
            bar.set_color('green')
        elif val < 100:
            bar.set_color('orange')
        else:
            bar.set_color('red')

    st.pyplot(fig)

