import os
import joblib
import pandas as pd

from sklearn.linear_model import Ridge

from src.preprocessing.preprocessing import load_preprocessor


def train_production_model(
    data_path="data/processed/train_features.csv",
    preprocessor_path="artifacts/preprocessor.pkl",
    model_path="models/best_model.pkl"
):
    """
    Train the production Ridge model and save it.
    """

    # Load Training Data
    
    df = pd.read_csv(data_path)

    X = df.drop(
        columns=["SalePrice", "Id"],
        errors="ignore"
    )

    y = df["SalePrice"]

    # Load Preprocessor

    preprocessor = load_preprocessor(preprocessor_path)

    # Feature Validation

    expected_features = list(preprocessor.feature_names_in_)

    if list(X.columns) != expected_features:

        missing = set(expected_features) - set(X.columns)
        extra = set(X.columns) - set(expected_features)

        raise ValueError(
            f"""
Feature mismatch!

Missing:
{missing}

Extra:
{extra}
"""
        )

    # Transform Features

    X_processed = preprocessor.transform(X)

    # Train Model

    model = Ridge(
        alpha=20.0,
        solver="svd",
        random_state=42,
        max_iter=10000
    )

    model.fit(X_processed, y)

    # -----------------------------
    # Save Model
    # -----------------------------
    os.makedirs(
        os.path.dirname(model_path),
        exist_ok=True
    )

    joblib.dump(model, model_path)

    print("\nModel trained")
    print(f"Model saved to:\n{model_path}")

    return model


if __name__ == "__main__":

    train_production_model()