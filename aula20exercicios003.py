"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n1 = input('Digite um número inteiro: ')

if n1.isnumeric():
    n1 = int(n1)

    if n1 % 2 == 0:
       print(f'{n1} é par')
    elif n1 % 2 != 0:
       print(f'{n1} é impar')
    
else:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite um horário: ')

if hora.isnumeric():
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora > 11 and hora <= 17:
        print('Boa Tarde')
    elif hora > 17 and hora <= 23:
        print('Boa Noite')
    else:
        print('Não conheço essa hora')

else:
    print('Dados inválidos')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('informe o seu nome: ')
# pode -se colocar o len numa váriavel chamada tamanho_nome
tamanho_nome = len(nome)

if nome.isnumeric():
    print('Dados inválidos')
else:
    print('Recebendo informações')
    if tamanho_nome > 1:
       if tamanho_nome <= 4:
           print('Seu nome é curto')
       elif tamanho_nome > 4 and tamanho_nome <= 6:
           print('Seu nome é normal')
       elif tamanho_nome > 6:
           print('Seu nome é longo')
    else:
        print('Digite mais letras.')



# Em todos os exercicios pode se usar try & except.
  
