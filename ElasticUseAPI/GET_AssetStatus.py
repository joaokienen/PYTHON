# Importa a classe Elasticsearch do módulo elasticsearch
from elasticsearch import Elasticsearch

# Cria uma conexão com o Elasticsearch
es = Elasticsearch(
    ['https://cybersec.domain.com.br:9200/.fleet-agents/'],
    http_auth=('user', 'pass')
)

# Define host de consulta
host = 'cpanel09-idc.domain.com.br'

# Define a consulta de query EXATA
query = {
  "_source": ["last_checkin_status"],
  "size": 10,
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "local_metadata.host.hostname.keyword": {
              "value": f"{host}"
            }
          }
        }
      ]
    }
  }
}

# Define a consulta de query APROXIMADA
"""
query = {
  "_source": ["last_checkin_status"],
  "size": 2,
  "query": {
      "wildcard": {
      "local_metadata.host.hostname.keyword": {
        "value": f"*{host}*"
      }
    }
  }
}
"""

# Realiza a consulta
response = es.search(body=query)

# itera sobre os resultados
for hit in response['hits']['hits']:
    source = hit['_source']
    # processa os campos retornados
    status = source.get('last_checkin_status')
    print(f"Status: {status}\n")







