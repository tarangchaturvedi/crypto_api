# cryptocurrency data updater

A Python script for fetching cryptocurrency data from the CoinMarketCap API and updating it in a CSV file.

## Features

- Fetches cryptocurrency data from the CoinMarketCap API.
- Updates the data in a CSV file, including a timestamp for each update.
- Provides error handling for API requests and data processing.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- CoinMarketCap API Key (Replace 'YOUR_API_KEY' with your actual key in the code).

## Usage
- Replace 'YOUR_API_KEY' with your actual CoinMarketCap API key in the code.
- The script will periodically update the data (defined by update_interval and no_itr in the code).
- The updated data will be saved to the api_project.csv file.

## Data Cleaning
After fetching and updating cryptocurrency data, you may need to clean and preprocess the data according to your specific requirements. Depending on your use case, you can implement additional data cleaning steps in the code, such as removing duplicates, handling missing values, or performing any data transformations.
## Contributing
Contributions are welcome! To contribute to this project, please follow these steps:

- Fork the project.
- Create a new branch with your feature or bug fix: git checkout -b feature/your-feature.
- Make your changes and commit them: git commit -m 'Add some feature'.
- Push to the branch: git push origin feature/your-feature.
- Submit a pull request.
