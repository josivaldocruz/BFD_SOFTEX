# Crie um programa que peça ao usuário um número inteiro.
#Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

try:
    valor = int(input("Digite um número inteiro\n"))

except: print("Favor Digite um número valido")
else:
    print(f"Conversão for bem-sucedida, você digitou o número: {valor}")