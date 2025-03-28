# 3. Informações de um livro

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
