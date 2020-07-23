from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 11', 'ParedeRRrr')

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print('-'*45)
print(f'''Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura*altura}m
Para pintar essa parede, você precisará de {(largura*altura)/2}L de tinta''')
