from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 24', 'SANTORRrr')

cidade = input('Cidade: ').upper().split()
if 'SANTO' and 'SÃO' in cidade[0]:
    res = 'Tem SANTO no nome da cidade'
else:
    res = 'Não tem SANTO no nome da cidade'
print(f'A cidade começa com SANTO? {res}')