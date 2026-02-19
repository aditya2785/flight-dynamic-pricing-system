from flask import Flask, request, jsonify
import joblib
import numpy as np

from flask import render_template

from src.optimizer import optimize_prices

app = Flask(__name__)

# Load model and scaler
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flight Dynamic Pricing API is running 🚀"})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        if "features" not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400

        features = np.array(data["features"]).reshape(1, -1)

        features = scaler.transform(features)
        predicted_price = model.predict(features)[0]

        optimization_result = optimize_prices(
            np.array([predicted_price])
        )

        return jsonify({
            "predicted_price": float(predicted_price),
            "optimization": optimization_result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
