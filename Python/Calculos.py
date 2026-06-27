n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))

#calculo
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2 


print(f'Soma {soma:.2f}')
print(f'Subtração {subtracao:.2f}')
print(f'Multiplicação {multiplicacao:.2f}')
print(f'Divisão {divisao:.2f}')
if n2 != 0:
    divisao = n1 / n2
else:
    print('Não é possivel dividir por zero.')