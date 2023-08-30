# Realiza a importação de módulos necessários
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression




# --------> Parte 0: Configuração de Ambiente
# --
# Define o símbolo da ação que você deseja recuperar os dados
symbol = 'NAMER.SA'


# Calcula o tempo de dados que iremos recuperar
end_date = datetime.now()
start_date = end_date - timedelta(days=7)


# Recupera os dados históricos da ação usando a API yfinance
stock_data = yf.download(symbol, start=start_date, end=end_date)


# Converte o DataFrame em uma lista de dicionários, mantendo a data como índice
data_list = stock_data.reset_index().to_dict(orient='records')
# --
# --------> Parte 0: Configuração de Ambiente






# --------> Parte 1: Tratamento de dados históricos, acuracidade e gráficos
# --
# Carregará os dados históricos em ordem crescente por Date
history_data = sorted(data_list, key=lambda x: x['Date'])


# Aponta colunas que serão utilizados para treinamento
features = ['Open', 'High', 'Low', 'Volume']


# Define as variáveis de entrada (X) e saída (y)
X = [[item[feature] for feature in features] for item in history_data] # Que iremos fornecer
y = [item['Close'] for item in history_data] # Que queremos prever


# Cria e treina o modelo de regressão linear
model = LinearRegression()
model.fit(X, y)


# Cria previsões para todos os dados
y_pred = model.predict(X)


# Cria um DataFrame com as características dos dados e as predições
results_df = pd.DataFrame({'Previsão': y_pred, 'Real': y})
# Mostra o DataFrame com os resultados das predições
#print(results_df)


# Avaliar o modelo e sua acuracidade
score = model.score(X, y)
a = score * 100
b = f'{a:.0f}%'
#print('Acurácia do modelo:', b)


# Define variável para obtenção de Datas, para utilização em gráficos
dates = stock_data.index.strftime('%d/%m')


# Gráfico de referência
'''
# Plotar as previsões em relação aos valores reais
plt.plot(dates, y_pred, linestyle='--', color='blue', label='Valores preditivos')
plt.plot(dates, y, color='red', label='Valores reais')
plt.ylabel('Valores por ação')
plt.title('Gráfico de Referência Linear')
plt.grid(True)
plt.ylim(min(y) - 0.5, max(y) + 0.5)
plt.xticks(rotation=45)
plt.legend()
plt.savefig('grafico_referencia_linear.png', bbox_inches='tight')
'''


# Gráfico de dispersão
'''
# Plotar as previsões em relação aos valores reais
plt.scatter(y, y_pred, color='blue', label='Previsões')
plt.plot([min(y), max(y)], [min(y), max(y)], linestyle='--', color='red', label='Linha de apoio')
plt.title('Gráfico de Dispersão Linear')
plt.grid(True)
plt.ylim(min(y) - 0.5, max(y) + 0.5)
plt.xticks(rotation=45)
plt.legend()
plt.savefig('grafico_dispersao_linear.png', bbox_inches='tight')
'''
# --
# --------> Parte 1: Tratamento de dados históricos, acuracidade e gráficos





# --------> Parte 2: Geramento de previsões para o próximo dia útil
# --
# Carregará os dados históricos em ordem decrescente por Date
history_data = sorted(data_list, key=lambda x: x['Date'], reverse=True)


# Iremos obter aqui o valor da coluna [Último] do dia anterior
last_value = history_data[0]['Adj Close']


# Esse valor será adicionado como valor de [Abertura] na lista do próximo dia útil
# Criaremos a nossa lista que receberá os dados de previsão
prev_dados = []
prev_dados.append({'Open': float(f"{last_value:.3f}")})


# Aponta itens que serão previsto, até chegar no valor de fechamento [ Close ]
itens = ['High', 'Low', 'Volume', 'Close']


# Para cada item na lista
for i in itens:


    # Aponta colunas que serão utilizados para treinamento
    features = prev_dados[0].keys()


    # Define as variáveis de entrada (X) e saída (y)
    X_train = [[item[feature] for feature in features] for item in history_data] # Que iremos fornecer
    y_train = [item[i] for item in history_data] # Que queremos prever


    # Cria e treina o modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)


    # Usaremos o modelo treinado para fazer previsões
    X_test = [list(prev_dados[0][feature] for feature in features)]
    y_pred = model.predict(X_test)


    # O resultado da previsão foi gerado em [y_pred]
    # Dessa forma iremos adiciona-lo em nossa lista base
    prev_dados[0][i] = float(f"{y_pred[0]:.3f}")


print(f"Previsões para próximo dia útil: {prev_dados[0]}")
# --
# --------> Parte 2: Geramento de previsões para o próximo dia útil
