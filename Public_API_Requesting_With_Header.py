import requests
import sys


def requesting():
    # The URL that we requesting
    url = "https://jsonplaceholder.typicode.com/posts"

    # Header/ Metadata
    header = {
        "User-Agent": "MyDataEngineeringClient/1.0", 
        "Accept": "application/json"
    }

    try:
        response = requests.get(url=url, headers=header, timeout=5)
        # Check for the succession Code
        if response.status_code == 200:
            print(f"Status Code: {response.status_code}")
        else:
            response.raise_for_status()

        data = response.json()

        # Check for the response Data Type validataion
        if isinstance(data, list):
            print(f"Type of Response: {type(data)}")
        else:
            print("Type of data is not list")
            sys.exit()
        
        # Check for the amount of Records
        if len(data) > 0:
            print(f"Total Records: {len(data)}")
        else:
            print("There is not data")
            sys.exit()
        
        # First post [id, userId, title]
        print(f"ID: {data[0]['id']}, UserID: {data[0]['userId']}, Title: {data[0]['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    

requesting()