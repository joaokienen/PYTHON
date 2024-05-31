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
def search_spotter(BASE_URL, token):
    url = f"{BASE_URL}/ws/spotter/index/search"
    
    query_parameters = {
        "query": 'index= activity | STATS @devicehostname @accountname @ipaddress',
        "eventtime_from": "03/04/2024 00:00:00",   
        "eventtime_to": "03/04/2024 23:59:59"     
    }
    
    headers = {
        "token": token
    }
    
    response = requests.get(url, params=query_parameters, headers=headers)
    # print(response.text)

# ---> 

# Call the function to get query results
search_spotter(BASE_URL, TOKEN)
