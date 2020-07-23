from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 34', 'AUMENTORRrr')

salario = float(input('Qual é o salario do funcionario? R$'))

if salario > 1250:
    aumento = (salario*10)/100
else:
    aumento = (salario*15)/100

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento+salario:.2f} agora.')