# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
numero = int(input("Digite um número: "))

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

resultado = par_ou_impar(numero)
print(f'O número {numero} é {resultado}')
#print(par_ou_impar(numero))