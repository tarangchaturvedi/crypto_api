import requests
import datetime
import pandas as pd
import json
import time

def api_runner():
    session = requests.Session()

    json_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
        }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
        }


    # Get the current timestamp
    timestamp = datetime.datetime.now()
    # Send an HTTP GET request to the JSON URL with the specified headers within the session
    response = session.get(json_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Load the JSON data
        try:
            data = json.loads(response.text)
        except json.JSONDecodeError:
            print("Failed to parse JSON response.")
            data = None

        if data:
            # Normalize the JSON data and create a DataFrame
            crypto_data = pd.json_normalize(data['data'])

            # Example: Extract and process data from the normalized DataFrame
            # (Modify this part according to the JSON structure)
            crypto_data['Timestamp'] = timestamp
            crypto_data['Timestamp'] = pd.to_datetime(crypto_data['Timestamp'])

            # Load the existing data from the CSV file (if it exists)
            csv_filename = 'E:\\projects\\crypto_api\\api_project.csv'
            try:
                existing_data = pd.read_csv(csv_filename)
            except FileNotFoundError:
                existing_data = pd.DataFrame()

            # Concatenate the new data with the existing data (if any)
            updated_data = pd.concat([existing_data, crypto_data])

            # Save the updated data to the CSV file
            updated_data.to_csv(csv_filename, index=False)

            print(f"Data updated and saved to {csv_filename}")
        else:
            print("No data to process.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

    #print(crypto_data.head(4))
