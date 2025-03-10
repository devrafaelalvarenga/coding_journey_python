import logging
import random
import time

# Configuração
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='test_logs.log',
    filemode='w'
)

# Mensagens de erro fictícias
error_messages = [
    "Erro ao conectar ao banco de dados",
    "Tempo limite excedido na requisição",
    "Arquivo não encontrado",
    "Divisão por zero detectada",
    "Erro de permissão ao acessar o arquivo",
    "Falha na leitura do sensor",
    "Erro de rede: conexão perdida",
    "Erro de sintaxe no arquivo de configuração",
    "Memória insuficiente para alocação",
    "Erro de validação dos dados de entrada"
]

# Função para gerar logs de erro fictícios


def gerar_log_ficticio():
    for _ in range(10):  # Gera 10 logs fictícios
        # Seleciona uma mensagem de erro aleatória
        error_message = random.choice(error_messages)
        log_level = random.choice(
            # Seleciona um nível de log aleatório
            [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL])

        # Simula um atraso aleatório entre os logs
        time.sleep(random.uniform(0.1, 1.0))

        # Gera o log
        logging.log(log_level, error_message)


def filtrar_logs_por_severidade():
    arquivo = open('test_logs.log', 'r')
    log = arquivo.readlines()
    arquivo.close()

    encontrou_erro = False

    for l in log:
        if 'ERROR' in l:
            print(l)
            encontrou_erro = True

    if not encontrou_erro:
        print("Nenhum log com severidade 'ERROR' encontrado.")


if __name__ == "__main__":
    gerar_log_ficticio()
    print("Logs fictícios gerados com sucesso no arquivo 'test_logs.log'.")
    filtrar_logs_por_severidade()
