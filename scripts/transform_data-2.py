import numpy as np
from sklearn.preprocessing import MinMaxScaler
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pandas as pd

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def transform_data(data_dict):
    """
    Transform the extracted data using pandas.

    Parameters:
    - data_dict: dict, keys as dataset names and values as pandas DataFrames.

    Returns:
    - transformed_data_dict: dict, keys as dataset names and values as transformed DataFrames.
    """
    # Unpack DataFrames
    web_traffic_df = data_dict["web_traffic"]
    customer_reviews_df = data_dict["customer_reviews"]

    # Handling missing values
    web_traffic_df.fillna(method="ffill", inplace=True)
    customer_reviews_df.dropna(subset=["Review"], inplace=True)

    # Normalize 'TrafficCount' feature
    scaler = MinMaxScaler()
    web_traffic_df['TrafficCount'] = scaler.fit_transform(web_traffic_df[['TrafficCount']])

    # Convert 'Timestamp' to datetime and extract features
    web_traffic_df['Timestamp'] = pd.to_datetime(web_traffic_df['Timestamp'])
    web_traffic_df['Year'] = web_traffic_df['Timestamp'].dt.year
    web_traffic_df['Month'] = web_traffic_df['Timestamp'].dt.month
    web_traffic_df['Day'] = web_traffic_df['Timestamp'].dt.day
    web_traffic_df['Hour'] = web_traffic_df['Timestamp'].dt.hour
    web_traffic_df['Minute'] = web_traffic_df['Timestamp'].dt.minute
    web_traffic_df['DayOfWeek'] = web_traffic_df['Timestamp'].dt.dayofweek
    web_traffic_df['DayOfYear'] = web_traffic_df['Timestamp'].dt.dayofyear
    web_traffic_df['WeekOfYear'] = web_traffic_df['Timestamp'].dt.isocalendar().week

    # Create cyclical features
    web_traffic_df['Hour_sin'] = np.sin(2 * np.pi * web_traffic_df['Hour'] / 24)
    web_traffic_df['Hour_cos'] = np.cos(2 * np.pi * web_traffic_df['Hour'] / 24)
    web_traffic_df['Month_sin'] = np.sin(2 * np.pi * web_traffic_df['Month'] / 12)
    web_traffic_df['Month_cos'] = np.cos(2 * np.pi * web_traffic_df['Month'] / 12)

    # Remove duplicates
    web_traffic_df.drop_duplicates(inplace=True)
    customer_reviews_df.drop_duplicates(inplace=True)

    # Customer Reviews: Text Processing
    # Lowercasing
    customer_reviews_df['cleaned_text'] = customer_reviews_df['Review'].str.lower()

    # Removing Punctuation
    customer_reviews_df['cleaned_text'] = customer_reviews_df['cleaned_text'].apply(
        lambda x: x.translate(str.maketrans('', '', string.punctuation))
    )

    # Tokenization
    customer_reviews_df['tokenized_text'] = customer_reviews_df['cleaned_text'].apply(word_tokenize)

    # Stop Words Removal
    stop_words = set(stopwords.words('english'))
    customer_reviews_df['tokenized_text'] = customer_reviews_df['tokenized_text'].apply(
        lambda x: [word for word in x if word not in stop_words]
    )

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    customer_reviews_df['lemmatized_text'] = customer_reviews_df['tokenized_text'].apply(
        lambda x: [lemmatizer.lemmatize(word) for word in x]
    )

    # Joining lemmatized words back into a single string
    customer_reviews_df['lemmatized_text'] = customer_reviews_df['lemmatized_text'].apply(
        lambda x: ' '.join(x)
    )

    # Sentiment Polarity and Subjectivity
    customer_reviews_df['sentiment_polarity'] = customer_reviews_df['lemmatized_text'].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )
    customer_reviews_df['subjectivity_score'] = customer_reviews_df['lemmatized_text'].apply(
        lambda x: TextBlob(x).sentiment.subjectivity
    )
    customer_reviews_df.rename(columns={'Review': 'original_review'}, inplace=True)


    # Visualization: Web Traffic Over Time
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=web_traffic_df, x='Timestamp', y='TrafficCount')
    plt.title('Web Traffic Over Time')
    plt.savefig('web_traffic_over_time.png')  # Save as an image file
    plt.close()  # Close the figure after saving

    # Visualization: Distribution of sentiment polarity
    plt.figure(figsize=(10, 6))
    sns.histplot(customer_reviews_df['sentiment_polarity'], bins=20, kde=True)
    plt.title('Distribution of Sentiment Polarity')
    plt.savefig('sentiment_polarity_distribution.png')  # Save as an image file
    plt.close()  # Close the figure after saving

    # Save transformed data to CSV files
    web_traffic_df.to_csv('transformed_web_traffic.csv', index=False)
    customer_reviews_df.to_csv('transformed_customer_reviews.csv', index=False)

    print(web_traffic_df.columns)
    print(customer_reviews_df.columns)

    # Store transformed DataFrames in a dictionary
    transformed_data_dict = {
        "web_traffic": web_traffic_df,
        "customer_reviews": customer_reviews_df
    }
    
    
    return transformed_data_dict
