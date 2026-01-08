import requests
import sys

def requesting():
    try:
        # The URL that we request
        url = "https://jsonplaceholder.typicode.com/posts"

        # header/ Metadata
        header = {
            "User-Agent": "DataEngineerClient/1.0", 
            "Accept": "application/json"
        }

        parameters = {
            "_limit": 10, 
            "_page": 2
        }

        # requesting
        response = requests.get(url=url, headers=header, params=parameters, timeout=5)

        # Check for the status code
        if response.status_code == 200:
            print(f"Status code: {response.status_code}")
        else:
            response.raise_for_status()
        
        # Parse to json
        data = response.json()

        # Data validation
        if isinstance(data, list):
            print(f"Correct Data type: {type(data)}")
        else:
            print("Incorrect Data type")
            sys.exit()
        
        # Check for records
        if len(data) > 0:
            print(f"Total records: {len(data)}")
        else:
            print("Not data")
            sys.exit()
        
        # first record
        print(f"ID: {data[0]['id']}, UserID: {data[0]['userId']}, Title: {data[0]['title']}")
    

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


requesting()