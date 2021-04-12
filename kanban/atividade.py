#definir aqui a estrutura de uma atividade
#Contem: nome, descrição, data, e uma lista de reponsáveis, e uma coluna

from collections import namedtuple



Atividade = namedtuple("Atividade", "Nome Descricao Data Lista_de_responsaveis Coluna")

def criarAtividade(nome, descricao, data, lista_de_responsaveis, coluna):
    atividade = Atividade(nome, descricao, data, lista_de_responsaveis, coluna)
    return atividade