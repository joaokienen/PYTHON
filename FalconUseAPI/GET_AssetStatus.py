# Realiza as importações necessárias
import requests

# Declara o host que será localizado
host = 'cpanel09-idc.domain.com.br'

# Prepara chamada em url destacada
url1 = f"https://api.us-2.com/devices/queries/devices/v1?filter=hostname%3A'{host}'"
# Declara permissionamento
headers1 = {
    "accept": "application/json",
    "authorization": "Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
}

# Obtem primeira resposta
response1 = requests.get(url1, headers=headers1)

# Declara primeira variável [ data ] para consulta na segunda parte deste código
if response1.status_code == 200:
    data = response1.json()
    #print(data['resources'][0])
else:
    print("Erro na requisição:", response1.status_code)


################################

# Prepara chamada em url destacada com várivel anterior
url = f"https://api.us-2.com/devices/entities/online-state/v1?ids={data['resources'][0]}"
# Declara permissionamento
headers = {
    "accept": "application/json",
    "authorization": "Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
}

# Obtem segunda resposta
response = requests.get(url, headers=headers)

# Finaliza com status final do host procurado
if response.status_code == 200:
    data = response.json()
    print(data['resources'][0]['state'])
else:
    print("Erro na requisição:", response.status_code)















