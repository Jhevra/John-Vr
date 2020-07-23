from funções.UtilidadesCev.Dados import cabecalho
from funções.UtilidadesCev.Functions import leiaint, leiafloat

cabecalho('Desafio 133', 'AprofundaRRrr')


inteiro = leiaint('Dígite um valor \033[33;1mInteiro\033[m: ')
real = leiafloat('Dígite um valor \033[33;1mReal\033[m: '.replace(',', '.'))

print('-'*45)

print(f'''O valor inteiro dígitado foi {inteiro}
E o valor real dígitado foi {real:.2f}''')
