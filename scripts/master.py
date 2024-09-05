from extract_data import extract_data
from transform_data import transform_data
from create_tables import create_tables
from load_data import load_data_to_db
import psycopg2

web_traffic_path = yourpath
customer_reviews_path = yourpath
db_host = your_credentials
db_port = your_credentials
db_name = your_credentials
db_user = your_credentials
db_password = your_credentials
web_traffic_path = yourpath
customer_reviews_path = yourpath


data_dict = extract_data(web_traffic_path, customer_reviews_path)
transformed_data_dict = transform_data(data_dict)

try:
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )
    print("Connection to PostgreSQL DB successful")
    create_tables(connection)
    load_data_to_db(connection, transformed_data_dict)

except Exception as e:
    print(f"Error: {e}")

finally:
    if connection is not None:
        connection.close()
        print("PostgreSQL connection is closed")
