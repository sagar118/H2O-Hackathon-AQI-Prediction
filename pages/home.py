from h2o_wave import ui

home_content = '''=
# Air Quality Forecasting in India: Using Machine Learning to Improve Public Health

<hr/>

Welcome to the dashboard for the "Predicting the Air Quality Index of Indian Cities using Machine Learning" competition, where the goal is to forecast the Air Quality Index (AQI) for major Indian AQI stations for the upcoming 28 days using machine learning techniques. 

Air quality monitoring is crucial for our well-being, and this competition utilizes historical daily averages of various air pollutants to build accurate models that can predict the AQI for each station. Our team has extensively analyzed the data and constructed models that we believe will help us achieve our objective. So, let us delve into our journey.

The dashboard consists of several tabs to analyze and visualize the dataset, our solution approach, and provide additional details about the pollutants. Firstly, the "Dashboard" tab allows you to visualize different features in the dataset and the target feature, AQI. This tab offers insights into how different pollutants are distributed and how the AQI varies across different stations, providing an essential understanding of the data.

Secondly, the "Solution" tab is dedicated to detailing our journey to build the solution, including preprocessing, visualizations, feature engineering, model tuning, and model explainability. This tab provides valuable information about our approach to building the best model to predict the AQI and can assist in getting an idea of the techniques we used in our models. This tab is particularly useful for participants who want to replicate or understand our methods better.

Finally, the "Appendix" tab contains more information about the different pollutants in the dataset and what they signify in detail. This tab provides a comprehensive understanding of the dataset, which can help in building better models by understanding the pollutants' effects and their role in determining the AQI.

In conclusion, this dashboard provides a wealth of resources and insights into the dataset and our approach to building accurate models for predicting the AQI. We hope this dashboard will aid participants in building exceptional models to forecast the AQI, and we look forward to seeing the submissions.

## Data Description

<hr/>

The dataset consists of historical daily average pollutants, including SO, CO, PM2.5, and other important factors that affect the air quality index. Keep in mind that different AQI stations have different lengths of historical data.

**train.csv** - 2 years of historical data for 40 Indian AQI stations
ID_Date: Unique identifier of state, stationid and date

*   `StateCode`: State where the AQI station is located
*   `StationId`: AQI station ID
*   `Date`: Date when the observations where recorded
*   `PM2.5`: Average PM2.5 pollutant level
*   `PM10`: Average PM10 pollutant level
*   `O3`: Average O3 pollutant level
*   `CO`: Average CO pollutant level
*   `SO2`: Average SO2 pollutant level
*   `AQI`: Average Air Quality Index - target variable

**Evaluation Metric**:

Submissions are evaluated on Modified Mean Absolute Error (MMAE) between forecasts and the actual values. The modification here is that it will penalize the under-predictions more heavily than over-predictions with a ratio of 1.5:1.
'''

home_page = ui.markdown_card(
    box='content',
    title='',
    content=home_content
)

'''
## Goal of the Competition

<hr/>

Air is what keeps humans alive. Monitoring it and understanding its quality is of immense importance to our well-being. In this hackathon, we're forecastiing the AQI for major Indian AQI stations for the upcoming 28 days. The dataset consists of the historical daily average of several air pollutants which directly affect the Air Quality Index.

We have analyzed the data and used it to build accurate models that can predict the AQI for each station.
'''