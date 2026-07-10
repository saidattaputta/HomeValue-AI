import streamlit as st

st.title('HomeValue AI')
st.subheader('House Price Prediction Platform')
st.markdown('-------')
st.markdown(
    """
Welcome to **HomeValue AI**, an end-to-end Machine Learning application
that predicts house prices using a production-ready ML pipeline.

### Features

- End-to-End ML Pipeline
- Feature Engineering
- Data Preprocessing
- Ridge Regression Model
- Hyperparameter Tuning
- SHAP Explainability
- FastAPI Backend
- Batch Prediction
- Deployment Ready
"""
)
st.markdown('-------')

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        'Model',
        'Ridge Regression'
    )

with col2:
    st.metric(
        'API',
        'FastAPI'
    )

with col3:
    st.metric(
        'Deployment',
        'Ready'
    )

st.markdown('-------')

st.success("Select a page from the sidebar to get started.")