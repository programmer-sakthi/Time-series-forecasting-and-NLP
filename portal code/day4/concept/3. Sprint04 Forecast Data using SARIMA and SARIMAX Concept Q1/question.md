Problem Description:

This problem focuses on modeling and forecasting monthly power consumption using a Seasonal ARIMA (SARIMA) model to capture both long-term trends and seasonal patterns present in the data. Power consumption data typically exhibits strong annual seasonality due to climatic cycles and recurring events, making SARIMA an appropriate choice.

The dataset consists of time-stamped monthly consumption values along with contextual information such as festivals and special events. The analysis primarily models the Consumption series, while differencing and seasonal components are used internally by the SARIMA model to achieve stationarity.

1. Use the SARIMA Model to Make Predictions

The Datetime column is converted to a datetime index to enable time-series operations.
Missing values are checked and removed to ensure data consistency.
The dataset is split into training (80%) and testing (20%) sets.
A SARIMA model is automatically selected using auto_arima with:
Seasonality enabled (seasonal=True)
Seasonal period m = 12, reflecting yearly seasonality in monthly data.

The selected model structure is:

SARIMA((1, 0, 2) × (0, 1, [1], 12)), which includes:

Non-seasonal AR(1) and MA(2) terms,
Seasonal differencing of order 1,
A seasonal MA term at lag 12.

Using this fitted model, forecasts are generated for the entire test period.

2. Forecast Visualization and Interpretation

The SARIMA Forecast Plot displays:

Training data (blue),
Actual test observations (orange dashed),
Forecasted values (green dashed).

Interpretation:

The SARIMA model effectively captures the upward trend and repeating seasonal cycles in power consumption.
Forecasted values closely follow the seasonal peaks and troughs of the actual data.
Minor deviations occur during extreme demand periods, but overall alignment is strong, indicating good predictive performance.

3. Evaluation Metrics

To quantitatively assess forecast accuracy, standard evaluation metrics are calculated:

MAE (Mean Absolute Error) – average deviation between actual and predicted consumption.
MAPE (Mean Absolute Percentage Error) – relative error expressed as a percentage.
RMSE (Root Mean Squared Error) – emphasizes larger forecasting errors.

The metric values demonstrate that the SARIMA model outperforms non-seasonal models (AR, MA, ARMA, ARIMA) by effectively accounting for recurring seasonal patterns.

4. Residual Analysis and Model Adequacy

Residual diagnostics are performed to verify that the SARIMA model has captured all systematic information in the data:

Residual time plot shows random fluctuations around zero with no visible trend or seasonality.
Absence of autocorrelation in residuals indicates that temporal dependence has been adequately modeled.
Residuals resemble white noise, satisfying a key assumption of SARIMA modeling.

Conclusion

The SARIMA((1, 0, 2) × (0, 1, [1], 12)) model:

Successfully captures both trend and annual seasonality in monthly power consumption,
Produces accurate and stable forecasts,
Passes residual diagnostics, confirming model adequacy.

This makes SARIMA a robust and reliable approach for medium- to long-term power consumption forecasting. Further improvements may be achieved by incorporating exogenous variables (SARIMAX) such as festivals or weather conditions.
