"""
Python = Linguagem de Programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

# Aspas Simples
print('ViniciusOP')
print(1, 'Vinicius"OP"')

# Aspas Duplas
print("ViniciusOP")
print(2, "Vinicius'OP'")

# Escape
print('Vinicius \"OP\"')

# r
print(r"Vinicius \"OP\"")

'''
Tipo Int
int -> número inteiro
O tipo int representa qualquer número positivo ou negativo.
int sem sinal é considerado positivo
'''
print(12)
print(-12)
print(0)

'''
Tipo Float
float -> número de ponto flutuante
O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
float sem sinal é considerado positivo.
'''
print(1.2)
print(-1.2)

'''
A função type mostra o tipo que o Python inferiu ao valor
'''
print(type('Carro'))
print(type(14), type(0))
print(type(1.1), type(-7.8), type(0.0))

"""
Tipo de dado bool (Boolean)
Ao questionar algo em um programa, só existem duas respostas possíveis sim (True) e não (False).
Existem vários operadores para "questionar", dentre eles o ==, que é um operador lógico
que questiona se um valor é igual a outro.
"""
print(10==10)
print(10==11)
print(type(True), type(False))
print(type(10==10), type(10==11))