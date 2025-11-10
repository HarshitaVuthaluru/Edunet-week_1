import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Air Quality Prediction 🌿", page_icon="🌤️", layout="wide")

# ---------- TITLE ----------
st.title("🌿 Air Quality Prediction – Week 2")
st.markdown("### Enhanced Model + Interactive Visualizations")

# ---------- LOAD MODEL ----------
try:
    model = joblib.load("air_quality_classifier_week2.pkl")
    st.success("✅ Improved model loaded successfully!")
except:
    st.warning("⚠️ Model not found. Please upload `air_quality_classifier_week2.pkl`.")

# ---------- SIDEBAR INPUT ----------
st.sidebar.header("🔢 Input Pollutant Values")
pm25 = st.sidebar.number_input("PM2.5 (µg/m³)", 0.0, 1000.0, 60.0)
pm10 = st.sidebar.number_input("PM10 (µg/m³)", 0.0, 1000.0, 90.0)
no2 = st.sidebar.number_input("NO₂ (µg/m³)", 0.0, 500.0, 25.0)
so2 = st.sidebar.number_input("SO₂ (µg/m³)", 0.0, 500.0, 15.0)
co = st.sidebar.number_input("CO (mg/m³)", 0.0, 10.0, 1.0)
o3 = st.sidebar.number_input("O₃ (µg/m³)", 0.0, 500.0, 30.0)

# ---------- TABS ----------
tab1, tab2 = st.tabs(["🔮 Prediction", "📊 Visualizations"])

# =====================================================
# TAB 1 – PREDICTION
# =====================================================
with tab1:
    st.subheader("Predict Air Quality Category")
    if st.button("🌤️ Predict AQI"):
        data = np.array([[pm25, pm10, no2, so2, co, o3]])
        prediction = model.predict(data)[0]
        categories = ['Good', 'Moderate', 'Poor', 'Satisfactory', 'Severe', 'Very Poor']

        if prediction < len(categories):
            st.success(f"Predicted AQI Category: **{categories[prediction]}**")
        else:
            st.error("Unexpected output – check model.")

        # --- Bar Graph for pollutant levels ---
        pollutants = ['PM2.5', 'PM10', 'NO₂', 'SO₂', 'CO', 'O₃']
        values = [pm25, pm10, no2, so2, co, o3]

        fig, ax = plt.subplots()
        bars = ax.bar(pollutants, values)
        for bar, val in zip(bars, values):
            if val < 50: bar.set_color('green')
            elif val < 100: bar.set_color('orange')
            else: bar.set_color('red')
        ax.set_ylabel("Concentration (µg/m³)")
        ax.set_title("Pollutant Contribution")
        st.pyplot(fig)

# =====================================================
# TAB 2 – VISUALIZATIONS
# =====================================================
with tab2:
    st.subheader("City-wise & Trend Visualizations")

    # Load dataset
    try:
        df = pd.read_csv("city_day.csv")
        df = df[['City', 'PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'AQI']]
        df.dropna(inplace=True)

        # --- Top 10 Cities by Average PM2.5 ---
        city_avg = df.groupby('City')['PM2.5'].mean().sort_values(ascending=False).head(10)
        st.write("### 🌆 Top 10 Cities by Average PM2.5 Levels")
        fig1, ax1 = plt.subplots(figsize=(8,4))
        sns.barplot(x=city_avg.index, y=city_avg.values, palette='viridis', ax=ax1)
        ax1.set_ylabel("Average PM2.5")
        ax1.set_xlabel("City")
        ax1.set_title("Top 10 Cities by Pollution Level")
        plt.xticks(rotation=45)
        st.pyplot(fig1)

        # --- Trend Plot for Selected City ---
        city_list = df['City'].unique()
        city_name = st.selectbox("Select a City for Trend Plot", city_list)
        city_data = df[df['City'] == city_name].head(100)  # limit for speed

        fig2, ax2 = plt.subplots(figsize=(8,4))
        ax2.plot(city_data.index, city_data['PM2.5'], color='crimson', label='PM2.5')
        ax2.plot(city_data.index, city_data['PM10'], color='orange', label='PM10')
        ax2.legend()
        ax2.set_title(f"Pollutant Trend – {city_name}")
        ax2.set_xlabel("Days")
        ax2.set_ylabel("Concentration (µg/m³)")
        st.pyplot(fig2)

    except FileNotFoundError:
        st.error("Dataset file 'city_day.csv' not found. Please upload it to your folder.")
