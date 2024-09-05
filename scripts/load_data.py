def load_data_to_db(connection, transformed_data_dict):
    """
    Load transformed data into the PostgreSQL database.

    Parameters:
    - connection: psycopg2 connection object.
    - transformed_data_dict: dict, keys as dataset names and values as transformed DataFrames.
    """
    if connection is not None:
        cursor = connection.cursor()

        # Load data into web_traffic table
        web_traffic_df = transformed_data_dict['web_traffic']
        for index, row in web_traffic_df.iterrows():
            cursor.execute('''
                INSERT INTO web_traffic (timestamp, traffic_count, year, month, day, hour, minute, 
                day_of_week, day_of_year, week_of_year, hour_sin, hour_cos, month_sin, month_cos) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            ''', tuple(row))

        # Load data into customer_reviews table
        customer_reviews_df = transformed_data_dict['customer_reviews']
        for index, row in customer_reviews_df.iterrows():
            cursor.execute('''
                INSERT INTO customer_reviews (original_review, cleaned_text, tokenized_text, lemmatized_text, sentiment_polarity, subjectivity_score) 
                VALUES (%s, %s, %s, %s, %s, %s);
            ''', (
                row['Review'],
                row['cleaned_text'],
                row['tokenized_text'],  # Convert list to string if necessary
                row['lemmatized_text'],
                row['sentiment_polarity'],
                row['subjectivity_score']
            ))

        connection.commit()
        cursor.close()
        print("Data loaded successfully")
