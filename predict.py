import os
import pandas as pd
from src.pipelines.pipeline import PredictionPipeline

if __name__ == "__main__":

    print("Production Pipeline Initialized")

    pipeline = PredictionPipeline()

    raw_data_path = "/Users/saidattaputta/Desktop/HomeValue-AI/data/raw/train.csv"

    if os.path.exists(raw_data_path):

        full_df = pd.read_csv(raw_data_path, nrows=1)

        if "SalePrice" in full_df.columns:
            full_df = full_df.drop(columns=["SalePrice"])

        mock_house = full_df

        print("\nInput Features")
        print(mock_house.head())

    else:
        print(f"Could not find {raw_data_path}")
        exit(1)

    try:

        predicted_price = pipeline.predict(mock_house)

        print("\nPrediction pipeline executed successfully.")
        print(f"Estimated House Price: ${predicted_price[0]:,.2f}")

    except Exception as e:
        print(f"Prediction failed: {e}")