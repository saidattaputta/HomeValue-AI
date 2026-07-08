import os
import joblib
import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def create_preprocessor(num_cols, cat_cols):
    """
    Create a preprocessor for numerical and categorical features.

    Parameters:
    num_cols (list): List of numerical feature column names.
    cat_cols (list): List of categorical feature column names.

    Returns:
    ColumnTransformer: A preprocessor that can be used to transform the data.
    """
    
    num_pipeline = Pipeline(steps=[
        ('imputer',SimpleImputer(strategy='median')),
        ('scaler',StandardScaler())
    ])
    cat_pipeline = Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='most_frequent')),
    ('onehot',OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer([
    ('num',num_pipeline,num_cols),
    ('cat',cat_pipeline,cat_cols)
    ])

    return preprocessor