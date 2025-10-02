#Crie uma classe abstrata pessoa que tenha os metodo: falar,
# andar e comer e subclasses funcionario e aluno, que herde as caracteristicas
# e metodos pessoa. instancie um objeto para cada subclasse.

from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        print("A pessoa está falando.")
    @abstractmethod
    def andar(self):
        print("A pessoa está andando.")
    @abstractmethod
    def comer(self):
        print("A pessoa está comendo.")

class Funcionario(Pessoa):
    def falar(self):
        super().falar()
    def andar(self):
        super().andar()
    def comer(self):
        super().comer()

class Aluno(Pessoa):
    def falar(self):
        super().falar()
    def andar(self):
        super().andar()
    def comer(self):
        super().comer()
funcionario1 = Funcionario()
funcionario1.falar()
funcionario1.andar()
funcionario1.comer()
aluno1 = Aluno()
aluno1.falar()
aluno1.andar()
aluno1.comer()
print("---------------------------------------------------")

#usando o mesmo exemplo da questão anterior, mas converta a classe pessoa em uma interface.


from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        ...
    @abstractmethod
    def andar(self):
        ...
    @abstractmethod
    def comer(self):
        ...
class Funcionario(Pessoa):
    def falar(self,nome="Funicionário"):
        print(f"O {nome} está falando.")
    def andar(self,nome="Funicionário"):
        print(f"O {nome} está falando.")
    def comer(self,nome="Funicionário"):
        print(f"O {nome} está falando.")

class Aluno(Pessoa):
    def falar(self, nome):
        print(f"O {nome} está falando.")
    def andar(self,nome):
        print(f"O {nome} está andando.")
    def comer(self,nome):
        print(f"O {nome} está comendo.")

funcionario1 = Funcionario()
funcionario1.falar("pedro")
funcionario1.andar("pedro")
funcionario1.comer()
aluno1 = Aluno()
aluno1.falar("João")
aluno1.andar("João")
aluno1.comer("João")
