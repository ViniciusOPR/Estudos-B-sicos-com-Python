"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Gato'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)
print(string.zfill(10))