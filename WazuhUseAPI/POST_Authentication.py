# API Reference: https://documentation.wazuh.com/current/user-manual/api/reference.html

#################################### Part 0: Environment Evaluation ->

# Imports necessary modules
import os
import urllib3
import requests
from requests.auth import HTTPBasicAuth

# Disable insecure https warnings (for self-signed SSL certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# -------------->

# Getting variables
from dotenv import load_dotenv
load_dotenv("./.env")

API_URL = os.getenv("API_URL")
API_USER = os.getenv("API_USER")
API_PASS = os.getenv("API_PASS")



#################################### Part 1: API Request ->

# Generate endpoint
endpoint = f"{API_URL}/security/user/authenticate"

# API request
try:
    response = requests.post(endpoint, auth=HTTPBasicAuth(API_USER, API_PASS), verify=False).json()
    print(response)

except Exception as error: 
    print(error)