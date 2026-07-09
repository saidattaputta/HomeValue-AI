import json
import joblib
import numpy as np
import pandas as pd

from src.data.data_cleaning import (
    handle_missing_values,
    handle_rare_categories
)

from src.features.feature_engineering import (
    create_interaction_features,
    apply_log_transformations
)


class PredictionPipeline:

    def __init__(
        self,
        preprocessor_path="artifacts/preprocessor.pkl",
        model_path="models/best_model.pkl",
        freq_path="artifacts/categorical_frequencies.json"
    ):

        self.preprocessor = joblib.load(preprocessor_path)
        self.model = joblib.load(model_path)

        with open(freq_path, "r") as f:
            self.saved_frequencies = json.load(f)

    def predict(self, input_df: pd.DataFrame):

        df = input_df.copy()

        # -------------------------------------------------
        # Remove Target
        # -------------------------------------------------

        if "SalePrice" in df.columns:
            df = df.drop(columns=["SalePrice"])

        # -------------------------------------------------
        # Remove Id
        # -------------------------------------------------

        if "Id" in df.columns:
            df = df.drop(columns=["Id"])

        # -------------------------------------------------
        # Numerical & Categorical Columns
        # -------------------------------------------------

        num_cols = df.select_dtypes(include=np.number).columns.tolist()

        cat_cols = df.select_dtypes(
            exclude=np.number
        ).columns.tolist()

        # -------------------------------------------------
        # Missing Values
        # -------------------------------------------------

        df = handle_missing_values(
            df,
            num_cols,
            cat_cols
        )

        # -------------------------------------------------
        # Rare Categories
        # -------------------------------------------------

        df, _ = handle_rare_categories(
            df=df,
            cat_cols=cat_cols,
            threshold=0.01,
            is_train=False,
            train_frequencies=self.saved_frequencies
        )

        # -------------------------------------------------
        # Feature Engineering
        # -------------------------------------------------

        df = create_interaction_features(df)

        # -------------------------------------------------
        # Log Transformations
        # -------------------------------------------------

        df = apply_log_transformations(
            df,
            is_train=False
        )

        # -------------------------------------------------
        # Match Training Feature Order
        # -------------------------------------------------

        expected_columns = list(
            self.preprocessor.feature_names_in_
        )

        df = df[expected_columns]

        # -------------------------------------------------
        # Transform
        # -------------------------------------------------

        X = self.preprocessor.transform(df)

        # -------------------------------------------------
        # Predict
        # -------------------------------------------------

        prediction = self.model.predict(X)

        # -------------------------------------------------
        # Reverse Log(Target)
        # -------------------------------------------------

        prediction = np.expm1(prediction)

        return prediction