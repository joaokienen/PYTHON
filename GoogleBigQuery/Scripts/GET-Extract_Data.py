# --------> Parte 0: Configurações de Ambiente

# Realiza a importação de módulos necessários
import os
import sys
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account


# Obtendo caminho atual
current_dir = os.path.dirname(os.path.realpath(__file__))

# Obtendo caminho do arquivo de autenticação
key_path = os.path.join(current_dir, f'../Auth/rm348777-9e5efd68bf57.json')

# Verifica se arquivo de autenticação existe
if not os.path.exists(key_path):
    print("Arquivo de autenticação não existe!")
    # Caso não, o script é encerrado
    sys.exit(5)

# Cria um objeto de credencial usando a chave de autenticação
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])




# --------> Parte 1: Criação de funções + dicionários

# Criado valores conforme planilha de dicionários que foi disponibilizada
uf = {11:'Rondônia',12:'Acre',13:'Amazonas',14:'Roraima',15:'Pará',16:'Amapá',17:'Tocantins',21:'Maranhão',22:'Piauí',23:'Ceará',24:'Rio Grande do Norte',25:'Paraíba',26:'Pernambuco',27:'Alagoas',28:'Sergipe',29:'Bahia',31:'Minas Gerais',32:'Espírito Santo',33:'Rio de Janeiro',35:'São Paulo',41:'Paraná',42:'Santa Catarina',43:'Rio Grande do Sul',50:'Mato Grosso do Sul',51:'Mato Grosso',52:'Goiás',53:'Distrito Federal'}
# Realizado função com base em dicionário anterior
def ufr(param):
    estado = uf[param]
    return estado

# Criado valores conforme planilha de dicionários que foi disponibilizada
sexo = {1:'Homem',2:'Mulher'}
# Realizado função com base em dicionário anterior
def sexor(param):
    genero = sexo[param]
    return genero

# Criado valores conforme planilha de dicionários que foi disponibilizada
quests_1 = {1:'Sim',2:'Não',3:'Não sabe',9:'Ignorado'}
# Realizado função com base em dicionário anterior
def quests_1r(param):
    if param == None:
        quests = 'Ignorado'
    else:
        quests = quests_1[param]
    return quests

# Criado valores conforme planilha de dicionários que foi disponibilizada
escolaridade = {1:'Sem instrução',2:'Fundamental incompleto',3:'Fundamental completa',4:'Médio incompleto',5:'Médio completo',6:'Superior incompleto',7:'Superior completo',8:'Pós-graduação, mestrado ou doutorado'}
# Realizado função com base em dicionário anterior
def escolaridader(param):
    if param == None:
        quests = 'Ignorado'
    else:
        quests = escolaridade[param]
    return quests




# --------> Parte 2: Criação de looping + dicionários

# Cria lista para verificar qual mês será consultado dentro do Google BigQuery
list_var = ['05_2020', '06_2020', '07_2020']

# Cria looping de for para passar por cada item da lista anterior, fazendo a consulta em todas as bases de dados
for consult in list_var:

    # Define variável de dicionário que logo será alimentada 
    dic = ''

    # Os dois primeiros meses possuem dicionários na mesma ordem, sendo assim, essa será a base:
    if consult == '05_2020' or consult == '06_2020':
        dic = {'Ano': 0, 'UF': 1, 'CAPITAL': 2, 'RM_RIDE': 3, 'V1008': 4, 'V1012': 5, 'V1013': 6, 'V1016': 7, 'Estrato': 8, 'UPA': 9, 'V1022': 10, 'V1023': 11, 'V1030': 12, 'V1031': 13, 'V1032': 14, 'posest': 15, 'A001': 16, 'A001A': 17, 'A001B1': 18, 'A001B2': 19, 'A001B3': 20, 'A002': 21, 'A003': 22, 'A004': 23, 'A005': 24, 'B0011': 25, 'B0012': 26, 'B0013': 27, 'B0014': 28, 'B0015': 29, 'B0016': 30, 'B0017': 31, 'B0018': 32, 'B0019': 33, 'B00110': 34, 'B00111': 35, 'B00112': 36, 'B002': 37, 'B0031': 38, 'B0032': 39, 'B0033': 40, 'B0034': 41, 'B0035': 42, 'B0036': 43, 'B0037': 44, 'B0041': 45, 'B0042': 46, 'B0043': 47, 'B0044': 48, 'B0045': 49, 'B0046': 50, 'B005': 51, 'B006': 52, 'B007': 53, 'C001': 54, 'C002': 55, 'C003': 56, 'C004': 57, 'C005': 58, 'C0051': 59, 'C0052': 60, 'C0053': 61, 'C006': 62, 'C007': 63, 'C007A': 64, 'C007B': 65, 'C007C': 66, 'C007D': 67, 'C007E': 68, 'C007E1': 69, 'C007E2': 70, 'C008': 71, 'C009': 72, 'C010': 73, 'C0101': 74, 'C01011': 75, 'C01012': 76, 'C0102': 77, 'C01021': 78, 'C01022': 79, 'C0103': 80, 'C0104': 81, 'C011A': 82, 'C011A1': 83, 'C011A11': 84, 'C011A12': 85, 'C011A2': 86, 'C011A21': 87, 'C011A22': 88, 'C012': 89, 'C013': 90, 'C014': 91, 'C015': 92, 'C016': 93, 'C017A': 94, 'D0011': 95, 'D0013': 96, 'D0021': 97, 'D0023': 98, 'D0031': 99, 'D0033': 100, 'D0041': 101, 'D0043': 102, 'D0051': 103, 'D0053': 104, 'D0061': 105, 'D0063': 106, 'D0071': 107, 'D0073': 108, 'F001': 109, 'F0021': 110, 'F0022': 111, 'F0061': 112, 'F006': 113}

    # Caso o mês seja 07_2020, a ordem será outra:
    if consult == '07_2020':
        dic = {'Ano': 0, 'UF': 1, 'CAPITAL': 2, 'RM_RIDE': 3, 'V1008': 4, 'V1012': 5, 'V1013': 6, 'V1016': 7, 'Estrato': 8, 'UPA': 9, 'V1022': 10, 'V1023': 11, 'V1030': 12, 'V1031': 13, 'V1032': 14, 'posest': 15, 'A001': 16, 'A001A': 17, 'A001B1': 18, 'A001B2': 19, 'A001B3': 20, 'A002': 21, 'A003': 22, 'A004': 23, 'A005': 24, 'A006': 25, 'A007': 26, 'A008': 27, 'A009': 28, 'B0011': 29, 'B0012': 30, 'B0013': 31, 'B0014': 32, 'B0015': 33, 'B0016': 34, 'B0017': 35, 'B0018': 36, 'B0019': 37, 'B00110': 38, 'B00111': 39, 'B00112': 40, 'B00113': 41, 'B002': 42, 'B0031': 43, 'B0032': 44, 'B0033': 45, 'B0034': 46, 'B0035': 47, 'B0036': 48, 'B0037': 49, 'B0041': 50, 'B0042': 51, 'B0043': 52, 'B0044': 53, 'B0045': 54, 'B0046': 55, 'B005': 56, 'B006': 57, 'B007': 58, 'B008': 59, 'B009A': 60, 'B009B': 61, 'B009C': 62, 'B009D': 63, 'B009E': 64, 'B009F': 65, 'B0101': 66, 'B0102': 67, 'B0103': 68, 'B0104': 69, 'B0105': 70, 'B0106': 71, 'B011': 72, 'C001': 73, 'C002': 74, 'C003': 75, 'C004': 76, 'C005': 77, 'C0051': 78, 'C0052': 79, 'C0053': 80, 'C006': 81, 'C007': 82, 'C007A': 83, 'C007B': 84, 'C007C': 85, 'C007D': 86, 'C007E': 87, 'C007E1': 88, 'C007E2': 89, 'C007F': 90, 'C008': 91, 'C009': 92, 'C009A': 93, 'C010': 94, 'C0101': 95, 'C01011': 96, 'C01012': 97, 'C0102': 98, 'C01021': 99, 'C01022': 100, 'C0103': 101, 'C0104': 102, 'C011A': 103, 'C011A1': 104, 'C011A11': 105, 'C011A12': 106, 'C011A2': 107, 'C011A21': 108, 'C011A22': 109, 'C012': 110, 'C013': 111, 'C014': 112, 'C015': 113, 'C016': 114, 'C017A': 115, 'D0011': 116, 'D0013': 117, 'D0021': 118, 'D0023': 119, 'D0031': 120, 'D0033': 121, 'D0041': 122, 'D0043': 123, 'D0051': 124, 'D0053': 125, 'D0061': 126, 'D0063': 127, 'D0071': 128, 'D0073': 129, 'E001': 130, 'E0021': 131, 'E0022': 132, 'E0023': 133, 'E0024': 134, 'F001': 135, 'F0021': 136, 'F0022': 137, 'F002A1': 138, 'F002A2': 139, 'F002A3': 140, 'F002A4': 141, 'F002A5': 142, 'F0061': 143, 'F006': 144}





    # --------> Parte 3: Preparação para consulta

    # Cria o cliente BigQuery com as credenciais
    client = bigquery.Client(credentials=credentials)

    # Declara query de consulta
    QUERY = (
        f'SELECT * FROM `rm348777.Fase_3.{consult}` '
        'LIMIT 1')
    query_job = client.query(QUERY)
    rows = query_job.result()

    # Cria lista para receber novos resultados tratados
    lister = []

    # Para cada item recebido na consulta, baseado nos dicionários declarados no inicio do código
    for row in rows:

        # Variáveis serão identificadas
        estado = row[dic['UF']]
        idade = row[dic['A002']]
        genero = row[dic['A003']]

        quest_1 = row[dic['B0011']]
        quest_2 = row[dic['B0013']]
        quest_3 = row[dic['B0016']]
        quest_4 = row[dic['B00112']]
        quest_5 = row[dic['B00110']]
        quest_6 = row[dic['B0014']]

        quest_7 = row[dic['B0031']]
        quest_8 = row[dic['B0032']]
        quest_9 = row[dic['B0033']]
        quest_10 = row[dic['B0034']]

        quest_11 = row[dic['B007']]
        quest_12 = row[dic['C006']]
        quest_13 = row[dic['C014']]
        quest_14 = row[dic['A005']]

        # Variáveis serão adiconadas em nova lista criada anteriormente [ lister ], passando em suas respectivas funções para tratamento de dados:
        lister.append({'Estado': ufr(estado),'Idade': idade,'Sexo': sexor(genero),'Quest_1': quests_1r(quest_1),'Quest_2': quests_1r(quest_2), 'Quest_3': quests_1r(quest_3), 'Quest_4': quests_1r(quest_4), 'Quest_5': quests_1r(quest_5),'Quest_6': quests_1r(quest_6),'Quest_7': quests_1r(quest_7),'Quest_8': quests_1r(quest_8),'Quest_9': quests_1r(quest_9),'Quest_10': quests_1r(quest_10),'Quest_11': quests_1r(quest_11),'Quest_12': quests_1r(quest_12),'Quest_13': quests_1r(quest_13),'Quest_14': escolaridader(quest_14)})





    # --------> Parte 4: Salvando informações

    # Declara local de salvamento
    save = os.path.join(current_dir, f'../Datas/Output/Data-{consult}.csv')

    # Realiza criação dos Data Frames 
    df1 = pd.DataFrame(lister)

    # --> Cria [ csv ]
    df1.to_csv(save, index=False, encoding='utf-8')

