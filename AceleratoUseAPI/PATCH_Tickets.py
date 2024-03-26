# Realiza a importação de módulos necessários
import os
import json
import requests
from requests.auth import HTTPBasicAuth

# -------->

# Define URL de chamada
url = "https://atendimento.acelerato.com/api/publica/v2/chamados/{}/campos-personalizados"

# Declara credenciais de autenticação
from dotenv import load_dotenv
load_dotenv('./.env')

mail = os.getenv('MAIL')
token = os.getenv('TOKEN')


# -------->

# Define payload de requisições
payload = {
    "camposPersonalizados": [
        {
            "campoPersonalizadoKey": 0,
            "valor": "API"
        }
    ]
}

# Convertendo o corpo da solicitação para JSON
payload_json = json.dumps(payload)

# Define headers
headers = {
'Content-Type': 'application/json;'
}

# Realiza a requisição PATCH com autenticação básica
response = requests.patch(url, headers=headers, data=payload_json, auth=HTTPBasicAuth(mail, token))
