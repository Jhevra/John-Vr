from funções.UtilidadesCev.Dados import cabecalho
from funções.UtilidadesCev.Functions import fatorial

cabecalho('Desafio 102', 'FatoriArRrr')


# Programa principal
numero = int(input('Dígite um número: '))
mostrar = input('Quer que o processo seja mostrado? [S/N]: ').strip().upper()

print(f'O fatorial de {numero} é igual a {fatorial(numero, mostrar)}')
print('-=' * 35)

ajuda = input('Você quer ver os DOCSTRINGS? [S/N]: ').upper().strip()
print('-=' * 35)

if ajuda == 'S':
    help(fatorial)
