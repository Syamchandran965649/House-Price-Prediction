import pandas as pd

# Read your engineered features
df = pd.read_csv("data/features/X_train.csv")

# Add an entity column
df["property_id"] = range(1, len(df) + 1)

# Add an event timestamp column
df["event_timestamp"] = pd.Timestamp.now()

# Save inside Feast data folder
df.to_parquet(
    "house_price_repo/feature_repo/data/house_features.parquet",
    index=False
)

print("Parquet file created successfully!")