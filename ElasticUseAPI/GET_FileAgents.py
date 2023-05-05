# Importa a classe Elasticsearch do módulo elasticsearch
from elasticsearch import Elasticsearch

# Cria uma conexão com o Elasticsearch
es = Elasticsearch(
    ['https://cybersec.domain.com.br:9200/.fleet-agents/'],
    http_auth=('user', 'pass')
)

# Define a consulta
query = {
  "_source": ["_id", "enrolled_at", "local_metadata.host.hostname", "local_metadata.host.ip", "local_metadata.host.mac", "local_metadata.os.full", "last_checkin", "unenrolled_at", "tags"],
  "size": 100,
  "query": {
    "bool": {
      "must": [
        {
          "exists": {
            "field": "unenrolled_at"
          }
        }
      ]
    }
  }
}

# Realiza a consulta
response = es.search(body=query)

# itera sobre os resultados
for hit in response['hits']['hits']:
    source = hit['_source']
    # processa os campos retornados
    id = hit.get('_id')
    enrolled_at = source.get('enrolled_at')
    hostname = source.get('local_metadata', {}).get('host', {}).get('hostname')
    ip = source.get('local_metadata', {}).get('host', {}).get('ip')
    mac = source.get('local_metadata', {}).get('host', {}).get('mac')
    os_full = source.get('local_metadata', {}).get('os', {}).get('full')
    last_checkin = source.get('last_checkin')
    unenrolled_at = source.get('unenrolled_at')
    tags = source.get('tags')
    # imprime os valores dos campos
    #print(f"id: {id}, enrolled_at: {enrolled_at}, hostname: {hostname}, ip: {ip}, mac: {mac}, os_full: {os_full}, last_checkin: {last_checkin}, unenrolled_at: {unenrolled_at}, tags: {tags}")
    print(f"hostname: {hostname}, ip: {ip}, system: {os_full},tags: {tags} \n")
