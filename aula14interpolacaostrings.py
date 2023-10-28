"""
Interpolação Básica de Strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1006.5959933
variavel = '%s, o preço é de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (15, 15))