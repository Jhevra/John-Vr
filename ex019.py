from random import choice
from funções.UtilidadesCev.Dados import cabecalho
turma = list()
cabecalho('Desafio 19', 'ORDERNARRRrr')

for alunos in range(1, 5):
    turma.append(input(f'{alunos}º aluno: '))

print('-'*45)
print(f'O aluno sorteado foi {choice(turma)}')