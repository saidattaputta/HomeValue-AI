import numpy as np
import pandas as pd


def create_interaction_features(df):
    """
    Create new engineered features for the Ames Housing dataset.
    """

    engineered_df = df.copy()

    # Age Features

    engineered_df["HouseAge"] = (
        engineered_df["YrSold"] - engineered_df["YearBuilt"]
    )

    engineered_df["YearsSinceRemodel"] = (
        engineered_df["YrSold"] - engineered_df["YearRemodAdd"]
    )

    engineered_df["GarageAge"] = (
        engineered_df["YrSold"] - engineered_df["GarageYrBlt"]
    )

    engineered_df["GarageAge"] = engineered_df["GarageAge"].clip(lower=0)

    # Bathroom Features

    engineered_df["TotalBathrooms"] = (
        engineered_df["FullBath"]
        + 0.5 * engineered_df["HalfBath"]
        + engineered_df["BsmtFullBath"]
        + 0.5 * engineered_df["BsmtHalfBath"]
    )

    # Porch Features

    engineered_df["TotalPorchArea"] = (
        engineered_df["OpenPorchSF"]
        + engineered_df["EnclosedPorch"]
        + engineered_df["3SsnPorch"]
        + engineered_df["ScreenPorch"]
    )

    # Room Features

    engineered_df["TotalRooms"] = engineered_df["TotRmsAbvGrd"]

    # Interaction Features

    engineered_df["Qual_LivingArea"] = (
        engineered_df["OverallQual"]
        * engineered_df["GrLivArea"]
    )

    engineered_df["GarageCapacityArea"] = (
        engineered_df["GarageCars"]
        * engineered_df["GarageArea"]
    )

    engineered_df["OverallQual_Squared"] = (
        engineered_df["OverallQual"] ** 2
    )

    return engineered_df


def apply_log_transformations(df, is_train=True):
    """
    Apply log transformations to skewed numerical features.

    SalePrice is transformed only during training.
    """

    transformed_df = df.copy()

    skewed_features = [
        "LotArea",
        "GrLivArea",
        "1stFlrSF",
        "Qual_LivingArea",
    ]

    for col in skewed_features:

        if col in transformed_df.columns:
            transformed_df[col] = np.log1p(transformed_df[col])

    if is_train and "SalePrice" in transformed_df.columns:
        transformed_df["SalePrice"] = np.log1p(
            transformed_df["SalePrice"]
        )

    return transformed_df