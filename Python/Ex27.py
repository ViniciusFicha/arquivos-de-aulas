# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0

for pergunta in perguntas:
    print('\n' + '-' * 40) # separador visual

    print('pergunta:', pergunta['Pergunta'])
    print('Opções:')

    for i, opcao in enumerate(pergunta['Opções']):
        print(f' {i}) {opcao}')

    resposta = input('\nEscolha uma opção: ')

    if pergunta['Opções'][int(resposta)] == pergunta['Resposta']:
        print('\n✅ Resposta correta!')
        respostas_certas += 1
    else:
        print('\n❌ Resposta errada!')

        print(f'Você acertou {respostas_certas} de 3 perguntas.')
        print('-' * 40) # Outro separador visual

print(f'\n🎉 Você acertou {respostas_certas} de {len(perguntas)} perguntas no total!')