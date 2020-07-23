from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 36', 'ALUGARRrr')

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Anos de financiamento: '))
parcelas = casa / (anos*12)
sal = (salario*30)/100

if parcelas > sal:
    print(f'''Para pagar uma casa de \033[32mR${casa:.2f}\033[m em {anos} anos a prestação será de \033[32mR${parcelas:.2f}\033[m
\033[31mEmpréstimo NEGADO!\033[m''')

else:
    print(f'''Para pagar uma casa de \033[32mR${casa:.2f}\033[m em {anos} anos a prestação será de \033[32mR${parcelas:.2f}\033[m
\033[32mEmpréstimo APROVADO!\033[m''')
