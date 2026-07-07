import joblib
import pandas as pd
from fastapi import FastAPI

from api.schemas import HouseData

app = FastAPI(
    title="House Price Prediction API",
    version="1.0"
)

model = joblib.load("models/best_model.pkl")


@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running"}


@app.post("/predict")
def predict(data: HouseData):

    input_df = pd.DataFrame([{
        "property_type": data.property_type,
        "location": data.location,
        "city": data.city,
        "province_name": data.province_name,
        "latitude": data.latitude,
        "longitude": data.longitude,
        "baths": data.baths,
        "purpose": data.purpose,
        "bedrooms": data.bedrooms,
        "Area Type": data.Area_Type,
        "Area Size": data.Area_Size,
        "Area Category": data.Area_Category
    }])

    prediction = model.predict(input_df)

    return {
        "Predicted Price": float(prediction[0])
    }