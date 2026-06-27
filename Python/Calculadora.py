n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
operacao = input(' Escolha a operação (+, -, *, /): ')

if operacao == "+":
    print(f'Resultado: {n1 + n2}')
elif operacao == "-":
    print(f'Resultado: {n1 - n2}')
elif operacao == "*":
    print(f'Resultado: {n1 * n2}')
elif operacao == "/":
    if n2 != 0:
        print(f'Resultado: {n1 / n2:.2f} ')
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print('Operação invalida')    
    