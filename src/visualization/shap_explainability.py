import os
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

def generate_shap_plots(
        model_path='/Users/saidattaputta/Desktop/HomeValue-AI/models/best_model.pkl',
        X_test_processed_path = None,
        feature_names = None
    ):
    
    if not os.path.exists(model_path):
        print(f"Model file not found at {model_path}")
        return
    
    model = joblib.load(model_path)

    if X_test_processed_path:
        X_test_processed = joblib.load(X_test_processed_path)
    else:
        print("Background test matrix must be provided to compute SHAP arrays.")
        return
    
    explainer = shap.LinearExplainer(model,X_test_processed)
    shap_values = explainer(X_test_processed)

    if feature_names:
        shap_values.feature_names = list(feature_names)
        if 'num__Id' in shap_values.feature_names:
            id_idx = shap_values.feature_names.index('num__Id')
            shap_values = shap_values[:, [i for i in range(shap_values.shape[1]) if i != id_idx]]

    plt.figure(figsize=(12, 8))
    shap.summary_plot(shap_values, max_display=15, show=False)
    plt.title("Top 15 Features Driving House Price Predictions", fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig("../artifacts/shap_global_summary.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    shap.plots.waterfall(shap_values[0], max_display=10, show=False)
    plt.title("Step-by-Step Valuation Analysis for House #1", fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig("../artifacts/shap_local_waterfall.png")
    plt.close()

    print("SHAP plots saved as static assets inside '../artifacts/'.")

if __name__ == "__main__":
    print("Run script inside execution pipeline or dashboard environment.")