"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis = índices e fatiamento
métodos úteis: 
append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update Delete (CRUD) - Criar, ler, atualizar e apagar.
"""

# .......+01234
# .......-54321
string = 'abcde' # 5 caracteres (len)
# print(bool([])) # falsy
# print(lista, type(lista))

# .......0....1......2........3....4
#.......-5....-4....-3......-2....-1
lista = [123, True, 'Carlos', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

lista2 = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
del lista2[-1]
# lista.clear()
lista2.insert(100, 5)
print(lista2[3])
print(lista2)
print(lista, 'Removido', ultimo_valor)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
print(lista_c)

"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)