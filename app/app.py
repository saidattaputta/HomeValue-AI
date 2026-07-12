import streamlit as st

st.set_page_config(
    page_title="HomeValue AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("HomeValue AI")

st.subheader("Enterprise House Price Prediction Platform")

st.markdown("""
Welcome to **HomeValue AI**, an end-to-end Machine Learning application for
predicting residential house prices using the Ames Housing Dataset.

This project demonstrates the complete machine learning lifecycle, from data
preprocessing and feature engineering to model deployment using FastAPI and
an interactive Streamlit dashboard.

### <-- Navigate using the sidebar to explore:

- **Home** – Project overview and workflow
- **Predict** – Predict the price of a single house
- **Batch Predict** – Predict prices for multiple houses using a CSV file
- **Model Insights** – SHAP explainability and feature importance
- **About** – Dataset, project structure, and developer information
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.success("Single House Prediction")
    st.success("Batch Prediction")
    st.success("SHAP Explainability")

with col2:
    st.success("FastAPI Backend")
    st.success("Streamlit Dashboard")
    st.success("Ridge Regression Model")

st.divider()

st.info(
    "Select a page from the sidebar to explore the HomeValue AI application."
)