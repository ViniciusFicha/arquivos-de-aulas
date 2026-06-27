'''CPF: 498.723.200-63'''
cpf = '498723200'

soma = 0 
multiplicador = 10

for digito in cpf:
    soma += int(digito) * multiplicador
    multiplicador -= 1

resultado = (soma * 10) % 11
primeiro_digito = 0 if resultado > 9 else resultado

# ...código do primeiro dígito...

cpf_com_primeiro = cpf + str(primeiro_digito)
soma2 = 0
multiplicador = 11

for digito in cpf_com_primeiro:
    soma2 += int(digito) * multiplicador
    multiplicador -= 1

resultado2 = (soma2 * 10) % 11
segundo_digito = 0 if resultado2 > 9 else resultado2

print(f'O primeiro dígito verificado é: {primeiro_digito} ')
print(f'O Segundo dígito verificado é: {segundo_digito} ')
