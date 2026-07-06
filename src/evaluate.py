import joblib
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class ModelEvaluation:
    def __init__(self):
        self.model_path = "models/best_model.pkl"
        self.feature_path = "data/features"

    def evaluate_model(self):
        # Load model
        model = joblib.load(self.model_path)

        # Load test data
        X_test = pd.read_csv(f"{self.feature_path}/X_test.csv")
        y_test = pd.read_csv(f"{self.feature_path}/y_test.csv").squeeze()

        # Prediction
        y_pred = model.predict(X_test)

        # Metrics
        mae = mean_absolute_error(y_test, y_pred)
        rmse = mean_squared_error(y_test, y_pred) ** 0.5
        r2 = r2_score(y_test, y_pred)

        print("=" * 60)
        print("Model Evaluation")
        print("=" * 60)
        print(f"Mean Absolute Error : {mae:,.2f}")
        print(f"Root Mean Squared Error : {rmse:,.2f}")
        print(f"R² Score : {r2:.4f}")
        print("=" * 60)


if __name__ == "__main__":
    evaluator = ModelEvaluation()
    evaluator.evaluate_model()