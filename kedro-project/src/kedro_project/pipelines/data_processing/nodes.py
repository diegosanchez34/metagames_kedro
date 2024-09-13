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


def eliminar_columnas(data: pd.DataFrame, columnas: list) -> pd.DataFrame:
    """
    Elimina las columnas especificadas de un DataFrame.

    Args:
        data (pd.DataFrame): El DataFrame de entrada.
        columnas (list): Lista de nombres de columnas a eliminar.

    Returns:
        pd.DataFrame: El DataFrame resultante con las columnas eliminadas.
    """
    # Eliminar las columnas especificadas
    data = data.drop(columns=columnas, errors='ignore')
    return data
