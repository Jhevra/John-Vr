from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 5', 'Chiqulete com banana')

exemplor = input('Dígite algo: ')

print('-'*45)
print(f'''O tipo primitivo desse valor é \033[33;1m{type(exemplor)}\033[m
Só tem espaços? \033[33;1m{exemplor.isspace()}\033[m
É número? \033[33;1m{exemplor.isnumeric()}\033[m
É alfabético? \033[33;1m{exemplor.isalpha()}\033[m
É alfanumérico \033[33;1m{exemplor.isalnum()}\033[m
Está em maiúsculas? \033[33;1m{exemplor.isupper()}\033[m
Está em minúsculas? \033[33;1m{exemplor.islower()}\033[m
Está capitalizada? \033[33;1m{exemplor.istitle()}\033[m''')
