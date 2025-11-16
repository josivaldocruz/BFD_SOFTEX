# Crie uma função dividir(a, b) que lance (raise) uma exceção
# ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro de Divisão, b não pode ser igual a zero")
    return a / b


try:
    a = int(input("Digite um numero\n"))
    b = int(input("Digite um numero\n"))
    e = dividir(a, b)

except ZeroDivisionError as e:
    print(f"{e}")
