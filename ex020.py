from random import shuffle
from funções.UtilidadesCev.Dados import cabecalho

cabecalho('Desafio 20', 'SORTEARrrr')

turma = []

for aluno in range(1, 5):
    turma.append(input(f'{aluno}º aluno: '))
print('-'*45)
shuffle(turma)

for gente in turma:
    print(gente, end=' ')
    print()
