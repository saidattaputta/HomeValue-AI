import requests
import pandas as pd
import streamlit as st

API_URL = "http://127.0.0.1:8000/batch_predict"

st.title("📂 Batch House Price Prediction")

st.markdown(
    """
Upload a CSV file containing house information.

The model will predict house prices for every row.
"""
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    df = df.where(pd.notnull(df), None)

    st.subheader("Preview")

    st.dataframe(df.head())

    st.write(f"Rows : {len(df)}")

    st.write(f"Columns : {len(df.columns)}")

    st.divider()

    if st.button(
        "Predict All Houses",
        type="primary"
    ):

        with st.spinner("Predicting..."):

            try:

                houses = (
                    df.astype(object)
                    .where(pd.notnull(df), None)
                    .to_dict(orient="records")
                    )

                response = requests.post(
                    API_URL,
                    json={
                        "houses": houses
                    },
                    timeout=60
                )

                if response.status_code == 200:

                    predictions = response.json()["predictions"]

                    result = df.copy()

                    result["PredictedPrice"] = predictions

                    st.success("Prediction Completed")

                    st.dataframe(result)

                    csv = result.to_csv(
                        index=False
                    ).encode("utf-8")

                    st.download_button(
                        "Download Predictions",
                        data=csv,
                        file_name="predictions.csv",
                        mime="text/csv"
                    )

                else:

                    st.error(response.json())

            except Exception as e:

                st.exception(e)