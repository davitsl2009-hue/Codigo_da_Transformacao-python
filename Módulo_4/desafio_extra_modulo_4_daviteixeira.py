'''

Desafio Extra: Criar um sistema de agenda de contatos usando dicionários.
Desenvolva um programa que permita armazenar contatos em um dicionário, onde o nome é a chave e o número de telefone é o valor. O programa deve permitir adicionar, remover e buscar contatos.

'''

def agenda_contatos():

    contatos = {}

    while True:

        print("\n1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Buscar contato")
        print("4 - Ver todos")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            nome = input("Nome: ")
            telefone = input("Telefone: ")
            contatos[nome] = telefone

        elif opcao == "2":

            nome = input("Nome para remover: ")
            if nome in contatos:
                del contatos[nome]

            else:
                print("Contato não encontrado.")

        elif opcao == "3":
            nome = input("Nome para buscar: ")

            if nome in contatos:
                print(f"{nome}: {contatos[nome]}")

            else:
                print("Contato não encontrado.")

        elif opcao == "4":
            print("Agenda completa:", contatos)

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")

agenda_contatos()