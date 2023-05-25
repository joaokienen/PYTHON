# Realiza as importações necessárias
from tenable.io import TenableIO
tio = TenableIO('XXXXXXXXXX', 'XXXXXXXXXXX')

# Declara host que vamos precisar
host = '179.domain.net.br'

# Obtém a lista de todos os agentes
agents = list(tio.agents.list())

#print(len(agents))
#print(agents[0]['status'])

# Gera filtro por host declarado anteriormente
filtered_list = list(filter(lambda val: f"{host}" in val["name"], agents))

# Exibir os resultado de status do [ Host ]
for item in filtered_list:
    print(item['status'])