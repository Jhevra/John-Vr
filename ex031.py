from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 31', 'VIAJARRrr')

viajem = float(input('Qual é a distância da sua viagem? '))

if viajem > 200:
    preco = viajem * 0.45
else:
    preco = viajem * 0.50

print(f'''Você está prestes a começar uma viagem de {viajem:.1f}Km.
E o preço da sua passagem será de R${preco:.2f}''')