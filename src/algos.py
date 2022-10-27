# write your algos here

from datetime import datetime
from typing import Dict, Tuple, Optional

import pandas as pd

def get_real_data(interval: Dict[str, datetime])->pd.DataFrame:
    """
    real data consist of index which is date and real price
    :return:
    """
    print(f"slice or real data from {interval['t_start_testing']} to {interval['t_end_testing']}")
    return pd.DataFrame()
def data_preparation(interval: Dict[str, datetime])->Tuple[pd.DataFrame,pd.DataFrame,pd.DataFrame]:
    """
    - this function takes interval in order to split data into training, validation and testing
    - in case your model does not take validation data, you can just split it into training and testing
    :param interval: walkforward interval
    :return: train_data, validation_data, testing_data
    """
    print("==============example of spliting into training, validation, testing=================")
    print(f"training data from {interval['t_start_training']} to {interval['t_start_validating']}")
    print(f"validation data from {interval['t_start_validating']} to {interval['t_start_testing']}")
    print(f"testing data from {interval['t_start_testing']} to {interval['t_end_testing']}")
    print("==============example of spliting into training, testing==============================")
    print(f"training data from {interval['t_start_training']} to {interval['t_start_testing']}")
    print(f"testing data from {interval['t_start_testing']} to {interval['t_end_testing']}")
    """
    - feel free to adjust your training and validation data but NOT testing data
    - remember that you CAN NOT change testing interval which is from interval['t_start_testing'] to interval['t_end_testing']
    - data don't have to be in pd.DataFrame, you are free to use any type of data such as numpy
    """
    return pd.DataFrame(),pd.DataFrame(),pd.DataFrame()


def run_training(train_data:pd.DataFrame, val_data:pd.DataFrame)->Optional['forecaster model']:
    return None


def run_testing(model:Optional['forecaster model'],test_data:pd.DataFrame)->pd.DataFrame:
    forecast_results=pd.DataFrame()
    return forecast_results


def calculate_metric(forecast_value:pd.DataFrame, real_value:pd.DataFrame) -> float:

    return 0.5
