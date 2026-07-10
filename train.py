import os
import joblib
import pandas as pd


from src.preprocessing.preprocessing import create_preprocessor
from src.models.model_training import train_production_model
from src.models.hyperparameter_tuning import tune_model
from src.visualization.shap_explainability import generate_shap_plots

project_root = os.path.dirname(os.path.abspath(__file__))

train_data = os.path.join(project_root,'data','processed','train_features.csv')

artifacts_dir = os.path.join(project_root,'artifacts')

models_dir = os.path.join(project_root,'models')

preprocessing_path = os.path.join(
    artifacts_dir,
    'preprocessor.pkl'
)

model_path = os.path.join(
    models_dir,
    'best_model.pkl'
)

shap_value_path = os.path.join(
    artifacts_dir,
    'shap_values.pkl'
)

def main():

    print("="*50)
    print("     HomeValue AI Training Pipeline")
    print("="*50)

    os.makedirs(artifacts_dir,exist_ok=True)
    os.makedirs(models_dir,exist_ok=True)

    # Load Data

    train = pd.read_csv(train_data)

    print(f"Rows    : {train.shape[0]}")
    print(f"Columns : {train.shape[1]}")

    X = train.drop(columns=['SalePrice','Id'])
    y = train['SalePrice']

    num_cols = X.select_dtypes(include=['int64','float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object']).columns.tolist()

    print(f"Numerical Features  : {len(num_cols)}")
    print(f"Categorical Features: {len(cat_cols)}")

    # Create Proprocessor

    preprocessor = create_preprocessor(
        num_cols=num_cols,
        cat_cols=cat_cols
    )

    preprocessor.fit(X)

    joblib.dump(preprocessor,preprocessing_path)

    print(" Preprocessor Saved")

    # Train Model

    train_production_model(
        data_path=train_data,
        preprocessor_path=preprocessing_path,
        model_path=model_path
    )

    print(" Base Model Training Completed")

    # Hyperparameter Tuning

    tune_model(
        data_path=train_data,
        preprocessor_path=preprocessing_path,
        model_path=model_path
    )

    print(" Hyperparameter Tuning Completed")

    #  SHAP Explainability

    try:

        X_processed = preprocessor.transform(X)

        joblib.dump(
            X_processed,
            shap_value_path
        )

        generate_shap_plots(
            model_path=model_path,
            feature_names=preprocessor.get_feature_names_out(),
            X_test_processed_path = shap_value_path
        )

        print("SHAP Plots Generated")

    except Exception as e:

        print(f"SHAP generation skipped: {e}")

    print("\n" + "=" * 60)
    print("Training Pipeline Completed Successfully")
    print("=" * 60)

    print("\nGenerated Files")

    print(f" {preprocessing_path}")
    print(f" {model_path}")
    print(f" {shap_value_path}")
    print(" SHAP Summary Plot")
    print(" SHAP Waterfall Plot")


if __name__ == "__main__":
    main()

