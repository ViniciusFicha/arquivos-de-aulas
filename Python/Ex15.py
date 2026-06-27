"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora (0-24): ")
try: 
    hora = int(hora)
    if 0 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    elif 18 <= hora < 24:
        print("Boa noite!")
except ValueError:
        print("Hora inválida.")