# Escreva um programa que peça ao usuário para digitar um número.
# Trate o erro caso ele digite algo que não seja um número inteiro.

try:
    valor = int(input("Digite um número\n"))
except:
    print("Favor Digite um número valido")
else:
    print(f"Obrigado por digitar o número: {valor}")
