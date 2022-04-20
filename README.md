# MedicarAPI

A API medicar é baseada em um sistema para gestão de consultas em uma clínica médica, na qual o administrador pode cadastrar médicos e agendas para os médicos e o cliente pode marcar consultas para o médico desejado.

### Configuração da Máquina

Passo 1:

Antes de iniciar a instalação do projeto, deve-se configurar a máquina com os pré-requisitos. Deve-se verificar se o Python3, pip e virtualenv estão instalados na máquina.

```sh
$ python3 –-version
```

```sh
$ python3 -m pip --version
```

```sh
$ virtualenv --version
```

Passo 2:

Caso algum não estiver instalado, deve ser instalado, através dos seguintes comandos:

```sh
$ sudo apt-get install python3.8
```

```sh
$ sudo apt-get install python3-pip
```

```sh
$ sudo pip install virtualenv
```
### Instalação do Projeto

Após a configuração da máquina, pode-se instalar o projeto.

# Passo 1 - Copie o código do projeto:

(CHAVE HTTPS)
```sh
https://github.com/flavioCoder1/medicarAPI.git
```

(CHAVE SSH) 
```sh
git@github.com:flavioCoder1/medicarAPI.git
```

# Passo 2: Criar o ambiente virtual e ativá-lo:

```sh
virtualenv env && source ~/app_medicar/.venv/bin/activate
```

# Passo 3 - Instalar dependências:

```sh
pip install -r requirements.txt
```

# Passo 4 - Executar migrate:

```sh
python3 manage.py migrate
```

# Passo 5 - Criar o superusuário (admin):

```sh
python3 manage.py createsuperuser
```

# Passo 6 - Executar aplicação:

```sh
python3 manage.py runserver
```

# Passo 7 :

Acesse http://127.0.0.1:8000/ no seu navegador para abrir a aplicação.

## Tecnologias

- <img src="https://camo.githubusercontent.com/e34e1fd8b88a76ad738eff256a773aa6c69b412c/68747470733a2f2f7777772e646a616e676f70726f6a6563742e636f6d2f732f696d672f6c6f676f732f646a616e676f2d6c6f676f2d6e656761746976652e706e67" width="150">
- <img src="https://www.django-rest-framework.org/img/logo.png" width="150">
- <img src="https://www.python.org/static/community_logos/python-logo.png" width="150">
- <img src="https://www.docker.com/wp-content/uploads/2022/03/horizontal-logo-monochromatic-white.png" width="150">
- <img src="https://www.seekpng.com/png/full/525-5256723_docker-compose-logo.png" width="150">
