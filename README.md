# BFD_MODULO_01
Back-Eend Python Aula 01

criar testo de versionamento
pip freeze > requirements



Preparando o ambiente
Criar diretório para o projeto
Criar e iniciar o ambiente virtual
python -m venv .site_pessoal

#linux
source .site_pessoal/bin/activate

#windows
.site_pessoal/Scripts/activate
Instalar o django
python -m pip install django

Criar um projeto django
Criar um projeto django
django-admin startproject site_pessoal .

Configuração inicial do projeto
Abra o arquivo settings.py
Modificar time zone: TIME_ZONE = 'America/Sao_Paulo'
Modificar idioma: LANGUAGE_CODE = 'pt-BR'
Definir path para arquivos estáticos: STATIC_ROOT = BASE_DIR / 'static'
Criando banco de dados python manage.py migrate
Iniciando o servidor local python manage.py runserver
Criando arquivos de variáveis de ambiente
Instalar python-decouple python -m pip install python-decouple
Na raiz crie um arquivo .env
Abra o arquivo .env e adicione:
SECRET_KEY=
DEBUG=True
Copie o SECRET_KEY do arquivo settings.py (sem aspas) e adicione ao arquivo .env
No arquivo settings.py adicione e modifique:
from decouple import config
#
#
SECRET_KEY = config('SECRET_KEY')
#
#
DEBUG = config('DEBUG', default=False, cast=bool)
Criando super user
python manage.py createsuperuser

Visualizar o Painel django admin
Criar um app django
Criar app: python manage.py startapp blog
Adicionando o app ao settings.py:
Criar o model da postagem
Abra o arquivo models.py
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
Criar tabela do banco de dados
Preparar o arquivo de migração: python manage.py makemigrations blog
Aplicando as modificações no banco de dados python manage.py migrate blog
Atualizando o django admin
No arquivo blog/admin.py adicione:
from django.contrib import admin
from .models import Post

admin.site.register(Post)
URLs no Django
Abra o arquivo urls.py do projeto.
Criando a URL do blog
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
Criando as views
Abra o arquivo views.py
Adicione:
def post_list(request):
    return render(request, 'blog/post_list.html', {})
Brincando com HTML
Dentro do Diretório da aplicação Blog, crie um diretório templates e dentro dele outro diretório chamado blog
Agora crie o arquivo post_list.html dentro do diretório blog/templates/blog
Vamos alimentar o arquivo com um pouco de HTML:
<html>
    <body>
        <p>Olá Mundo!</p>
    </body>
</html>
Django ORM
Vamos entender como funciona a comunicação do Django com o banco de dados.
Vamos iniciar um shell do Django: python manage.py shell
Vamos acessar os posts criados: `Post.objects.all()
Um erro ocorre pois o Django não conhece Post vamos precisar importa-lo.
from blog.models import Post
Post.objects.all()
Se quizermos visualizar os usuários?
User.objects.all()

Vamos criar uma postagem:
Post.objects.create(author="Fred", title="Testando ORM", text="Vamos testar o ORM do Django!!!")
Filtrando dados
Post.objects.filter(author=2)

Post.objects.filter(title__contains='ORM')

Ordenando dados
Post.objects.order_by('create_date)

Publicando uma postagem
post = Post.objects.filter(title__contains='ORM')

post.publish()


source .Projeto_django_site_pessoal/bin/activate
python manage.py runserver

Comando do python para acessar banco de dados
ORM django
python manage.py shell

Comando para acessar banco de dados
Post.objects.all()
Post.object.create()

Criar variavel para usar dentro do Shell
jo = User.objects.get(username="josivaldo")
Post.objects.create(author=jo, title="Testando ORM", text="Vamos testar o ORM do Django!!!")
Post.objects.order_by('create_date)

Post.objects.order_by('created_date')

site para criar pagina
https://getbootstrap.com/
https://fonts.google.com/
