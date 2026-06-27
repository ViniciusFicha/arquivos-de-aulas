# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

#resultado = multiplica(1, 2, 3, 4, 5)
#print(resultado)
resultado = multiplica(n1, n2)
print(f'O resultado da Multiplicação entre {n1} e {n2} é: {resultado}')
