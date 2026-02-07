Problem Description:

SARIMAX Modeling with External Variables and Granger Causality Analysis

This task extends the SARIMA model by incorporating external (exogenous) variables to improve forecasting accuracy using a SARIMAX framework. The workflow evaluates whether external factors (e.g., festivals/special events) have predictive power for power consumption and assesses the resulting model both visually and quantitatively.

1. Granger Causality Test

The Granger Causality test is used to examine whether past values of an external variable help predict the target variable (Consumption).

Methodology:

The test is conducted between:
Consumption (target)
Festivals/Special_events (exogenous variable)
Lags from 1 to 12 months are evaluated.
The null hypothesis: The external variable does not Granger-cause the target variable.

Interpretation:

p-value < 0.05 at any lag ⇒ Reject the null hypothesis → the external variable provides statistically significant predictive information.
p-value ≥ 0.05 ⇒ No significant causal relationship at that lag.

If one or more lags show statistically significant p-values, it justifies including the external variable in the SARIMAX model.

2. SARIMAX Model Specification and Fitting

Based on parameters selected via auto_arima, the following structure is used:

Non-seasonal order (p, d, q): (1, 0, 2)
Seasonal order (P, D, Q, s): (0, 1, 1, 12)
Exogenous variable: Festivals/Special_events

The SARIMAX model is trained on the training dataset, incorporating both:

Autoregressive and moving-average components,
Seasonal differencing to handle annual seasonality,
External regressors to capture event-driven consumption changes.

3. Forecast Generation

Using the fitted SARIMAX model:

Forecasts are generated for the test period.
The corresponding exogenous values for the test set are supplied to ensure consistency.

This allows the model to adjust forecasts dynamically based on expected festival or special event intensity.

4. Visualization and Performance Check

The forecast plot compares:

Training data (blue),
Actual test data (orange dashed),
SARIMAX forecasts (green dashed).

Observations:

The SARIMAX forecasts track the seasonal fluctuations more closely than SARIMA alone.
Peaks during high-event periods are better captured due to the inclusion of external information.
Overall alignment with actual values indicates improved model responsiveness.

5. Quantitative Evaluation Metrics

The SARIMAX model is evaluated using:

MAE (Mean Absolute Error): Measures average absolute forecast error.
MAPE (Mean Absolute Percentage Error): Indicates relative forecasting accuracy in percentage terms.
RMSE (Root Mean Squared Error): Penalizes larger errors more heavily.

﻿

Lower values across these metrics—especially when compared to SARIMA and Seasonal Naïve baselines—confirm the effectiveness of including exogenous variables.

Conclusion

The Granger Causality test validates whether external variables have predictive power.
The SARIMAX model successfully integrates seasonality, autocorrelation, and external influences.
Visual and metric-based evaluations indicate improved forecasting accuracy over models without exogenous inputs.
SARIMAX is particularly suitable for power consumption forecasting where events and external drivers play a significant role.

This structured approach ensures both statistical justification and practical forecasting improvements.

