import os
import pandas as pd
from src.pipelines.pipeline import PredictionPipeline

if __name__ == "__main__":
    print("Production Pipeline initiaized")
    pipeline = PredictionPipeline()

    raw_data_path = '/Users/saidattaputta/Desktop/HomeValue-AI/data/raw/train.csv'

    if os.path.exists(raw_data_path):
        full_df = pd.read_csv(raw_data_path,nrows=1)
        if 'SalePrice' in full_df.columns:
            full_df = full_df.drop('SalePrice', axis=1)

        mock_house = full_df
    else:
        print(f"Could not find {raw_data_path} to extract schema. Please verify your data directory.")
        exit(1)
    
    try:
        predicted_price = pipeline.predict(mock_house)
        print(f"\n Pipeline executed")
        print(f"Estimated Price: ${predicted_price[0]:,.2f}")
    except Exception as e:
        print(f"Pipeline transformation error: {e}")
    