 🌿 Air Quality Prediction (Sustainability Project)

Description
This project predicts Air Quality Index (AQI) categories based on pollutant levels such as PM2.5, PM10, NO₂, SO₂, CO, and O₃.  
It supports sustainability by helping monitor and forecast pollution levels.

Model
- Algorithm: Random Forest Classifier
- Dataset: Air Quality Data in India (Kaggle)
- Evaluation: Accuracy, Precision, Recall, F1-score
- Saved Model: `air_quality_classifier.pkl`

Streamlit UI
A simple user interface where users enter pollutant levels and view:
- Predicted AQI category  
- Bar chart visualization of pollutant contributions  

 Tools Used
- Python
- Pandas, NumPy, scikit-learn
- Matplotlib
- Streamlit

How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

Perfect, Harshita 🌿 — here’s your **Week 2 `README.md`** file, fully written for your GitHub repository (you can replace your current one or add below the Week 1 section).

 🌿 Air Quality Prediction – Week 2 (Sustainability Project)

Overview

In Week 2, the project was enhanced by improving the machine learning model’s performance and adding advanced data visualizations.
The model predicts Air Quality Index (AQI) categories using environmental parameters — **PM2.5, PM10, NO₂, SO₂, CO, and O₃** — supporting the goal of sustainable urban planning and pollution awareness.

Week 2 Improvements

| Area                   | Description                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Model Optimization     | Applied **GridSearchCV** to perform hyperparameter tuning of Random Forest Classifier, improving model accuracy and robustness.    |
| Model Saving           | Compressed and saved as `air_quality_classifier_week2.pkl` for efficient use in the Streamlit app.                                 |
| Data Visualization     | Added city-wise PM2.5 comparison chart and pollutant trend line graph for any selected city.                                       |
| Enhanced UI            | Updated Streamlit interface with **tabs** — one for prediction and another for visualizations — and sidebar inputs for pollutants. |
| Evaluation Metrics     | Checked accuracy, classification report, and confusion matrix for detailed model performance.                                      |

Features

* Predicts AQI category (Good / Moderate / Poor / Severe etc.)
* Displays color-coded pollutant bar chart
* Shows **Top 10 cities** with highest average PM2.5 levels
* Plots **trend graph** for pollutants (PM2.5 & PM10) of any selected city
* User-friendly and visually clean Streamlit UI

Tech Stack

* Python 3
* Libraries: Pandas • NumPy • Scikit-Learn • Matplotlib • Seaborn • Streamlit • Joblib
* Tools: Google Colab (for model training) • VS Code (for UI development)

Results

* Improved accuracy after hyperparameter tuning
* Detailed visualization of pollutant levels across cities
* Interactive web interface allowing real-time predictions

How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Make sure the following files are in the same folder:

```
app.py
air_quality_classifier_week2.pkl
city_day.csv
requirements.txt
```
Repository Structure

```
AI-ML-Sustainability-Week2/
│
├── app.py
├── air_quality_classifier_week2.pkl
├── city_day.csv
├── requirements.txt
├── README.md
└── screenshots/
    ├── ui.png
    ├── graph.png
```
Outputs

* Prediction Tab: Predicts AQI and displays pollutant bar chart
* Visualization Tab: Shows Top 10 cities by PM2.5 and city-specific pollutant trends



