# Realiza a importação de módulos necessários
import os
import socket
import pickle



# ---> Parte 0: Configuração de ambiente
# -->

# Dados obtidos atráves de arquivo do projeto
from dotenv import load_dotenv
load_dotenv('./.env')

# Define variáveis de IP e Porta para inicialização e escuta
server_ip = os.getenv('SERVER_IP')
server_port = int(os.getenv('PORT'))

#Cria variável de identificação para seleção posterior
identd = 'JvkScript'
# Define local de arquivo que queremos recuperar
file_to_retrieve = os.getenv('FILE_CHECKER')

# Cria compactação de itens para envio único
data_to_send = {'identd': identd, 'file_to_retrieve': file_to_retrieve}
# Serializa o dicionário para uma representação de bytes
serialized_data = pickle.dumps(data_to_send, protocol=2)

# Cria um socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Envie os dados ao servidor
client_socket.sendto(serialized_data, (server_ip, server_port))
# Define um timeout de alguns segundos
client_socket.settimeout(15)



# ---> Parte 1: Lidando com recebimento de requisições
# -->
try:
    # Recebe dados de resposta do servidor
    file_data, server_address = client_socket.recvfrom(20480)

    # Verifica se o arquivo foi encontrado
    if "Error_404_or_401" in file_data.decode():
        print("Arquivo não encontrado no servidor ou token inválido.")
    else:
        # Imprime o conteúdo do arquivo
        print("Conteúdo do arquivo:")
        print(file_data.decode())

except socket.timeout:
    # Captura um timeout se a operação não for concluída dentro do tempo limite
    print("Timeout ocorreu. O servidor não respondeu a tempo.")

except Exception as e:
    # Retorna erros
    print("Erro:", e)

finally:
    # Encerra conexão
    client_socket.close()
# -->
