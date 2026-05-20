'''

Crie um sistema de notas que armazena dados em CSV.
Um arquivo CSV é usado para armazenar dados em tabelas

Desenvolva um programa que permita adicionar notas de alunos e salve os dados em um arquivo .csv. Depois
implemente uma funcionalidade para carregar e exibir essas informações.

'''

import csv

with open("notas.csv", "w", newline="") as arquivo:

    escritor = csv.writer(arquivo)
    escritor.writerow(["Davi", 8.5, 7.0, 9.2])
    escritor.writerow(["Ivan", 6.0, 5.5, 7.0])

with open("notas.csv", "r") as arquivo:

    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)