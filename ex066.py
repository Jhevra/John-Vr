from funções.UtilidadesCev.Dados import cabecalho

cabecalho('Desafio 66', 'BREKARRrr')

n = s = tot = 0

while True:
    n = int(input('Dígite um valor [999 para sair]: '))
    if n == 999:
        break
    tot += 1
    s += n
print(f'As somas dos {tot} números dígitados, foi de {s}')