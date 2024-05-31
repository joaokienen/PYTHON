# https://github.com/DelineaXPM/python-tss-sdk

# Imports necessary modules
import os

# Vault DevOps
from delinea.secrets.vault import (
    PasswordGrantAuthorizer,
    SecretsVault,
    SecretsVaultAccessError,
    SecretsVaultError,
    VaultSecret,
)


# ---> Config
current_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_dir, f'./.env')
# ---> 


# ---> Call main function with Vault
from dotenv import load_dotenv
if os.path.exists(env_path):
    
    load_dotenv(env_path)

    # Get .env variables
    BASE_URL = os.getenv('BASE_URL')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    PATH_ID = os.getenv('PATH_ID')

    # If valid itens
    if BASE_URL and CLIENT_ID and CLIENT_SECRET and PATH_ID:

        # Init extract data
        try:

            # Getting variables in Delinea DevOps
            authorizer = PasswordGrantAuthorizer(BASE_URL, CLIENT_ID, CLIENT_SECRET)  
            vault = SecretsVault(BASE_URL, authorizer)
            secret = VaultSecret(**vault.get_secret(PATH_ID))
            
            # Define local variables
            TOKEN = secret.data['TOKEN']

            # Call main function
            # print(TOKEN)

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
