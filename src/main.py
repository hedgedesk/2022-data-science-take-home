from src.config import Settings
from src.data import get_marketdata
from src.walkforward import get_intervals
settings = Settings()


if __name__ == '__main__':
    marketdata = get_marketdata(
        start_date="2022-10-30",
        end_date="2015-01-01",
    )
    times = get_intervals(
        t_start_validating="2021-06-27",
        t_start_training="2020-06-27"
    )
