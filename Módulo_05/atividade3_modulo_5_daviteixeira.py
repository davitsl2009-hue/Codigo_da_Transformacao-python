'''

Crie uma função que recebe uma lista de números e retorna o maior e o menor.
Escreva uma função chamada maior_menor() que receba uma lista de números e retorne o maior e o menor valores da lista.

'''
def maior_menor(lista):

    maior = max(lista)
    menor = min(lista)
    return maior, menor

numeros = [3, 7, 1, 9, 4]
print("Maior e menor:", maior_menor(numeros))
