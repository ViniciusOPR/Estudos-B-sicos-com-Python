nome = "Vinicius"
altura = 1.80
peso = 80.12
imc = peso / (altura * altura)

resposta_formatada = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}'

print(resposta_formatada)

# Método FORMAT

a= -1
b= 12
c= 1.1
string = 'b={n2} a={n1} c={n3} '
format = string.format(
    n1=a, n2=b, n3=c
    )

print(format)

"""
 Formatação Básica de Strings

s - string
d - int
f- float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - esquerda
< - direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion Flags - !r, !s, !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.48734879:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')