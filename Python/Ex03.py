nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
ano_nascimento = 2025 - idade
maior_de_idade = idade >= 18
altura_cm = float(input('Digite sua altura em centímetros: '))
altura_metros = altura_cm / 100
#Resultados

print(f'Seu nome completo é: {nome} {sobrenome}, você tem {idade} anos')
print(f'Você nasceu em {ano_nascimento} e é maior de idade? {maior_de_idade}')