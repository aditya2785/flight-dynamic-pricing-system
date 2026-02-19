✈️ Flight Dynamic Pricing System

An end-to-end Machine Learning system that predicts airline ticket prices and simulates revenue optimization through an interactive web dashboard.

🚀 What It Does
Predicts flight ticket prices using XGBoost
Applies dynamic price adjustment logic
Simulates revenue impact
Exposes a Flask REST API
Provides a clean interactive dashboard

🧠 ML Model
XGBoost Regressor
Feature engineering & encoding
StandardScaler preprocessing
Hyperparameter tuning (Optuna)
Evaluated using RMSE & R²
Key Features Used:
Flight duration
Days before departure
Departure & arrival time
Stop type
Travel date popularity

💰 Optimization Logic
After predicting ticket price, the system simulates revenue impact:

             Revenue=Price×Demand(simulated)
Displays:
Predicted price
Revenue before adjustment
Revenue after adjustment
% Improvement

🏗️ Tech Stack
Python • Pandas • NumPy • Scikit-learn • XGBoost • Optuna • Flask • HTML/CSS

📂 Project Structure
src/            # Core ML logic
templates/      # Dashboard UI
app.py          # API
train.py        # Model training
optimizer.py    # Revenue logic

▶️ Run Locally
pip install -r requirements.txt
python -m src.train
python app.py

Open:
http://127.0.0.1:5000/dashboard
