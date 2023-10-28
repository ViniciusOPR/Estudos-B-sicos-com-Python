"""
Operadores IN e Not In
Strings são iteráveis
0-1-2-3-4-5
o-t-a-v-i-o
5-4-3-2-1-0
"""

nome = 'rian'
print(nome[2])
print(nome[-1])
print('r' in nome)
print('vi' in nome)
print(10 * '-')
print('r' not in nome)
print('vi' not in nome)



nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome: 
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')