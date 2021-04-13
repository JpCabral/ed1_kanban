#Definir aqui a estrutura de uma coluna
#colunas contém atividades

from collections import namedtuple

Coluna = namedtuple("Coluna", "Nome Lista_de_atividades")

def criarColuna(nome, lista_de_atividades):
    coluna = Coluna(nome, lista_de_atividades)
    return coluna