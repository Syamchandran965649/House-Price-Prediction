import pandas as pd

def load_data():
    data_path = "data/raw/zameen-updated.csv"
    df = pd.read_csv(data_path,encoding="ISO-8859-1")
    return df

if __name__ == "__main__":
    data = load_data()
    print(data.head())
    print(data.shape)