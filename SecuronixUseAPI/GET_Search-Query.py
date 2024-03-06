# Imports necessary modules
import os
import requests

def search_spotter(BASE_URL, token):
    # Construct the URL for spotter search
    url = f"{BASE_URL}/ws/spotter/index/search"
    
    # Define query parameters for the search
    query_parameters = {
        "query": 'index= activity | STATS @devicehostname @accountname @ipaddress',  # Define the search query
        "eventtime_from": "03/04/2024 00:00:00",   # Define the start time for the search
        "eventtime_to": "03/04/2024 23:59:59"      # Define the end time for the search
    }
    
    # Set headers for the request including the token
    headers = {
        "token": token  # Include the token obtained for authentication
    }
    
    # Send a GET request to the constructed URL with the query parameters and headers
    response = requests.get(url, params=query_parameters, headers=headers)

    # Print the response content
    print(response.text)
    
    # Check if the response status code indicates success (200)
    if response.status_code == 200:
        print("Successful request.")
        print(response.json())  # Here you can process the JSON response as needed
    else:
        print(f"Request failed. Status code: {response.status_code}")

# Example usage:
BASE_URL = os.getenv('BASE_URL')  # Get the base URL from environment variables
TOKEN = os.getenv('TOKEN')        # Get the token from environment variables

search_spotter(BASE_URL, TOKEN)   # Call the function to perform the spotter search
