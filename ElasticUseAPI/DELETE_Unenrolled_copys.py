# Importa a classe Elasticsearch do módulo elasticsearch
from elasticsearch import Elasticsearch

# Cria uma conexão com o Elasticsearch
es = Elasticsearch(
    ['https://cybersec.domain.com.br:9200/'],
    http_auth=('user', 'pass')
)

# Define a consulta de hosts ativos
query_on = {
  "_source": ["_id", "local_metadata.host.hostname"], 
  "size": 1000,
  "query": {
    "bool": {
      "must": [
        {
          "match": { 
            "active": "true"
          }
        }
      ]
    }
  }
}

# Realiza a consulta de hosts ativos
response_on = es.search(index='.fleet-agents', body=query_on)

# Itera sobre os resultados de hosts ativos
assets_on = []
for hit in response_on['hits']['hits']:
    source = hit['_source']
    hostname = source.get('local_metadata', {}).get('host', {}).get('hostname')
    id = hit.get('_id')
    assets_on.append(hostname)


#############################


# Define a consulta de hosts unenrolled
query_off = {
  "_source": ["_id", "local_metadata.host.hostname"], 
  "size": 1000,
  "query": {
    "bool": {
      "must": [
        {
          "match": { 
            "active": "false"
          }
        }
      ]
    }
  }
}

# Realiza a consulta de hosts unenrolled
response_off = es.search(index='.fleet-agents', body=query_off)

# Itera sobre os resultados de hosts unenrolled
assets_off = []
for hit in response_off['hits']['hits']:
    source = hit['_source']
    hostname = source.get('local_metadata', {}).get('host', {}).get('hostname')
    id = hit.get('_id')
    assets_off.append({'id': id, 'host': hostname})


# Cria lista de exclusão com hosts unenrolled que possuem cópias ativas
exclud = []
for item in assets_off:
    if item['host'] in assets_on:
        exclud.append(item['id'])

# Verbose de quantidade de id's
print(len(exclud))
print(exclud)

# Realiza a exclusão
#for item in exclud:
    #response = es.delete(index='.fleet-agents', id=item)

