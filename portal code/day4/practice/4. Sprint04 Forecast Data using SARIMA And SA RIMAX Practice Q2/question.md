Problem Statement 

A financial analytics team is analyzing historical monthly stock price data to understand seasonal trends and forecast future closing prices. The dataset contains market information such as opening price, high, low, closing price, volume, and derived indicators.

To build a reliable forecasting model, the analyst must preprocess the data, handle missing values, remove non-essential indicators, and apply a Seasonal ARIMA (SARIMA) model. The objective is to automate seasonal model selection while ensuring the solution runs safely on an online evaluation platform that may execute multiple test cases sequentially.

You are required to implement a robust, fault-tolerant Python program that reads the dataset dynamically, preprocesses it safely, performs an 80–20 train-test split, and attempts to build a SARIMA model using automated parameter selection. The program must handle missing libraries gracefully and never crash during evaluation.

 

CSV File Structure

Sample Data :

Date,Open,High,Low,Close,Volume,Close_diff,SMA_10,SMA_30,SES

2010-09-30 00:00:00,74.78619048,75.27190476,74.37142857,74.86142857,4068479.762,2.527792208,67.8628594,61.26061722,67.28532288

2010-10-31 00:00:00,76.81619048,77.33380952,76.41714286,76.83571429,4768821.905,1.974285714,69.31443083,61.90865619,68.80054402

2010-11-30 00:00:00,78.79619048,79.19238095,78.34666667,78.87380952,4220362.667,2.038095238,70.92949599,62.54371968,70.40757807

2010-12-31 00:00:00,77.76363636,78.00363636,77.37590909,77.64090909,3881497.773,-1.232900433,72.28148164,63.19395633,72.10082436

2011-01-31 00:00:00,74.747,75.13,74.063,74.4735,3571548.8,-3.167409091,73.15222294,63.71473966,73.20884131

2011-02-28 00:00:00,75.13578947,75.61368421,74.71052632,75.17736842,4156749.684,0.703868421,73.71557883,64.12968369,73.46177305

Input format :
CSV File Input:

The program prompts the user to enter the name of the CSV file containing the needed data.
Input must include the file extension .csv.
Output format :
Output Format 

The program should print outputs in the following fixed order: 

Dataset Preview – First few records 
Dataset Information – Structure and data types 
Missing Value Check – Before and after handling 
Train-Test Split Summary – Record counts 
SARIMA Model Summary Status – 
Printed only if SARIMA dependencies are available 
Otherwise, a clear skip message 

Refer to the sample output for exact formatting specifications. 

Code constraints :
Dataset Constraints 

Input file is a CSV supplied at runtime 
Must contain a Date column and Close price column 
Columns may contain missing values 

Program Constraints 

Filename must be read using input() 
File must be resolved using sys.path[0] 
No hardcoded paths or filenames 
All logic must be inside main() 
Non-standard modules must use conditional imports 

 

Sample test cases :
Input 1 :
Sample.csv
Output 1 :
Dataset Preview:
Date Open High ... SMA_10 SMA_30 SES
0 2006-01-31 00:00:00 34.854000 35.166500 ... NaN NaN 34.818000
1 2006-02-28 00:00:00 35.901579 36.162105 ... NaN NaN 34.818000
2 2006-03-31 00:00:00 34.624783 34.889130 ... NaN NaN 35.036189
3 2006-04-30 00:00:00 34.625263 34.901053 ... NaN NaN 34.963212
4 2006-05-31 00:00:00 34.499545 34.672273 ... NaN NaN 34.908044

[5 rows x 10 columns]

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 57 entries, 0 to 56
Data columns (total 10 columns):

# Column Non-Null Count Dtype

---

0 Date 57 non-null object
1 Open 57 non-null float64
2 High 57 non-null float64
3 Low 57 non-null float64
4 Close 57 non-null float64
5 Volume 57 non-null float64
6 Close_diff 56 non-null float64
7 SMA_10 48 non-null float64
8 SMA_30 28 non-null float64
9 SES 57 non-null float64
dtypes: float64(9), object(1)
memory usage: 4.6+ KB
None

Missing Value Check:
Open 0
High 0
Low 0
Close 0
Volume 0
Close_diff 1
dtype: int64
After missing value handling:
Open 0
High 0
Low 0
Close 0
Volume 0
Close_diff 0
dtype: int64

Train-Test Split:
Training records: 44
Testing records: 12

SARIMA Model Summary:
pmdarima not available. SARIMA modeling skipped.
