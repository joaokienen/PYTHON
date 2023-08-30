'''
Arquivo: [base_data.csv]

"Data","Último","Abertura","Máxima","Mínima","Vol.","Var%"
"17.08.2023","114.982","115.592","116.610","114.859","12,75M","-0,53%"
"16.08.2023","115.592","116.171","117.338","115.534","18,86M","-0,50%"
...
"24.06.2019","102.062","102.018","102.617","101.589","3,67M","0,05%"
"21.06.2019","102.013","100.305","102.100","100.305","5,66M","1,70%"

Script:
'''

'''------------->
 
Análise com modelo de regressão linear:


1. CSV com dados históricos será checado
2. Será iniciado o treinamento do modelo com toda a base histórica
3. Iremos obter uma previsão do próximo dia útil da ação, se baseando apenas nas coluna de [Abertura, Máxima e Mínima]


Começaremos treinando o modelo com a origem do campo Abertura, a qual se refere ao campo Último do dia útil anterior.
1. Vamos usar o campo Abertura para obter o campo Máxima
2. Usaremos os campos Abertura e Máxima para obter o campo Mínima
3. Usaremos os campos Abertura, Máxima e Mínima para obter o campo Último


- Nossa base histórica possui dados até o dia 17/08.
- com isso, iremos fazer uma previsão dos dados no dia 18/08.
<-------------'''


# --------> Parte 0: Configurações de ambiente:


# Realiza a importação de módulos necessários
import pandas as pd
from sklearn.linear_model import LinearRegression


# ---->
# Realiza a criação de variáveis necessárias


# Carregará os dados históricos
history_data = pd.read_csv('base_data.csv')
# Iremos jogar o csv em uma lista []
history_data = history_data.to_dict(orient='records')


# Faremos uma limpa e vamos excluir os campos não utilizados nesse teste
for dicionario in history_data:
    exclude = ['Vol.', 'Var%']
    for i in exclude:
        if i in dicionario:
            del dicionario[i]


# Padroniza os dados no formato float
def convert_volume(volume):
    try:
        return float(volume.replace(',', '.'))
    except:
        return volume


# Realiza a atualização do dado na base histórica
for dicionario in history_data:
    dicionario['Máxima'] = convert_volume(dicionario['Máxima'])
    dicionario['Mínima'] = convert_volume(dicionario['Mínima'])
    dicionario['Último'] = convert_volume(dicionario['Último'])
    dicionario['Abertura'] = convert_volume(dicionario['Abertura'])


# Iremos obter aqui o valor da coluna [Último] do dia 17/08
last_value = history_data[0]['Último']


# Esse valor será adicionado como valor de [Abertura] na lista de 18/08
# Criaremos a nossa lista que receberá os dados de previsão
prev_dados_18_08_2023 = []
prev_dados_18_08_2023.append({'Abertura': last_value})

# ---->




# --------> Parte 1: Obtendo previsões:

itens = ['Máxima', 'Mínima', 'Último']


for i in itens:
    # Aponta colunas que serão utilizados para treinamento
    features = prev_dados_18_08_2023[0].keys()


    # Define as variáveis de entrada (X) e saída (y)
    X_train = [[item[feature] for feature in features] for item in history_data] # Que iremos fornecer
    y_train = [item[i] for item in history_data] # Que queremos prever


    # Cria e treina o modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)


    # Usaremos o modelo treinado para fazer previsões
    X_test = [list(prev_dados_18_08_2023[0][feature] for feature in features)]
    y_pred = model.predict(X_test)


    # O resultado da previsão foi gerado em [y_pred]
    # Dessa forma iremos adicioná-lo em nossa lista base
    prev_dados_18_08_2023[0][i] = float(f"{y_pred[0]:.3f}")


print(f"Previsões para 18/08/2023: {prev_dados_18_08_2023[0]}")
