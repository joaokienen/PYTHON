# https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/authentication.htm

# Example .env tokens:
BASE_URL = os.getenv('BASE_URL') 
TOKEN = os.getenv('TOKEN') 
USER_ID = os.getenv('USER_ID') 
PASS_ID = os.getenv('PASS_ID') 

# Imports necessary modules
import os
import requests

def generate_token(BASE_URL, token):
    url = f"{BASE_URL}/ws/token/generate"
    
    # Set headers for the request including username, password, and validity of the token
    headers = {
        "username": USER_ID,  
        "password": PASS_ID,   
        "validity": "365"      
    }
    
    response = requests.get(url, headers=headers)
    print(response.text)

# Call the function to generate a token
generate_token(BASE_URL, TOKEN)
