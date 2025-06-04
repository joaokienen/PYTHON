# https://docs.netskope.com/en/netskope-platform-rest-apis.html

# Imports necessary modules
import os
import requests
from datetime import datetime, timedelta

# Vault DevOps
from delinea.secrets.vault import (
    PasswordGrantAuthorizer,
    SecretsVault,
    SecretsVaultAccessError,
    SecretsVaultError,
    VaultSecret
)


# ---> Config
current_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_dir, f"./.env")

timestamp = int(datetime.now().timestamp())
timestamp_previous = int((datetime.now() - timedelta(days=30)).timestamp())
# ---> 


# ---> Function request
def get_netskope_users(tenant_url, api_token):
    
    url = f"https://{tenant_url}/api/v1/clients"
    headers = {"Content-Type": "application/json"}
    
    skip = 0
    limit = 5000
    devices = []

    while True:
        body = {
            "token": api_token,
            "query": f"last_hostinfo_update_timestamp from {timestamp_previous} to {timestamp}",
            "limit": limit,
            "skip": skip
        }

        response = requests.post(url, headers=headers, json=body)
        data = response.json().get("data", [])
        if not data: break 

        for item in data:
            try:
                user_os = item["attributes"]["host_info"]["os"]
                user_device = item["attributes"]["host_info"]["hostname"]
                user_name = item["attributes"]["users"][0]["username"]
                status = item["attributes"]["last_event"]["status_v2"]
                devices.append({
                    "Type": user_os,
                    "Device": user_device,
                    "User": user_name,
                    "Status": status
                })
            except (KeyError, IndexError): continue

        skip += limit

    print(len(devices))
    return devices
# --->


# ---> Call main function with Vault
from dotenv import load_dotenv
if os.path.exists(env_path):
    
    load_dotenv(env_path)

    # Get .env variables
    BASE_URL = os.getenv("BASE_URL")
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    PATH_ID = os.getenv("PATH_ID")

    # If valid itens
    if BASE_URL and CLIENT_ID and CLIENT_SECRET and PATH_ID:

        # Init extract data
        try:

            # Getting variables in Delinea DevOps
            authorizer = PasswordGrantAuthorizer(BASE_URL, CLIENT_ID, CLIENT_SECRET)  
            vault = SecretsVault(BASE_URL, authorizer)
            secret = VaultSecret(**vault.get_secret(PATH_ID))
            
            # Define local variables
            TENANT_URL = secret.data["TENANT_URL"]
            TOKEN = secret.data["TOKEN"]

            # Call main function
            get_netskope_users(TENANT_URL, TOKEN)


        # Except errors
        except SecretsVaultAccessError as e:
            print(e.message)

        except SecretsVaultError as e:
            print(e.response.text)

    else:
        print(".env file exists but is missing some variables!")

else:
    print(".env file does not exist!")
# --->
