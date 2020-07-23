from funções.UtilidadesCev.Dados import cabecalho
from funções.UtilidadesCev.ex115 import *

cabecalho('Desafio 115', 'CadatraRRrr bunito')

arq = 'CADASTRO.txt'

if not arquivoExist(arq):
    criarArquivo(arq)

while True:
    res = opcoes(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if res == 1:
        lerArquivo(arq)
    elif res == 2:
        menu('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif res == 3:
        menu('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31;1mERRO! Dígite uma opção válida\033[m')
