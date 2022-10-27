from datetime import datetime
import pytz
tz = pytz.timezone('UTC')


def str2datetime(date_time_data) -> datetime:
    if isinstance(date_time_data, datetime):
        return tz.localize(date_time_data)
    else:
        return tz.localize(datetime.strptime(date_time_data, '%Y-%m-%d'))


def datetime2str(date_time_data) -> str:
    if isinstance(date_time_data, str):
        return date_time_data
    else:
        return date_time_data.strftime("%Y-%m-%d")
