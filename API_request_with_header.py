# API request with header 
import requests

url = "https://api.exchangerate.host/latest"

# Metadata about the request
header = {
    "Content-Type": "application/json", 
    "Accept": "application/json"
}

# Requesting for Data 
try:
    # Requesting for data
    response = requests.get(url=url, headers=header, timeout=10)
    # Check for server or client error
    response.raise_for_status()

    # Parse the data into a json file
    data = response.json()
    print(data)

# It will detect every kind of error
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")