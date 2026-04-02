# fetch_data.py

import requests
import pandas as pd

def get_clean_data():
    # -------------------------------
    # 1. Fetch data from API
    # -------------------------------
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        return pd.DataFrame()

    data = response.json()

    # -------------------------------
    # 2. Convert to DataFrame
    # -------------------------------
    df = pd.DataFrame(data)

    # -------------------------------
    # 3. Data Cleaning
    # -------------------------------
    df.rename(columns={"userId": "user_id"}, inplace=True)
    df.drop(columns=["id"], inplace=True)

    # -------------------------------
    # 4. Feature Engineering
    # -------------------------------
    df["post_length"] = df["body"].apply(len)

    # Observation:
    # post_length shows size of each post

    return df