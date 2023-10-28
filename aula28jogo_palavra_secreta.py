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
import os
palavra_secreta = 'fallout'
letras_acertadas = ''
numero_tentativas = 0

while True:
        
        letra = input('Digite uma letra: ')
        numero_tentativas += 1

        if letra.isnumeric():
            print('Digite apenas letras.')
            continue

        elif len(letra) > 1:
            print('Digite apenas uma letra.')
            continue
    
        if letra in palavra_secreta:
            letras_acertadas += letra
        
        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print('palavra_formada: ', palavra_formada)
       
        if palavra_formada == palavra_secreta:
            os.system('cls')
            print('VOCÊ GANHOU!!!, a palavra era: ', palavra_secreta)
            print('Tentativas: ', numero_tentativas)
            letras_acertadas = ''
            numero_tentativas = 0