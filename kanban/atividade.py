#definir aqui a estrutura de uma atividade
#Contem: nome, descrição, data, e uma lista de reponsáveis, e uma coluna

from collections import namedtuple



Atividade = namedtuple("Atividade", "Nome Descricao Data Responsavel Coluna")

def criarAtividade(nome, descricao, data, responsavel, coluna):
    atividade = Atividade(nome, descricao, data, responsavel, coluna)
    return atividade