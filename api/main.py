import joblib
import pandas as pd
from fastapi import FastAPI
from feast import FeatureStore
from monitoring.logger import log_prediction
from monitoring.monitor import monitor_predictions

from api.schemas import HouseData

app = FastAPI(
    title="House Price Prediction API",
    version="1.0"
)

# Load trained model
model = joblib.load("models/best_model.pkl")

# Connect to Feast
store = FeatureStore(
    repo_path="feature_store/feature_repo/feature_repo"
)


@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running"}


@app.post("/predict")
def predict(data: HouseData):

    # Entity dataframe
    entity_df = pd.DataFrame({
        "property_id": [data.property_id]
    })

    # Fetch features from Feast
    feature_vector = store.get_online_features(
        features=[
            "house_features:property_type",
            "house_features:location",
            "house_features:city",
            "house_features:province_name",
            "house_features:latitude",
            "house_features:longitude",
            "house_features:baths",
            "house_features:purpose",
            "house_features:bedrooms",
            "house_features:Area Type",
            "house_features:Area Size",
            "house_features:Area Category",
        ],
        entity_rows=entity_df.to_dict("records"),
    ).to_df()

    # ---------------- DEBUG ----------------
    print("=" * 80)
    print("Property ID:", data.property_id)
    print("Features returned from Feast:")
    print(feature_vector)
    print("=" * 80)
    # ---------------------------------------

    # Remove entity column if present
    if "property_id" in feature_vector.columns:
        feature_vector = feature_vector.drop(columns=["property_id"])

    # Arrange columns in the same order used during model training
    feature_vector = feature_vector[
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

    prediction = model.predict(feature_vector)

    log_prediction(
        property_id=data.property_id,
        features=feature_vector.iloc[0].to_dict(),
        prediction=float(prediction[0])
    )
    try:
        monitor_predictions()
    except Exception as e:
        print(f"Monitoring error:{e}")    

    return {
        "Predicted Price": float(prediction[0])
    }