import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class FeatureEngineering:
    def __init__(self):
        self.input_path = "data/processed/processed_data.csv"
        self.output_dir = "data/features"

    def engineer_features(self):
        # Load processed dataset
        df = pd.read_csv(self.input_path)

        # Separate features and target
        X = df.drop("price", axis=1)
        y = df["price"]

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # Scale numeric columns
        scaler = StandardScaler()

        numeric_columns = X_train.select_dtypes(include=["int64", "float64"]).columns

        X_train[numeric_columns] = scaler.fit_transform(X_train[numeric_columns])
        X_test[numeric_columns] = scaler.transform(X_test[numeric_columns])

        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)

        # Save datasets
        X_train.to_csv(f"{self.output_dir}/X_train.csv", index=False)
        X_test.to_csv(f"{self.output_dir}/X_test.csv", index=False)

        y_train.to_csv(f"{self.output_dir}/y_train.csv", index=False)
        y_test.to_csv(f"{self.output_dir}/y_test.csv", index=False)

        print("=" * 60)
        print("Feature Engineering Completed Successfully")
        print(f"Training Samples : {len(X_train)}")
        print(f"Testing Samples  : {len(X_test)}")
        print("=" * 60)

        return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    feature_engineering = FeatureEngineering()
    feature_engineering.engineer_features()