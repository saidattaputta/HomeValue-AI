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

    # Load first 10 houses
    houses = pd.read_csv(raw_data_path).head(10)

    # Save actual prices
    if "SalePrice" in houses.columns:
        actual_prices = houses["SalePrice"]
        houses = houses.drop(columns=["SalePrice"])
    else:
        actual_prices = None

    print("\nInput Houses")
    print(houses.head())

    # Predict
    predictions = pipeline.predict(houses)

    print("\nPredictions\n")

    for i, pred in enumerate(predictions):

        print(f"House {i+1}")

        print(f"Predicted : ${pred:,.2f}")

        if actual_prices is not None:
            print(f"Actual    : ${actual_prices.iloc[i]:,.2f}")


if __name__ == "__main__":
    main()