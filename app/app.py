import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="HomeValue AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

ASSETS = Path(__file__).parent / "assets"

logo = ASSETS / "logo.png"

if logo.exists():
    st.logo(str(logo))

st.sidebar.title("HomeValue AI")

st.sidebar.caption(
    "Enterprise House Price Prediction Platform"
)

st.sidebar.divider()

st.sidebar.success("End-to-End Machine Learning")

st.sidebar.success("FastAPI Backend")

st.sidebar.success("Streamlit Dashboard")

st.sidebar.success("SHAP Explainability")

st.sidebar.success("Batch Prediction")

st.sidebar.divider()

st.sidebar.caption("Developed by Sai Datta Putta")

