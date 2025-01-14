## Requisitos

* Python 3 ou superior - Conferir a versão: python --version
* Django 5 ou superior - Conferir a versão: django-admin --version

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