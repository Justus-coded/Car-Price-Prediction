import requests
from io import BytesIO
from typing import List
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    # response = requests.get(
    #             'https://github.com/Justus-coded/Car-Price-Prediction/blob/main/data/train.csv'
    #         )

    

    # if response.status_code != 200:
    #     raise Exception(response.text)

    df = pd.read_csv('https://github.com/Justus-coded/Car-Price-Prediction/blob/main/data/train.csv')
    #dfs.append(df)

    return df
    #return {}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'