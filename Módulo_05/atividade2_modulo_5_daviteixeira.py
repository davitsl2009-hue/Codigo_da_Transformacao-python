'''

Desenvolva uma função para calcular a média de um aluno e determinar se foi aprovado ou reprovado.
Crie uma função chamada calcular_media() que receba as notas de um aluno, calcule a média e exiba se o aluno foi aprovado ou reprovado com base na média 7.

'''

def calcular_media(notas):

    media = sum(notas) / len(notas)

    if media >= 7:
        print(f"Média: {media:.2f} - Aluno aprovado!")
        
    else:
        print(f"Média: {media:.2f} - Aluno reprovado.")

calcular_media([8.0, 6.5, 7.5])
