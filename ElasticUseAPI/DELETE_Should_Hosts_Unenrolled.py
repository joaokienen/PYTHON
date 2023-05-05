# Importa a classe Elasticsearch do módulo elasticsearch
from elasticsearch import Elasticsearch

# Cria uma conexão com o Elasticsearch
es = Elasticsearch(
    ['https://cybersec.domain.com.br:9200/'],
    http_auth=('user', 'pass')
)

# Cria lista de hosts a serem deletados
assets_names_exclud = []

# Define a consulta
query_names = {
    "_source": ["_id", "local_metadata.host.hostname"], 
    "size": 10,
    "query": {
        "bool": {
            "must": [
                {
                    "bool": {
                        "should": [
                            {
                                "term": {
                                    "local_metadata.host.hostname.keyword": {
                                        "value": "WIN-6D8O8RFHPHL"
                                    }
                                }
                            },
                            {
                                "term": {
                                    "local_metadata.host.hostname.keyword": {
                                        "value": "thiavs-virtual-machine"
                                    }
                                }
                            },
                            {
                                "term": {
                                    "local_metadata.host.hostname.keyword": {
                                        "value": "logstash"
                                    }
                                }
                            },
                            {
                                "term": {
                                    "local_metadata.host.hostname.keyword": {
                                        "value": "fastnetmon"
                                    }
                                }
                            },
                            {
                                "term": {
                                    "local_metadata.host.hostname.keyword": {
                                        "value": "WIN-6D8O8RFHPHL"
                                    }
                                }
                            }
                        ]
                    }
                },
                {
                    "match": { 
                        "active": "false"
                    }
                }
            ]
        }
    }
}

# Realiza a consulta
response_names = es.search(index='.fleet-agents', body=query_names)

# Itera sobre os resultados
for hit in response_names['hits']['hits']:
    source = hit['_source']
    hostname = source.get('local_metadata', {}).get('host', {}).get('hostname')
    id = hit.get('_id')
    assets_names_exclud.append(id)
    
# Verbose de quantidade de id's
print(assets_names_exclud)
print(len(assets_names_exclud))

# Realiza a exclusão
#for item in assets_names_exclud:
    #response = es.delete(index='.fleet-agents', id=item)