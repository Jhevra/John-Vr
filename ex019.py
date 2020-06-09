from random import choice

print(f'\033[40;31;1m{"Desafio 19":=^20}\033[m\n\033[33;1m{"PlAvraR":^20}\033[m')
aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')
mylist = [aluno4, aluno3, aluno2, aluno1]
print(f'O aluno escolhido foi o \033[34;1m{choice(mylist)}\033[m')
