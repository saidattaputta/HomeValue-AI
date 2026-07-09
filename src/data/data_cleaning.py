import pandas as pd

def handle_rare_categories(df, cat_cols, threshold=0.01, is_train=True, train_frequencies=None):
    """
    Groups rare categories in categorical columns into a single 'Rare' label 
    based on training set frequencies to prevent data leakage.
    """
    df_out = df.copy()
    
    if is_train:
        train_frequencies = {}
        for col in cat_cols:
            if col in df_out.columns:
                freqs = (
                    df_out[col]
                    .value_counts(normalize=True, dropna=False)
                    .to_dict()
                        )
                # Ensure keys are strings for clean JSON saving
                train_frequencies[col] = {str(k): v for k, v in freqs.items()}
                df_out[col] = df_out[col].apply(lambda x: x if freqs.get(x, 0) >= threshold else 'Rare')
        return df_out, train_frequencies
    else:
        if train_frequencies is None:
            raise ValueError("train_frequencies must be provided when is_train=False")
            
        for col in cat_cols:
            if col in df_out.columns and col in train_frequencies:
                freqs = train_frequencies[col]
                
                # Defensive check: If freqs somehow loaded as a list/unexpected type, default to empty dict
                if not isinstance(freqs, dict):
                    freqs = {}
                
                # Check both string and original type version of the category to protect against JSON type-casting
                df_out[col] = df_out[col].where(
                    df_out[col].map(lambda x: freqs.get(str(x), freqs.get(x, 0)) >= threshold),"Rare")
                
        return df_out, train_frequencies