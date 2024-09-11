"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node

from .nodes import filter_numeric_columns


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=filter_numeric_columns,
            inputs="games",
            outputs="numeric_games",
            name="filter_numeric_columns_node",
        )
    ])