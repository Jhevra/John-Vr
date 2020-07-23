def cabecalho(aula, nomedoex):
    """
    -> Faz o cabeçalho no console
    :param aula: Nome, marcador da aula
    :param nomedoex: Nome do exercicio
    :return: None
    """
    print(f'\033[40;33;1m{aula:=^100}\033[m\n\033[40;31;1m{nomedoex:^100}\033[m')


def questinonardor(resposta):
    while True:
        while resposta[0] != 'N' and resposta[0] != 'S':
            resposta = input('\033[31;1mERRO!\033[m Quer continuar? [S/N]: ').strip().upper()
        if resposta[0] == 'N':
            break


def metade(num, formatar):
    """
    -> Divide por 2
    :param formatar: Resposta do usuario, se quer formatado ou não
    :param num: Número a ser dividido
    :return: Retorna a metade do número
    """
    if formatar:
        valor = num / 2
        valor = f'R${valor:.0f},00'
        return valor
    else:
        valor = num / 2
        return valor


def dobro(num, formatar):
    """
    -> Faz o número ser dobrado
    :param formatar: Resposta do usuario, se quer formatado ou não
    :param num: Número proposto a ser multiplicado
    :return: Retorna o dobro dp número
    """
    if formatar:
        valor = num * 2
        valor = f'R${valor:.0f},00'
        return valor
    else:
        valor = num * 2
        return valor


def aumentar(num, porcen, formatar):
    """
    -> Faz a soma de uma porcentagem solicitada
    :param formatar: Resposta do usuario, se quer formatado ou não
    :param num: Número a ser somando com porcentagem
    :param porcen: Porcentagem solicitada
    :return: Retorna a soma do número com o acrescimo da porcentagem
    """
    if formatar:
        valor = num + (num * porcen / 100)
        valor = f'R${num:.0f},00'
        res = valor
        return res
    else:
        valor = num + (num * porcen / 100)
        res = valor
        return res


def diminuir(num, porcen, formatar):
    """
    -> Diminui tantos porcento de um número
    :param formatar: Resposta do usuario, se quer formatado ou não
    :param num: Número a ser diminuido
    :param porcen: Porcentagem solicitada
    :return: Retorna o número reduzido pela porcentagem
    """
    if formatar:
        valor = num - (num * porcen / 100)
        valor = f'R${num:.0f},00'
        res = valor
        return res
    else:
        valor = num - (num * porcen / 100)
        res = valor
        return res


def resumo(preco, aumentado, reduzido):
    trintaporcen = reduzido * preco
    trintaporcen = trintaporcen / 100
    result = preco - trintaporcen
    result = f'R${result:.2f}'

    oitetaporcen = aumentado * preco
    oitetaporcen = oitetaporcen / 100
    resultado = oitetaporcen + preco
    resultado = f'R${resultado:.2f}'

    metader = preco / 2
    metader = f'R${metader:.2f}'

    duplicate = preco * 2
    duplicate = f'R${duplicate:.2f}'

    preco = f'R${preco:.2f}'

    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<16}', end='')
    print(f'{preco:>13}')
    print(f'{"Dobro do preço:":<16}', end='')
    print(f'{duplicate:>13}')
    print(f'{"Metade do preço:":<16}', end='')
    print(f'{metader:>13}')
    print(f'{"80% de aumento:":<10}', end='')
    print(f'{resultado:>14}')
    print(f'{"35% de redução:":<10}', end='')
    print(f'{result:>14}')
    print('-' * 30)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
