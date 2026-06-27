"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para 
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está 
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu 
usuário.
"""

palavra_secreta = 'celular'
tentativas = 0
letras_acertadas = ''

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) != 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta and letra not in letras_acertadas:
        letras_acertadas += letra

    palavra_formada = ''
    for l in palavra_secreta:
        if l in letras_acertadas:
            palavra_formada += l
        else:
            palavra_formada += '*'

    print('Palavra:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f'Parabéns! Você acertou a palavra em {tentativas} tentativas.')
        break
