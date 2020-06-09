print(f'''\033[40;31;1m{"Desafio 40":=^20}\033[m\n\033[33;1m{"Mediador 2.0":^20}\033[m''')
nota1 = float(input('Digite a nota antiga do aluno: '))
nota2 = float(input('Digite a nota mais recente do aluno: '))
media = (nota1 + nota2)/2
if media > 7:
    print(f'O aluno foi aprovado com uma média de {media}')
elif 5 < media < 6.9:
    print(f'O aluno ficou em recuperação com uma média de {media}')
else:
    print(f'O aluno foi reprovado com uma média de {media}')
