
from atividade1_modulo_8_daviteixeira import Carro

class CarroEletrico(Carro):
    """
    Classe CarroEletrico: Herda de Carro e adiciona um atributo específico.
    """
    
    def __init__(self, marca, modelo, autonomia_bateria):

        super().__init__(marca, modelo) 
        

        self.autonomia_bateria = autonomia_bateria 
        self.carga_bateria = 100

    def exibir_info(self):

        super().exibir_info() 
        print(f"Autonomia da Bateria: {self.autonomia_bateria} km")
        print(f"Carga Atual: {self.carga_bateria}%")

carro_eletrico = CarroEletrico("Tesla", "Model S", 500)

print("\n--- Informações do Carro Elétrico ---")

carro_eletrico.exibir_info()

carro_eletrico.ligar()