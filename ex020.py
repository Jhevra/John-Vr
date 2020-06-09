from random import shuffle

print(f'\033[40;31;1m{"Desafio":=^20}\033[m\n\033[33;1m{"Calderar+":^20}\033[m')
alu1 = input('Nome do 1º aluno: ')
alu2 = input('Nome do 2º aluno: ')
alu3 = input('Nome do 3º aluno: ')
alu4 = input('Nome do 4º aluno: ')
alu5 = input('Nome do 5º aluno: ')
lista = [alu1, alu2, alu3, alu4, alu5]
shuffle(lista)
print(f'''A ordem de apresentação será 
\033[34;1m{lista}\033[m''')
