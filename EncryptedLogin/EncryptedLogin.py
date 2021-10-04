from usuarios import *
from hashlib import sha256

x = 0

username = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

senha = (sha256(senha.encode('utf-8')).hexdigest())

for i in usuarios:
  if username in i['username'] == username and senha in i['password'] == senha:
    x = x + 1
    print("{} logado!".format(i['name']))

for i in usuarios:
  if (username not in i['username'] or senha not in i['password']):
    while (x<1):
      print("Usuário/Senha inválidos!")
      x = x + 1
