"""
Funções com Parâmetros (Saudação Personalizada)

Objetivo:

Vamos modificar nossa função de saudação. Agora, ela deverá receber 
um nome como parâmetro e usar esse nome para 
exibir uma mensagem personalizada para diferentes pessoas.
"""

def saudacao_personalizada(nome):
    print("----------------------------------------------------")
    print(f"Olá, {nome}! Seja bem-vindo(a) ao nosso programa.")
    print("----------------------------------------------------")

# Testando a função com diferentes nomes

print("\nChamando a função para a primeira pessoa...")
saudacao_personalizada("Alice")

print("\nChamando a função para a segunda pessoa...")
saudacao_personalizada("Bob")  

print("\nChamando a função para a terceira pessoa...")
saudacao_personalizada("Carlos")