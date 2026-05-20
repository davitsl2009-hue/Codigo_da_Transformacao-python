'''

Crie um arquivo .txt, grave e leia informações a partir dele.
Nesta atividade, você criará um programa que escreve informações em um arquivo .txt e
em seguida, lê e exibe essas informações. Isso é útil para armazenar dados simples e reutilizá-los.

'''


with open("dados.txt", "w") as arquivo:

    arquivo.write("Este é um teste de gravação em arquivo.\n")
    arquivo.write("O professor ivan esta corrigindo esta atividade!")


with open("dados.txt", "r") as arquivo:

    conteudo = arquivo.read()
    print("Conteúdo do arquivo TXT:\n", conteudo)
