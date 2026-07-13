import os
import pandas as pd


class FeastLoader:

    def __init__(self):
        self.input_path = "data/processed/processed_data.csv"
        self.output_path = "feature_store/feature_repo/data/house_features.parquet"

    def create_feast_dataset(self):

        print("=" * 60)
        print("Creating Feast Dataset")
        print("=" * 60)

        df = pd.read_csv(self.input_path)

        # Rename columns
        df.rename(
            columns={
                "Area Type": "area_type",
                "Area Size": "area_size",
                "Area Category": "area_category",
            },
            inplace=True,
        )

        df.insert(0, "property_id", range(1, len(df) + 1))
        df["property_id"] = df["property_id"].astype("int64")

        df["event_timestamp"] = pd.Timestamp.now()

        os.makedirs(
            "feature_store/feature_repo/data",
            exist_ok=True,
        )

        df.to_parquet(
            self.output_path,
            index=False,
        )

        print(df.head())


if __name__ == "__main__":
    FeastLoader().create_feast_dataset()