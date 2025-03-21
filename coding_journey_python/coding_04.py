# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.


import re
import logging
import time
import random


def gerar_dados_vendas(num_registros):
    itens = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E']
    dados_vendas = []

    for n in range(num_registros):
        item = random.choice(itens)  # item aleatório
        quantidade = random.randint(-50, 50)  # quantidade aleatória
        preco = round(random.uniform(-500.0, 500.0), 2)  # preço aleatório
        dados_vendas.append(
            # Adiciona um dicionário com os dados de venda
            {'item': item, 'quantidade': quantidade, 'preco': preco})

    return dados_vendas


# Gerar dados de vendas
num_registros = 15
dados_validos = []
dados_invalidos = []

dados_vendas = gerar_dados_vendas(num_registros)
for registro in dados_vendas:
    if registro['quantidade'] > 0 and registro['preco'] > 0:
        dados_validos.append(registro)
    else:
        dados_invalidos.append(registro)
print('"Dados válidos:"', dados_validos)
print('"Dados inválidos:"', dados_invalidos)

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'


def gerar_dados_temperatura(num_registros):
    dados_temperatura = []

    for n in range(num_registros):
        temperatura = random.randint(0, 50)  # temperatura aleatória
        if temperatura < 18:
            dados_temperatura.append(
                {'classificacao': 'Baixa', 'temperatura': temperatura})
        elif temperatura >= 18 and temperatura <= 26:
            dados_temperatura.append(
                {'classificacao': 'Normal', 'temperatura': temperatura})
        elif temperatura > 26:
            dados_temperatura.append(
                {'classificacao': 'Alta', 'temperatura': temperatura})
    return dados_temperatura

# Gerar dados de temperatura


num_registros = 10
dados_temperatura = gerar_dados_temperatura(num_registros)
print(dados_temperatura)


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.


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
    arquivo_log = arquivo.readlines()
    arquivo.close()

    # Verifica se algum log ERROR foi encontrado
    encontrou_erro = False

    for log in arquivo_log:
        if 'ERROR' in log:
            print(log)
            encontrou_erro = True

    if not encontrou_erro:
        print("Nenhum log com severidade 'ERROR' encontrado.")


if __name__ == "__main__":
    gerar_log_ficticio()
    print("Logs fictícios gerados com sucesso no arquivo 'test_logs.log'.")
    filtrar_logs_por_severidade()


# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.


def is_alpha_space(str) -> str:
    return all(char.isalpha() or char.isspace() for char in str)


def is_digit_space(str) -> str:
    return (str.isnumeric() or str.isspace())


def valida_nome(msg) -> str:
    while True:
        nome = input(msg)
        if not (is_alpha_space(nome) and len(nome) >= 4):
            print("OPS! Valores inválidos ou nome curto demais.")
        else:
            return nome


def valida_idade(msg):
    idade_minima = 18
    idade_maxima = 65
    while True:
        idade = input(msg)
        if not (is_digit_space(idade)):
            print("OPS! Valores inválidos.")
        elif int(idade) < 18 or int(idade) > 65:
            print("OPS! Idade fora do limite.")
        else:
            return idade


def valida_email(msg):
    while True:
        email = input(msg)
        r = re.compile(r'^[\w.-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        if not r.match(email):
            print("OPS! Email inválido. Tente novamente.")
        else:
            return email


if __name__ == "__main__":

    nome_usuario = valida_nome('Digite o seu nome: ').title()
    idade_usuario = valida_idade("Digite a sua idade: ")
    email_usuario = valida_email("Digite o seu email: ")
    print(
        f'Dados de usuário válidos: \n Nome: {nome_usuario} \n Idade: {idade_usuario} \n Email: {email_usuario}')


# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Exercícios com WHILE

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
