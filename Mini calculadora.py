def calculadora():
    print("Mini Calculadora Simples")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    operacao = input("Escolha a operação (1/2/3/4): ")

    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida!")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite números válidos.")
        return

    if operacao == '1':
        resultado = num1 + num2
    elif operacao == '2':
        resultado = num1 - num2
    elif operacao == '3':
        resultado = num1 * num2
    elif operacao == '4':
        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
            return
        resultado = num1 / num2

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()