# https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/authentication.htm

# Imports necessary modules
import os
import requests

def validate_token(BASE_URL, token):
    # Construct the URL for token validate
    url = f"{BASE_URL}/ws/token/validate"
    
    # Set headers for the request including username, password, and validity of the token
    headers = {
        "token": token
    }
    
    # Send a GET request to the constructed URL with the headers
    response = requests.get(url, headers=headers)

    # Print the response content
    print(response.text)
    
    # Check if the response status code indicates success (200)
    if response.status_code == 200:
        print("Valid token.")   # Print message if token is valid
    else:
        print(f"Invalid token. Status code: {response.status_code}")  # Print message if token is invalid along with status code

# Example usage:
BASE_URL = os.getenv('BASE_URL')  # Get the base URL from environment variables
TOKEN = os.getenv('TOKEN')        # Get the token from environment variables

# Call the function to generate a token
validate_token(BASE_URL, TOKEN)
