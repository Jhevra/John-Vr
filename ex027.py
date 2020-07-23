from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 27', 'NOMERRRrr')

nomec = str(input('Digite seu nome: ')).strip().split()

print(f'''Seu primeiro nome é {nomec[0]}
Seu ultimo nome é {nomec[len(nomec)-1]}''')
