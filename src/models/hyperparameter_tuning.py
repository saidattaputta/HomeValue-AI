import os
import joblib
import pandas as pd
import numpy as np

from sklearn.linear_model import Ridge
from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    RandomizedSearchCV
)
from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score
)

from src.preprocessing.preprocessing import load_preprocessor


def tune_model(
    data_path="data/processed/train_features.csv",
    preprocessor_path="artifacts/preprocessor.pkl",
    model_path="models/best_model.pkl"
):
    """
    Hyperparameter tuning for Ridge Regression.
    """

    # Load data

    df = pd.read_csv(data_path)

    X = df.drop(
        columns=["SalePrice", "Id"],
        errors="ignore"
    )

    y = df["SalePrice"]

    # Load preprocessor

    preprocessor = load_preprocessor(preprocessor_path)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    X_train = preprocessor.transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Base model

    model = Ridge(
        random_state=42,
        max_iter=10000
    )

    # Grid Search

    param_grid = {
        "alpha": [0.01, 0.1, 1, 5, 10, 20, 50, 100],
        "solver": [
            "auto",
            "svd",
            "cholesky",
            "lsqr"
        ]
    }

    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=5,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(
        X_train,
        y_train
    )

    print("\nGrid Search Results")
    print(grid_search.best_params_)
    print(grid_search.best_score_)

    # Random Search

    param_distribution = {
        "alpha": np.random.uniform(
            0.001,
            200,
            100
        ),
        "solver": [
            "auto",
            "svd",
            "cholesky",
            "lsqr"
        ]
    }

    random_search = RandomizedSearchCV(
        estimator=model,
        param_distributions=param_distribution,
        n_iter=20,
        cv=5,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
        random_state=42,
        verbose=1
    )

    random_search.fit(
        X_train,
        y_train
    )

    print("\nRandom Search Results")
    print(random_search.best_params_)
    print(random_search.best_score_)

    # Select best search

    if grid_search.best_score_ >= random_search.best_score_:
        best_search = grid_search
    else:
        best_search = random_search

    best_params = best_search.best_params_

    print("\nSelected Parameters")
    print(best_params)

    # Train on FULL dataset

    X_processed = preprocessor.transform(X)

    final_model = Ridge(
        random_state=42,
        max_iter=10000,
        **best_params
    )

    final_model.fit(
        X_processed,
        y
    )

    # Evaluation

    predictions = final_model.predict(X_test)

    print("\nEvaluation")
    print(
        "MAE:",
        round(
            mean_absolute_error(
                y_test,
                predictions
            ),
            4
        )
    )

    print(
        "RMSE:",
        round(
            root_mean_squared_error(
                y_test,
                predictions
            ),
            4
        )
    )

    print(
        "R2:",
        round(
            r2_score(
                y_test,
                predictions
            ),
            4
        )
    )

    # Save model

    os.makedirs(
        os.path.dirname(model_path),
        exist_ok=True
    )

    joblib.dump(
        final_model,
        model_path
    )

    print("\nTuned model saved.")
    print(model_path)

    return final_model


if __name__ == "__main__":

    tune_model()