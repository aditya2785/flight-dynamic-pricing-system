✈️ Flight Dynamic Pricing Optimization System
📌 Overview

This project is an end-to-end Airline Dynamic Pricing Simulation System that predicts ticket prices using machine learning and applies revenue optimization logic through an interactive web dashboard.

The system includes:

Data preprocessing & feature engineering pipeline

XGBoost regression model

Revenue optimization engine

Flask REST API

Interactive frontend dashboard

Modular, production-style project structure

🚀 Problem Statement

Airline ticket prices vary dynamically based on:

Days before departure

Flight duration

Time of departure & arrival

Stop type

Travel date popularity

The goal of this system is to:

Predict flight ticket prices based on booking characteristics and simulate revenue impact through dynamic pricing adjustments.

🧠 Machine Learning Approach
Model

XGBoost Regressor

Hyperparameter tuning with Optuna

StandardScaler for feature normalization

Evaluation using:

RMSE

R² Score

Feature Engineering

Final model features:

Flight Duration

Days Before Flight

Journey Day

Arrival Category (Before/After 7 PM)

Departure Hour

Arrival Hour

Stops (1-stop encoded)

Stops (Non-stop encoded)

Day Popularity (Frequency Encoding)

💰 Revenue Optimization Logic

After predicting ticket price, the system simulates a dynamic price adjustment:


Revenue=∑Price

A pricing multiplier is applied to simulate revenue improvement:
Improvement%=
Revenue
before
	​

Revenue
after

This demonstrates how small price adjustments can impact overall revenue.

🏗️ Project Structure
Dynamic-Pricing-System/
│
├── data/                # Raw dataset
├── models/              # Saved model artifacts (not pushed to GitHub)
├── notebooks/           # EDA & experimentation
├── src/                 # Core logic
│   ├── data_gen.py
│   ├── train.py
│   ├── optimizer.py
│
├── templates/           # Frontend dashboard
│   └── index.html
│
├── app.py               # Flask API
├── requirements.txt
├── Dockerfile
└── README.md

🌐 Dashboard Features

The interactive dashboard allows users to:

Enter flight parameters

Select stop type

Adjust booking timing

Predict ticket price

View revenue before and after optimization

The dashboard is styled for a clean, SaaS-like presentation.

🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

XGBoost

Optuna

Flask

HTML/CSS (Frontend)

📊 Example Workflow

User enters flight parameters

Data is scaled using trained StandardScaler

Model predicts ticket price

Optimization logic simulates revenue adjustment

Results displayed in dashboard

▶️ How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/yourusername/flight-dynamic-pricing-system.git
cd flight-dynamic-pricing-system

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train Model
python -m src.train

4️⃣ Run Application
python app.py


Open in browser:

http://127.0.0.1:5000/dashboard
