import json
import os


def save_category_levels(
    dataframe,
    categorical_columns,
    output_path="artifacts/category_levels.json"
):
    """
    Save all unique categorical values from the training data.

    This file is used by the Streamlit frontend to populate
    dropdown menus automatically.
    """

    category_levels = {}

    for column in categorical_columns:

        values = sorted(
            dataframe[column]
            .fillna("None")
            .astype(str)
            .unique()
            .tolist()
        )

        category_levels[column] = values

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    with open(output_path, "w") as file:

        json.dump(
            category_levels,
            file,
            indent=4
        )

    print(f"Category levels saved to: {output_path}")