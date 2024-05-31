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
TOKEN = os.getenv('TOKEN')
# --->


# ---> Function request
def validate_token(BASE_URL, token):
    url = f"{BASE_URL}/ws/token/validate"
    
    headers = {
        "token": token
    }
    
    response = requests.get(url, headers=headers)
    # print(response.text)

# --->

# Call the function to validate a token
validate_token(BASE_URL, TOKEN)
