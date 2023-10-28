"""
Operadores Lógicos - And (E), Or (Ou), Not (Não)

And - Todas as condições precisam ser verdadeiras. Se qualquer valor for considerado como falso, 
a expressão inteira será avaliada naquele valor. 

Or - Qualquer condição como verdadeira avalia toda a expressão como verdadeira. Se qualquer valor for 
considerado verdadeiro a expressão inteira será avaliada naquele valor.

Not - Usado para inverter expressões (Not True = False, Not False = True)

São considerados Falsy (que vc já viu) - 0, 0.0, '', False.
Também existe o tipo None que é usado para representar um não valor.
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
print(0 or False or 0.0 or 'abc' or True)

# senha = input('Senha: ') or 'Sem senha'
senha = input('Senha: ')
if not senha:
    print('Você não digitou nada')



if 0 and 1:
    print(True and 1)

print(not 0)
print(not True)
