from pathlib import Path
import streamlit as st

ASSETS = Path(__file__).parent / "assets"

logo_path = ASSETS / "logo.png"

if logo_path.exists():
    st.sidebar.image(str(logo_path), use_container_width=True)

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

