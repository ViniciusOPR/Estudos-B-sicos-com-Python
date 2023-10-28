"""
Faça uma lista de compras com listas. O usuário deve ter a possibilidade
de inserir, apagar e listar valores da sua lista. Não permita que o 
programa quebre com erros de índices inexistentes na lista.
"""
  
import os

lista_de_compras = []
while True:
        print('Selecione uma opção')
        opcao = input('[i]nserir [a]pagar [l]istar: ')


        if opcao == 'i':
            os.system('cls')
            valor = input('Valor: ')
            lista_de_compras.append(valor)

        elif opcao == 'a':
            
            indice_str = input('Escolha um índice para apagar: ')
            try:
                indice = int(indice_str)
                del lista_de_compras[indice]
            except ValueError:
                print('Por favor digite um número inteiro')
            except IndexError:
                print('índice não existe na lista')
            except Exception:
                print('Erro Desconhecido')
            

        elif opcao == 'l':
            os.system('cls')

            if len(lista_de_compras) == 0:
                print('Nada para listar')

            for indice, valor in enumerate(lista_de_compras):
                print(indice, valor)
        
        else: 
            print('Por favor, escolha i, a ou l')
        
   
    
        