from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 40', 'MEDIARRrr')

nota1 = float(input('1º Nota: '))
nota2 = float(input('2º Nota: '))
media = (nota2 + nota1) / 2

print('-'*45)

if media >= 7:
    print(f'''Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}
\033[32mO aluno está APROVADO!\033[m''')

elif 5 <= media <= 6.9:
    print(f'''Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}
\033[33mO aluno está em RECUPERAÇÃO!\033[m''')

else:
    print(f'''Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}
\033[31mO aluno está REPROVADO!\033[m''')