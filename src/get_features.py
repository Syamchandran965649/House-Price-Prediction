from feast import FeatureStore
import pandas as pd
from sklearn.model_selection import train_test_split


store = FeatureStore(
    repo_path="feature_repo/feature_repo"
)


df = pd.read_parquet(
    "feature_repo/data/features.parquet"
)


X = df.drop(
    ["price","event_timestamp"],
    axis=1
)

y = df["price"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


X_train.to_csv(
    "data/features/X_train.csv",
    index=False
)

X_test.to_csv(
    "data/features/X_test.csv",
    index=False
)

y_train.to_csv(
    "data/features/y_train.csv",
    index=False
)

y_test.to_csv(
    "data/features/y_test.csv",
    index=False
)