from time import sleep
print(f'''\033[40;31;1m{"Desafio 57":=^20}\033[m\n\033[33;1m{"SEXOR":^20}\033[m''')
cont = 0
sexo = str(input('Dígite seu sexo [\033[36;1mM\033[m/\033[31;1mF\033[m]: ')).upper().strip()
while sexo[0] != 'M' and sexo[0] != 'F':
    sexo = str(input('\033[31;1mERRO!\033[m Dígite seu sexo novamente [M/F]: ')).strip().upper()
    cont += 1