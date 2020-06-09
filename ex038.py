print(f'''\033[40;31;1m{"Desafio 38":=^20}\033[m\n\033[33;1m{"Igualador":^20}\033[m''')
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
menor = n1
maior = n1
if n2 > n1:
    maior = n2
    print(f'O menor numero é {menor} e o maior é {maior}')
elif n2 < n1:
    menor = n2
    print(f'O menor numero é {menor} e o maior é {maior}')
elif n1 == n2:
    print('Os dois são iguais')

