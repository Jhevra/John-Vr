from funções.UtilidadesCev.Dados import cabecalho
from funções.UtilidadesCev.Functions import leiaint

cabecalho('Desafio 104', 'INTEIRORRrr')


# Programa principal
n = leiaint('Dígite um número: ')
print('-='*36)
print(f'Você acabou de dígitar \033[31;1m{n}\033[m')
