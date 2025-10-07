class Motor:
    def __init__(self, potencia: int):
        self.potencia = potencia
    def Ligar(self):
        print(f'Motor de {self.potencia} cavalos ligado')

class Carro:
    def __init__(self, modelo: str, pontencia_motor: int):
        self.modelo = modelo
        self.motor = Motor(pontencia_motor)
