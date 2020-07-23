from funções.UtilidadesCev.Dados import cabecalho
cabecalho('Desafio 8', 'ESSE FAZ CRECK')
metros = float(input('Uma distância em metros: '))

print('-'*45)
print(f'''A medida de {metros} corresponde a
{metros/1000}Km
{metros/100}Hm
{metros/10}Dam
{metros*10}Dm
{metros*100}Cm
{metros*100}Mm''')
