# Realiza a importação de módulos necessários
import os
import requests
from requests.auth import HTTPBasicAuth


# -------->

# Define URL de chamada
url = "http://atendimento.acelerato.com/api/publica/tickets/1474/anexos"

# Declara credenciais de autenticação
from dotenv import load_dotenv
load_dotenv('./.env')

mail = os.getenv('MAIL')
token = os.getenv('TOKEN')


# -------->

# Realiza a leitura do arquivo
with open('arquivo.xlsx', 'rb') as file:
    # Envia o arquivo no método POST
    response_upload = requests.post(url, auth=HTTPBasicAuth(mail, token), files={'arquivo': file})

# Realiza output
if response_upload.status_code == 200:
    print('Upload concluído com sucesso.')
else:
    print(f'Erro na requisição de upload: {response_upload.status_code} - {response_upload.text}')
