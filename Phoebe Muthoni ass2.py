import requests

# URL of the dataset
url = "https://gist.github.com/pravalliyaram/5c05f43d2351249927b8a3f3cc3e5ecf"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content of the response to a file
    with open("customer_dataset.csv", "wb") as file:
        file.write(response.content)
    print("Dataset downloaded successfully!")
else:
    print("Failed to download dataset.")

import pandas as pd

# Load the dataset into a DataFrame
try:
    df = pd.read_csv("customer_dataset.csv", encoding="utf-8", error_bad_lines=False)
    print("Dataset loaded successfully!")
    
    # Get the number of records (rows) in the DataFrame
    num_records = df.shape[0]
    print("Number of records:", num_records)

except Exception as e:
    print("Error:", e)
