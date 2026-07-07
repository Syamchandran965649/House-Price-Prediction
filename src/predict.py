import joblib
import pandas as pd


class HousePricePredictor:

    def __init__(self):
        # Path of the trained model
        self.model_path = "models/best_model.pkl"

    def predict(self):

        # Load the trained model
        model = joblib.load(self.model_path)

        # Sample input data
        # Replace these values with the details of the house
        input_data = pd.DataFrame({

            "property_type": [1],
            "location": [100],
            "city": [2],
            "province_name": [1],
            "latitude": [33.6844],
            "longitude": [73.0479],
            "baths": [3],
            "purpose": [1],
            "bedrooms": [4],
            "Area Type": [1],
            "Area Size": [10.0],
            "Area Category": [13]

        })

        # Predict the house price
        predicted_price = model.predict(input_data)

        print("=" * 60)
        print("House Price Prediction")
        print("=" * 60)
        print(f"Predicted Price : {predicted_price[0]:,.2f}")
        print("=" * 60)


if __name__ == "__main__":

    predictor = HousePricePredictor()
    predictor.predict()