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

def data_scaling(data:pd.DataFrame,interval: Dict[str, datetime])->pd.DataFrame:
    """
    Perform scaling here
    :param data: marketdata
    :param interval: scaling params such as mean or var should be calculated only use training data
    :return:
    """
    scaled_data = data
    return scaled_data

def data_slice(data:pd.DataFrame,interval: Dict[str, datetime]):
    """
    - split data into training, validation and testing
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

    train_data=data.loc[interval['t_start_training']:interval['t_start_validating']]
    val_data=data.loc[interval['t_start_validating']:interval['t_start_testing']]
    test_data=data.loc[interval['t_start_testing']:interval['t_end_testing']]
    return train_data, val_data, test_data



def run_training(train_data:pd.DataFrame, val_data:Optional[pd.DataFrame]=None):
    """
    Use train_data and val_data to train your model
    :param train_data:
    :param val_data:
    :return: model
    """
    return None


def run_testing(model,test_data:pd.DataFrame)->pd.DataFrame:
    """
    :param model: your ai model
    :param test_data: test data
    :return: forecasting result for test_data
    """
    forecast_results=pd.DataFrame()
    return forecast_results


def calculate_metric(forecast_value:pd.DataFrame, real_value:pd.DataFrame) -> float:
    """
    calculate metric for forecast_value and real_value
    :param forecast_value: 
    :param real_value: 
    :return: 
    """
    return 0.5
