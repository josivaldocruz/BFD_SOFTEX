# Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):
    def cadastrar_idade(idade):
        if b <= 0:
            raise IdadeInvalidaError("numero não pode ser menor que zero")
    
        return
try:
    b = int(input("digite aqui\n"))
except IdadeInvalidaError as b:
    print(f"b")
    
