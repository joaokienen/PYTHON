# Importação de módulos necessários
import os
import pandas as pd
import streamlit as st




### -----------------> Configurações da Página

current_dir = os.path.dirname(os.path.realpath(__file__))

st.set_page_config(
    page_title="Data Analytics | JvkScript.me",
    page_icon="◾",
    layout="wide"
)

### <----



### -----------------> Título e Apresentação

with st.container(border=True):
    st.title('[◾] Análise de precificação do petróleo em 2022')

    st.divider()
   
    with st.container(border=True):
        st.text("Saudações!\n\n"
                "-> Neste projeto, exploraremos os dados de preços do petróleo e faremos um comparativo \n"
                "dos preços dos combustíveis ao longo do ano. Além disso, aplicaremos uma análise preditiva \n"
                "para ilustrar as tendências futuras.")

        with st.expander("Etapas realizadas para ilustração desse projeto:"):
            st.text(
                "1. Análise de Negócios: \n    Nesta fase, foi realizado uma análise detalhada dos objetivos e metas do projeto. Identificando as métricas-chave necessárias\n para avaliar o desempenho dos preços do petróleo e dos combustíveis ao longo do ano de 2022.\n\n"
                "2. Coleta de dados públicos: \n    Iniciado o projeto coletando dados públicos relacionados aos preços do petróleo e dos combustíveis. Utilizando fontes confiáveis\n e acessíveis publicamente para garantir a integridade e a transparência dos dados.\n\n"
                "3. Tratamento e Limpeza dos Dados: \n    Após a coleta, foi dedicado uma atenção especial ao tratamento e limpeza dos dados. Isso envolveu a remoção de valores nulos, a\n correção de inconsistências e a padronização dos formatos. Garantindo que os dados estivessem prontos para análise, livres de qualquer\n ruído ou distorção.\n\n"
                "4. Exploração dos Dados: \n    Foi conduzido uma análise exploratória dos dados para entender suas características fundamentais. Utilizando técnicas estatísticas\n e visualizações para identificar padrões, tendências e anomalias nos preços do petróleo e dos combustíveis ao longo do ano.\n\n"
                "5. Estruturação de Modelo Preditivo: \n    Para prever as tendências futuras, foi desenvolvido um modelo preditivo. Isso envolveu a escolha de algoritmos adequados, a divisão \ndos dados em conjuntos de treinamento e teste, o ajuste do modelo e a validação dos resultados. O objetivo era fornecer insights sobre \npossíveis cenários futuros.\n\n"
                "6. Criação de Estrutura de Código: \n    Foi desenvolvido uma estrutura de código robusta para facilitar a manutenção e expansão do projeto. Adotando boas práticas de\n programação, garantindo a clareza, a modularidade e a reutilização de código.\n\n"
                "7. Visualização de Dados: \n    Foi implementado visualizações de dados interativas e informativas. Utilizando ferramentas como Streamlit, Matplotlib ou Altair\n para criar gráficos e gráficos que comunicassem efetivamente os insights derivados da análise."
            )

### <----


st.divider()


### -----------------> Container de Dados históricos do Petróleo

with st.container(border=True):

    st.text("Dados históricos do petróleo no ano:")

    with st.container(border=True):
        dir_petr = os.path.join(current_dir, f'Datas/Pred-Linear_2022.csv')

        df_petr = pd.read_csv(dir_petr, sep=';')

        # Convertendo a coluna 'Date' para datetime
        df_petr['Date'] = pd.to_datetime(df_petr['Date'], format='%d/%m/%Y')

        # Ordenando o DataFrame pela coluna 'Date'
        df_petr = df_petr.sort_values(by='Date')

        min = df_petr['Valor_real'].describe()['min'].round(2)
        men = df_petr['Valor_real'].describe()['mean'].round(2)
        max = df_petr['Valor_real'].describe()['max'].round(2)

        
        col1, col2 = st.columns([1,3])
        with col1:
            view = st.selectbox('Visualização:',('Métricas', 'Tabela'))

            if view == 'Métricas':
                col1.metric("Menor Preço Histórico", f'U$ {min}', '-')
                col1.metric("Preço Médio Histórico", f'U$ {men}', '=', delta_color="off")
                col1.metric("Maior Preço Histórico", f'U$ {max}', '+')
            if view == 'Tabela':
                    data_show = df_petr[['Date', 'Valor_real']]
                    data_show = data_show.rename(columns={'Valor_real': 'Preço U$'})
                    data_show['Date'] = data_show['Date'].dt.date

                    st.dataframe(data_show, height=250, hide_index=True, use_container_width=True)

                    @st.cache_data
                    def convert_df(df_file):
                        return df_file.to_csv().encode('utf-8')

                    csv = convert_df(data_show)
                    st.download_button(label='Baixar arquivo CSV', data=csv, file_name='Data-Fuel-2022.csv', mime='text/csv', use_container_width=True)

        with col2:
            with st.container(border=True):
                chart_data = df_petr[['Date', 'Valor_real']]
                st.line_chart(chart_data.set_index('Date'), color='#000000', use_container_width=True)
                    
                st.caption("Fonte da extração de preços do petróleo: http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view")
        
    ### <----



    ### -----------------> Container de valores de combustíveis

    st.text("Comparação com os preços de combustíveis comercializados no Brasil no mesmo ano:")

    with st.container(border=True):
        dir_insig = os.path.join(current_dir, f'Datas/Insights_2022.csv')

        df_insig = pd.read_csv(dir_insig, sep=';')
        
        listing = ['ETANOL', 'GASOLINA ADITIVADA', 'DIESEL', 'GASOLINA', 'DIESEL S10']

        df_listing = pd.DataFrame()

        for fuel in listing:
            df_fuel = df_insig[df_insig['Produto'] == fuel].copy()
            df_fuel['Data da Coleta'] = pd.to_datetime(df_fuel['Data da Coleta'], errors='coerce')
            df_fuel = df_fuel.dropna(subset=['Data da Coleta'])
            df_media_mensal_fuel = df_fuel.groupby(df_fuel['Data da Coleta'].dt.to_period("M"))['Valor de Venda'].mean().reset_index()
            df_media_mensal_fuel['Data da Coleta'] = df_media_mensal_fuel['Data da Coleta'].dt.to_timestamp()
            df_media_mensal_fuel['Valor de Venda Etanol'] = df_media_mensal_fuel['Valor de Venda'].round(2)

            if fuel == 'ETANOL':
                df_listing['Dates'] = df_media_mensal_fuel['Data da Coleta']

            df_listing[fuel] = df_media_mensal_fuel['Valor de Venda Etanol']

        col1, col2 = st.columns([5,1], gap="medium")
        with col1:
            with st.container(border=True):
                chart_data = df_listing[['Dates', 'DIESEL', 'DIESEL S10', 'ETANOL', 'GASOLINA', 'GASOLINA ADITIVADA']]
                st.line_chart(chart_data.set_index('Dates'), color=['#d76161', '#c19d78', '#e3ecf4', '#edf56e', '#b4e150'], use_container_width=True)

                st.caption("Fonte da extração de preços de combustíveis: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos")

        with col2:
            a = st.selectbox('Tipo de combustível:',('DIESEL', 'DIESEL S10', 'ETANOL', 'GASOLINA', 'GASOLINA ADITIVADA'))

            def fuel(type, fu):
                df_fuel_ = df_insig[df_insig['Produto'] == type].copy()
                if fu == 1:
                    return df_fuel_['Valor de Venda'].describe()['min'].round(2)
                if fu == 2:
                    return df_fuel_['Valor de Venda'].describe()['mean'].round(2)
                if fu == 3:
                    return df_fuel_['Valor de Venda'].describe()['max'].round(2)

            st.metric("Menor Preço Histórico", f'R$ {fuel(a, 1)}')
            st.metric("Preço Médio Histórico", f'R$ {fuel(a, 2)}')
            st.metric("Maior Preço Histórico", f'R$ {fuel(a, 3)}')

    ### <----
            

    st.divider()


    ### -----------------> Container de valores preditivos
    
    st.text("Modelos de predição para tomadas de decisão:")

    with st.container(border=True):
        col1, col2 = st.columns([1,2])

        with col1:
            code_view = st.selectbox('Modelo Preditivo:',('Regressão Linear', 'Arima (AutoRegressive)'))

            if code_view == 'Regressão Linear':
                code = '''
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
                df_predict.to_csv('Pred-Linear_2022.csv', index=False, sep=';')

                # Geração de CSV para visualização posterior —>
                '''
            
            if code_view == 'Arima (AutoRegressive)':
                code = '''
                # Base de dados
                data = [...]

                # Formatação para cada item
                for entry in data:
                    entry['Date'] = pd.to_datetime(entry['Date'], format='%d/%m/%Y')
                    entry['Valor'] = float(entry['Valor'])

                # Cria um DataFrame a partir dos dados
                df = pd.DataFrame(data)

                # Ordena o DataFrame por data
                df = df.sort_values(by='Date')

                # Define a data como índice
                df = df.set_index('Date')

                # Ajusta o modelo ARIMA
                model = ARIMA(df['Valor'], order=(1, 1, 1))
                result = model.fit()

                # Faz a previsão para '02/01/2023'
                forecast = result.get_forecast(steps=1)

                predicted_value = forecast.predicted_mean.iloc[0]
                confidence_interval_lower = forecast.conf_int().iloc[0][0]
                confidence_interval_upper = forecast.conf_int().iloc[0][1]
                std_errors = forecast.se_mean.iloc[0]

                
                # Geração de CSV para visualização posterior —>

                # Salvando em CSV
                file = []
                file.append({'Valor predito em U$':predicted_value, 'Intervalo de Confiança L': confidence_interval_lower, 'Intervalo de Confiança U': confidence_interval_upper, 'Intervalo de Erro das Previsões': std_errors})

                # Adiciona lista em um DataFrame
                df_predict = pd.DataFrame(file)

                # Salva o DataFrame em um arquivo CSV
                df_predict.to_csv('Pred-Arima_2022.csv', index=False, sep=';')

                # Geração de CSV para visualização posterior —>
                '''

            with st.container(border=True):
                st.text("Exemplificação do código do modelo ->")
                st.code(code, language='python')

        with col2:
            if code_view == 'Regressão Linear':
                data_df_petr = df_petr.rename(columns={'Valor_real': 'Valores reais em U$', 'Valor_predito': 'Valores preditos em U$'})
                data_df_petr['Date'] = data_df_petr['Date'].dt.date
                data_df_petr['Valores preditos em U$'] = data_df_petr['Valores preditos em U$'].round(2)

                with st.container(border=True):
                    st.text("Arquivo (.CSV) gerado:")
                    st.dataframe(data_df_petr, height=250, hide_index=True, use_container_width=True)
            
                with st.container(border=True):
                    st.text("Com a base do arquivo (.CSV), temos uma visualização gráfica ->\n\nLinha do tempo em 2022: \n    Valores reais x Valores previstos")
                    chart_data = data_df_petr[['Date', 'Valores reais em U$', 'Valores preditos em U$']]
                    st.line_chart(chart_data.set_index('Date'), color=['#a8fd40', '#000000'], use_container_width=True)

                with st.container(border=True):
                    st.caption("Exemplo do modelo de regrssão em tempo real: https://postech-data.vercel.app/predictive_analytics")

            if code_view == 'Arima (AutoRegressive)':
                dir_arima = os.path.join(current_dir, f'Datas/Pred-Arima_2022.csv')
                dir_arima = pd.read_csv(dir_arima, sep=';')

                dir_arima = dir_arima.round(2)

                with st.container(border=True):
                    st.text("Arquivo (.CSV) gerado:")
                    st.dataframe(dir_arima, height=150, hide_index=True, use_container_width=True)

                with st.container(border=True):
                    st.text("Com a base do arquivo (.CSV), temos as seguintes métricas extraídas ->")
                    
                    with st.container(border=True):
                        st.text("Seguindo a base histórica de 2022, iremos fazer a previsão para o primeiro dia útil de 2023:\n\n     Date: [02/01/2023]")

                        col1, col2 = st.columns(2)

                        with col1:
                            with st.container(border=True):
                                st.metric("Preço real em U$", "82.82", "=", delta_color="off")
                            
                        with col2:
                            with st.container(border=True):
                                st.metric("Preço previsto em U$", "82.96", "0.14")

                        with st.container(border=True):
                            st.text("Estatísticas da predição:")

                            col1, col2, col3 = st.columns(3)

                            with col1:
                                with st.container(border=True):
                                    st.metric("Menor valor previsto", "76.77", "-6,05")

                            with col2:
                                with st.container(border=True):
                                    st.metric("Maior valor previsto", "89.15", "6,33")

                            with col3:
                                with st.container(border=True):
                                    st.metric("Intervalo de erro", "3.16", "0", delta_color="off")

    with st.container(border=True):
        st.text("Para referência ->")
        st.caption("Github: https://github.com/joaokienen/PYTHON/tree/main/Streamlits/Fuels-Analytics")
    ### <----
