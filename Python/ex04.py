num = int(input(" Digite um número inteiro: "))

# Verificando se o número é PAR ou Impar.

if num % 2 == 0:
    print(f"O número {num} é PAR")
else:
    print(f"O número {num} é ímpar")

# Verificando se o número é Positivo ou Negativo.

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é Zero.")
