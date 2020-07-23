from funções.UtilidadesCev.Moeda import cabecalho
from funções.UtilidadesCev.Functions import calculador

cabecalho('Desafio 96', 'CONTROLE DE TERRENOS')

print(f' {"Controle de Terrenos":^55} ')
print('-=' * 30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTE (m): '))
calculador(larg, comp)
