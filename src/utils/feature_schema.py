import json
import os


def save_feature_schema(
    dataframe,
    categorical_columns,
    numerical_columns,
    output_path="artifacts/feature_schema.json"
):
    """
    Save feature metadata for dynamically generating
    the Streamlit prediction form.
    """

    schema = {}

    # Numerical Features
    for column in numerical_columns:

        values = dataframe[column]

        schema[column] = {
            "type": "numeric",
            "min": float(values.min()),
            "max": float(values.max()),
            "default": float(values.median())
        }

    # Categorical Features
    for column in categorical_columns:

        schema[column] = {
            "type": "categorical"
        }

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    with open(output_path, "w") as f:

        json.dump(
            schema,
            f,
            indent=4
        )

    print(f"Feature schema saved to {output_path}")