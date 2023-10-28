adicao = 10 + 10
print("Adição:", adicao)

subtracao = 5 - 2
print("Subtração:", subtracao)

multiplicacao = 10 * 10 
print("Multiplicação:", multiplicacao)

divisao = 10 / 3
print("Divisão:", divisao)

divisao_inteira = 10 // 3
print("Divisão Inteira:", divisao_inteira)

exponenciacao = 2 ** 10
print("Exponenciação:", exponenciacao)

modulo = 55 % 2 # resto da divisão
print("Módulo:", modulo)

print(10 % 8 == 0)
print(64 % 4 == 0)
print(10 % 3 == 0)

# Peculiaridades - Concatenação e Repetição

concatenacao = 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'a' * 10
luiz_tres_vezes = 3 * "Luiz"
print(luiz_tres_vezes)
print(a_dez_vezes)

# Precedência em Operadores Aritméticos

"""
1. (n + n), 2. **, 3. * / // &, 4. + -

"""
conta = (1 + int(0.5 +0.5)) ** (5 + 5)
print(conta)

# Cálculo IMC

nome = "Vinicius"
altura = 1.80
peso = 80.12
imc = peso / (altura * altura)

print(nome, "tem", altura, "de altura, pesa", peso, "quilos e seu IMC é", imc)