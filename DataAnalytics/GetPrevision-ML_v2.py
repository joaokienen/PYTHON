'''
Arquivo: [base_data.csv]

"Data","Último","Abertura","Máxima","Mínima","Vol.","Var%"
"16.08.2023","115.592","116.171","117.338","115.534","18,86M","-0,50%"
...
"21.06.2019","102.013","100.305","102.100","100.305","5,66M","1,70%"


Arquivo: [geter.csv]


"Data","Último","Abertura","Máxima","Mínima","Vol.","Var%"
"17.08.2023","114.982","115.592","116.610","114.859","12,75M","-0,53%"



Script:
'''

'''------------->
 
Análise com modelo de regressão linear:


1. CSV com dados históricos será checado
2. Será iniciado o treinamento do modelo com toda a base histórica
3. Iremos obter uma previsão do próximo dia útil da ação, se baseando apenas na coluna de [Abertura]


<-------------'''


# --------> Parte 0: Configurações de ambiente:

# Realiza a importação de módulos necessários
import pandas as pd
from sklearn.linear_model import LinearRegression


# ---->
# Realiza a criação de variáveis necessárias

# Carregará os dados históricos
history_data = pd.read_csv('base_data.csv')
# ---->



# --------> Parte 1: Treinamento de modelo:


# Aponta colunas que serão utilizados para treinamento
features = ['Abertura']


# Define as variáveis de entrada (X) e saída (y)
X_train = history_data[features] # Que iremos fornecer
y_train = history_data['Último'] # Que queremos prever


# Cria e treina o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)




# --------> Parte 2: Teste do modelo de previsão:

'''------------->


O último dia histórico da nossa lista é do dia 17/08/2023


Linha:
"17.08.2023","114.982","115.592","116.610","114.859","12,75M","-0,53%"


Iremos excluir essa linha da nossa base e adicionar essa linha em um novo arquivo, chamado de geter.csv
Dessa forma, vamos poder prever o valor da ação no próximo dia e comparar com o valor real.


<-------------'''


# Carregará o dado que queremos prever
base_predit = pd.read_csv('geter.csv')


# Usaremos o modelo treinado para fazer previsões
X_test = base_predit[features]  # Usando 'Abertura' como entrada para previsão, já declarada na variável [features]
y_pred = model.predict(X_test)


# --->
# OBS: Iremos pegar o campo de abertura, pois o valor de [Abertura] é o mesmo valor da coluna [Último] do dia anterior
# --->


# Cria um DataFrame com as características do conjunto de teste e as predições
results_df = pd.DataFrame({ 'Data de previsão': base_predit['Data'],
                           'Previsão da informação da coluna [ Último ]': y_pred,
                           'Real valor': base_predit['Último']})


# Mostra o DataFrame com os resultados das predições
print(results_df)

# Resultado de acuracidade da previsão feita na base histórica
score = model.score(X_train, y_train)
print(f"Score do modelo: {score:.2f}")
