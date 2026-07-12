import streamlit as st

st.set_page_config(
    page_title="HomeValue AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# HERO SECTION

st.title("HomeValue AI")

st.subheader("Enterprise House Price Prediction Platform")

st.markdown("""
Welcome to **HomeValue AI**, an end-to-end Machine Learning application
for predicting residential house prices using the **Ames Housing Dataset**.

The project demonstrates the complete Machine Learning lifecycle,
starting from exploratory data analysis and feature engineering to
model deployment using **FastAPI** and an interactive **Streamlit**
dashboard.

This application is designed to showcase production-ready Machine
Learning engineering practices including modular pipelines,
REST APIs, explainability using SHAP, and deployment.
""")

st.divider()

# PROJECT HIGHLIGHTS

st.header("Project Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Dataset", "Ames Housing")

with c2:
    st.metric("Features", "79")

with c3:
    st.metric("Model", "Ridge Regression")

with c4:
    st.metric("Problem", "Regression")

st.divider()

# FEATURES

st.header("Key Features")

col1, col2 = st.columns(2)

with col1:

    st.success("Single House Price Prediction")

    st.success("Batch Prediction using CSV")

    st.success("SHAP Explainability")

    st.success("Model Insights Dashboard")

with col2:

    st.success("FastAPI REST API")

    st.success("Streamlit Interactive UI")

    st.success("Feature Importance Analysis")

    st.success("Deployment Ready")

st.divider()

# SYSTEM ARCHITECTURE

st.header("System Architecture")

st.code("""
                    User
                      │
                      ▼
           Streamlit Dashboard
                      │
          HTTPS REST API Request
                      │
                      ▼
              FastAPI Backend
                      │
                      ▼
          Prediction Pipeline
                      │
      Data Preprocessing Pipeline
                      │
                      ▼
       Ridge Regression Model
                      │
                      ▼
          Predicted House Price
""", language="text")

st.divider()

# ML WORKFLOW

st.header("Machine Learning Workflow")

st.code("""
Raw Dataset
     │
     ▼
Exploratory Data Analysis
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
Hyperparameter Tuning
     │
     ▼
Model Training
     │
     ▼
SHAP Explainability
     │
     ▼
FastAPI Deployment
     │
     ▼
Streamlit Dashboard
""", language="text")

st.divider()

# TECH STACK

st.header("Technology Stack")

tech1, tech2 = st.columns(2)

with tech1:

    st.markdown("""
### Programming

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- SHAP

### Visualization

- Matplotlib
""")

with tech2:

    st.markdown("""
### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- Streamlit

### Version Control

- Git
- GitHub

### Deployment

- Render
- Streamlit Community Cloud
""")

st.divider()

# PROJECT STRUCTURE

st.header("Project Structure")

st.code("""
HomeValue-AI
│
├── api/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│
├── app/
│   ├── app.py
│   ├── pages/
│   └── assets/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── preprocessing/
│   ├── pipelines/
│   ├── models/
│   └── visualization/
│
├── notebooks/
├── artifacts/
├── models/
├── data/
├── train.py
└── requirements.txt
""", language="text")

st.divider()

# DATASET

st.header("Dataset Information")

d1, d2 = st.columns(2)

with d1:

    st.markdown("""
### Dataset

- Ames Housing Dataset
- Residential properties
- Ames, Iowa
""")

with d2:

    st.markdown("""
### Problem Details

- Regression Problem
- Target: SalePrice
- 79 Input Features
""")

st.divider()

# MODEL

st.header("Machine Learning Model")

st.markdown("""
### Ridge Regression

The final model uses **Ridge Regression**, chosen after
hyperparameter tuning and model comparison.

#### Why Ridge Regression?

- Handles multicollinearity effectively
- Reduces overfitting using L2 regularization
- Produces stable coefficient estimates
- Good generalization performance
""")

st.divider()

# API

st.header("REST API Endpoints")

st.code("""
GET     /

GET     /health

POST    /predict

POST    /batch_predict
""", language="text")

st.divider()

# SHAP

st.header("Explainable AI")

st.markdown("""
The project integrates **SHAP (SHapley Additive Explanations)** to
interpret model predictions.

Available visualizations include:

- SHAP Summary Plot
- SHAP Beeswarm Plot
- SHAP Feature Importance
- SHAP Decision Plot
- SHAP Waterfall Plot
- SHAP Dependence Plots
- Ridge Coefficient Analysis
""")

st.divider()

# OBJECTIVES

st.header("Project Objectives")

o1, o2 = st.columns(2)

with o1:

    st.checkbox("End-to-End ML Pipeline", value=True, disabled=True)
    st.checkbox("Production-ready REST API", value=True, disabled=True)
    st.checkbox("Interactive Dashboard", value=True, disabled=True)
    st.checkbox("Batch Inference", value=True, disabled=True)

with o2:

    st.checkbox("Explainable AI", value=True, disabled=True)
    st.checkbox("Modular Codebase", value=True, disabled=True)
    st.checkbox("Deployment Ready", value=True, disabled=True)
    st.checkbox("Industry-style Project Structure", value=True, disabled=True)

st.divider()

# NAVIGATION

st.info(""" 
    **Navigate using the sidebar to explore the application**

- Home
- Predict
- Batch Predict
- Model Insights
- About
""")

st.divider()

# FOOTER

st.caption(
    "Developed by Sai Datta Putta | Integrated M.Sc Mathematics | "
    "National Institute of Technology Warangal | "
    "Machine Learning • Data Science • AI"
)