'''

Salve e carregue um dicionário de clientes em um arquivo JSON.

JSON é um formato amplamente utilizado para troca de dados

Crie um programa que salve um dicionário de clientes em um arquivo .json e, depois, carregue e exiba os dados.

'''

import json

clientes = {
    "cliente1": {"nome": "Davi", "idade": 16},
    "cliente2": {"nome": "Ivan", "idade": 80}
}

with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo)

with open("clientes.json", "r") as arquivo:

    dados = json.load(arquivo)
    print("Dados carregados do JSON:", dados)
