Problem Statement 

Electricity consumption data often exhibits temporal dependency, seasonal variations, and short-term fluctuations influenced by external factors such as festivals or special events. To analyze such patterns effectively, time series modeling techniques are commonly used. 

In this problem, you are provided with a cleaned and pre-processed electricity consumption dataset containing monthly observations along with a datetime index and derived differenced values. Your task is to explore the time series characteristics of electricity consumption, identify potential autoregressive and moving average components, and prepare the data for model fitting. 

Specifically, you will: 

Load and inspect the electricity consumption dataset 
Convert the datetime column into a proper time index 
Handle missing values safely 
Generate ACF and PACF plots to identify suitable AR and MA orders 
Split the dataset into training and testing sets using an 80–20 ratio for future forecasting and evaluation 

This process forms the foundation for building reliable ARIMA or ARMA models for electricity consumption forecasting. 

 

CSV File Structure

Sample Data ;

Datetime,Consumption,Festivals/Special_events,Power_Consumption_diff

2002-11-01,117.2025,7,1.5615999999999985

2002-12-01,129.5113,8,12.308800000000005

2003-01-01,137.2301,5,7.7187999999999874

2003-02-01,129.2989,3,-7.93119999999999

2003-03-01,123.0927,6,-6.20620000000001

2003-04-01,116.4425,8,-6.650199999999998

2003-05-01,119.4552,5,3.0127000000000095

Input format :
CSV File Input:

The program prompts the user to enter the name of the CSV file containing the needed data.
Input must include the file extension .csv.
Output format :
Output Format 

The program must print outputs in the following fixed order: 

Dataset Preview 
Display the first five rows of the dataset 
Dataset Structure Information 
Show column names, data types, and non-null counts 
Missing Value Check 
Print missing value counts before and after handling them 
ACF and PACF Analysis Status 
Indicate whether ACF and PACF plots were generated or skipped 
Train–Test Split Information 
Display the number of records in the training dataset 
Display the number of records in the testing dataset  

Refer to the sample output for exact formatting specifications. 

Code constraints :
Constraints 

CSV File Constraints 

The CSV file is provided as input at runtime 
The file exists in the same directory as the Python script 
Column names are case-sensitive 
Required columns: 
Datetime 
Consumption 

Data Constraints 

Datetime must be convertible to a datetime format 
Consumption values must be numeric 
Missing values must be handled gracefully without crashing the program 

Program Constraints 

Must use the pandas library 
Must read the filename using input() 
Must not fail if optional modules are unavailable 
Must work correctly when multiple test cases are executed together 
Must not hardcode file names or file paths 
Sample test cases :
Input 1 :
Sample.csv
Output 1 :
Dataset Preview:
Datetime Consumption Festivals/Special_events Power_Consumption_diff
0 1988-01-01 107.5052 6 NaN
1 1988-02-01 105.6720 1 -1.8332
2 1988-03-01 97.4502 1 -8.2218
3 1988-04-01 92.4714 1 -4.9788
4 1988-05-01 90.3151 1 -2.1563

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50 entries, 0 to 49
Data columns (total 4 columns):

# Column Non-Null Count Dtype

---

0 Datetime 50 non-null object
1 Consumption 50 non-null float64
2 Festivals/Special_events 50 non-null int64  
 3 Power_Consumption_diff 49 non-null float64
dtypes: float64(2), int64(1), object(1)
memory usage: 1.7+ KB
None

Missing Value Check:
Consumption 0
Festivals/Special_events 0
Power_Consumption_diff 1
dtype: int64
After missing value handling:
Consumption 0
Festivals/Special_events 0
Power_Consumption_diff 0
dtype: int64

ACF and PACF Analysis:
Time series module not available. Skipping ACF/PACF plots.

Train-Test Split:
Training records: 39
Testing records: 10
