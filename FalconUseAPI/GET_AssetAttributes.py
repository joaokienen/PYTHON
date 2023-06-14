#################################### Parte 0: Avaliação de Ambiente ->

# Realiza as importações necessárias
import os
import sys
import json
import requests
import datetime


# Obtendo data atual no formato ( MM-AAAA )
current_date = datetime.datetime.now()
formatted_date = current_date.strftime('%m-%Y')

# Obtendo caminho atual para salvamento do arquvio na pasta ./datas/Entry/
current_dir = os.path.dirname(os.path.realpath(__file__))

# Verifica se diretório existe, caso não o mesmo é criado
dir = os.path.join(current_dir, f'{formatted_date}')
if not os.path.exists(dir):
    os.makedirs(dir)

_dir = os.path.join(current_dir, f'{formatted_date}/hosts-falcon-{formatted_date}.json')

# Verifica se arquivo já existe, caso exista o script é finalizado com código '5'
if os.path.exists(_dir):
    print("Arquivo já existente!")

    sys.exit(5)

# Caso o arquivo não exista, a obtenção de dados é iniciada
else:

    #################################### Parte 1: Obtendo token de autorização ->

    # Declara variáveis
    token_url = 'https://api..crowdstrike.com/oauth2/token'
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



    #################################### Parte 2: Obtendo lista completa de [ id's ] com token recebido ->

    # Prepara variáveis para chamada de [ id's ]
    filter_limit = 1
    
    filter_lastseen_ = 30
    filter_lastseen__ = datetime.datetime.now() - datetime.timedelta(days=filter_lastseen_)
    filter_lastseen = filter_lastseen__.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    filter_type = 'Server'

    # Prepara chamada em url destacada
    token_url_ = f"https://api..crowdstrike.com/devices/queries/devices/v1?limit={filter_limit}&filter=product_type_desc%3A%20'{filter_type}'%2C%20last_seen%3A%20'{filter_lastseen}'%20"

    # Declara permissionamento
    headers_ = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token}"
    }

    # Obtem primeira resposta
    response_ = requests.get(token_url_, headers=headers_)

    data_ = response_.json()
    data = data_['resources']


    #################################### Parte 3: Obtendo lista a partir de [ id's] ->

    assets = []
    for id in data:
        token_url__ = f"https://api..crowdstrike.com/devices/entities/devices/v2?ids={id}"
        response_ = requests.get(token_url__, headers=headers_)
        datar = response_.json()
        datar_ = datar['resources'][0]
        if 'mac_address' in datar_:
            assets.append(datar_['mac_address'])

    

    #################################### Parte 4: Salvando as informações ->


    # Finaliza com o salvamento dos dados
    if response_.status_code == 200:
                
        # Mostra resultado
        print(assets)

        # Armazena a lista em formato json no diretório declarado anteriormente
        with open(_dir, 'w') as f:
            json.dump(assets, f)

    else:
        print("Erro na requisição:", response_.status_code)


