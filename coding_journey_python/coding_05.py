# type hints

import json
nome = 'Lucas'  # sem type hint
nome: str = 'Lucas'  # type hint


# listas e dicionários
lista: list = []
lista: list = [1, 2, 3, 'eu', 'você', 4.5, 5.5]

dicionario: dict = {}
dicionario1: dict[str, int] = {
    'nome': 'Yasmin', 'idade': 15, 'cidade': 'Campinas'}
dicionario2: dict = {'nome': 'Dalva', 'idade': 25, 'cidade': 'São Paulo'}
dicionario3: dict = {'nome': 'Bruna', 'idade': 30, 'cidade': 'Rio de Janeiro'}

lista_dicionarios: list = []
lista_dicionarios.append(dicionario1)
lista_dicionarios.append(dicionario2)
lista_dicionarios.append(dicionario3)

# json
lista_dicionarios_json: str = json.dumps(lista_dicionarios, indent=4)
print(lista_dicionarios_json)


# Exercício 1: lista de numeros ao quadrado

lista: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [x ** 2 for x in lista]
print(quadrados)

# Exercício 2: Modificar lista de linguagens

linguagens = ['Python', 'Java', 'C#', 'JavaScript', 'PHP']
linguagens = [x.lower() for x in linguagens]
linguagens.pop(2)
linguagens.append('C++')
linguagens.append('Ruby')
print(linguagens)

# Exercício 3: Informações de um livro

from typing import Union


livro1: dict[str, Union[str, int, float]] = {
    'titulo': 'Python para desenvolvedores',
    'autor': 'Luiz Eduardo Borges',
    'ano': 2019,
    'preco': 100.00
}

livro2: dict[str, Union[str, int, float]] = {
    'titulo': 'Python Fluente',
    'autor': 'Luciano Ramalho',
    'ano': 2015,
    'preco': 150.00
}

livro3: dict[str, Union[str, int, float]] = {
    'titulo': 'Python Cookbook',
    'autor': 'David Beazley',
    'ano': 2013,
    'preco': 200.00
}

livro4: dict[str, Union[str, int, float]] = {
    'titulo': 'Python Data Science Handbook',
    'autor': 'Jake VanderPlas',
    'ano': 2016,
    'preco': 250.00
}

livro5: dict[str, Union[str, int, float]] = {
    'titulo': 'Python Machine Learning',
    'autor': 'Sebastian Raschka',
    'ano': 2015,
    'preco': 300.00
}

livros = [
    livro1, livro2, livro3, livro4, livro5
]


def busca_livro(nome_do_livro: str) -> str:
    for livro in livros:
        if nome_do_livro.lower() == livro['titulo'].lower():
            print(
                f"Nome do livro: {livro['titulo']}\nAutor: {livro['autor']}\nAno: {livro['ano']}\nPreço: {livro['preco']}")


if __name__ == '__main__':
    nome_do_livro = input('Digite o nome do livro: ')
    busca_livro(nome_do_livro)
