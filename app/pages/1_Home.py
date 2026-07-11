import streamlit as st

st.set_page_config(
    page_title="HomeValue AI",
    page_icon="🏠",
    layout="wide"
)

# ==========================================================
# Header
# ==========================================================

st.title("🏠 HomeValue AI")

st.subheader("Enterprise House Price Prediction Platform")

st.markdown(
    """
Welcome to **HomeValue AI**, an end-to-end Machine Learning application
for predicting residential house prices using the Ames Housing Dataset.

This project demonstrates the complete machine learning lifecycle:

- Data Cleaning
- Feature Engineering
- Model Training
- Explainability with SHAP
- FastAPI REST API
- Streamlit Dashboard
"""
)

st.divider()

# ==========================================================
# FEATURES
# ==========================================================

st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.success("🏡 Single House Prediction")

    st.success("📂 Batch Prediction")

    st.success("🧠 SHAP Explainability")

with col2:

    st.success("⚡ FastAPI Backend")

    st.success("🎨 Streamlit Dashboard")

    st.success("📊 Model Insights")

st.divider()

# ==========================================================
# WORKFLOW
# ==========================================================

st.header("🔄 Machine Learning Workflow")

st.code(
    """
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing Pipeline
      │
      ▼
Ridge Regression Model
      │
      ▼
FastAPI REST API
      │
      ▼
Streamlit Dashboard
""",
    language="text"
)

st.divider()

# ==========================================================
# TECH STACK
# ==========================================================

st.header("🛠 Tech Stack")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
### 🤖 Machine Learning

- Python
- Scikit-learn
- SHAP
- Pandas
- NumPy
"""
    )

with col2:

    st.markdown(
        """
### ⚡ Backend

- FastAPI
- Uvicorn
- REST API
"""
    )

with col3:

    st.markdown(
        """
### 🎨 Frontend

- Streamlit
- Matplotlib
- Git
- GitHub
"""
    )

st.divider()

# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

st.header("📈 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric("Dataset", "Ames Housing")

with c2:

    st.metric("Features", "79")

with c3:

    st.metric("Model", "Ridge Regression")

with c4:

    st.metric("Deployment", "FastAPI + Streamlit")

st.divider()

st.info(
    "👈 Use the navigation menu on the left to explore predictions, batch inference, model explainability, and project information."
)