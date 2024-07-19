# Imports the necessary modules
import os
import requests
from dotenv import load_dotenv


try:

    #################################### Part 1: Obtaining authorization token ->

    # Obtaining query variables
    load_dotenv("./.env")
    BASE_URL = os.getenv("BASE_URL")
    CLIENT_ID = os.getenv("CLIENT_ID")
    SECRET_ID = os.getenv("SECRET_ID")

    # ->
    url = f"{BASE_URL}/oauth2/token"

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": SECRET_ID
    }

    response = requests.post(url, data=payload)
    ACCESS_TOKEN = response.json().get("access_token")
    # ->



    #################################### Part 2: Creating batch with selected hosts ->

    # List of host_ids
    hosts_aid = []

    # ->
    url = f"{BASE_URL}/real-time-response/combined/batch-init-session/v1"

    payload = {
        "host_ids": hosts_aid,
        "queue_offline": True
    }

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.post(url, headers=headers, json=payload)
    BARCH_ID = response.json()["batch_id"]
    # ->



    #################################### Part 3: Executing commands in obtained batch ->

    # ->
    url = f"{BASE_URL}/real-time-response/combined/batch-admin-command/v1"

    payload = {
        "base_command": "mv",
        "batch_id": BARCH_ID,
        "command_string": "mv C:\\Windows\\System32\\drivers\\CrowdStrike\\C-00000291*.sys C:\\Temp",
        "optional_hosts": [],
        "persist_all": True
    }

    response = requests.post(url, headers=headers, json=payload)
    # ->


except Exception as response:
    print(response)
