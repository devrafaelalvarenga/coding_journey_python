# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
''' 
def somar(num_1 = int, num_2 = int) -> int: # Função que recebe dois números inteiros e retorna a soma deles
    return num_1 + num_2

def obtem_numero_inteiro(mensagem = str) -> int: # Função que solicita um número inteiro ao usuário
    while True: 
        try:
            return int(input(mensagem))
        except ValueError: # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')

if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite o primeiro número inteiro: ')
    num_2 = obtem_numero_inteiro('Digite o segundo número inteiro: ')
    resultado = somar(num_1, num_2)
    print(f'A soma dos números é: {resultado}')    
'''
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
'''
def dividir(num_1 = int, num_2 = int) -> int: # Função que recebe dois números inteiros e retorna o resto da divisao deles
    return num_1 % num_2

def obtem_numero_inteiro(mensagem = str) -> int: # Função que solicita um número inteiro ao usuário
    while True: 
        try:
            return int(input(mensagem))
        except ValueError: # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')

if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    num_2 = 5
    resultado = dividir(num_1, num_2)
    print(f'O resto da divisão do numero {num_1} por {num_2} dos números é: {resultado}')
'''

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
''''
def multiplicar(num_1 = int, num_2 = int) -> int: # Função que recebe dois números inteiros e retorna a multiplicação dos valores
    return num_1 * num_2

def obtem_numero_inteiro(mensagem = str) -> int: # Função que solicita um número inteiro ao usuário
    while True: 
        try:
            return int(input(mensagem))
        except ValueError: # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')

if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    num_2 = obtem_numero_inteiro('Digite o segundo número inteiro: ')
    resultado = multiplicar(num_1, num_2)
    print(f'O resultado da multiplicação do numero {num_1} por {num_2} dos números é: {resultado}')
'''
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
# Função que recebe dois números inteiros e retorna a divisão inteira dos valores
def dividir_inteiro(num_1=int, num_2=int) -> int:
    return num_1 // num_2

# Função que solicita um número inteiro ao usuário
def obtem_numero_inteiro(mensagem=str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:  # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')


if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    num_2 = obtem_numero_inteiro('Digite o segundo número inteiro: ')
    try:
        num_2 != 0
        resultado = dividir_inteiro(num_1, num_2)
        print(
            f'O resultado da divisão inteira do numero {num_1} por {num_2} dos números é: {resultado}')
    except ZeroDivisionError:
        print('Não é possível dividir por zero.')
'''
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
calcular_expoente = pow # Função que recebe dois números inteiros e eleva um número a uma potência

def obtem_numero_inteiro(mensagem=str) -> int: # Função que solicita um número inteiro ao usuário
    while True:
        try:
            return int(input(mensagem))
        except ValueError:  # Tratamento de erro para caso o usuário digite um valor inválido
            print('Digite um número inteiro válido.')


if __name__ == "__main__":  # Executa o código abaixo apenas se este arquivo for executado diretamente
    num_1 = obtem_numero_inteiro('Digite um número inteiro: ')
    expoente = 2
    resultado = calcular_expoente(num_1, expoente)
    print(f'O calculo do numero {num_1} ao quadrado é: {resultado}')
'''

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''
def somar(num_1=float, num_2=float) -> float:
    return num_1 + num_2


def obtem_numero_flutuante(mensagem=str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número flutuante válido.')


if __name__ == "__main__":
    num_1 = obtem_numero_flutuante('Digite o primeiro número flutuante: ')
    num_2 = obtem_numero_flutuante('Digite o segundo número flutuante: ')
    resultado = somar(num_1, num_2)
    print(f'A soma dos números é: {resultado}')
    '''
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''
def calcular_media(num_1=float, num_2=float) -> float:
    return (num_1 + num_2) / 2

def obtem_media(mensagem=str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número flutuante válido.')

if __name__ == "__main__":
    num_1 = obtem_media('Digite o primeiro número flutuante: ')
    num_2 = obtem_media('Digite o segundo número flutuante: ')
    resultado = calcular_media(num_1, num_2)
    print(f'A média dos números é: {resultado}')
'''
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
''' 
def calcular_potencia(base=int, expoente=int) -> int:
    return pow(base, expoente)


def obtem_base_expoente(mensagem=str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite um número inteiro válido.')


if __name__ == "__main__":
    base = obtem_base_expoente('Digite um valor para a base: ')
    expoente = obtem_base_expoente('Digite um valor para o expoente: ')
    resultado = calcular_potencia(base, expoente)
    print(f'O resultado da potência do numero {base} elevado a {expoente} é: {resultado}')
'''
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
'''
def converter_celsius_para_fahrenheit(celsius=float) -> float:
    return (celsius * 9/5)+32


def obtem_temperatura(mensagem=str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número flutuante válido.')


if __name__ == "__main__":
    celcius = obtem_temperatura('Digite a temperatura em Celsius a ser convertida em Fahrenheit: ')
    resultado = converter_celsius_para_fahrenheit(celcius)
    print(f'Temperatura {celcius}°C convertido em Fareinheit é: {resultado}°F')
'''
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
''' 
def calcula_area_circulo(raio=float) -> float:
    import math
    return math.pi * pow(raio, 2)


def obtem_raio(mensagem=str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número flutuante válido.')


if __name__ == "__main__":
    raio = obtem_raio('Digite o raio do circulo:')
    resultado = calcula_area_circulo(raio)
    print(f'A área do círculo com raio {raio} é: {resultado:.2f}')
'''

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
'''
def converter_maiscula(texto=str) -> str:
    return texto.upper()


def obtem_texto(mensagem=str) -> str:
    return input(mensagem)


if __name__ == '__main__':
    texto = obtem_texto('Digite um texto: ')
    resultado = converter_maiscula(texto)
    print(f'O texto em maiusculo é: {resultado}')
'''
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
'''def remover_espacos(texto=str) -> str:
    return texto.strip() # Remove os espaços em branco no início e no final da string

def obtem_texto(mensagem=str) -> str:
    return input(mensagem)

if __name__ == '__main__':
    texto = obtem_texto('Digite um texto: ')
    resultado = remover_espacos(texto)
    print(f'O texto sem espaços é: {resultado}')
'''
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
'''
def separar_data(data=str) -> str:
    # Separa a data em uma lista de strings a partir do caracter '/'
    return data.split(sep='/', maxsplit=3)


def obtem_data(mensagem=str) -> str:
    return input(mensagem)


if __name__ == '__main__':  # Executa o código abaixo apenas se este arquivo for executado diretamente
    data = obtem_data('Digite uma data no formato dd/mm/yyyy: ')
    resultado = separar_data(data)
    print(f'Dia: {resultado[0]} Mês: {resultado[1]} Ano: {resultado[2]}')
'''
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''
def concatenar_texto(texto_1=str, texto_2=str) -> str:
    return texto_1+''+texto_2


def obtem_texto(mensagem=str) -> str:
    return input(mensagem)


if __name__ == '__main__':
    texto_1 = obtem_texto('Digite a primeira frase: ')
    texto_2 = obtem_texto('Digite a segunda frase: ')
    resultado = concatenar_texto(texto_1, texto_2)
    print(f'O texto concatenado é: {resultado}')
'''
# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
'''
def operacao_and(exp_1=bool, exp_2=bool) -> bool:
    return exp_1 and exp_2


def obtem_expressao_booleana(mensagem=str) -> bool:
    entrada = input(mensagem).capitalize().strip()
    if entrada == 'True':
        return True
    elif entrada == 'False':
        return False
    else:
        raise ValueError("Entrada inválida. Digite 'True' ou 'False'.")


if __name__ == '__main__':

    exp_1 = obtem_expressao_booleana(
        'Digite a primeira expressão booleana (True ou False): ')
    exp_2 = obtem_expressao_booleana(
        'Digite a segunda expressão booleana (True ou False): ')
    resultado = operacao_and(exp_1, exp_2)
    print(f'O resultado da operação AND entre as expressões é: {resultado}')
'''
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
'''
def operacao_or(exp_1=bool, exp_2=bool) -> bool:
    return exp_1 or exp_2


def obtem_expressao_booleana(mensagem=str) -> bool:
    entrada = input(mensagem).capitalize().strip()
    if entrada == 'True':
        return True
    elif entrada == 'False':
        return False
    else:
        raise ValueError("Entrada inválida. Digite 'True' ou 'False'.")


if __name__ == '__main__':

    exp_1 = obtem_expressao_booleana(
        'Digite a primeira expressão booleana (True ou False): ')
    exp_2 = obtem_expressao_booleana(
        'Digite a segunda expressão booleana (True ou False): ')
    resultado = operacao_and(exp_1, exp_2)
    print(f'O resultado da operação OR entre as expressões é: {resultado}')
'''
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
'''
def alterar_expressao_booleana(exp_1: bool) -> bool:
    return not exp_1


def obtem_expressao_booleana(mensagem=str) -> bool:
    # Converte a entrada para maiúsculo e remove espaços em branco
    entrada = input(mensagem).capitalize().strip()
    if entrada == 'True':
        return True
    elif entrada == 'False':
        return False
    else:
        raise ValueError("Entrada inválida. Digite 'True' ou 'False'.")


if __name__ == '__main__':
    exp_1 = obtem_expressao_booleana(
        'Digite expressão booleana (True ou False): ')
    resultado = alterar_expressao_booleana(exp_1)
    print(f'A inversão da expressão booleana {exp_1} é: {resultado}')
'''
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
'''
def comparar_numeros(num_1=float, num_2=float) -> float:
    if num_1 == num_2:
        return 'Nümeros iguais'
    else:
        return 'Números diferentes'


def obtem_numero(mensagem=str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número válido.')


if __name__ == '__main__':
    num_1 = obtem_numero('Digite o primeiro número: ')
    num_2 = obtem_numero('Digite o segundo número: ')
    resultado = comparar_numeros(num_1, num_2)
    print(f'Os números {num_1} e {num_2} são: {resultado}')
'''
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
'''
def comparar_numeros(num_1=int, num_2=int) -> int:
    if num_1 == num_2:
        return 'Nümeros iguais'
    else:
        return 'Números diferentes'


def obtem_numero(mensagem=str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite um número inteiro válido.')


if __name__ == '__main__':
    num_1 = obtem_numero('Digite o primeiro número: ')
    num_2 = obtem_numero('Digite o segundo número: ')
    resultado = comparar_numeros(num_1, num_2)
    print(f'Os números são: {resultado}')
'''


# #### try-except e if

# 21: Conversor de Temperatura
def converter_celsius_para_fahrenheit(celsius=float) -> float:
    return (celsius * 9/5)+32


def obtem_temperatura(mensagem=str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digite um número válido.')


if __name__ == "__main__":
    celcius = obtem_temperatura(
        'Digite a temperatura em Celsius a ser convertida em Fahrenheit: ')
    resultado = converter_celsius_para_fahrenheit(celcius)
    print(f'Temperatura {celcius}°C convertido em Fareinheit é: {resultado}°F')

# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
