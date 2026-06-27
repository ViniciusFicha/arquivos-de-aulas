# Tipos int e float
# int -> números inteiros
# o tipo int representa qualquer número
# positivo ou negativo. in sem sinal é considerado positivo
#print(11) # int
#print(-11) # int
#print(0)

# float -> número com ponto flutuante
# o tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
#print(1.1, 10.11)  # float

# A função type mostra o tipo que o python
# inferiu ao valor.
print(type('Otávio'))  # <class 'int'>
print(type(1))  # <class 'int'>
print(type(1.1))  # <class 'float'>
print(type(0))  # <class 'int'>
print(type(-1))  # <class 'int'>
print(type(-1.1))  # <class 'float'>
print(type(1.1), type(1), type(-1)) # <class 'float'> <class 'int'> <class 'int'>