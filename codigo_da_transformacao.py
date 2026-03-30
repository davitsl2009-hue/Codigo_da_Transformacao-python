'''

login e senha do usuario, juntamente com a autorização de idade, identificando se o usuario é maior
ou menor de idade

'''

print('\nSITE DE APOSTAS')
print('===============')

idade_usuario = int(input('Nos informe a sua idade: '))

if idade_usuario >= 18:
    print('Você esta autorizado para entrar no nosso site.')
    login_usuario = input('Digite o seu login: ')
    senha_usuario = input('Digite sua senha: ')
    
    if senha_usuario == 'vocacao2025':
        print('SENHA CORRETA! Seja Bem-vindo ao site de apostas.')
    else:
        print('SENHA INCORRETA! você esta saindo do nosso site.')
else:
    print('Você não esta autorizado para entrar no site.')

