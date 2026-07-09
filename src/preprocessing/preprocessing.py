import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def create_preprocessor(num_cols, cat_cols):
    """
    Create preprocessing pipeline for numerical and categorical features.
    """

    num_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]
    )

    cat_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipeline, num_cols),
            ("cat", cat_pipeline, cat_cols)
        ]
    )

    return preprocessor


def fit_preprocessor(
    train_df,
    target_column="SalePrice",
    id_column="Id"
):
    """
    Fit the preprocessor on training data.
    """

    X = train_df.drop(
        columns=[target_column, id_column],
        errors="ignore"
    )

    num_cols = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    cat_cols = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    preprocessor = create_preprocessor(
        num_cols,
        cat_cols
    )

    preprocessor.fit(X)

    return preprocessor


def save_preprocessor(
    preprocessor,
    output_path
):
    """
    Save fitted preprocessor.
    """

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    joblib.dump(
        preprocessor,
        output_path
    )

    print(f"Preprocessor saved to:\n{output_path}")


def load_preprocessor(
    preprocessor_path
):
    """
    Load fitted preprocessor.
    """

    if not os.path.exists(preprocessor_path):
        raise FileNotFoundError(
            f"Preprocessor not found:\n{preprocessor_path}"
        )

    return joblib.load(preprocessor_path)