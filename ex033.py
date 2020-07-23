from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 33', 'MAIORRrr e MENORRrr')

menor = maior = 0
for n in range(3):
    valor = int(input(f'{n+1}º valor: '))
    if n == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print(f'O maior número foi {maior}, e o menor foi {menor}')