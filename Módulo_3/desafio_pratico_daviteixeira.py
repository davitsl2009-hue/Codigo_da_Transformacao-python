'''

Um sistema que identifica a idade da pessoa e nomeia se é criança, adolescente, adulto ou idoso. 

e um desafio extra da propria plataforma.

'''
#ATIVIDADE PRINCIPAL

idade_usuario = int(input('Nos informe a sua idade: '))

if idade_usuario <= 10:

    print('Você é uma criança!')

elif idade_usuario >= 10:
    print('Você é um adolescente! ')

elif idade_usuario >= 20:
    print('Você é um adulto! ')

elif idade_usuario >= 60:
    print('Você é um idoso! ')




#DESAFIO EXTRA

print('1. Adição')
print('2. Subtração')
print('0. Sair do sistema')

while True:

    escolha_usuario = input('Qual operação você deseja efetivar? ')

    if escolha_usuario == '1':
        print('Você escolheu a operação Adição!')

        numero_um = int(input('Digite o primeiro número da soma: '))

        numero_dois = int(input('Digite o Segundo número da soma: '))

        result = (numero_um + numero_dois)

        print(f'Sua Soma é {result}!')

    elif escolha_usuario == '2':
        print('Você escolheu a operação Subtração!')

        numero_um = int(input('Digite o primeiro número da subtração: '))

        numero_dois = int(input('Digite o Segundo número da subtração: '))

        result = (numero_um - numero_dois)

        print(f'Sua subtração é {result}!')


    elif escolha_usuario == '0':
        print('Saindo Do Sistema...')
        break

    else:
        print('Opção inválida! tente novamente.')