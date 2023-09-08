# Realiza a importação de módulos necessários
import os
import sys
import pickle
import socket
import signal



# ---> Parte 0: Configuração de ambiente
# -->

# Dados obtidos atráves de arquivo do projeto
from dotenv import load_dotenv
load_dotenv('./.env')

# Define variáveis de IP e Porta para inicialização e escuta
server_ip = "0.0.0.0"
server_port = int(os.getenv('PORT'))

# Criação do socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Configura o socket para reutilizar o endereço
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Vincula o socket ao endereço e porta
server_socket.bind((server_ip, server_port))

# Debugger para checkpoint alcançado
print("Servidor UDP ouvindo na porta", server_port)

# Define variáveis onde arquivos de recebimento estão fixados
# Caminho do arquivo para registro de hostname
item_log_file = os.getenv('FILE_CHECKER')

# Função para encerrar o servidor de forma limpa
def shutdown_server(signal, frame):
    print("\nEncerrando o servidor UDP...")
    server_socket.close()
    sys.exit(0)
# Captura o sinal SIGINT (Ctrl+C) para encerrar o servidor
signal.signal(signal.SIGINT, shutdown_server)
# -->

# Valida se diretório existe
if not os.path.exists(item_log_file):
    os.makedirs(item_log_file)



# ---> Parte 1: Lidando com recebimento de requisições
# -->
# Cria looping infinito, até que resposta seja enviada
while True:

    # Realiza tentativa de execução do seguinte bloco
    try:

        # Define variáveis de conexão
        serialized_data, client_address = server_socket.recvfrom(20480)

        # Após definições e prevenções anteriores, vamos realizar uma nova tentativa de execução:
        try:

            # Nesse bloco, tentaremos descompactar a váriavel [serialized_data] com picke, caso de erro, será porque a requisição do cliente quer alimentar o arquivo [item_log_file] e não recupera-lo para HostsProtegidos
           
            # Define chave de identificação
            identd = 'JvkScript'

            # Descompacta variável do cliente
            data = pickle.loads(serialized_data)
            # Declara variáveis
            file_request = data['file_to_retrieve']
            identifer = data['identd']

            # Se arquivo conferir e identificador conferir, o servidor retornará o arquivo para o cliente
            if file_request == item_log_file and identifer == identd:
                with open(item_log_file, 'rb') as file:
                    file_content = file.read()
                server_socket.sendto(file_content, client_address)
            else:
                error_message = "Error_404_or_401"
                server_socket.sendto(error_message.encode(), client_address)
            
        # Caso váriavel [serialized_data] não seja do formato picke, método convencional será realizado, alimentando o arquivo [item_log_file]
        except:

            # Define variável
            decoded_data = serialized_data.decode()

            # Obtém o hostname da origem (que é o conteúdo do pacote)
            source = decoded_data.strip()  # Remove espaços em branco e quebras de linha

            # Verifica se o hostname está entre colchetes
            if source.startswith("[") and source.endswith("]"):
                # Verifica se o hostname já existe no arquivo
                with open(item_log_file, "r") as file:
                    existing_hostnames = set(line.strip() for line in file)

                if source not in existing_hostnames:
                    # Abre o arquivo de registro de hostname para escrita em modo de adição ("a")
                    with open(item_log_file, "a") as file:
                        # Escreve o hostname da origem no arquivo
                        file.write(source + "\n")
                        file.flush()  # Força a escrita no arquivo

    # Caso retorno erros:
    except Exception as e:
        print("Erro:", e)
# -->
