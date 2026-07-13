import joblib
import pandas as pd
from feast_service import get_features


class HousePricePredictor:

    def __init__(self):
        self.model_path = "models/best_model.pkl"

    def predict(self, property_id):

        # Load trained model
        model = joblib.load(self.model_path)

        # Fetch features from Feast
        feature_data = get_features(property_id)

        # Convert to DataFrame
        input_data = pd.DataFrame(feature_data)

        # Remove entity column
        input_data.drop(columns=["property_id"], inplace=True)

        # Rename columns to match the model
        input_data.rename(
            columns={
                "area_type": "Area Type",
                "area_size": "Area Size",
                "area_category": "Area Category",
            },
            inplace=True,
        )

        # Arrange columns in the same order used during training
        input_data = input_data[
            [
                "property_type",
                "location",
                "city",
                "province_name",
                "latitude",
                "longitude",
                "baths",
                "purpose",
                "bedrooms",
                "Area Type",
                "Area Size",
                "Area Category",
            ]
        ]

        # Predict
        predicted_price = model.predict(input_data)

        print("=" * 60)
        print("House Price Prediction")
        print("=" * 60)
        print(f"Property ID     : {property_id}")
        print(f"Predicted Price : {predicted_price[0]:,.2f}")
        print("=" * 60)


if __name__ == "__main__":
    predictor = HousePricePredictor()
    predictor.predict(1)