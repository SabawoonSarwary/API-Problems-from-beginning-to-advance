import requests
import sys

def requesting():
    try:
        # The URL that we request to
        url = "https://jsonplaceholder.typicode.com/posts"


        # Parameter
        parameter = {
            "userId": 1
        }

        response = requests.get(url=url, params= parameter, timeout=5)

        # Check for the status code
        if response.status_code == 200:
            print(f"Status code: {response.status_code}")
        else:
            response.raise_for_status()
        
        # parse data to json
        data = response.json()

        # Data type validation
        if isinstance(data, list):
            print(f"Received Data is: {type(data)}")
        else:
            print("Type of data is not list")
            sys.exit()
        
        # Check for total records
        if len(data) > 0:
            print(f"Total records: {len(data)}")
        else:
            print("No data")
            sys.exit()
        
        # first record
        print(f"ID: {data[0]['id']}, UserID: {data[0]['userId']}, Title: {data[0]['title']}")


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


requesting()        

