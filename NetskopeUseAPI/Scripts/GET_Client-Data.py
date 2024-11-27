# https://docs.netskope.com/en/netskope-platform-rest-apis.html

# Imports necessary modules
import os
import requests
from datetime import datetime, timedelta


# ---> Config
timestamp = datetime.now().timestamp()
timestamp_previous = (datetime.now() - timedelta(days=30)).timestamp()

current_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_dir, f'./.env')

from dotenv import load_dotenv
load_dotenv(env_path)

# Example .env tokens:
TENANT_URL = os.getenv('TENANT_URL') 
TOKEN = os.getenv('TOKEN') 
# ---> 


# ---> Function request
def get_netskope_users(tenant_url, api_token):

    url = f"https://{tenant_url}/api/v1/clients"

    headers = {'Content-Type': 'application/json'}
    body = {
        'token': api_token,
        'query': f'last_event_timestamp from {timestamp_previous} to {timestamp}',
        'limit': 5000
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=body)

    devices = []

    for i in response.json()['data']:
        user_os = i['attributes']['host_info']['os']
        user_device = i['attributes']['host_info']['hostname']
        user_name = i['attributes']['users'][0]['username']
        status = i['attributes']['last_event']['status_v2']
        devices.append({'Type': user_os, 'Device': user_device, 'User': user_name, 'Status': status})
    
    print(devices)

# --->

# Call main function
get_netskope_users(TENANT_URL, TOKEN)
