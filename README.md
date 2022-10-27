# 2022-data-science-take-home


## Code a forecaster

the detail instruction is provided in [this page](https://drive.google.com/drive/folders/1qoSrSde9dLzmDZ2s7QR7Hf67bD7fq8Dx)

In this section you are asked to code 'data preparation', 'training', and 'validation' pipeline

1. create your virtual environment
2. pip install -r requirements.txt
3. python main.py to run the entire pipeline


## Explanation for each script
 - alogs.py : this is where you should fill in the blank function with your code. these will be executed in main.py
 - config.py : path management. It is optional for you to use this. you can use this if you need to store your model
 - main.py: the pipeline from end to end

## src.walkforward.get_intervals
```python
from src.walkforward import get_intervals
walkforward_intervals = get_intervals(
t_start_validating="2021-06-27",
t_start_training="2020-06-27"
)
```
walkforward_intervals will give you time segmentation to perform walkforward validation.
your training, and testing data slice is govern by this


## Notes
- It is allowed to retreive more historical data by changing start_date in src.data.get_marketdata()
- You can change proportion for training and testing data by changing t_start_training and 
t_start_validating in src.walkforward.get_intervals
- the goal is for you to calculate avg_mae based on mae across different time interval
- You don't have to always follow the patterns in main.py or algos.py. You can try your best to be creative in this test.
- You are free to include other marketdata such as SNP500 to make multivariate timeseries