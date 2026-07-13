import joblib
import pandas as pd
from fastapi import FastAPI

from src.feast_service import get_features

app = FastAPI(
    title="House Price Prediction API",
    version="1.0"
)

model = joblib.load("models/best_model.pkl")


@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running"}


@app.get("/predict/{property_id}")
def predict(property_id: int):

    # Get features from Feast
    feature_data = get_features(property_id)

    input_df = pd.DataFrame(feature_data)

    # Remove entity column
    input_df.drop(columns=["property_id"], inplace=True)

    # Rename columns to match the trained model
    input_df.rename(
        columns={
            "area_type": "Area Type",
            "area_size": "Area Size",
            "area_category": "Area Category",
        },
        inplace=True,
    )

    # Arrange columns in training order
    input_df = input_df[
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

    prediction = model.predict(input_df)

    return {
        "property_id": property_id,
        "predicted_price": float(prediction[0])
    }