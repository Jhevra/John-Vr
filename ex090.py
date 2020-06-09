print(f'''\033[40;31;1m{"Desafio 90":=^20}\033[m\n\033[33;1m{"MEDIARRR":^20}\033[m''')
ficha = dict()
ficha['Nome'] = input('Nome: ').strip()
ficha['Média'] = float(input('Medía: '))
print('-='*35)

if ficha['Média'] >= 6:
    print(f'''O estado do aluno \033[33;1m{ficha["Nome"]}\033[m é \033[32;1mAPROVADO\033[m
Média = \033[32;1m{ficha["Média"]}\033[m''')

else:
    print(f'''O estado do aluno \033[33;1m{ficha["Média"]}\033[m é \033[31;1mREPROVADO\033[m
Média = \033[31;1m{ficha["Média"]}\033[m''')