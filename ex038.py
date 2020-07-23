from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 38', 'MAIORRrr e MENORRrr')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    maior = n1
    print(f'O primeiro valor é maior')

elif n2 > n1:
    maior = n2
    print(f'O segundo valor é maior')

else:
    print(f'Os dois valores são iguais.')