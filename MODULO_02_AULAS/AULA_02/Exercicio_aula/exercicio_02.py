# Peça ao usuário dois números e tente multiplicá-los.
# Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    valor = int(input("Digite um número\n"))
    valor2 = int(input("Digite outro número\n"))

except: print("Favor Digite um número valido")
else:
    print(f" {valor} * {valor2} é igual: {valor*valor2}")