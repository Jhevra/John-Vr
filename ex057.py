from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 57', 'VALIDARRrr')


sexo = input('Informe seu sexo [M/F]: ').strip().upper()
while sexo[0] != 'M' and sexo[0] != 'F':
    sexo = input('\033[31mDados inválidos.\033[m Por favor, informe seu sexo [M/F]: ').upper().strip()
print(f'\033[33;1mSexo {sexo} registrado com sucesso.\033[m')
