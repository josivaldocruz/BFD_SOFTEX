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