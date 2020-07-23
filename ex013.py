from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 13', 'AumentoRRrr')

salario = float(input('Qual é o salário do Funcionário? R$'))
aumento = (salario*15)/100
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${salario+aumento:.2f}')