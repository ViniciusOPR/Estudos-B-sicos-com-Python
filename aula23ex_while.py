"""
Iterando strings com While
"""

nome = 'Vinicius'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[0:8])

nova_string = 0
while nova_string < tamanho_nome:
    print(nova_string, nome[nova_string])
    nova_string +=1
    

      

print('Acabou')

