# Parte 0: Configurações de ambiente:
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# Parte 1: Treinamento de modelo:

# Base histórica
base_data = [...]

# Converte as datas para o formato datetime e os valores para float
for entry in base_data:
    entry['Valor_end'] = float(entry['Valor_end'])
    entry['Valor_init'] = float(entry['Valor_init'])
    entry['Date'] = pd.to_datetime(entry['Date'], format='%d/%m/%Y')

# Cria um DataFrame a partir dos dados
history_data = pd.DataFrame(base_data)

# Define as variáveis de entrada (X) e saída (y)
X_train = history_data['Valor_init'].values.reshape(-1, 1)
y_train = history_data['Valor_end']

# Cria e treina o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Geração de CSV para visualização posterior —>
# Cria lista
predict = []

# Realiza extração de valores reais e valores de predição
for i in range(len(y_train)):
    valor_predito = model.predict([[X_train[i][0]]])[0]
    predict.append({'Date': history_data['Date'][i].strftime('%d/%m/%Y'), 'Valor_predito': valor_predito, 'Valor_real': y_train[i]})

# Adiciona lista em um DataFrame
df_predict = pd.DataFrame(predict)

# Salva o DataFrame em um arquivo CSV
df_predict.to_csv('../Datas/Pred-Linear_2022.csv', index=False, sep=';')

# Geração de CSV para visualização posterior —>



# Parte 2: Teste do modelo de previsão:

# Cria base de predição:
base_predit = [{'Date': '02/01/2023', 'Valor_end': '82.82', 'Valor_init': '82.82'}]

# Converte as datas para o formato datetime e os valores para float
for entry in base_predit:
    entry['Valor_init'] = float(entry['Valor_init'])
    entry['Date'] = pd.to_datetime(entry['Date'], format='%d/%m/%Y')

# Usaremos o modelo treinado para fazer previsões
X_test = np.array([entry['Valor_init'] for entry in base_predit]).reshape(-1, 1)
y_pred = model.predict(X_test)

# Cria um DataFrame com as características do conjunto de teste e as predições
results_df = pd.DataFrame({'Data de previsão': [base_predit[0]['Date']],
                           'Previsão da informação da coluna [ Valor ]': [y_pred[0]],
                           'Real valor': [base_predit[0]['Valor_end']]})

# Mostra o DataFrame com os resultados das predições
print(results_df)

# Resultado de acuracidade da previsão feita na base histórica
score = model.score(X_train, y_train)
print(f"Score do modelo: {score:.2f}")

# Com esse código, geramos um CSV para visualização posterior
