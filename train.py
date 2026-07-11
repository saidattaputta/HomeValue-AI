import os
import joblib
import pandas as pd

from src.preprocessing.preprocessing import create_preprocessor
from src.models.model_training import train_production_model
from src.models.hyperparameter_tuning import tune_model
from src.visualization.shap_explainability import generate_shap_plots

from src.utils.category_levels import save_category_levels


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

TRAIN_DATA = os.path.join(
    PROJECT_ROOT,
    "data",
    "processed",
    "train_features.csv"
)

ARTIFACTS_DIR = os.path.join(
    PROJECT_ROOT,
    "artifacts"
)

MODELS_DIR = os.path.join(
    PROJECT_ROOT,
    "models"
)

PREPROCESSOR_PATH = os.path.join(
    ARTIFACTS_DIR,
    "preprocessor.pkl"
)

MODEL_PATH = os.path.join(
    MODELS_DIR,
    "best_model.pkl"
)

SHAP_VALUES_PATH = os.path.join(
    ARTIFACTS_DIR,
    "shap_values.pkl"
)


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("        HomeValue AI Training Pipeline")
    print("=" * 60)

    os.makedirs(ARTIFACTS_DIR, exist_ok=True)
    os.makedirs(MODELS_DIR, exist_ok=True)

    print("\nLoading Training Data...")

    train = pd.read_csv(TRAIN_DATA)

    print(f"Rows    : {train.shape[0]}")
    print(f"Columns : {train.shape[1]}")

    X = train.drop(columns=["SalePrice", "Id"])
    y = train["SalePrice"]

    num_cols = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    cat_cols = X.select_dtypes(
        include=["object"]
    ).columns.tolist()

    print(f"\nNumerical Features   : {len(num_cols)}")
    print(f"Categorical Features : {len(cat_cols)}")

    # ======================================================
    # Save Category Levels
    # ======================================================

    save_category_levels(
        dataframe=X,
        categorical_columns=cat_cols,
        output_path=os.path.join(
            ARTIFACTS_DIR,
            "category_levels.json"
        )
    )

    print("Category Levels Saved")

    # ======================================================
    # Create Preprocessor
    # ======================================================

    print("\nCreating Preprocessor...")

    preprocessor = create_preprocessor(
        num_cols=num_cols,
        cat_cols=cat_cols
    )

    preprocessor.fit(X)

    joblib.dump(
        preprocessor,
        PREPROCESSOR_PATH
    )

    print("Preprocessor Saved")

    # ======================================================
    # Train Model
    # ======================================================

    print("\nTraining Base Model...")

    train_production_model(
        data_path=TRAIN_DATA,
        preprocessor_path=PREPROCESSOR_PATH,
        model_path=MODEL_PATH
    )

    print("Base Model Training Completed")

    # ======================================================
    # Hyperparameter Tuning
    # ======================================================

    print("\nHyperparameter Tuning...")

    tune_model(
        data_path=TRAIN_DATA,
        preprocessor_path=PREPROCESSOR_PATH,
        model_path=MODEL_PATH
    )

    print("Hyperparameter Tuning Completed")

    # ======================================================
    # SHAP Explainability
    # ======================================================

    print("\nGenerating SHAP Explainability...")

    generate_shap_plots(
        data_path=TRAIN_DATA,
        preprocessor_path=PREPROCESSOR_PATH,
        model_path=MODEL_PATH,
        output_dir=ARTIFACTS_DIR
    )

    print("SHAP Plots Generated")

    # ======================================================
    # Summary
    # ======================================================

    print("\n" + "=" * 60)
    print("Training Pipeline Completed Successfully")
    print("=" * 60)

    print("\nGenerated Files")

    print(f"✓ {PREPROCESSOR_PATH}")
    print(f"✓ {MODEL_PATH}")
    print(f"✓ {os.path.join(ARTIFACTS_DIR,'category_levels.json')}")
    print(f"✓ {SHAP_VALUES_PATH}")
    print("✓ SHAP Summary Plot")
    print("✓ SHAP Waterfall Plot")


if __name__ == "__main__":
    main()