from funções.UtilidadesCev.Dados import cabecalho
from time import sleep
cabecalho('Desafio 21', 'ANALISADORRrr')

nome = input('Dígite seu nome: ').strip()
print('Analisando seu nome...')
print('-='*45)
sleep(0.5)

print(f'''Seu nome em maiúsculo é {nome.upper()}
Seu nome em minúsculo é {nome.lower()}
Seu nome ao todo tem {len(nome) - nome.count(' ')}''')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e tem {len(nome[0])}')
