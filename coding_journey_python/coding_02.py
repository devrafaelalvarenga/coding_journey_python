# Cálculo de KPI

# 1) Solicita ao usuário que digite seu nome
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
# 4) Calcule o valor do bônus final
# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus


# Verifica se a string contém apenas letras e espaços.
def isalpha_with_spaces(s: str) -> bool:
    return all(char.isalpha() or char.isspace() for char in s)


def coletar_nome(mensagem=str) -> str:
    tentativas = 0
    while tentativas < 3:
        try:
            nome_usuario = input(mensagem).title()
            if isalpha_with_spaces(nome_usuario) == False:
                raise ValueError("Nome inválido. Use apenas letras e espaços.")
        except ValueError as e:
            print(e)
            tentativas += 1
            if tentativas == 3:
                print("Número de tentativas excedido. Tente novamente mais tarde.")
                exit()
            else:
                print(f"Tentativas restantes: {3 - tentativas}")
        else:
            return nome_usuario


def coletar_salario(valor_salario=float) -> float:
    try:
        valor_salario = float(input('Digite o valor do seu salário: '))
        if valor_salario <= 0:
            raise ValueError
        elif valor_salario.is_integer() == False:
            raise ValueError
    except ValueError:
        print('Digite um valor válido')
    else:
        return valor_salario


def coletar_bonus(valor_bonus=float) -> float:
    valor_maximo_bonus = 10
    try:
        valor_bonus = float(input('Digite o valor do seu bônus: '))
        if valor_bonus <= 0 or valor_bonus > valor_maximo_bonus:
            raise ValueError
    except ValueError:
        print('Digite um valor válido')
    else:
        return valor_bonus


def calcular_valor_kpi(valor_salario=float, valor_bonus=float, valor_variavel=10) -> float:
    valor_kpi = valor_variavel + (valor_salario * valor_bonus)
    return valor_kpi


if __name__ == '__main__':
    periodo_analisado = 2025
    nome_usuario = coletar_nome('Digite seu nome: ')
    valor_salario = coletar_salario('Digite o valor do seu salário: ')
    valor_bonus = coletar_bonus('Digite o valor do seu bônus: ')
    valor_kpi = calcular_valor_kpi(valor_salario, valor_bonus)
    print(f'Olá {nome_usuario}, seu salário é de R$ {valor_salario:.2f} e seu bônus tem peso {valor_bonus}.\n'
          f'Seu KPI para o ano de {periodo_analisado} é de R$ {valor_kpi:.2f}.')
