import requests
import streamlit as st

from components.forms import create_prediction_form


# ==========================================================
# Configuration
# ==========================================================

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# ==========================================================
# Header
# ==========================================================

st.title("🏠 House Price Prediction")

st.markdown(
    """
Estimate the selling price of a house using our trained Machine Learning model.

Fill in the property details below and click **Predict House Price**.
"""
)

st.divider()


# ==========================================================
# Prediction Form
# ==========================================================

house = create_prediction_form()

st.divider()


# ==========================================================
# Prediction Button
# ==========================================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    predict = st.button(
        "Predict House Price",
        use_container_width=True,
        type="primary"
    )


# ==========================================================
# Prediction
# ==========================================================

if predict:

    with st.spinner("Predicting house price..."):

        try:

            response = requests.post(
                API_URL,
                json={
                    "features": house
                },
                timeout=30
            )

            if response.status_code == 200:

                prediction = response.json()["predicted_price"]

                st.divider()

                st.success("Prediction Completed Successfully")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        label="Estimated House Price",
                        value=f"${prediction:,.2f}"
                    )

                with col2:

                    st.info(
                        """
This estimate is generated using the trained
HomeValue AI Machine Learning model.
                        """
                    )

                with st.expander("View Submitted Features"):

                    st.json(house)

            else:

                st.error("Prediction Failed")

                try:
                    st.json(response.json())
                except Exception:
                    st.write(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                """
Cannot connect to FastAPI.

Start the API using:

uvicorn api.main:app --reload
"""
            )

        except Exception as e:

            st.exception(e)