import os
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt


def generate_shap_plots(
    model_path="/Users/saidattaputta/Desktop/HomeValue-AI/models/best_model.pkl",
    preprocessor_path="/Users/saidattaputta/Desktop/HomeValue-AI/artifacts/preprocessor.pkl",
    data_path="/Users/saidattaputta/Desktop/HomeValue-AI/data/processed/train_features.csv",
    artifact_dir="/Users/saidattaputta/Desktop/HomeValue-AI/artifacts"
):

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found: {model_path}")

    if not os.path.exists(preprocessor_path):
        raise FileNotFoundError(f"Preprocessor not found: {preprocessor_path}")

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found: {data_path}")

    os.makedirs(artifact_dir, exist_ok=True)

    model = joblib.load(model_path)
    preprocessor = joblib.load(preprocessor_path)

    df = pd.read_csv(data_path)

    X = df.drop(columns=["SalePrice", "Id"])
    y = df["SalePrice"]

    assert list(X.columns) == list(preprocessor.feature_names_in_), (
        "Feature mismatch between dataset and preprocessor."
    )

    X_processed = preprocessor.transform(X)

    feature_names = preprocessor.get_feature_names_out()

    X_processed = pd.DataFrame(
        X_processed,
        columns=feature_names
    )

    explainer = shap.LinearExplainer(model, X_processed)

    shap_values = explainer(X_processed)

    shap.summary_plot(
        shap_values,
        X_processed,
        max_display=15,
        show=False
    )

    plt.title(
        "Top 15 Features Driving House Price Predictions",
        fontsize=16,
        fontweight="bold",
        pad=20
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(artifact_dir, "shap_global_summary.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    shap.plots.waterfall(
        shap_values[0],
        max_display=10,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(artifact_dir, "shap_local_waterfall.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    joblib.dump(
        shap_values,
        os.path.join(artifact_dir, "shap_values.pkl")
    )

    print("SHAP analysis completed successfully.")
    print(f"Artifacts saved to: {artifact_dir}")


if __name__ == "__main__":
    generate_shap_plots()