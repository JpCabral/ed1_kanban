#Definir aqui um responsável
#possui nome e sobrenome

from collections import namedtuple

Responsavel = namedtuple("Responsavel", "Nome Sobrenome Funcao")

def criarResponsavel(nome, sobrenome, funcao):
    responsavel = Responsavel(nome, sobrenome, funcao)
    return responsavel