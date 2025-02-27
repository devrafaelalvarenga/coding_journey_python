# try-except e if

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
