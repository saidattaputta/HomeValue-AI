from pathlib import Path

import pandas as pd
import streamlit as st

# Configuration

st.set_page_config(
    page_title="Model Insights",
    layout="wide"
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ARTIFACTS = PROJECT_ROOT / "artifacts"

# Header

st.title("Model Insights")

st.markdown(
    """
Explore the trained **HomeValue AI** model through
performance metrics, SHAP explainability and model coefficients.
"""
)

st.divider()

# Tabs

performance_tab, explainability_tab, coefficients_tab = st.tabs(
    [
        "Performance",
        "Explainability",
        "Feature Importance"
    ]
)

# PERFORMANCE TAB

with performance_tab:

    st.subheader("Model Comparison")

    comparison_file = ARTIFACTS / "comparision.csv"

    if comparison_file.exists():

        comparison = pd.read_csv(comparison_file)

        st.dataframe(
            comparison,
            use_container_width=True
        )

    else:

        st.warning("comparison.csv not found.")

    st.divider()

    st.subheader("Project Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Algorithm",
            "Ridge Regression"
        )

    with c2:

        st.metric(
            "Task",
            "Regression"
        )

    with c3:

        st.metric(
            "Dataset",
            "Ames Housing"
        )

    with c4:

        st.metric(
            "Pipeline",
            "Production Ready"
        )

# EXPLAINABILITY TAB

with explainability_tab:

    global_tab, local_tab, dependence_tab = st.tabs(
        [
            "Global",
            "Local",
            "Dependence"
        ]
    )

    # GLOBAL

    with global_tab:

        st.subheader("SHAP Summary Plot")

        summary = ARTIFACTS / "shap_global_summary.png"

        if summary.exists():

            st.image(
                str(summary),
                use_container_width=True
            )

        else:

            st.info("Summary plot not found.")

        st.divider()

        st.subheader("SHAP Bar Plot")

        bar = ARTIFACTS / "shap_bar.png"

        if bar.exists():

            st.image(
                str(bar),
                use_container_width=True
            )

        else:

            st.info("Bar plot not found.")

        st.divider()

        st.subheader("SHAP Beeswarm Plot")

        beeswarm = ARTIFACTS / "shap_beeswarm.png"

        if beeswarm.exists():

            st.image(
                str(beeswarm),
                use_container_width=True
            )

        else:

            st.info("Beeswarm plot not found.")

    # LOCAL

    with local_tab:

        st.subheader("Waterfall Plot")

        waterfall = ARTIFACTS / "shap_local_waterfall.png"

        if waterfall.exists():

            st.image(
                str(waterfall),
                use_container_width=True
            )

        else:

            st.info("Waterfall plot not found.")

        st.divider()

        st.subheader("Decision Plot")

        decision = ARTIFACTS / "shap_decision.png"

        if decision.exists():

            st.image(
                str(decision),
                use_container_width=True
            )

        else:

            st.info("Decision plot not found.")

    # DEPENDENCE

    with dependence_tab:

        plots = [

            ("Overall Quality",
             "dependence_num__OverallQual.png"),

            ("Living Area",
             "dependence_num__GrLivArea.png"),

            ("Garage Capacity",
             "dependence_num__GarageCars.png"),

            ("Year Built",
             "dependence_num__YearBuilt.png")

        ]

        for title, filename in plots:

            st.subheader(title)

            file = ARTIFACTS / filename

            if file.exists():

                st.image(
                    str(file),
                    use_container_width=True
                )

            else:

                st.info(f"{filename} not found.")

            st.divider()

# FEATURE IMPORTANCE TAB

with coefficients_tab:

    st.subheader("Top Ridge Coefficients")

    coeff_plot = ARTIFACTS / "ridge_coefficients.png"

    if coeff_plot.exists():

        st.image(
            str(coeff_plot),
            use_container_width=True
        )

    else:

        st.info("Coefficient plot not found.")

    st.divider()

    st.subheader("Coefficient Table")

    coeff_csv = ARTIFACTS / "ridge_coefficients.csv"

    if coeff_csv.exists():

        coeff = pd.read_csv(coeff_csv)

        st.dataframe(
            coeff,
            use_container_width=True,
            height=600
        )

    else:

        st.info("Coefficient CSV not found.")

# Footer

st.divider()

st.success("Model insights loaded successfully.")