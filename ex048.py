from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 48', 'CONTARRrr E SOMARRrr')
s = 0

for c in range(1, 501, 2):
    print(c)
    if c % 3 == 0:
        s += c
print(f'A soma de todos os multiplos de 3, foi de {s}')