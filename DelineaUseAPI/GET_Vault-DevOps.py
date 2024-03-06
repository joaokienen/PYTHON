# https://github.com/DelineaXPM/python-dsv-sdk

# Imports necessary modules
import os

from delinea.secrets.vault import (
    PasswordGrantAuthorizer,
    SecretsVault,
    SecretsVaultAccessError,
    SecretsVaultError,
    VaultSecret,
)

# Vault DevOps
BASE_URL = os.getenv('BASE_URL')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('SECRET_ID')
PATH_ID = os.getenv('PATH_ID')

# Create kitten main
def main():

    try:
        authorizer = PasswordGrantAuthorizer(BASE_URL, CLIENT_ID, CLIENT_SECRET)
        
        vault = SecretsVault(BASE_URL, authorizer)
        
        secret = VaultSecret(**vault.get_secret(PATH_ID))
        
        # Show obtained secret 
        print(secret)

    except SecretsVaultAccessError as e:
        print(e.message)
    except SecretsVaultError as e:
        print(e.response.text)


if __name__ == "__main__":
    main()
