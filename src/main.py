import numpy as np

from src.algos import run_training, run_testing, calculate_metric, get_real_data, data_slice, data_scaling
from src.config import Settings
from src.data import get_marketdata
from src.walkforward import get_intervals

settings = Settings()

if __name__ == '__main__':
    marketdata = get_marketdata(
        start_date="2015-01-01"
    )
    walkforward_intervals = get_intervals(
        t_start_validating="2021-06-27",
        t_start_training="2020-06-27"
    )
    list_mae = []
    for key, interval in walkforward_intervals.items():
        scaled_data=data_scaling(marketdata,interval)
        train_data, val_data, test_data = data_slice(scaled_data,interval)
        model = run_training(train_data, val_data)
        forecast_results = run_testing(model, test_data)

        real_data = get_real_data(interval)
        mae = calculate_metric(forecast_results, real_data)
        list_mae.append(mae)

    avg_mae = np.average(list_mae)
    print(avg_mae)
