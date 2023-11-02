import requests
import datetime
import pandas as pd
import json

API_KEY = 'YOUR_API_KEY'  # Replace with your CoinMarketCap API key
API_URL = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
PARAMS = {
    'start': '1',
    'limit': '15',
    'convert': 'USD'
}

def get_crypto_data(api_url, params, api_key):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    try:
        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred while making the API request: {e}")
        return None

def update_csv(data, csv_filename):
    if data:
        timestamp = datetime.datetime.now()
        crypto_data = pd.json_normalize(data['data'])
        
        # Convert the 'Timestamp' column to datetime type
        crypto_data['Timestamp'] = pd.to_datetime(timestamp)
        
        try:
            existing_data = pd.read_csv(csv_filename)
        except FileNotFoundError:
            existing_data = pd.DataFrame()

        updated_data = pd.concat([existing_data, crypto_data])
        updated_data.to_csv(csv_filename, index=False)
        print(f"Data updated and saved to {csv_filename}")
    else:
        print("No data to process")

if __name__ == "__main__":
    crypto_data = get_crypto_data(API_URL, PARAMS, API_KEY)
    if crypto_data:
        update_csv(crypto_data, 'api_project.csv')
