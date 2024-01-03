# Realiza a importação de módulos necessários
import os
import requests
from requests.auth import HTTPBasicAuth


# -------->

# Define URL de chamada
url = "http://atendimento.acelerato.com/api/publica/v2/chamados/1474"

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

# Realiza a requisição GET com autenticação básica
response = requests.get(url, headers=headers, auth=HTTPBasicAuth(mail, token))
