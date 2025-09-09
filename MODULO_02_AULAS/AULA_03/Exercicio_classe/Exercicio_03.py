# Crie uma classe Carro com os atributos marca,
# modelo e ano. Use o método __init__ para inicializar esses valores.
# Crie três objetos e mostre suas informações.

class Carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
    
