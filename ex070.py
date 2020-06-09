print(f'\033[40;33;1m{"Desafio 68":=^20}\033[m\n\033[40;31;1m{"ANALISADORRRRRRR":^20}\033[m')
cont = 1
cmais = barato = tot = 0
menor = ""
while True:
    print('-='*20)
    nome = input(f'Nome do {cont}º produto: ').upper().strip()
    valor = float(input(f'Valor do {cont}º produto: R$'))
    res = input('Quer continuar [S/N]? ').upper().strip()
    if cont == 1 or valor < barato:
        barato = valor
        menor = nome
    while res != 'S' and res != 'N':
        res = input('ERRO! Quer continuar [S/N]? ').upper().strip()
    cont += 1
    tot += valor
    if res == 'N':
        break
    if valor >= 1000:
        cmais += 1
print(f'''O total gasto foi de R${tot:.2f}
O total de produtos acima de R$1000,00 foi de {cmais} produtos
O produto mais barato é {menor} que custa R${barato}''')