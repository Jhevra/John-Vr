from funções.UtilidadesCev.Dados import cabecalho
from funções.UtilidadesCev.Functions import contagem

cabecalho('Desafio 98', 'Contagem')

contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 35)
print('Agora é sua vez de personalizar a contagem')
comeco = int(input('Inicio: '))
final = int(input('Fim: '))
pula = int(input('Passo: '))
contagem(comeco, final, pula)
print('-=' * 35)
