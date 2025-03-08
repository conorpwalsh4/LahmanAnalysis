import pandas as pd

def avoid_overlap(df, threshold=3):
    to_keep = []
    prev_index = -threshold - 1  # Initial value to ensure first row is kept
    
    for index in df.index:
        if index >= prev_index + threshold:
            to_keep.append(index)
            prev_index = index
            
    return df.loc[to_keep]

def min_max_norm(data:pd.DataFrame, column_name:str):
    """
    Apply min-max normalization to a specified column in a dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    column_name (str): The name of the column to normalize.

    Returns:
    pd.Series: The normalized column.
    """
    min_val = data[column_name].min()
    max_val = data[column_name].max()
    normalized_column = (data[column_name] - min_val) / ((max_val - min_val) + 1e-6)
    
    return normalized_column

def mean_normalization(data:pd.DataFrame, column_name:str):
    """
    Apply meannormalization to a specified column in a dataframe.

    Parameters:
    df (pd.DataFrame): The dataframe containing the data.
    column_name (str): The name of the column to normalize.

    Returns:
    pd.Series: The normalized column.
    """ 
    min_val = data[column_name].min()
    max_val = data[column_name].max()
    mean_val = data[column_name].mean()

    normalized_column = (data[column_name] - mean_val) / ((max_val - min_val) + 1e-6)

    return normalized_column