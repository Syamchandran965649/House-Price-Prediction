import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/zameen-updated.csv")

print("=" * 50)
print("DATA VALIDATION REPORT")
print("=" * 50)

# Shape
print(f"\nRows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Data Types
print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Check Target Column
print("\nTarget Column (price):")
print(df["price"].describe())

# Check Negative Prices
negative_prices = (df["price"] < 0).sum()
print(f"\nNegative Prices: {negative_prices}")