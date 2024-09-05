import pandas as pd

def extract_data(web_traffic_path, customer_reviews_path):
    """
    Extract data from CSV files into pandas DataFrames.

    Parameters:
    - web_traffic_path: str, path to the web traffic CSV file.
    - customer_reviews_path: str, path to the customer reviews CSV file.

    Returns:
    - data_dict: dict, keys as dataset names and values as DataFrames.
    """
    web_traffic_df = pd.read_csv(your_path)
    customer_reviews_df = pd.read_csv(your_path)
    
    # Print the first few rows of each DataFrame
    print(web_traffic_df.head())
    print(customer_reviews_df.head())

    data_dict = {
        "web_traffic": web_traffic_df,
        "customer_reviews": customer_reviews_df
    }
    
    return data_dict
