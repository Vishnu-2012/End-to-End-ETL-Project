import psycopg2

def create_tables(connection):
    """
    Create tables in the PostgreSQL database.

    Parameters:
    - connection: psycopg2 connection object.
    """
    if connection is not None:
        cursor = connection.cursor()

        # Create web_traffic table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS web_traffic (
                timestamp TIMESTAMPTZ,
                traffic_count FLOAT,
                year INT,
                month INT,
                day INT,
                hour INT,
                minute INT,
                day_of_week INT,
                day_of_year INT,
                week_of_year INT,
                hour_sin FLOAT,
                hour_cos FLOAT,
                month_sin FLOAT,
                month_cos FLOAT
            );
        ''')

        # Create customer_reviews table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer_reviews(
                original_review TEXT,
                rating INT,  
                cleaned_text TEXT,
                tokenized_text TEXT[],
                lemmatized_text TEXT,
                sentiment_polarity REAL,
                subjectivity_score REAL
            );
        ''')

        connection.commit()
        cursor.close()
