# Realiza a importação de módulos necessários
import os
import json
import requests
from requests.auth import HTTPBasicAuth

# -------->

# Define URL de chamada
url = "https://atendimento.acelerato.com/api/publica/chamados"

# Declara credenciais de autenticação
from dotenv import load_dotenv
load_dotenv('./.env')

mail = os.getenv('MAIL')
token = os.getenv('TOKEN')


# -------->

# Define payload de requisições
payload = {
    "titulo": "Teste - excluir",
    'descricao': 'teste - excluir',
    'categoria':{'categoriaKey':940},
    'kanbanStatus':{'kanbanStatusKey':122},
    'organizacao':{'equipeKey': 26},
    'tipoDePrioridade':{'tipoDePrioridadeKey':46},
    'tipoDeTicket':{'tipoDeTicketKey':20}
}

# Convertendo o corpo da solicitação para JSON
payload_json = json.dumps(payload)

# Define headers
headers = {
'Content-Type': 'application/json;'
}

# Realiza a requisição POST com autenticação básica
response = requests.post(url, headers=headers, data=payload_json, auth=HTTPBasicAuth(mail, token))
