from datetime import date
print(f'\033[40;33;1m{"Desafio 54":=^20}\033[m\n\033[40;31;1m{"NASCIMENTOR":^20}\033[m')
maior = menor = 0
for cont in range(1, 8):
    ano = int(input(f'Dígite o ano de nascimento da {cont}º pessoa: '))
    cont += 1
    if date.today().year - ano > 18:
        maior+= 1
    else:
        menor += 1
print(f'''Foi o total de \033[36;1m{maior} pessoas maiores\033[m de idade
E \033[33;1m{menor} menores\033[m de idade''')