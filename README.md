## Requisitos

* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version
* GIT - Conferir a instalação: git -v

## Como rodar o projeto baixado

Baixar o projeto do GitHub.
```
git clone https://github.com/celkecursos/master-week-python-e-django-two.git .
```

Criar o ambiente virtual.
```
python -m venv venv
```

Ativar o ambiente virtual.
```
venv\Scripts\activate
```

Instalar as dependências.
```
pip install -r requirements.txt
```

Executa as migration para criar as tabelas no banco de dados.
```
python manage.py migrate
```

Executar as seeds para cadastrar registro de teste.
```
python manage.py seed_home
python manage.py seed_address_contact
python manage.py seed_about
```

Criar o super usuário.
´´´
python manage.py createsuperuser
´´´
´´´
Username (leave blank to use 'cesar'): admin
Email address: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
´´´

Rodar o projeto.
```
python manage.py runserver
```

Acessar o padrão do Python.
```
http://127.0.0.1:8000/
```

Acessar o sistema administrativo padrão do Django.
´´´
http://127.0.0.1:8000/admin
´´´

Usuário: admin<br>
Senha: 123456A#



## Sequencia para criar o projeto

Criar o ambiente virtual.
```
python -m venv venv
```

Ativar o ambiente virtual.
```
venv\Scripts\activate
```

Instalar o Django.
```
pip install Django
```

Criar o projeto com Django.
```
django-admin startproject admin .
```

Gerar o arquivo com as dependências.
Após instalar a dependência, execute o comando abaixo.
```
pip freeze > requirements.txt
```

Executa as migration.
```
python manage.py migrate
```

Rodar o projeto.
```
python manage.py runserver
```

Acessar o padrão do Python.
```
http://127.0.0.1:8000/
```

Criar um super usuário.
```
python manage.py createsuperuser
```
```
Usuário (leave blank to use 'cesar'): admin
Endereço de email: cesar@celke.com.br
Password: 123456A#
Password (again): 123456A#
```

Acessar o sistema administrativo padrão do Python.
```
http://127.0.0.1:8000/admin
```

Criar novo app.
```
python manage.py startapp nome-do-app
```
```
python manage.py startapp courses
```

Criar a migration que será responsável em criar a tabela no banco de dados.
```
python manage.py makemigrations
```

Executar as migrations para criar as tabelas no banco de dados.
```
python manage.py migrate
```

Executar as seeds para cadastrar registro de teste.
```
python manage.py seed_home
```

## Como usar o GitHub.

Inicializar um novo repositorio GIT.
```
git init
```

Adicionar todos os arquivos modificados na área de preparação.
´´´
git add .
´´´

Commit registra as alterações feitas nos arquivos que foram adicionados na área de preparação.
´´´
git commit -m "Base do projeto"
´´´

Verificar em qual branch está.
´´´
git branch
´´´

Renomear a branch atual no GIT para main.
´´´
git branch -M main
´´´

Adicionar um repositório remoto ao repositório local.
´´´
git remote add origin https://github.com/celkecursos/master-week-python-e-django-two.git
´´´

Enviar os commits locais para um repositório remoto.
´´´
git push -u origin main
´´´
