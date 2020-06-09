print(f'''\033[40;31;1m{"Desafio 29":=^20}\033[m\n\033[33;1m{"Radar":^20}\033[m
{"Bem Vindo ao Radar":-^30}''')
velocidade = float(input('Digite a velocidade que o carro estava: '))
if velocidade > 80:
    print(f'''Sua multa é de \033[31;1mR${(velocidade-80)*7:.2f}\033[m
Preste mais atenção no transito!''')
else:
    print(f'\033[32;1mVocê não recebeu multa, lembre de sempre usar cinto de segurança!\033[m')
print('\033[33;1mTenha um bom dia!\033[m')