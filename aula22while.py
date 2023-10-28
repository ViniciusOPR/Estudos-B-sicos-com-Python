"""
Repetições
while (enquanto)
Executa uma ação enquanto a condição for verdadeira
Loop Infinito -> Quando um código não tem fim

operadores de atribuição
=, +=, -=, *=, //=, /=, %=, **=
"""

condicao = True

while condicao:
    nome= input('Qual é o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
print('-' * 10)

# while com contador

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1 # ou contador +=1

print('Acabou')
print('-' * 10)

# while com continue

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')
print('-' * 10)

# while com while

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')