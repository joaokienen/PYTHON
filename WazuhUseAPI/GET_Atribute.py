# API Reference: https://documentation.wazuh.com/current/user-manual/api/reference.html

#################################### Part 0: Environment Evaluation ->

# Imports necessary modules
import os
import urllib3
import requests

# Disable insecure https warnings (for self-signed SSL certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# -------------->

# Getting variables
from dotenv import load_dotenv
load_dotenv("./.env")

API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")



#################################### Part 1: API Request ->

# Generate endpoint variables
endpoint = f"{API_URL}/syscollector/{453}/netiface"
params = {"select": "mac"}
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# API request
try:
    response = requests.get(endpoint, headers=headers, params=params, verify=False).json()
    print(response)

except Exception as error: 
    print(error)