"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
n1 = input("Digite um número inteiro: ")
try:
    n1 = int(n1)
    if n1 % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Não é um número inteiro.")
