"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
Exiba:
   Seu nome é {nome}
   Seu nome é {nome invertido}
   Seu nome contém (ou não) espaços
   Seu nome tem {n} letras 
   A primeira letra do seu nome é {letra}
   A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
   exiba "desculpe, você deixou campos vazios"
"""

nome = input('Digite o seu nome: ')
idade = input ('Digite o sua idade: ')
nome_invertido = nome[::-1]
primeira_letra = nome[0]
ultima_letra = nome[-1]
n = len(nome)

if nome and idade:
    print(f'Seu nome é {nome}, seu nome invertido é {nome_invertido}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {n} letras')
    print(f'A primeira letra do seu nome é {primeira_letra} e a última é {ultima_letra}')
else:
    print('Desculpe, você deixou campos vazios')