from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 7', 'Uno com escada em cima')

aluno = input('Dígite o nome do aluno: ')
nota1 = float(input('Dígite a 1º nota: '))
nota2 = float(input('Dígite a 2º nota: '))

print(f'O aluno {aluno} teve a media {(nota2 + nota1)/2}')