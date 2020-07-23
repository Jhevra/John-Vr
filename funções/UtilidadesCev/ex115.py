from funções.UtilidadesCev.Functions import leiaint


def linha(tam=41 + 4):
    print('-' * tam)


def menu(msg):
    linha()
    print(msg.center(41))
    linha()


def opcoes(lista):
    menu('MENU PRINCIPAL')
    c = 1
    for cont in lista:
        print(f'\033[33;1m{c}\033[m - \033[36;1m{cont}\033[m')
        c += 1
    linha()
    opc = leiaint('\033[32mSua Opção:\033[m ')
    return opc


def arquivoExist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
        a = open(nome, 'rt')
        for li in a:
            dado = li.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    else:
        menu('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a = open(nome, 'rt')
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}')
        except:
            print('Erro na horar do registro')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
