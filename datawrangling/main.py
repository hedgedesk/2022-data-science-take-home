"""
load Options update.csv in the datasets folder and follow the instruction in the following page
"""
import pandas as pd

def data_processing(df_raw:pd.DataFrame)->pd.DataFrame:
    """

    :param df_raw:
    :return:
    """

    return df_clean


if __name__ == '__main__':
    df_raw=pd.read_csv('data.csv')
    df_clean=data_processing(df_raw)