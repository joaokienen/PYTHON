# https://documentation.securonix.com/bundle/securonix-cloud-user-guide/page/content/authentication.htm

# Example .env tokens:
BASE_URL = os.getenv('BASE_URL') 
TOKEN = os.getenv('TOKEN') 

# Imports necessary modules
import os
import requests

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
    print(response.text)

search_spotter(BASE_URL, TOKEN)
