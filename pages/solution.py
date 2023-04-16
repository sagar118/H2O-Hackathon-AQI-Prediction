import pandas as pd
import datetime as dt
from h2o_wave import ui
from utils.load_data import load_data

df = load_data('train.csv')

# Look at since when the data was collected for each state. Also, till when was the data collected.
grouped = df.groupby(by=["StateCode"])

start_dates = grouped.Date.min()
end_dates = grouped.Date.max()

date_df = pd.DataFrame(list(zip(start_dates.values, end_dates.values)), index=start_dates.index.values, columns=["StartDate", "EndDate"]).sort_values("StartDate")

date_df.StartDate = date_df.StartDate.apply(lambda x: x.date())
date_df.EndDate = date_df.EndDate.apply(lambda x: x.date())

date_df['Difference'] = date_df.EndDate - date_df.StartDate


content_md = f"""=
## Table of Contents
1. Exploratory Data Analysis
    1. Statistical Summary
    2. Missing Values
    3. Historical Data Range
2. Preprocessing
3. Feature Engineering
4. Model Building
5. Model Explanability
6. Model Results

As this is a time-series competition, we will begin our analysis by examining some fundamental statistics of the data. Subsequently, we will delve into the techniques employed for pre-processing, feature engineering, and the results of our models.

## Exploratory Data Analysis <a name="dashboard#eda"></a>
<hr/>

### <u>Statistical Summary</u>
We'll start with a brief overview on descriptive statistics and how they can be used to understand the data. 

*   `PM2.5`, `PM10`, `O3`, `CO`, `SO2`, `AQI` - These are numeric (float64) columns.
*   `StationId`: It is a numeric (int64) column.
*   `ID_Date`, `StateCode`, `Date` - These columns are of type object.

{df.describe().to_markdown()}

We find:

*   Maximum values for each feature are quite high compared to their 75% quartile range - refers to skewness present in the data.
*   Mean values are near to their median values expect for `PM2.5` and `AQI`.

### <u>Missing Values</u>

{df.isnull().sum().sort_values(ascending=False).to_markdown()}

*   There are some missing values present in the dataset. On further analysis (not shown here), we find that:
*   Particularly the majority of the missing values are for `Delhi` on 2nd & 3rd of August 2020.
*   Another instance of missing values is in `Karnataka` on 4th and 5th of January 2021.
*  The missing values are not random but are absent in the start of the data collection period. Hence, we planned to either impute the missing values or drop the rows with missing values.

### <u>Historical Data Range</u> 

{date_df.to_markdown()}

We find:

*   We observe that the start dates for each state varies.
*   `Delhi` has data for more than a year when compared to other states. This also indicates why we have more data for some states.

In depth EDA can be found in our `EDA notebook`.

## Preprocessing
<hr/>

**We dealt with the missing values by imputing them with the mean of the following two values.** We also checked for seasonality and stationarity of the data. We found that the data was not stationary and hence we applied differencing (1 level) to make it stationary. We also checked for autocorrelation and partial autocorrelation of the data.

Some checks we performed on the data while using the `VAR` (Vector Auto Regression) model:

The basis behind Vector AutoRegression is that each of the time series in the system influences each other. That is, you can predict the series with past values of itself along with other series in the system.

*   Testing Causation using Granger's Causality Test:
    *   Using Granger’s Causality Test, it’s possible to test this relationship before even building the model.
    *   Granger’s causality tests the null hypothesis that the coefficients of past values in the regression equation is zero.
    *   In simpler terms, the past values of time series (X) do not cause the other series (Y). So, if the p-value obtained from the test is lesser than the significance level of 0.05, then, you can safely reject the null hypothesis.
*   Cointegration Test:
    *   Cointegration is a statistical technique that can be used to determine if two or more time series are linearly dependent.
    *   If two time series are cointegrated, then it means they can be represented by a single equation with a linear combination of the two series.
    *   When two or more time series are cointegrated, it means they have a long run, statistically significant relationship.

Some checks we performed after creating the `VAR` model:
*   Check for Serial Correlation of Residuals (Errors) using Durbin Watson Statistic:
    *   Serial correlation of residuals is used to check if there is any leftover pattern in the residuals (errors).
    *   If there is any correlation left in the residuals, then, there is some pattern in the time series that is still left to be explained by the model. In that case, the typical course of action is to either increase the order of the model or induce more predictors into the system or look for a different algorithm to model the time series.
    *   So, checking for serial correlation is to ensure that the model is sufficiently able to explain the variances and patterns in the time series.

## Feature Engineering
<hr/>

We also tried to transform our target variable `AQI` using the BoxCox and Log transformations. Both of these transformations gave better results than the original data. **Among the two, the BoxCox transformation gave better results on the evaluation metric.**

## Model Building
<hr/>

Data used for training were a combination of either had none or one of the transformations applied to it. We made model for each state-station combination.

We tried various models like `Prophet`, `ARIMA`, `SARIMA`, `VAR`, and `LSTM`. 

*Note*: If the model paramters such as (p, d, q) were not specified, we used the `auto_arima` function from the `pmdarima` library to try and find the best parameters. Mentioning all the parameters for each model would have made the context too long. Hence, we have not mentioned them here.

Our take on the data distribution and model predictions is as follows:

*   Distribution of `AQI` in each state for different stations are more or less similar.
*   There were a few huge spikes in the data for `AQI` in 'Assam', 'Karnataka', and 'Tamil Nadu'.
*   There were also many data points were `AQI` had a plateaued value which we are not sure about. Either the data was not collected or the data was not recorded and hence the previous value was repeated.

Although we tried to tune the model for each time-series, we found that **ARIMA(7, 1, 2) with BoxCox Transformation worked the best across all the states-station pairs**.

## Model Explanability
<hr/>

Why does ARIMA(7, 1, 2) work the best?

*   There were many state-station pairs for which we had data less than a year. For such cases, there were not enough historical data points available for us to build accurate models.
*   We also didn't find any seasonality in the data. Hence, we SARIMA was not a good fit for the data.
*   The abrupt spikes and falls in the data does not follow any historical pattern.
*   The 7 in ARIMA(7,1,2) represents the number of autoregressive terms used in the model, the 1 represents the degree of differencing used to make the series stationary, and the 2 represents the number of moving average terms used in the model.
    *   In simpler terms, ARIMA(7,1,2) tries to capture the patterns and trends in the time series data by looking at the values from 7 time periods ago and combining them in different ways with the current value. 
    *   It also takes into account the difference between consecutive values to account for any trends in the data. (Make it stationary).
    *   Finally, it looks at the moving average of the values to smooth out any noise or fluctuations in the data. 
*   **Meaning recent values are more important than the older values which makes sense cause `AQI` doesn't follow any climatic pattern and is more dependent on the current pollution levels.**


## Model Results
<hr/>

Below are the results of the models on the test (submission) data.

| Model | Transformation Technique | MMAE |
| --- | --- | --- |
| VAR | - | 32.2173 |
| Prophet | - | 34.5853 |
| Holt Smoothing | - | 30.979 |
| SARIMA | - | 32.2173 |
| ARIMA (auto-arima) | BoxCox | 29.7475 |
| ARIMA (auto-arima) | Log | 29.4992 |
| ARIMA (7,1,2) | - | 28.942 |
| ARIMA (7,1,2) | Log | 28.0175 |
| **ARIMA (7,1,2)** | **BoxCox** | **28.0001** |
| ARIMA (7,1,2) | Differencing only if not stationary | 30.09 |


"""

sol_md = ui.markdown_card(
    box='sol_content',
    title='',
    content=content_md
)