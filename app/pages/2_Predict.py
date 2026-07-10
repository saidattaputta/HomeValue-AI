import streamlit as st

from components.forms import create_prediction_form


st.title("House Price Prediction")

st.markdown(
    """
Fill in the house details below.
"""
)

st.divider()

house = create_prediction_form()

st.divider()

st.subheader("Collected Input")

st.json(house)