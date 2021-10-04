# Na situação apresentada temos a missão de requisitar um hash de um site pré configurado com a intenção de receber um hash assim que o login requisitado for válido.
# Abaixo podemos ver o processo em funcionamento.

# In the presented situation, we have the mission to request a hash from a pre-configured site with the intention of receiving a hash as soon as the requested login is valid.
# Below we can see the process in operation.

import requests

dados = {
  "rm": 2222,
  "senha":"Your-Pass"
}

response = requests.post('https://YourLink/getHash', data=dados)

print(response.text)
