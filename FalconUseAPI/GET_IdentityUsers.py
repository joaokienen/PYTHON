# https://falcon..crowdstrike.com/documentation/184/identity-protection-apis

# Realiza as importações necessárias
from falconpy import IdentityProtection
import json

# Realiza conexão com Falconpy
falcon = IdentityProtection(client_id='token_id', client_secret='token_secret')

# Define resultados obtidos
idp_query = """
{
  entities(types: [USER], any: [
      { hasNeverExpiringPassword: true },
      { hasExposedPassword: true },
      { hasAgedPassword: true },
      { hasWeakPassword: true }
    ], first: 1000) {
    nodes {
      primaryDisplayName
      secondaryDisplayName
      riskScore
      riskScoreSeverity
      markTime
      creationTime
      entityId
      type
      ... on UserEntity {
         emailAddresses
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
            strength
            effectivePolicy {
              displayName 
            }
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

# Realiza a consulta
response = falcon.graphql(query=idp_query)
#print(response['body']['data']['entities']['nodes'][0])
#print(len(response['body']['data']['entities']['nodes']))
#print(response)

# Define local de salvamento
_dir = 'file.json'

# Realiza salvamento em arquivo especificado
with open(_dir, 'w') as f:
  json.dump(response['body']['data']['entities']['nodes'], f)
