#################################### Parte 1: Obtendo token de autorização ->

# Realiza as importações necessárias
import requests

# Declara variáveis
token_url = 'https://api.us-2.domain.com/oauth2/token'
client_id = 'tokenid'
client_secret = 'tokensecret'

# Define a carga útil para a solicitação de token
payload = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# Faz a solicitação do Token
response = requests.post(token_url, data=payload)

# Declara variável para acesso 
access_token = response.json().get('access_token')

# Validação de satus
if response.status_code != 200:
    print('Maybe, We failed to obtain the access token:', response.status_code)



#################################### Parte 2: Obtendo id de agente partindo de um hostname ->

# Declara o host que será localizado
host = 'cpanel09-idc.domain.com.br'

# Prepara chamada em url destacada
url1 = f"https://api.us-2.domain.com/devices/queries/devices/v1?filter=hostname%3A'{host}'"
# Declara permissionamento
headers1 = {
    "accept": "application/json",
    "authorization": f"Bearer {access_token}"
}

# Obtem primeira resposta
response1 = requests.get(url1, headers=headers1)

# Declara primeira variável [ data ] para consulta na segunda parte deste código
if response1.status_code == 200:
    data = response1.json()
    #print(data['resources'][0])
else:
    print("Erro na requisição:", response1.status_code)



#################################### Parte 3: Obtendo Status partindo de um id ->

# Prepara chamada em url destacada com várivel anterior
url = f"https://api.us-2.domain.com/devices/entities/online-state/v1?ids={data['resources'][0]}"
# Declara permissionamento
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {access_token}"
}

# Obtem segunda resposta
response = requests.get(url, headers=headers)

# Finaliza com status final do host procurado
if response.status_code == 200:
    data = response.json()
    print(data['resources'][0]['state'])
else:
    print("Erro na requisição:", response.status_code)