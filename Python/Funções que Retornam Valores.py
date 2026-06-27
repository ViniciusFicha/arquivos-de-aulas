"""
Funções que Retornam Valores (A Calculadora)

Objetivo:

Vamos criar uma função que funciona como uma mini-calculadora. 
Ela vai receber dois números, somá-los e, em vez de imprimir o resultado, vai nos 
devolver o valor calculado para que possamos usá-lo no resto do programa.
"""
def calcular_somar(num1, num2):
    return num1 + num2

# Usando a função e armazenando o resultado em uma variável
resultado = calcular_somar(15, 7)
print("O resultado da soma é:", resultado)
print(f"Agora vamos usar esse resultado: {resultado} + 10 = {resultado + 10}")