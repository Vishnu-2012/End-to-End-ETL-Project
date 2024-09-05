
# E-commerce ETL Pipeline with Data Analysis and Sentiment Insights

## Project Overview

This project aims to build a robust ETL (Extract, Transform, Load) pipeline for processing and analyzing e-commerce web traffic and customer reviews data. Our objective is to generate actionable insights that help improve business decisions related to marketing strategies and customer satisfaction.

## Data Sources

We used two primary datasets:
- **Web Traffic Data** (`web_traffic.csv`): Timestamped data of website visits, including traffic count over time.
- **Customer Reviews Data** (`tripadvisor_hotel_reviews.csv`): User-generated reviews and ratings for hotels, containing text feedback and rating scores.

## Data Extraction

Data was extracted from CSV files using Python's `pandas` library. The extraction process ensured all relevant fields were captured and handled potential data inconsistencies.

## Data Transformation

### Web Traffic Data:
- **Missing Data Handling**: Missing values were forward-filled.
- **Normalization**: The `TrafficCount` column was normalized using `MinMaxScaler`.
- **Feature Engineering**: We created features like `Year`, `Month`, `Day`, `Hour`, and cyclical features (`Hour_sin`, `Month_cos`) from the `Timestamp` column to capture temporal trends.
  
### Customer Reviews Data:
- **Text Processing**: We performed a series of steps to clean the text, including:
  - Lowercasing
  - Removing punctuation
  - Tokenization
  - Removing stop words
  - Lemmatization
- **Sentiment Analysis**: Sentiment polarity and subjectivity scores were calculated using the `TextBlob` library to analyze customer satisfaction.

## Data Loading

The cleaned and transformed data was loaded into a PostgreSQL database with two main tables:
1. **Web Traffic**: Stores normalized traffic data with timestamp-related features.
2. **Customer Reviews**: Contains original and processed review text along with sentiment scores.

## Data Analysis

### Web Traffic Analysis:
We analyzed traffic patterns over time to identify peak periods and daily/monthly trends. Cyclical features like `Hour_sin` and `Month_sin` revealed periodic patterns in web usage.

### Sentiment Analysis:
Sentiment analysis on customer reviews provided insights into customer satisfaction. We analyzed the distribution of sentiment polarity to identify positive and negative reviews.

### Visualizations:
- **Web Traffic**: Time-series plots to visualize traffic trends.
- **Sentiment Polarity**: Histograms showing sentiment distribution.
- **Word Cloud**: A word cloud of frequently mentioned terms in reviews.

## Insights and Conclusions

### Key Findings:
- **Web Traffic**: Peak traffic occurs during specific hours and months, suggesting a need for targeted marketing during these periods.
- **Customer Sentiment**: Sentiment analysis highlighted both positive and negative aspects of customer feedback, providing clear areas for business improvement.

### Recommendations:
- Optimize website performance during peak hours.
- Address common customer concerns identified through sentiment analysis to improve customer satisfaction.

## Future Work

- Integrate transaction data to provide deeper insights into customer behavior.
- Implement real-time data processing for more immediate insights.

## License

This project is licensed under the MIT License.

