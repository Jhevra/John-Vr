from funções.UtilidadesCev.Dados import cabecalho
import urllib
import urllib.request

cabecalho('Desafio 114', 'Pudim GostosoRrr')

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Erro')
else:
    print('Tudo ok')