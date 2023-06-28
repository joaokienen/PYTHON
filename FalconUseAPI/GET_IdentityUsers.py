# https://falcon.{codec}.crowdstrike.com/documentation/184/identity-protection-apis

# Realiza as importações necessárias
from falconpy import IdentityProtection
import json
import csv
import os

# Realiza conexão com Falconpy
falcon = IdentityProtection(client_id='XXXXXXXXXXXXXXXXXXXXXXXXXXX', client_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Define query de consulta e campos que serão retornados
idp_query = """
query ($after: Cursor) {
  entities(types: [USER], first: 1000, after: $after) {
    nodes {
      ... on UserEntity {
        associations(bindingTypes: [OWNERSHIP]) {
          ... on EntityAssociation {
            entity {
              primaryDisplayName 
              associations(bindingTypes: [LOCAL_ADMINISTRATOR]) {
                ... on LocalAdminLocalUserAssociation {
                  accountName
                }
                ... on LocalAdminDomainEntityAssociation {
                  entity {
                    secondaryDisplayName 
                  }
                }
              }
            } 
          }
        }
        primaryDisplayName
        secondaryDisplayName
        riskScore
        riskScoreSeverity
        creationTime
        AD_isAdminLocal: hasRole(type: LocalAdminRole)
        AD_isAdminDomain: hasRole(type: DomainAdminsRole)
      }
      accounts {
        ... on ActiveDirectoryAccountDescriptor {
          domain
          department
          passwordAttributes {
            aged 
            mayExpire
            exposed
            lastChange
          }
        }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
"""

# Cria lista ordenada para receber conteúdo bruto
identis = []

# Realiza a primeira consulta
response = falcon.graphql(query=idp_query)

# Cria atalho de consulta
consul_ = response['body']['data']['entities']

# Define o conteúdo recebido na resposta acima e adiciona pelo método [ extend ] na lista [ identis ]
identis.extend(consul_['nodes'])

# Cria atalho de consulta
consul = consul_['pageInfo']

# Obtem resposta de outras páginas, além das 1000 primeiras respostas recebidas
nextPage = consul['hasNextPage'] or False
endCursor = consul['endCursor'] or 'Cursor'

# Enquanto houver outras páginas, novos itens serão adiconados na lista [ identis ]
while nextPage == True:
  # Realiza nova consulta com variável que tem o código da próxima página de consulta
  res = falcon.graphql(query=idp_query, variables={"after": endCursor})
  # Cria atalho de consulta
  a_ = res['body']['data']['entities']
  # Realiza a adição da lista
  identis.extend(a_['nodes'])

  # Cria atalho de consulta
  a = a_['pageInfo']
  # Atualiza valores de loop While
  nextPage = a['hasNextPage'] or False
  endCursor = a['endCursor'] or 'Cursor'


# ------------------------------------------------------------- #


# Cria nova lista, para resultados filtrados 
identity = []

# Realiza função detalhada para obter campos fixos em circustâncias indefinidas
for i in identis:
  group = []
  x = False
  a = i['secondaryDisplayName']
  b = (i['associations'] and i['associations'][0]['entity'])
  machine = (b and b['primaryDisplayName']) or 'None'
  if b and b['associations']:
    list1 = [item for item in b['associations'] if 'entity' in item]
    for j in list1:
      c = (j and j['entity'] and j['entity']['secondaryDisplayName']) or 'None'
      if a == c:
        x = True
    list2 = [item for item in b['associations'] if 'accountName' in item] or {'accountName': 'None'}
    for k in list2:
      g = k['accountName']
      group.append(g)
  d = i['accounts'][0]
  e = d['passwordAttributes']
  identity.append({ 
    'Domain': d['domain'] or 'None',
    'Usuário': a, 
    'Host': machine, 
    'LocalAdmin in Máquina': x , 
    'LocalAdmin in AD': i['AD_isAdminLocal'], 
    'DomainAdmin in AD': i['AD_isAdminDomain'],
    'Departamento': d['department'] or 'None',
    'Senha Expira?': e['mayExpire'],
    'Senha Vencida?': e['aged'],
    'Senha Exposta?': e['exposed'],
    'RiskScore': i['riskScore'],
    'Other Users LocalAdmin in Machine': group
  })
# No fim, a lista [ identity ] está alimentada


# ------------------------------------------------------------- #


# Obtendo caminho atual para salvamento do arquvio
current_dir = os.path.dirname(os.path.realpath(__file__))

# Define nomes para arquivos .json e .csv
_dir_json = os.path.join(current_dir, f'identify-back.json')
_dir_csv = os.path.join(current_dir, f'identify-front.csv')

# Realiza salvamento em arquivo [ json ]
with open(_dir_json, 'w') as f:
  json.dump(identity, f)

# Prepara salvamento de arquivo [ csv ]
csv_data = []
for item in identity:
  csv_data.append(item)

# Armazena a lista no diretório declarado
with open(_dir_csv, "w", newline="", encoding="utf-8") as f:
  writer = csv.DictWriter(f, fieldnames=csv_data[0].keys())
  writer.writeheader()
  writer.writerows(csv_data)