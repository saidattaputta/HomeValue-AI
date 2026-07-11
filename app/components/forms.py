import json
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CATEGORY_FILE = PROJECT_ROOT / "artifacts" / "category_levels.json"


def load_categories():
    with open(CATEGORY_FILE, "r") as f:
        return json.load(f)


def get_options(categories, column):
    values = categories.get(column, [])

    if len(values) == 0:
        return ["None"]

    return values


def create_prediction_form():

    categories = load_categories()

    house = {}

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    st.header("🏡 General Information")

    col1, col2 = st.columns(2)

    with col1:

        house["MSSubClass"] = st.number_input(
            "MSSubClass",
            min_value=20,
            max_value=190,
            value=60
        )

        house["MSZoning"] = st.selectbox(
            "MSZoning",
            get_options(categories, "MSZoning")
        )

        house["Neighborhood"] = st.selectbox(
            "Neighborhood",
            get_options(categories, "Neighborhood")
        )

        house["Street"] = st.selectbox(
            "Street",
            get_options(categories, "Street")
        )

    with col2:

        house["LotShape"] = st.selectbox(
            "LotShape",
            get_options(categories, "LotShape")
        )

        house["LandContour"] = st.selectbox(
            "LandContour",
            get_options(categories, "LandContour")
        )

        house["Utilities"] = st.selectbox(
            "Utilities",
            get_options(categories, "Utilities")
        )

        house["LotConfig"] = st.selectbox(
            "LotConfig",
            get_options(categories, "LotConfig")
        )

    st.divider()

    # =====================================================
    # LOT INFORMATION
    # =====================================================

    st.header("🌳 Lot Information")

    col1, col2 = st.columns(2)

    with col1:

        house["LotFrontage"] = st.number_input(
            "Lot Frontage",
            min_value=0,
            value=70
        )

        house["LotArea"] = st.number_input(
            "Lot Area",
            min_value=1000,
            value=9000
        )

        house["LandSlope"] = st.selectbox(
            "LandSlope",
            get_options(categories, "LandSlope")
        )

    with col2:

        house["Condition1"] = st.selectbox(
            "Condition1",
            get_options(categories, "Condition1")
        )

        house["Condition2"] = st.selectbox(
            "Condition2",
            get_options(categories, "Condition2")
        )

    st.divider()

    # =====================================================
    # BUILDING INFORMATION
    # =====================================================

    st.header("🏠 Building Information")

    col1, col2 = st.columns(2)

    with col1:

        house["BldgType"] = st.selectbox(
            "Building Type",
            get_options(categories, "BldgType")
        )

        house["HouseStyle"] = st.selectbox(
            "House Style",
            get_options(categories, "HouseStyle")
        )

        house["OverallQual"] = st.slider(
            "Overall Quality",
            min_value=1,
            max_value=10,
            value=5
        )

        house["OverallCond"] = st.slider(
            "Overall Condition",
            min_value=1,
            max_value=10,
            value=5
        )

    with col2:

        house["YearBuilt"] = st.number_input(
            "Year Built",
            min_value=1800,
            max_value=2025,
            value=2000
        )

        house["YearRemodAdd"] = st.number_input(
            "Year Remodeled",
            min_value=1800,
            max_value=2025,
            value=2000
        )

        house["RoofStyle"] = st.selectbox(
            "Roof Style",
            get_options(categories, "RoofStyle")
        )

        house["RoofMatl"] = st.selectbox(
            "Roof Material",
            get_options(categories, "RoofMatl")
        )

    st.divider()

    # =====================================================
    # EXTERIOR
    # =====================================================

    st.header("🏡 Exterior")

    col1, col2 = st.columns(2)

    with col1:

        house["Exterior1st"] = st.selectbox(
            "Exterior Covering 1",
            get_options(categories, "Exterior1st")
        )

        house["Exterior2nd"] = st.selectbox(
            "Exterior Covering 2",
            get_options(categories, "Exterior2nd")
        )

        house["ExterQual"] = st.selectbox(
            "Exterior Quality",
            get_options(categories, "ExterQual")
        )

        house["ExterCond"] = st.selectbox(
            "Exterior Condition",
            get_options(categories, "ExterCond")
        )

    with col2:

        house["Foundation"] = st.selectbox(
            "Foundation",
            get_options(categories, "Foundation")
        )

        house["MasVnrType"] = st.selectbox(
            "Masonry Veneer Type",
            get_options(categories, "MasVnrType")
        )

        house["MasVnrArea"] = st.number_input(
            "Masonry Veneer Area",
            min_value=0,
            value=0
        )

    st.divider()

    # =====================================================
    # BASEMENT
    # =====================================================

    st.header("🧱 Basement")

    col1, col2 = st.columns(2)

    with col1:

        house["BsmtQual"] = st.selectbox(
            "Basement Quality",
            get_options(categories, "BsmtQual")
        )

        house["BsmtCond"] = st.selectbox(
            "Basement Condition",
            get_options(categories, "BsmtCond")
        )

        house["BsmtExposure"] = st.selectbox(
            "Basement Exposure",
            get_options(categories, "BsmtExposure")
        )

        house["BsmtFinType1"] = st.selectbox(
            "Basement Finish Type 1",
            get_options(categories, "BsmtFinType1")
        )

        house["BsmtFinType2"] = st.selectbox(
            "Basement Finish Type 2",
            get_options(categories, "BsmtFinType2")
        )

    with col2:

        house["BsmtFinSF1"] = st.number_input(
            "Finished Area 1",
            min_value=0,
            value=0
        )

        house["BsmtFinSF2"] = st.number_input(
            "Finished Area 2",
            min_value=0,
            value=0
        )

        house["BsmtUnfSF"] = st.number_input(
            "Unfinished Basement Area",
            min_value=0,
            value=0
        )

        house["TotalBsmtSF"] = st.number_input(
            "Total Basement Area",
            min_value=0,
            value=0
        )

        house["BsmtFullBath"] = st.number_input(
            "Basement Full Bathrooms",
            min_value=0,
            max_value=5,
            value=0
        )

        house["BsmtHalfBath"] = st.number_input(
            "Basement Half Bathrooms",
            min_value=0,
            max_value=5,
            value=0
        )

    st.divider()

    # =====================================================
    # HEATING & ELECTRICAL
    # =====================================================

    st.header("🔥 Heating & Electrical")

    col1, col2 = st.columns(2)

    with col1:

        house["Heating"] = st.selectbox(
            "Heating",
            get_options(categories, "Heating")
        )

        house["HeatingQC"] = st.selectbox(
            "Heating Quality",
            get_options(categories, "HeatingQC")
        )

    with col2:

        house["CentralAir"] = st.selectbox(
            "Central Air",
            get_options(categories, "CentralAir")
        )

        house["Electrical"] = st.selectbox(
            "Electrical System",
            get_options(categories, "Electrical")
        )

    st.divider()

    # =====================================================
    # LIVING AREA
    # =====================================================

    st.header("🛋 Living Area")

    col1, col2 = st.columns(2)

    with col1:

        house["1stFlrSF"] = st.number_input(
            "1st Floor Area",
            min_value=0,
            value=900
        )

        house["2ndFlrSF"] = st.number_input(
            "2nd Floor Area",
            min_value=0,
            value=0
        )

        house["LowQualFinSF"] = st.number_input(
            "Low Quality Finished Area",
            min_value=0,
            value=0
        )

    with col2:

        house["GrLivArea"] = st.number_input(
            "Above Ground Living Area",
            min_value=300,
            value=1500
        )

        house["WoodDeckSF"] = st.number_input(
            "Wood Deck Area",
            min_value=0,
            value=0
        )

    st.divider()

    # =====================================================
    # ROOMS
    # =====================================================

    st.header("🚪 Rooms")

    col1, col2 = st.columns(2)

    with col1:

        house["FullBath"] = st.number_input(
            "Full Bathrooms",
            min_value=0,
            max_value=6,
            value=2
        )

        house["HalfBath"] = st.number_input(
            "Half Bathrooms",
            min_value=0,
            max_value=6,
            value=0
        )

        house["BedroomAbvGr"] = st.number_input(
            "Bedrooms",
            min_value=0,
            max_value=10,
            value=3
        )

    with col2:

        house["KitchenAbvGr"] = st.number_input(
            "Kitchens",
            min_value=0,
            max_value=5,
            value=1
        )

        house["KitchenQual"] = st.selectbox(
            "Kitchen Quality",
            get_options(categories, "KitchenQual")
        )

        house["TotRmsAbvGrd"] = st.number_input(
            "Total Rooms Above Ground",
            min_value=2,
            max_value=20,
            value=6
        )

        house["Functional"] = st.selectbox(
            "Functionality",
            get_options(categories, "Functional")
        )

    st.divider()

    # =====================================================
    # FIREPLACE
    # =====================================================

    st.header("🔥 Fireplace")

    col1, col2 = st.columns(2)

    with col1:

        house["Fireplaces"] = st.number_input(
            "Number of Fireplaces",
            min_value=0,
            max_value=5,
            value=0
        )

    with col2:

        house["FireplaceQu"] = st.selectbox(
            "Fireplace Quality",
            get_options(categories, "FireplaceQu")
        )

    st.divider()

    # =====================================================
    # GARAGE
    # =====================================================

    st.header("🚗 Garage")

    col1, col2 = st.columns(2)

    with col1:

        house["GarageType"] = st.selectbox(
            "Garage Type",
            get_options(categories, "GarageType")
        )

        house["GarageYrBlt"] = st.number_input(
            "Garage Year Built",
            min_value=1900,
            max_value=2025,
            value=2000
        )

        house["GarageFinish"] = st.selectbox(
            "Garage Finish",
            get_options(categories, "GarageFinish")
        )

        house["GarageCars"] = st.number_input(
            "Garage Capacity",
            min_value=0,
            max_value=6,
            value=2
        )

    with col2:

        house["GarageArea"] = st.number_input(
            "Garage Area",
            min_value=0,
            value=500
        )

        house["GarageQual"] = st.selectbox(
            "Garage Quality",
            get_options(categories, "GarageQual")
        )

        house["GarageCond"] = st.selectbox(
            "Garage Condition",
            get_options(categories, "GarageCond")
        )

        house["PavedDrive"] = st.selectbox(
            "Paved Driveway",
            get_options(categories, "PavedDrive")
        )

    st.divider()

    # =====================================================
    # PORCH & OUTDOOR
    # =====================================================

    st.header("🌿 Porch & Outdoor")

    col1, col2 = st.columns(2)

    with col1:

        house["OpenPorchSF"] = st.number_input(
            "Open Porch Area",
            min_value=0,
            value=0
        )

        house["EnclosedPorch"] = st.number_input(
            "Enclosed Porch Area",
            min_value=0,
            value=0
        )

        house["3SsnPorch"] = st.number_input(
            "Three Season Porch",
            min_value=0,
            value=0
        )

    with col2:

        house["ScreenPorch"] = st.number_input(
            "Screen Porch",
            min_value=0,
            value=0
        )

        house["PoolArea"] = st.number_input(
            "Pool Area",
            min_value=0,
            value=0
        )

        house["PoolQC"] = st.selectbox(
            "Pool Quality",
            get_options(categories, "PoolQC")
        ) 
    st.divider()

    # =====================================================
    # FENCE & MISCELLANEOUS
    # =====================================================

    st.header("🛠 Miscellaneous")

    col1, col2 = st.columns(2)

    with col1:

        house["Fence"] = st.selectbox(
            "Fence",
            get_options(categories, "Fence")
        )

        house["MiscFeature"] = st.selectbox(
            "Misc Feature",
            get_options(categories, "MiscFeature")
        )

    with col2:

        house["MiscVal"] = st.number_input(
            "Miscellaneous Value",
            min_value=0,
            value=0
        )

    st.divider()

    # =====================================================
    # SALE INFORMATION
    # =====================================================

    st.header("💰 Sale Information")

    col1, col2 = st.columns(2)

    with col1:

        house["MoSold"] = st.selectbox(
            "Month Sold",
            options=list(range(1, 13)),
            index=5
        )

        house["YrSold"] = st.selectbox(
            "Year Sold",
            options=[2006, 2007, 2008, 2009, 2010],
            index=4
        )

    with col2:

        house["SaleType"] = st.selectbox(
            "Sale Type",
            get_options(categories, "SaleType")
        )

        house["SaleCondition"] = st.selectbox(
            "Sale Condition",
            get_options(categories, "SaleCondition")
        )

    st.divider()

    st.success("✅ All required information has been entered.")

    return house
    return house