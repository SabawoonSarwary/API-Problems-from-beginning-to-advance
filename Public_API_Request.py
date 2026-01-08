import requests
import sys

url = "https://jsonplaceholder.typicode.com/posts"


def requesting(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Status Code: {response.status_code}")
        # Check for server and client error
        response.raise_for_status()

        # Parse data into a json structure
        result = response.json()

        # Received data type
        print(f"Response Type: {type(result)}")

        if len(result) > 0:
            print(f"Total Records: {len(result)}")
        else:    
            print("Not Data")
            sys.exit()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    try:
        print(f"ID: {result[0]['id']}, UserID: {result[0]['userId']}, Title: {result[0]['title']}")
    except Exception as e:
        print(f"Error: {e}")
requesting(url)

