import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/zameen-updated.csv")

print("Dataset Loaded Successfully")
print("-" * 40)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())