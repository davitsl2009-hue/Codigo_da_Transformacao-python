'''

Criar um sistema de Biblioteca

Class Livro

Class biblioteca (main)

      (Produtos) Livros, Periodicos, Jornal, Maps, Gibi/Mangas
    
      (Processos / Serviços)
      Ler, Pesquisa, Emprestado-Devolução
Atributos - Metodo
'''

class Livros:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        return f" '{self.titulo}' - {self.autor} [status]"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo_procuarado):
        for livro in self,livros:
            if livro.titulo == titulo_procuarado:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Emprestimo de '{livro.titulo}' realizado!")
                else:
                    print(f"O Livro '{livro.titulo}' Já esta ocupado")
                return
        print("Livro Não encontrado no acervo. ")