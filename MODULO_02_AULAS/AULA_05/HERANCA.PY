# class Animal:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def som(self):
#         print("som indefinido")

# class Cachorro(Animal):
#     def som(self):
#         print("au au")

# doguinho = Cachorro("Rex", 5)

# print(doguinho.nome)
# print(doguinho.idade)

# doguinho.som()

class Mamifero:
    def __init__(self, idade, habitat, som):
        self.idade = idade
        self.habitat = habitat
        self.som = som
        self.prole = "gestação"
        self.alimento_infantil = "leite"

    def som(som):
        print(som)

class Morcego(Mamifero):
     def __init__(self, idade, habitat, som):
        super().__init__(idade, habitat, som)
        self.locomoção = "voa"

zubat = Morcego(1,"laje","assobio")

print(zubat.idade)
print(zubat.habitat)
print(zubat.som)
print(zubat.prole)
print(zubat.alimento_infantil)
print(zubat.locomoção)