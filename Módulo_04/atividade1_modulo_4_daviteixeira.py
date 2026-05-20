'''

Crie uma lista de compras e permita adicionar/remover itens dinamicamente.
Escreva um programa que gerencie uma lista de compras. O usuário deve poder adicionar itens, remover itens e visualizar a lista atualizada.

'''

def lista_compras():
    compras = []
    while True:
        print("\n1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Ver lista")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite o item para adicionar: ")
            compras.append(item)
        elif opcao == "2":
            item = input("Digite o item para remover: ")
            if item in compras:
                compras.remove(item)
            else:
                print("Item não encontrado.")
        elif opcao == "3":
            print("Lista de compras:", compras)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

lista_compras()