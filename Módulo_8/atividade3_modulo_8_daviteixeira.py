
class Pessoa:
    """
    Classe Pessoa: Demonstra o uso de __init__ e __str__.
    """
    

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def __str__(self):
        return f"Pessoa(Nome='{self.nome}', Idade={self.idade})"

    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"

pessoa1 = Pessoa("Alice", 30)

print("\n--- Representação de Objeto ---")


print(f"Resultado de print(pessoa1): {pessoa1}") 


print(f"Resultado em formato de lista: {[pessoa1]}")