import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Air Quality Prediction – Final Week", page_icon="🌿", layout="wide")

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------
st.title("🌿 Final Week – Air Quality Prediction Dashboard")
st.markdown("### ✔️ Enhanced Model | ✔️ Analytics | ✔️ Visual Insights | ✔️ Feature Importance")

# -------------------------------------------------------
# LOAD MODEL
# -------------------------------------------------------
try:
    model = joblib.load("air_quality_classifier_week3.pkl")
    st.success("✅ Final Week Model Loaded Successfully!")
except:
    st.warning("⚠️ Week-3 Model Not Found. Please upload `air_quality_classifier_week3.pkl`.")

# -------------------------------------------------------
# SIDEBAR INPUT
# -------------------------------------------------------
st.sidebar.header("🔢 Enter Pollutant Levels")

inputs = {
    "PM2.5": st.sidebar.number_input("PM2.5 (µg/m³)", 0.0, 1000.0, 60.0),
    "PM10": st.sidebar.number_input("PM10 (µg/m³)", 0.0, 1000.0, 90.0),
    "NO2": st.sidebar.number_input("NO₂ (µg/m³)", 0.0, 500.0, 25.0),
    "SO2": st.sidebar.number_input("SO₂ (µg/m³)", 0.0, 500.0, 15.0),
    "CO": st.sidebar.number_input("CO (mg/m³)", 0.0, 10.0, 1.0),
    "O3": st.sidebar.number_input("O₃ (µg/m³)", 0.0, 500.0, 30.0)
}

feature_values = np.array([[v for v in inputs.values()]])

# -------------------------------------------------------
# TABS
# -------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🔮 Prediction",
    "📊 Visualizations",
    "🔥 Feature Importance",
    "📥 Download Reports"
])

# -------------------------------------------------------
# TAB 1 – Prediction
# -------------------------------------------------------
with tab1:
    st.subheader("🌤️ Air Quality Prediction")

    if st.button("Predict AQI Category"):
        prediction = model.predict(feature_values)[0]

        labels = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']

        if prediction < len(labels):
            st.success(f"### 🌟 Predicted AQI Category: **{labels[prediction]}**")
        else:
            st.error("Unexpected output from model.")

        # ---------------- BAR CHART ----------------
        st.write("### Pollutant Levels Input Graph")
        fig, ax = plt.subplots()
        ax.bar(inputs.keys(), inputs.values())
        ax.set_ylabel("Concentration")
        plt.xticks(rotation=45)
        st.pyplot(fig)

# -------------------------------------------------------
# TAB 2 – Visualizations
# -------------------------------------------------------
with tab2:
    st.subheader("📊 Dataset Insights")

    try:
        df = pd.read_csv("city_day.csv")
        st.success("Dataset Loaded Successfully!")

        df = df[['City', 'PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'AQI']]
        df.dropna(inplace=True)

        # ---------------- TOP CITY BAR CHART ----------------
        st.write("### 🌆 Top Polluted Cities (Avg PM2.5)")
        city_avg = df.groupby('City')['PM2.5'].mean().sort_values(ascending=False).head(10)

        fig1, ax1 = plt.subplots()
        sns.barplot(x=city_avg.index, y=city_avg.values, palette="viridis", ax=ax1)
        plt.xticks(rotation=45)
        ax1.set_ylabel("Avg PM2.5")
        st.pyplot(fig1)

        # ---------------- TREND PLOT ----------------
        st.write("### 📈 Trend for Selected City")
        city_choice = st.selectbox("Select city:", df['City'].unique())
        city_data = df[df['City'] == city_choice].head(100)

        fig2, ax2 = plt.subplots()
        ax2.plot(city_data['PM2.5'], label="PM2.5")
        ax2.plot(city_data['PM10'], label="PM10")
        ax2.legend()
        ax2.set_title(f"Pollution Trend – {city_choice}")
        st.pyplot(fig2)

    except FileNotFoundError:
        st.error("❌ city_day.csv not found. Upload the dataset.")

# -------------------------------------------------------
# TAB 3 – Feature Importance
# -------------------------------------------------------
with tab3:
    st.subheader("🔥 Feature Importance (From Week-3 Model)")

    try:
        importances = model.feature_importances_
        features = list(inputs.keys())

        fig3, ax3 = plt.subplots()
        sns.barplot(x=features, y=importances, palette="magma", ax=ax3)
        plt.xticks(rotation=45)
        st.pyplot(fig3)

    except:
        st.warning("⚠️ Feature Importance Not Available for Your Model.")

# -------------------------------------------------------
# TAB 4 – Downloads
# -------------------------------------------------------
with tab4:
    st.subheader("📥 Download Data & Reports")

    try:
        st.download_button("Download Clean Dataset CSV", df.to_csv(index=False), "cleaned_dataset.csv")
    except:
        st.info("Upload dataset to enable downloads.")
