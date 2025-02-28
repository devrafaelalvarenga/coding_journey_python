import random

# Gerar um conjunto de dados de vendas


def gerar_dados_vendas(num_registros):
    itens = ['Item A', 'Item B', 'Item C', 'Item D', 'Item E']
    dados_vendas = []

    for n in range(num_registros):
        item = random.choice(itens)  # item aleatório
        quantidade = random.randint(-50, 50)  # quantidade aleatória
        preco = round(random.uniform(-500.0, 500.0), 2)  # preço aleatório
        dados_vendas.append(
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
