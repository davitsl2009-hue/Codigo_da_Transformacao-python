'''

Use math e random para criar um jogo de adivinhação.
Crie um jogo simples onde o programa gera um número aleatório entre 1 e 100, e o jogador precisa adivinhar

Use a biblioteca random para gerar o número e math para ajudar em cálculos adicionais, se necessário

'''

import random
import math

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Adivinhe o número entre 1 e 100!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("O número é maior.")
        else:
            print("O número é menor.")

        diferenca = abs(numero_secreto - palpite)
        print("Dica: distância aproximada =", math.sqrt(diferenca))

jogo_adivinhacao()