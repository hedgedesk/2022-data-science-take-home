import pandas as pd
import yfinance as yf

from forecaster.date import str2datetime


def get_marketdata(
        tickers: str = 'USDGBP=X',
        start_date: str = "2015-01-01",
        end_date: str = "2022-10-30",
        interval: str = '1d'
) -> pd.DataFrame:
    """
    :param start_date: str
    :param end_date: str
    :param interval: str
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
            Intraday data cannot extend last 60 days
    :return:
    """
    marketdata = yf.download(tickers, start=str2datetime(start_date), end=str2datetime(end_date), interval=interval)
    marketdata["Day"] = marketdata.reset_index()["Date"].dt.day_name().copy().tolist()
    return marketdata
