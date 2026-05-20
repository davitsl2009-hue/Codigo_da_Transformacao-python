'''

Desafio Extra:  Criar um sistema de login verificando usuário e senha.
Crie um sistema simples que utilize uma função para validar usuário e senha. Use um dicionário para armazenar os dados de login.

'''

def login(usuario, senha, dados_login):

    if usuario in dados_login and dados_login[usuario] == senha:
        print("Login realizado com sucesso!")

    else:
        print("Usuário ou senha incorretos.")

dados_login = {
    "admin": "1234",
    "davi": "senha123",
    "maria": "abc123"
}

login("davi", "senha123", dados_login)
login("maria", "abc132", dados_login)