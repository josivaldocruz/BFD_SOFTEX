# Crie uma classe Autenticacao com um método login().
# Crie outra classe Permissao com um método verificar_permissao().
# Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?.

class Autenticação:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    def login(self): pass
class Permissao:
    def verificar_permissao(self): pass
class Administrador(Autenticação, Permissao):
    def __init__(self, login, senha):
        super().__init__(login, senha)
        return f"Login: {self.login}, Senha: {self.senha}"

admin = Administrador("admin", "1234")
print(admin.login())