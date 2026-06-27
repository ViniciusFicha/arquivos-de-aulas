"""
split e join com list e str
split - divide uma string
join - une uma string
"""
frase = 'olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases):
    lista_frases.append(lista_frases[i].strip())

#print(lista_frases_cruas)
#print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
