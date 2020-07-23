from funções.UtilidadesCev.Dados import  cabecalho
cabecalho('Desafio 60', 'P.A RRrr')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont != 10:
    print(primeiro)
    primeiro += razao
    cont += 1
