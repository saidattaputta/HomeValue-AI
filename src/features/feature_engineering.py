import numpy as np
import pandas as pd

def create_interaction_features(df):
    
    engineered_df = df.copy()
    
    # Create interaction features
    engineered_df['HouseAge'] = engineered_df['YrSold'] - engineered_df['YearBuilt']
    engineered_df['YearsSinceRemodel'] = engineered_df['YrSold'] - engineered_df['YearRemodAdd']
    engineered_df['GarageAge'] = engineered_df['YrSold'] - engineered_df['GarageYrBlt']
    
    # Total Bathrooms
    engineered_df['TotalBathrooms'] = (engineered_df['FullBath'] + 
                                        0.5 * engineered_df['HalfBath'] + 
                                        engineered_df['BsmtFullBath'] + 
                                        0.5 * engineered_df['BsmtHalfBath'])
    
    # Total Porch Area
    engineered_df['TotalPorchArea'] = (engineered_df['OpenPorchSF'] + 
                                        engineered_df['EnclosedPorch'] + 
                                        engineered_df['3SsnPorch'] + 
                                        engineered_df['ScreenPorch'])
    
    # Total Rooms
    engineered_df['TotalRooms'] = (engineered_df['TotRmsAbvGrd'] + 
                                    engineered_df['FullBath'] + 
                                    0.5 * engineered_df['HalfBath'])
    
    # Interaction Features
    engineered_df['Qual_LivingArea'] = engineered_df['OverallQual'] * engineered_df['GrLivArea']
    engineered_df['GarageCapacityArea'] = engineered_df['GarageCars'] * engineered_df['GarageArea']
    engineered_df['OverallQual_Squared'] = engineered_df['OverallQual'] ** 2
    
    return engineered_df