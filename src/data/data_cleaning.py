import pandas as pd


def handle_missing_values(df, num_cols, cat_cols):
    """
    Handle missing values in numerical and categorical features.
    """

    cleaned_df = df.copy()

    # Numerical columns
    for col in num_cols:
        if col in cleaned_df.columns and cleaned_df[col].isnull().sum() > 0:

            if col in ["GarageYrBlt", "MasVnrArea"]:
                cleaned_df[col] = cleaned_df[col].fillna(0)
            else:
                cleaned_df[col] = cleaned_df[col].fillna(
                    cleaned_df[col].median()
                )

    # Categorical columns
    for col in cat_cols:
        if col in cleaned_df.columns and cleaned_df[col].isnull().sum() > 0:
            cleaned_df[col] = cleaned_df[col].fillna("None")

    return cleaned_df


def handle_outliers(df, is_train=True):
    """
    Remove only the well-known Ames Housing outliers from training data.
    """

    cleaned_df = df.copy()

    if is_train:
        cleaned_df = cleaned_df[
            ~(
                (cleaned_df["GrLivArea"] > 4000)
                &
                (cleaned_df["SalePrice"] < 300000)
            )
        ]

    return cleaned_df


def handle_rare_categories(
    df,
    cat_cols,
    threshold=0.01,
    is_train=True,
    train_frequencies=None
):
    """
    Group infrequent categories into a single 'Rare' label.

    During training:
        - Learns category frequencies.
        - Returns dictionary for later inference.

    During inference:
        - Uses saved training frequencies.
        - Never recalculates frequencies.
    """

    df_out = df.copy()

    if is_train:

        train_frequencies = {}

        for col in cat_cols:

            if col not in df_out.columns:
                continue

            freqs = (
                df_out[col]
                .value_counts(normalize=True, dropna=False)
                .to_dict()
            )

            train_frequencies[col] = {
                str(k): float(v)
                for k, v in freqs.items()
            }

            df_out[col] = df_out[col].apply(
                lambda x: (
                    x
                    if freqs.get(x, 0) >= threshold
                    else "Rare"
                )
            )

        return df_out, train_frequencies

    else:

        if train_frequencies is None:
            raise ValueError(
                "train_frequencies must be provided when is_train=False"
            )

        for col in cat_cols:

            if col in df_out.columns and col in train_frequencies:

                rare_categories = train_frequencies[col]

                if not isinstance(rare_categories, list):
                    rare_categories = []

                df_out[col] = df_out[col].apply(
                    lambda x: "Rare" if x in rare_categories else x
                )

        return df_out, train_frequencies