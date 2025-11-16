# Herança

# class Pessoa:
#     def __init__(self, nome, idade, cor):
#         self.nome = nome
#         self.idade = idade
#         self.cor = cor

# class Funcionario(Pessoa):
#     def __init__(self, nome, idade, cor, salario):
#         super().__init__(nome, idade, cor)
#         self.salario = salario

#     def apresentar(self):
#         return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, sou da cor {self.cor} e meu salário é R$ {self.salario}."

# Func1 = Funcionario("João", 30, "branca", 3000)

# print(Func1.apresentar())


class Computador:
    def __init__(self, modelo, processador, qtd_memoria, departamento):
        self.modelo = modelo
        self.processador = processador
        self.qtd_memoria = qtd_memoria
        self.departamento = departamento


class PlacaVideo(Computador):
    def __init__(self, modelo, processador, qtd_memoria, departamento, placa_video):
        super().__init__(modelo, processador, qtd_memoria, departamento)
        self.placa_video = placa_video

    def detalhes(self):
        return f"Computador modelo {self.modelo} com processador {self.processador}, {self.qtd_memoria}GB de memória, do departamento {self.departamento}, equipado com placa de vídeo {self.placa_video}."


Comp1 = PlacaVideo("Dell XPS", "Intel i7", 16, "TI", "NVIDIA RTX 3060")

print(Comp1.detalhes())
