print('{:=^20}\n'.format('Desafio 13'), 'Calculador de Aumento (%15)')
salario = float(input('Digite seu salario, para que seja acrescentado 15%: R$'))
print('Seu salario atual é de R${:.2f}, com um aumento de 15% fica {:.2f}, ou seja, você ganhou R${:.2f} a mais.'.format(salario, (salario*15)/100+salario, (salario*15)/100))
