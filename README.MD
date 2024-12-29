# Predict Tomorrow's Temperature Using Machine Learning

Welcome to my very simple prediction app! This project is designed to predict tomorrow's high and low temperatures using L2 regularization (also known as Ridge Regression). The app is built using Python and Flask, providing an easy-to-use web interface for temperature prediction.

[Link to App](https://temperature-prediction-with-ridge.onrender.com) 

[Link to Analysis](https://github.com/AveryNewkirk/Temperature_Prediction_With_Ridge_Regression/blob/main/CD_Weather_Cleaning_and_Analysis.ipynb)

## Features
- **Predict Tomorrow's Temperature**: Input today's weather details and get predictions for tomorrow's high and low temperatures.
- **Historical Data**: Uses historical weather data from Charlotte Douglass International airport going back to 1970.
- **Machine Learning**: Employs Ridge Regression to provide accurate predictions.

## To get started (for now)
### 1.  Clone the repository and navigate to the directory
```
git clone https://github.com/AveryNewkirk/Temperature_Prediction_With_Ridge_Regression.git
cd Temperature_Prediction_With_Ridge_Regression
```
### 2. Create and Activate a Virtual Enviornment
```
python -m venv venv
source venv/Scripts/activate # on linux or max venv/bin/activate
```
### 3. Install the dependncies
```
pip install -r requirements.txt
```

### 4. Run the app and play around with it
```
flask --debug run
```



