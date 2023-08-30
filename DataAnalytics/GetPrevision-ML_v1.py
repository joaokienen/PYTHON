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
2. Será iniciado o treinamento do modelo com 20% dos dados [test_size]
3. Iremos obter uma previsão de algumas datas fixas, conforme o [random_state]


<-------------'''


# --------> Parte 0: Configurações de ambiente:


# Realiza a importação de módulos necessários
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# ---->
# Realiza a criação de variáveis necessárias

test_size = 0.2 # Quantidade usada em treinamento do modelo
random_state = 42 # Fixação de sorteador base


# Carregará os dados históricos
history_data = pd.read_csv('base_data.csv')
# ---->


# Função para converter dados de Volume para valor numérico de comparação
# Função para converter valores com 'M' para milhões
def convert_volume(volume):
    if volume.endswith('M'):
        return float(volume.replace('M', '').replace(',', '')) * 1000000
    return float(volume)


# Realiza a atualização do dado na base histórica
history_data['Vol.'] = history_data['Vol.'].apply(convert_volume)




# --------> Parte 1: Utilização de modelo:

# Aponta colunas que serão utilizados para treinamento
features = ['Abertura', 'Máxima', 'Mínima', 'Vol.']


# Define as variáveis de entrada (X) e saída (y)
X = history_data[features] # Que iremos fornecer
y = history_data['Último'] # Que queremos prever


# Divide os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)


# Cria e treina o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)


# Cria previsões com o conjunto de teste
y_pred = model.predict(X_test)


# Cria um DataFrame com as características do conjunto de teste e as predições
results_df = pd.DataFrame({'Abertura': X_test['Abertura'],
                           'Máxima': X_test['Máxima'],
                           'Mínima': X_test['Mínima'],
                           'Vol.': X_test['Vol.'],
                           'Previsão': y_pred,
                           'Real': y_test})


# Mostra o DataFrame com os resultados das predições
print(results_df)

# Avaliar o modelo e sua acuracidade
score = model.score(X_test, y_test)
print('Acurácia do modelo:', score)
