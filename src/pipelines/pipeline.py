
import os
import joblib
import json
import pandas as pd
import numpy as np
from src.features.feature_engineering import create_interaction_features
from src.data.data_cleaning import handle_rare_categories

class PredictionPipeline:
    def __init__(self,
                 preprocessor_path = '/Users/saidattaputta/Desktop/HomeValue-AI/artifacts/preprocessor.pkl',
                 model_path = '/Users/saidattaputta/Desktop/HomeValue-AI/models/best_model.pkl',
                 freq_path = '/Users/saidattaputta/Desktop/HomeValue-AI/artifacts/categorical_frequencies.json'):
        
        if not os.path.exists(preprocessor_path) or not os.path.exists(model_path) or not os.path.exists(freq_path):
            raise FileNotFoundError("Missing pipeline assets. Please ensure artifacts and models are generated.")
        
        self.preprocessor = joblib.load(preprocessor_path)
        self.model = joblib.load(model_path)
        with open(freq_path, 'r') as f:
            self.saved_frequencies = json.load(f)

    def validate_input(self, df: pd.DataFrame):

        if df.empty:
            raise ValueError('Input DataFrame is empty.')
        
        columns_required = [
            "YrSold", "YearBuilt", "YearRemodAdd", "GarageYrBlt", 
            "FullBath", "HalfBath", "BsmtFullBath", "BsmtHalfBath",
            "OpenPorchSF", "EnclosedPorch", "3SsnPorch", "ScreenPorch",
            "TotRmsAbvGrd", "OverallQual", "GrLivArea", "GarageCars", "GarageArea"
        ]
        for col in columns_required:
            if col not in df.columns:
                raise ValueError(f"Missing critical feature required for engineering: {col}")
            
    def predict(self, input_data: pd.DataFrame) -> np.ndarray:
        df = input_data.copy()
        self.validate_input(df)

        # 1. Handle Rare Categories
        cat_cols = list(self.saved_frequencies.keys())
        df_cleaned, _ = handle_rare_categories(
            df, 
            cat_cols=cat_cols, 
            threshold=0.01, 
            is_train=False, 
            train_frequencies=self.saved_frequencies
        )

        # 2. Feature Engineering
        df_engineered = create_interaction_features(df_cleaned)

        # 3. Log Transformations (Keep this enabled!)
        log_columns = ['LotArea', 'Qual_LivingArea'] 
        for col in log_columns:
            if col in df_engineered.columns:
                df_engineered[col] = np.log1p(df_engineered[col])

        # 4. Preprocessing & Inference
        X_processed = self.preprocessor.transform(df_engineered)
        predictions = self.model.predict(X_processed)
        
        # 5. Reverse the log target transformation cleanly
        # If your model output is in the range of ~11.5 to 13.0, this returns actual USD.
        final_price = np.expm1(predictions)
        
        return final_price