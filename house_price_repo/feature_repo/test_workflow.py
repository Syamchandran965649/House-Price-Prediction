from datetime import datetime
import pandas as pd
from feast import FeatureStore

store = FeatureStore(repo_path=".")

entity_df = pd.DataFrame({
    "property_id": [1, 2, 3],
    "event_timestamp": [
        datetime.now(),
        datetime.now(),
        datetime.now()
    ]
})

training_df = store.get_historical_features(
    entity_df=entity_df,
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
).to_df()

print(training_df)