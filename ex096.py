print(f'\033[40;33;1m{"Desafio 96":=^20}\033[m\n\033[40;31;1m{"TERRONOR":^20}\033[m')


def area(tam):
    tam = terreno['LARGURA'] * terreno['COMPRIMENTO']
    print('-='*35)
    print(f'A área de um terreno {terreno["LARGURA"]}x{terreno["COMPRIMENTO"]}m² é de {tam:.2f}m²')


print(f'''{"CONTROLE DE TERRENOS":^65}
{"-=" * 35}''')
terreno = dict()
terreno['LARGURA'] = float(input('LARGURA (M): '))
terreno['COMPRIMENTO'] = float(input('COMPRIMENTO (M): '))
area(terreno)
