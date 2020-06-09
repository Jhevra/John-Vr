print(f'\033[40;33;1m{"Desafio 97":=^100}\033[m\n\033[40;31;1m{"ESCREVARRr":^100}\033[m')


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('\033[31;1mOlá, Mundo!\033[m')
escreva('\033[32;1mCurso de Python no Youtube\033[m')
escreva('\033[33;1mCeV\033[m')
