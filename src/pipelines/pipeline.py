
import os
import json
import joblib
import numpy as np
import pandas as pd

from src.features.feature_engineering import create_interaction_features
from src.data.data_cleaning import (
    handle_missing_values,
    handle_rare_categories
)


class PredictionPipeline:
    def __init__(
        self,
        preprocessor_path="/Users/saidattaputta/Desktop/HomeValue-AI/artifacts/preprocessor.pkl",
        model_path="/Users/saidattaputta/Desktop/HomeValue-AI/models/best_model.pkl",
        freq_path="/Users/saidattaputta/Desktop/HomeValue-AI/artifacts/categorical_frequencies.json"
    ):

        if not os.path.exists(preprocessor_path):
            raise FileNotFoundError(f"Preprocessor not found: {preprocessor_path}")

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")

        if not os.path.exists(freq_path):
            raise FileNotFoundError(f"Category frequency file not found: {freq_path}")

        self.preprocessor = joblib.load(preprocessor_path)
        self.model = joblib.load(model_path)

        with open(freq_path, "r") as f:
            self.saved_frequencies = json.load(f)

    def validate_input(self, df: pd.DataFrame):

        if df.empty:
            raise ValueError("Input DataFrame is empty.")

        required_columns = [
            "MSSubClass",
            "MSZoning",
            "LotFrontage",
            "LotArea",
            "Street",
            "Alley",
            "LotShape",
            "LandContour",
            "Utilities",
            "LotConfig",
            "LandSlope",
            "Neighborhood",
            "Condition1",
            "Condition2",
            "BldgType",
            "HouseStyle",
            "OverallQual",
            "OverallCond",
            "YearBuilt",
            "YearRemodAdd",
            "RoofStyle",
            "RoofMatl",
            "Exterior1st",
            "Exterior2nd",
            "MasVnrType",
            "MasVnrArea",
            "ExterQual",
            "ExterCond",
            "Foundation",
            "BsmtQual",
            "BsmtCond",
            "BsmtExposure",
            "BsmtFinType1",
            "BsmtFinSF1",
            "BsmtFinType2",
            "BsmtFinSF2",
            "BsmtUnfSF",
            "TotalBsmtSF",
            "Heating",
            "HeatingQC",
            "CentralAir",
            "Electrical",
            "1stFlrSF",
            "2ndFlrSF",
            "LowQualFinSF",
            "GrLivArea",
            "BsmtFullBath",
            "BsmtHalfBath",
            "FullBath",
            "HalfBath",
            "BedroomAbvGr",
            "KitchenAbvGr",
            "KitchenQual",
            "TotRmsAbvGrd",
            "Functional",
            "Fireplaces",
            "FireplaceQu",
            "GarageType",
            "GarageYrBlt",
            "GarageFinish",
            "GarageCars",
            "GarageArea",
            "GarageQual",
            "GarageCond",
            "PavedDrive",
            "WoodDeckSF",
            "OpenPorchSF",
            "EnclosedPorch",
            "3SsnPorch",
            "ScreenPorch",
            "PoolArea",
            "PoolQC",
            "Fence",
            "MiscFeature",
            "MiscVal",
            "MoSold",
            "YrSold",
            "SaleType",
            "SaleCondition"
        ]

        missing = [col for col in required_columns if col not in df.columns]

        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    def predict(self, input_data: pd.DataFrame):

        df = input_data.copy()

        self.validate_input(df)

        num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

        df = handle_missing_values(
            df,
            num_cols,
            cat_cols
        )

        df, _ = handle_rare_categories(
            df,
            cat_cols=cat_cols,
            threshold=0.01,
            is_train=False,
            train_frequencies=self.saved_frequencies
        )

        df = create_interaction_features(df)

        log_columns = [
            "LotArea",
            "Qual_LivingArea"
        ]

        for col in log_columns:
            if col in df.columns:
                df[col] = np.log1p(df[col])

        assert list(df.columns) == list(
            self.preprocessor.feature_names_in_
        ), "Feature mismatch between inference pipeline and preprocessor."

        X_processed = self.preprocessor.transform(df)

        predictions = self.model.predict(X_processed)

        predictions = np.expm1(predictions)

        return predictions.astype(float)