"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
#tamanho_nome = len(nome)
#print(nome)
#print(tamanho_nome)
#print(nome[2])

#nova_string = '*'
#nova_string += '*L*u*i*z* *O*t*á*v*i*o*'
indice = 0
nova_string = ''
while indice < len(nome):
    nova_string += '*' + nome[indice]
    indice += 1
nova_string += '*'
print(nova_string)