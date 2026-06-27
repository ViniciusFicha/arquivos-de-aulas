"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf = "861160990"

soma = 0
multiplicador = 10

for digito in cpf:
    soma += int(digito) * multiplicador
    multiplicador -= 1

resultado = (soma * 10) % 11
primeiro_digito = 0 if resultado > 9 else resultado

cpf_com_primeiro = cpf + str(primeiro_digito)

soma2 = 0
multiplicador1 = 11

for digito in cpf_com_primeiro:
    soma2 += int(digito) * multiplicador1
    multiplicador1 -= 1

resultado2 = (soma2 * 10) % 11
segundo_digito = 0 if resultado2 > 9 else resultado2

print(f'O resultado do primeiro digito é: {resultado}')
print(f'O resultado do segundo digito é: {resultado2}')
print(f'CPF completo: {cpf}{primeiro_digito}{segundo_digito}')
