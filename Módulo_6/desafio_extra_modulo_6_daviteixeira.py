'''

Criar um sistema de backup automático copiando arquivos para outra pasta.

O objetivo é criar um script que copie arquivos importantes de uma pasta para outra, simulando um sistema de backup

Use a biblioteca shutil para realizar as cópias.

'''
import shutil
import os

def backup(pasta_origem, pasta_destino):

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)


    for arquivo in os.listdir(pasta_origem):

        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)

        if os.path.isfile(caminho_origem):
            shutil.copy(caminho_origem, caminho_destino)
            print(f"Arquivo {arquivo} copiado para {pasta_destino}")

backup("pasta_origem", "pasta_backup")