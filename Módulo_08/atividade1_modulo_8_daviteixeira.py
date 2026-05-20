'''

crie uma classe carro que represente veiculos com informações como marca e modelo, e um metodo para exibir esses dados

'''

# Atividade 1: Crie uma classe Carro
class Carro:
    """
    Classe Carro: Representa um veículo com marca e modelo.
    """
    def __init__(self, marca, modelo):

        self.marca = marca  
        self.modelo = modelo
        self.ligado = False  


    def exibir_info(self):
        print(f"\n--- Detalhes do Carro ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Status: {estado}")
    

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} ligado. Pronto para usar!")
        else:
            print(f"{self.modelo} já está ligado.")

carro_a = Carro("Ford", "Mustang")
carro_b = Carro("Chevrolet", "Camaro")

carro_a.exibir_info()
carro_a.ligar()

carro_b.exibir_info()