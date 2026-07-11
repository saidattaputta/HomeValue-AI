import os
import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from src.preprocessing.preprocessing import load_preprocessor


def generate_shap_plots(
    data_path="data/processed/train_features.csv",
    preprocessor_path="artifacts/preprocessor.pkl",
    model_path="models/best_model.pkl",
    output_dir="artifacts"
):
    """
    Generate SHAP global and local explanation plots.
    """

    # --------------------------------------------------
    # Load Data
    # --------------------------------------------------

    df = pd.read_csv(data_path)

    X = df.drop(
        columns=["SalePrice", "Id"],
        errors="ignore"
    )

    y = df["SalePrice"]

    # --------------------------------------------------
    # Train/Test Split
    # --------------------------------------------------

    X_train, X_test, _, _ = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # --------------------------------------------------
    # Load Preprocessor
    # --------------------------------------------------

    preprocessor = load_preprocessor(preprocessor_path)

    X_train_processed = preprocessor.transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    feature_names = preprocessor.get_feature_names_out()

    X_train_processed = pd.DataFrame(
        X_train_processed,
        columns=feature_names
    )

    X_test_processed = pd.DataFrame(
        X_test_processed,
        columns=feature_names
    )

    # --------------------------------------------------
    # Load Model
    # --------------------------------------------------

    model = joblib.load(model_path)

    # --------------------------------------------------
    # SHAP
    # --------------------------------------------------

    explainer = shap.LinearExplainer(
        model,
        X_train_processed
    )

    shap_values = explainer(
        X_test_processed
    )

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    # --------------------------------------------------
    # Global Summary Plot
    # --------------------------------------------------

    plt.figure(figsize=(12, 8))

    shap.summary_plot(
        shap_values,
        X_test_processed,
        max_display=15,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "shap_global_summary.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------------------------
    # Local Waterfall Plot
    # --------------------------------------------------

    shap.plots.waterfall(
        shap_values[0],
        max_display=10,
        show=False
    )

    plt.savefig(
        os.path.join(
            output_dir,
            "shap_local_waterfall.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------------------------
    # Global Bar Plot
    # --------------------------------------------------

    plt.figure(figsize=(12, 8))

    shap.plots.bar(
        shap_values,
        max_display=15,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "shap_bar.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------------------------
    # Beeswarm Plot
    # --------------------------------------------------

    plt.figure(figsize=(12, 8))

    shap.plots.beeswarm(
        shap_values,
        max_display=15,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "shap_beeswarm.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------------------------
    # Decision Plot
    # --------------------------------------------------

    plt.figure(figsize=(14, 8))

    shap.decision_plot(
        explainer.expected_value,
        shap_values.values[0],
        X_test_processed.iloc[0],
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "shap_decision.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    def save_dependence_plot(feature_name):

        if feature_name not in X_test_processed.columns:
            return

        plt.figure(figsize=(8, 6))

        shap.dependence_plot(
            feature_name,
            shap_values.values,
            X_test_processed,
            interaction_index=None,
            show=False
        )

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_dir,
                f"dependence_{feature_name}.png"
            ),
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()
    # --------------------------------------------------
    # Dependence Plots
    # --------------------------------------------------

    save_dependence_plot("num__OverallQual")
    save_dependence_plot("num__GrLivArea")
    save_dependence_plot("num__GarageCars")
    save_dependence_plot("num__YearBuilt")

    coefficients = pd.DataFrame({
        "Feature": feature_names,
        "Coefficient": model.coef_
    })

    coefficients["AbsCoefficient"] = (
        coefficients["Coefficient"].abs()
    )

    coefficients = coefficients.sort_values(
        "AbsCoefficient",
        ascending=False
    )

    coefficients.to_csv(
        os.path.join(
            output_dir,
            "ridge_coefficients.csv"
        ),
        index=False
    )

    top = coefficients.head(20)

    plt.figure(figsize=(10, 8))

    plt.barh(
        top["Feature"],
        top["Coefficient"]
    )

    plt.gca().invert_yaxis()

    plt.xlabel("Coefficient")

    plt.title("Top 20 Ridge Coefficients")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_dir,
            "ridge_coefficients.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # --------------------------------------------------
    # Save SHAP Values
    # --------------------------------------------------

    joblib.dump(
        shap_values,
        os.path.join(
            output_dir,
            "shap_values.pkl"
        )
    )

    print("\nSHAP analysis completed successfully.")
    print("Artifacts saved to:", output_dir)


if __name__ == "__main__":

    generate_shap_plots()