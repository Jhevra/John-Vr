from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 25', 'SIlvarr?')

nome = input('Nome: ').upper().strip()
if 'SILVA' in nome:
    res = 'Tem SILVA no nome'
else:
    res = 'Não tem SILVA no nome'
print('-'*45)
print(f'No nome {nome}, {res}')