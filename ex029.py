from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 29', 'MULTARRrr')

velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'''\033[31mMULTADO! Você execeu o limite permitido que é de 80Km/h.
Você deve pagar uma multa de\033[m \033[33mR${multa:.2f}!\033[m''')

else:
    print(f'\033[32mParabéns, você está dentro do limite permitido.\033[m')

print(f'\033[32;1mTenha um bom dia! Dirija com segurança!\033[m')