# HomeValue-AI

An end-to-end residential property price prediction project using the Ames Housing dataset. The repository combines structured-data preparation, feature engineering, regression model comparison, hyperparameter tuning, SHAP-based explanation, prediction utilities, a FastAPI backend, and a Streamlit interface.

## Objective

Estimate residential sale prices from property attributes and provide an interpretable workflow for individual and batch property predictions.

## Key Capabilities

- Data preprocessing and feature engineering
- Regression model training and comparison
- Hyperparameter tuning
- SHAP-based global and local model explanation
- Single-property and CSV batch prediction utilities
- FastAPI inference backend
- Streamlit multi-page interface
- Separate model, preprocessing, and application modules

## Dataset

- **Dataset:** Ames Housing
- **Target:** `SalePrice`
- **Problem:** Regression
- **Input features:** property attributes from the source dataset

## Model Results

The existing project report lists the tuned Ridge Regression model with:

| Metric | Reported result |
|---|---:|
| MAE | 0.0784 |
| RMSE | 0.1160 |
| R² | 0.9202 |

The error metrics appear to be on a transformed or normalized target scale; they should not be interpreted as dollar-denominated errors. Confirm the evaluation split and target transformation before comparing these results with other house-price models.

## Workflow

1. Prepare training and inference features.
2. Fit preprocessing for numeric and categorical variables.
3. Train candidate regression models.
4. Tune the selected estimator.
5. Generate SHAP explanations.
6. Load model and preprocessing artifacts for inference.
7. Serve predictions through the API and Streamlit interface.

## Repository Structure

```text
.
├── api/                 # Prediction API
├── app/                 # Streamlit UI components and pages
├── artifacts/           # Preprocessing / explainability artifacts
├── data/                # Source and prepared data
├── images/              # Project visual assets
├── models/               # Trained estimators
├── notebooks/           # Analysis notebooks
├── src/                 # Reusable ML pipeline modules
├── predict.py           # Prediction utility
├── train.py             # Training workflow
├── app.py               # Empty placeholder in the current tree
├── requirements.txt
├── runtime.txt
└── README.md
```

The application code is organized under `app/`; the root-level `app.py` file is empty in the current repository snapshot. No source files were changed as part of this documentation update.

## Technology

Python, pandas, NumPy, scikit-learn, SHAP, Matplotlib, FastAPI, Uvicorn, Pydantic, Streamlit, and joblib.

## Local Setup

```bash
git clone https://github.com/saidattaputta/HomeValue-AI.git
cd HomeValue-AI
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Review the expected input-data paths in `train.py`. When the prepared training data is available at the configured path, run:

```bash
python train.py
```

The API and UI entry points are located within the project directories. Their module paths and deployment configuration should be checked before launching locally.

## Limitations

- Performance depends on the Ames Housing sample and feature-preparation choices.
- Metrics on a transformed target scale are not directly interpretable as monetary errors.
- SHAP describes model behavior, not causal effects of property attributes.
- Reproducibility requires the same split, preprocessing, data, and dependency versions.

---

**Sai Datta Putta**

[LinkedIn](https://www.linkedin.com/in/sai-datta-putta/)