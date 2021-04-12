from typing import List

from atividade import *
from atividade import Atividade
from responsavel import *
from coluna import *

def menu():
    print('\n1.Cadastrar uma atividade\n2.Listar todas as atividades\n3.Cadastrar um responsável\n4.Atribuir atividades'
        '\n5.Listar atividades de um responsável\n6.Cadastrar coluna\n7.Atribuir atividade a uma coluna\n8.Sair\n')

if __name__ == '__main__':
    print('Bem vindo ao Kanban!')

    lista_de_atividades: List[Atividade] = []

    opcao = True
    while opcao:
        menu()
        opcao = input("Selecione uma opção:")
        if opcao == "1":
            nome = input("Nome:")
            descricao = input("Descrição:")
            data = input("Data:")
            lista_de_responsaveis = False
            coluna = False
            lista_de_atividades.append(criarAtividade(nome, descricao, data, lista_de_responsaveis, coluna))
            print("\n"+str(len(lista_de_atividades))+"ª atividade criada com sucesso!")
        elif opcao == "2":
            for atividade in lista_de_atividades:
                print("\n------------------------------------")
                print("Nome:",atividade.Nome)
                print("Descrição:",atividade.Descricao)
                print("Data:", atividade.Data)
                print("Responsáveis:", atividade.Lista_de_responsaveis)
                print("Coluna:", atividade.Coluna)
        elif opcao == "3":
            print("\n Cadastrando um responsável...")
        elif opcao == "4":
            print("\n Atribuindo atividades...")
        elif opcao == "5":
            print("\n Listando atividades de um determinado responsável...")
        elif opcao == "6":
            print("\n Cadastrando uma coluna...")
        elif opcao == "7":
            print("\n Atribuindo atividade a uma coluna...")
        elif opcao == "8":
            print("\n Até mais!")
            opcao = False
        elif opcao != "":
            print("\n Selecione uma opção válida (1...7)")