# https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/authentication.htm

# Example .env tokens:
BASE_URL = os.getenv('BASE_URL') 
TOKEN = os.getenv('TOKEN') 

# Imports necessary modules
import os
import requests

def validate_token(BASE_URL, token):=
    url = f"{BASE_URL}/ws/token/validate"
    
    headers = {
        "token": token
    }
    
    response = requests.get(url, headers=headers)
    print(response.text)

# Call the function to validate a token
validate_token(BASE_URL, TOKEN)
