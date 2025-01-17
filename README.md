Código-fonte das lives sobre [Master Week Python e Django - Two](https://www.youtube.com/watch?v=1rFJ-eANS8k&list=PLmY5AEiqDWwBZurqD6xQdYdkbVEQwaU3O).<br>

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

## Conectar o PC ao servidor com SSH

Criar chave SSH (chave pública e privada).
```
ssh-keygen -t rsa -b 4096 -C "seu-email@exemplo.com"
```
```
ssh-keygen -t rsa -b 4096 -C "cesar@celke.com.br"
```

Local que é criado a chave pública.
```
C:\Users\SeuUsuario\.ssh\
```
```
C:\Users\cesar/.ssh/
```

Exibir o conteúdo da chave pública.
```
cat ~/.ssh/id_rsa.pub
```

Acessar o servidor com SSH.
```
ssh root@93.127.210.72
```

Digite yes quando for solicitado.
```
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

Para não informar o dominio e sair da configuração.
```
CTRL + C
```

Usar o terminal conectado ao servidor para listar os arquivo.
```
cd /usr/local/lsws/Example/html/demo
```

Listar os arquivo do servidor.
```
ls -l
```

Remover os arquivos do servidor.
```
rm -rf {*,.*}
```

Clonar os arquivos do repositório do GitHub.
```
git clone git@github.com:celkecursos/master-week-python-e-django-two.git .
```

Verificar o Python 3 Instalado.
```
python3 --version
```

Atualizar a lista de pacotes disponíveis.
```
sudo apt update
```

Instalar o pacote para gerar o ambiente virtual.
```
sudo apt install python3-venv -y
```

Criar o ambiente virtual.
```
python3 -m venv venv
```

Ativar o ambiente virtual no Linux.
```
source venv/bin/activate
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

Verificar o status do firewall.
```
sudo ufw status
```

Permitir o acesso à porta 7080 para acessar o painel administrativo do OpenLiteSpeed.
```
sudo ufw allow 7080
```

Definir a senha do administrador do painel administrativo do OpenLiteSpeed.
```
/usr/local/lsws/admin/misc/admpass.sh
```
```
User name [admin]: admin
Password: 123456A#
Retype password: 123456A#
```

Acessar o painel administrativo do OpenLiteSpeed.
```
http://93.127.210.72:7080
```

Remover a permissão de acesso ao OpenLiteSpeed.
```
sudo ufw delete allow 7080
```

Alterar o "Owner" dos arquivos e diretórios de root para "nobody".
```
sudo chown -R nobody:nogroup /usr/local/lsws/Example/html/demo
```

Reiniciar o OpenLiteSpeed.
```
/usr/local/lsws/bin/lswsctrl restart
```

Limpar cache do PIP.
```
pip cache purge
```

Acessar a página inicial do site criada com Django.
´´´
http://<ip-do-servidor>
´´´
´´´
http://93.127.210.72
´´´


## Conectar Servidor ao GitHub

Gerar a chave SSH no servidor.
```
ssh-keygen -t rsa -b 4096 -C "cesar@celke.com.br"
```

Imprimir a chave pública gerada.
```
cat ~/.ssh/id_rsa.pub
```

No GitHub, vá para Settings (Configurações) do seu repositório ou da sua conta, em seguida, vá para SSH and GPG keys e clique em New SSH key.<br>
Cole a chave pública no campo fornecido e salve.<br>

Verificar a conexão com o GitHub.
```
ssh -T git@github.com
```

Se gerar o erro "The authenticity of host 'github.com (xx.xxx.xx.xxx)' can't be established.".<br>
Isso é uma medida de segurança para evitar ataques de "man-in-the-middle".<br>
Necessário adicionar a chave do host do GitHub ao arquivo de known_hosts do seu servidor.<br>

Digite yes quando for solicitado.
```
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

Verificar a conexão novamente.
```
ssh -T git@github.com
```

Mensagem de conexão realizada com sucesso.<br>
Hi nome-usuario! You've successfully authenticated, but GitHub does not provide shell access.<br>