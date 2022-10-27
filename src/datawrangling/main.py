"""
load Options.csv in the datasets folder and follow the instruction in the following page
"""
import pandas as pd
from src.config import Settings

settings = Settings()
def data_processing(df_raw:pd.DataFrame)->pd.DataFrame:
    """
    Perform data wrangling here so that
    :param df_raw:
    :return:
    """
    df_clean=df_raw
    return df_clean


if __name__ == '__main__':
    df_raw=pd.read_csv(settings.datasets_dir/"Options.csv")
    df_clean=data_processing(df_raw)
    print(df_clean)