import requests

dados = {
  "rm": 2222,
  "senha":"Your-Pass"
}

response = requests.post('https://YourLink/getHash', data=dados)

print(response.text)
