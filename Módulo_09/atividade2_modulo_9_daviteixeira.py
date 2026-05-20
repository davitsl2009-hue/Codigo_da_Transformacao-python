class SaldoInsuficienteError(Exception):
    """
    Exceção levantada quando um saque tenta ultrapassar o saldo atual.
    """
    def __init__(self, saldo_atual, valor_saque):

        super().__init__(f"Tentativa de saque de R$ {valor_saque:.2f} falhou. Saldo atual: R$ {saldo_atual:.2f}")
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque


class ContaBancaria:
    """
    Simula uma conta bancária simples com funções de consulta e saque.
    """
    def __init__(self, saldo_inicial=0.0):

        self.saldo = saldo_inicial
        print(f"Conta criada. Saldo inicial: R$ {self.saldo:.2f}")

    def consultar_saldo(self):
        """ Retorna o saldo atual da conta. """
        return self.saldo

    def sacar(self, valor):
        """
        Realiza um saque, levantando SaldoInsuficienteError se necessário.
        """
        if valor <= 0:

            raise ValueError("O valor do saque deve ser positivo.")

        if valor > self.saldo:

            raise SaldoInsuficienteError(self.saldo, valor)
        else:

            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            print(f"Novo saldo: R$ {self.saldo:.2f}")

if __name__ == "__main__":

    minha_conta = ContaBancaria(saldo_inicial=500.00)

    print("\n--- TESTE 1: Saque bem-sucedido ---")
    try:
        minha_conta.sacar(200.00)
    except (SaldoInsuficienteError, ValueError) as e:

        print(f"Falha na transação: {e}")

    print("\n--- TESTE 2: Saque com Saldo Insuficiente ---")
    try:

        minha_conta.sacar(400.00) 
        

    except SaldoInsuficienteError as e:

        print(f"\nERRO DE NEGÓCIO: {e}")
        print("A transação não pôde ser concluída.")

    print(f"\nSaldo Final da Conta: R$ {minha_conta.consultar_saldo():.2f}")