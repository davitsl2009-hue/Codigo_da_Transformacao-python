
def calculadora():
    """
    Função principal que simula uma calculadora e trata erros de divisão por zero.
    """
    print("--- Calculadora Simples ---")
    

    try:

        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        
        operacao = input("Escolha a operação (+, -, *, /): ")
        
        resultado = None 

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
            

        elif operacao == '/':
            try:

                resultado = num1 / num2
                
            except ZeroDivisionError:
                print("\nERRO: Não é possível dividir por zero!")
                return
        else:

            print("\nERRO: Operação inválida. Use apenas +, -, *, ou /.")
            return

        if resultado is not None:
            print(f"\nResultado da operação: {num1} {operacao} {num2} = {resultado}")


    except ValueError:
        print("\nERRO: Entrada inválida. Certifique-se de inserir apenas números.")
    
    else:
        print("Operação concluída com sucesso.")

if __name__ == "__main__":
    calculadora()