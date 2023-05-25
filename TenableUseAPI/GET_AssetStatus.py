#################################### Parte 1: Obtendo [ last_seen ] de um agente ->

# Realiza as importações necessárias
import requests
from datetime import datetime, timedelta

# Declara o host que será localizado
host = 'cpanel09-idc.domain.com.br'

# Declara nossa url de destino
url = f"https://cloud.tenable.com/workbenches/assets?filter.0.filter=hostname&filter.0.quality=eq&filter.0.value={host}"

# Declara a autorização para acessar a url de destino
headers = {
    "accept": "application/json",
    "X-ApiKeys": "accessKey=XXXXXXXXXX;secretKey=XXXXXXXXXXXX;"
}

# Recupera resposta
response = requests.get(url, headers=headers)

# Converte resposta no formato [ json ]
data = response.json()

# Obtem campo necessário da resposta anterior
last_seen = data['assets'][0]['last_seen']



#################################### Parte 2: Validando se agente está ativo com base no [ last_seen ] ->

# Declara função de tempo, para verificar se host está ativo ou inativo
def is_more_than_10_days(last_seen):

    # Obtem a data atual
    current_date = datetime.utcnow()

    # Converte a string de data para um objeto datetime
    date = datetime.strptime(last_seen, "%Y-%m-%dT%H:%M:%S.%fZ")

    # Calcula a diferença entre as duas datas
    diff = current_date - date

    # Verifica se a diferença é maior que 10 dias
    if diff > timedelta(days=10):
        return "offline"
    else:
        return "online"

# Recupera status final
result = is_more_than_10_days(last_seen)
print(result)