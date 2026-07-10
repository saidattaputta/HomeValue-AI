import json
from pathlib import Path

import streamlit as st


# ==========================================================
# Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CATEGORY_FILE = PROJECT_ROOT / "artifacts" / "category_levels.json"
SCHEMA_FILE = PROJECT_ROOT / "artifacts" / "feature_schema.json"


# ==========================================================
# Load Files
# ==========================================================

def load_categories():

    with open(CATEGORY_FILE, "r") as f:
        return json.load(f)


def load_schema():

    with open(SCHEMA_FILE, "r") as f:
        return json.load(f)


# ==========================================================
# Dynamic Form
# ==========================================================

def create_prediction_form():

    categories = load_categories()
    schema = load_schema()

    house = {}

    st.header("🏠 House Information")

    numeric_features = []
    categorical_features = []

    # Separate numeric and categorical features
    for feature, info in schema.items():

        if info["type"] == "numeric":
            numeric_features.append(feature)
        else:
            categorical_features.append(feature)

    # ======================================================
    # Numerical Features
    # ======================================================

    st.subheader("📊 Numerical Features")

    col1, col2 = st.columns(2)

    for i, feature in enumerate(numeric_features):

        info = schema[feature]

        target_col = col1 if i % 2 == 0 else col2

        with target_col:

            house[feature] = st.number_input(
                label=feature,
                min_value=float(info["min"]),
                max_value=float(info["max"]),
                value=float(info["default"])
            )

    st.divider()

    # ======================================================
    # Categorical Features
    # ======================================================

    st.subheader("📋 Categorical Features")

    col1, col2 = st.columns(2)

    for i, feature in enumerate(categorical_features):

        options = categories.get(feature, ["None"])

        if len(options) == 0:
            options = ["None"]

        target_col = col1 if i % 2 == 0 else col2

        with target_col:

            house[feature] = st.selectbox(
                label=feature,
                options=options
            )

    return house