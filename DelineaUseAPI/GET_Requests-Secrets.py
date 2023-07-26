# Realiza a importação de módulos necessários
import requests

# Declara token de acesso
token = '00000000000'

# URL da API para obter o token de acesso
url = "https://secretserver.com/api/v2/secrets"

# Parâmetros da requisição
headers = {'Authorization':'Bearer ' + token, 'content-type':'application/json'}
params = {
    "take": 1
}

# Faz a requisição para obter resultado
response = requests.get(url, headers=headers, params=params)

# Mostra a saída convertida
print(response.text)

