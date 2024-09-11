"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.8
"""

import numpy as np
import pandas as pd

def filter_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:

    # Filtrar solo las columnas numéricas
    numeric_df = df.select_dtypes(include=[np.number])

    return numeric_df