# Neste projeto, temos um um dicionário representado pelo arquivo 'users'. 
# Precisamos realizar um consulta e validar se o username e senha digitados estão disponibilizados nesse dicionário.
# Mesmo sabendo que os dados estão criptografados em sha256.
# Com isso, temos na aplicação abaixo a exemplificação de todo o processo em funcionamento.

# In this project, we have a dictionary represented by the 'users' file.
# We need to perform a query and validate if the username and password entered are available in this dictionary.
# Even though the data is encrypted in sha256.
# With that, we have in the application below the example of the entire process in operation.

from Users import *
from hashlib import sha256

x = 0

username = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

senha = (sha256(senha.encode('utf-8')).hexdigest())

for i in Users:
  if username in i['username'] == username and senha in i['password'] == senha:
    x = x + 1
    print("{} logado!".format(i['name']))

for i in Users:
  if (username not in i['username'] or senha not in i['password']):
    while (x<1):
      print("Usuário/Senha inválidos!")
      x = x + 1
