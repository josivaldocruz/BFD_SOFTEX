class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self.idade = None

class Turma:
    def __init__(self, nome: str):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f'Aluno: {aluno.nome}, na Turma: {self.nome}')

a1 = Aluno('Ana')
a2 = Aluno('Bruno')

turma = Turma("turma A")
turma.adicionar_aluno(a1)
turma.adicionar_aluno(a2)
turma.listar_alunos()