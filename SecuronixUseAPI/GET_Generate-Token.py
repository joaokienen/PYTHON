# https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/authentication.htm

# Imports necessary modules
import os
import requests


# ---> Config
current_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_dir, f'./.env')

from dotenv import load_dotenv
load_dotenv(env_path)

# Example .env tokens:
BASE_URL = os.getenv('BASE_URL') 
USER_ID = os.getenv('USER_ID') 
PASS_ID = os.getenv('PASS_ID') 
# --->


# ---> Function request
def generate_token(BASE_URL):
    url = f"{BASE_URL}/ws/token/generate"
    
    headers = {
        "username": USER_ID,  
        "password": PASS_ID,   
        "validity": "365"      
    }
    
    response = requests.get(url, headers=headers)
    # print(response.text)

# --->

# Call the function to generate a token
generate_token(BASE_URL)
