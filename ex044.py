print(f'''\033[40;31;1m{"Desafio 44":=^20}\033[m\n\033[33;1m{"PAGADOR":^20}\033[m''')
normal = float(input('Digite o preço normal: '))
pagamento = input('''Escolha as formas de pagamento 
[1] Dinheiro/Cheque 
[2] Cartão
[3] 2x no cartão
[3] 3x ou mais
... ''').upper().strip()
if pagamento in 'DINHEIRO/CHEQUE':
    print(f'O valor a ser pago com um desconto de 10% será R${normal - (normal*10)/100}')
elif pagamento in 'CARTÃO':
    print(f'O valor a ser pago com um desconto de 5% será R${normal - (normal*9)/100 }')
elif pagamento in '2X NO CARTÃO':
    print(f'O valor a ser pago R${normal}')
elif pagamento in '3X OU MAIS':
    print(f'O valor a ser pago com um desconto de 20% será R${normal - (normal*20)/100 }')
