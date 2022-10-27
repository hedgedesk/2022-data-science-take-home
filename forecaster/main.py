import numpy as np

from forecaster.algos import run_training, run_testing, calculate_metric, get_real_data, data_slicing, data_scaling
from forecaster.config import Settings
from forecaster.data import get_marketdata
from forecaster.walkforward import get_intervals

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
        train_data, val_data, test_data = data_slicing(scaled_data,interval)
        model = run_training(train_data, val_data)
        forecast_results = run_testing(model, test_data)

        real_data = get_real_data(marketdata,interval)
        mae = calculate_metric(forecast_results, real_data)
        list_mae.append(mae)

    avg_mae = np.average(list_mae)
    print(avg_mae)
