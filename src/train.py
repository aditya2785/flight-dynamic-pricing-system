import joblib
import numpy as np
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

from src.data_gen import preprocess_pipeline


def train_model(data_path):

    df = preprocess_pipeline(data_path)

    X = df.drop('Price', axis=1)
    y = df['Price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = xgb.XGBRegressor(
        learning_rate=0.06,
        max_depth=7,
        subsample=0.77,
        colsample_bytree=0.76,
        min_child_weight=1
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    print("RMSE:", rmse)
    print("R2:", r2)

    joblib.dump(model, "models/model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")

    return model
if __name__ == "__main__":
    train_model("data/flight_data.csv")
