## Data Wrangling
You are asked to clean and transform the data in datasets/Options update.csv 
into a table described in [this page](https://docs.google.com/document/d/1jzxk1itNAUgwmJIzWonfWh8PlGJTIb0yvbpnKrwbyJQ/edit?usp=sharing)


## Columns of clean data

- date : get this from "Trade Date"
- pair : extracted from Reference Company and Security Description
  - e.g. 
    - CADSWO=R -> US Dollar/Canadian Dollar Spot Week ATM Option (CAD map to USD/CAD)
    - EURSWO=R -> Euro/US Dollar Spot Week ATM Option (EUR map to EUR/USD)
- tenor : extracted from Reference Company and Security Description
  - tenor variation:SW,1M,2M,3M,6M,9M,1Y,2Y
- name : extracted from Reference Company and Security Description
  - name variation:O=,O=R,10P,25P,45P,10C,25C,45C,RR,BF,R10,B10
  - change 'O=R' to 'A' and 'O=' to 'A'
- close : close. simply copy the value

## Example
![image](https://user-images.githubusercontent.com/91622834/198265712-a18a5da9-eb3b-43dd-a088-93feb9df6726.png)





## Instruction

1. read data from csv
2. Process, clean, and map these data to the format in the instruction. The data should be in pandas.DataFrame
3. Generate values (append the table) for the reverse currencies. 
4. Visualize the data



