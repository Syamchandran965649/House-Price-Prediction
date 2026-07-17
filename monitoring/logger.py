import os
import pandas as pd
from datetime import datetime

LOG_FILE = "monitoring/prediction_logs.csv"


def log_prediction(property_id, features: dict, prediction):
    os.makedirs("monitoring", exist_ok=True)

    new_data = pd.DataFrame([{
        "Timestamp": datetime.now(),
        "property_id": property_id,
        **features,
        "predicted_price": prediction
    }])

    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
        df = pd.read_csv(LOG_FILE)
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data

    df.to_csv(LOG_FILE, index=False)