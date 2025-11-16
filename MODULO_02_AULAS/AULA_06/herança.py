# continuação de henraça.


class Animal:
    def __init__(self, especie, habitat):
        self.especie = especie
        self.habitat = habitat


class Mamifero(Animal):
    def movimentar(self):
        print("Caminhando")

    def amamentar(self):
        print("alimentando o filhote")


class Cachorro(Mamifero):
    def __init__(self, especie, habitat, raca):
        super().__init__(especie, habitat)
        self.raca = raca

    def __str__(self):
        return f"O mamífero da espécie {self.especie}, da raça {self.raca} pode ser localizado no {self.habitat}"

    def correr_moto(self):
        print("O cachorro esta correndo atrás da moto")


dog02 = Cachorro("Canis Familiaris", "Rua do seu zé", "Caramelo")

print(dog02)
dog02.amamentar()
dog02.correr_moto()
