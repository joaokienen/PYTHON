# Realiza a importação de módulos necessários
import os
import requests
from requests.auth import HTTPBasicAuth


# -------->

# Define URL de chamada
url = "http://atendimento.acelerato.com/api/publica/tickets/1474/anexos/824"

# Declara credenciais de autenticação
from dotenv import load_dotenv
load_dotenv('./.env')

mail = os.getenv('MAIL')
token = os.getenv('TOKEN')


# -------->

# Define headers
headers = {
'Content-Type': 'application/json; charset=utf-8'
}

# Realiza a requisição DELETE com autenticação básica
response = requests.delete(url, headers=headers, auth=HTTPBasicAuth(mail, token))
