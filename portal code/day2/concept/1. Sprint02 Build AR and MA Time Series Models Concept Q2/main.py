# Testcases wont pass

import pandas as pd
import os
import sys
from statsmodels.tsa.arima.model import ARIMA

# ---------- Input ----------
filename = input().strip()

# ---------- File Path ----------
file_path = os.path.join(sys.path[0], filename)

# ---------- Load Dataset ----------
df = pd.read_csv(file_path)

# ---------- Parse Datetime ----------
df["Datetime"] = pd.to_datetime(df["Datetime"])

# ---------- Set Datetime as index with monthly frequency ----------
df = df.set_index("Datetime")
df = df.asfreq("MS")

# ---------- Drop first record with missing differenced value ----------
df = df.dropna(subset=["Power_Consumption_diff"])

# ---------- Extract target series ----------
series = df["Power_Consumption_diff"]

# ---------- Train-Test Split (80:20) ----------
train_size = int(len(series) * 0.8)
train_data = series.iloc[:train_size]
test_data = series.iloc[train_size:]

# ---------- Output Sizes ----------
print(f"Training data size: {len(train_data)}")
print(f"Testing data size: {len(test_data)}")
print()

# ---------- AR(2) Model ----------
ar_model = ARIMA(train_data, order=(2, 0, 0))
ar_result = ar_model.fit()

print("AR(2) Model Summary:")
print(ar_result.summary())
print()

# ---------- MA(1) Model ----------
ma_model = ARIMA(train_data, order=(0, 0, 1))
ma_result = ma_model.fit()

print("MA(1) Model Summary:")
print(ma_result.summary())
