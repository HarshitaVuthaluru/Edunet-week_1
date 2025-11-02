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
