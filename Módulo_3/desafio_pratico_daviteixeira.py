'''

Um sistema que identifica a idade da pessoa e nomeia se é criança, adolescente, adulto ou idoso. 

'''


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