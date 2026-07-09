import os
import pandas as pd

from src.pipelines.pipeline import PredictionPipeline


def main():

    print("Production Pipeline Initialized")

    pipeline = PredictionPipeline()

    raw_data_path = "data/raw/train.csv"

    if not os.path.exists(raw_data_path):
        print(f"File not found: {raw_data_path}")
        return

    houses = pd.read_csv(raw_data_path).head(10)

    if "SalePrice" in houses.columns:
        actual_prices = houses["SalePrice"]
        houses = houses.drop(columns=["SalePrice"])
    else:
        actual_prices = None

    print("\nInput Houses")
    print(houses.head())

    predictions = pipeline.predict(houses)
    
if __name__ == "__main__":
    main()