from typing import List

from atividade import *
from atividade import Atividade
from responsavel import *
from responsavel import Responsavel
from coluna import *
from coluna import Coluna

def menu():
    print('\n1.Cadastrar uma atividade\n2.Listar todas as atividades\n3.Cadastrar um responsável\n4.Listar responsáveis'
        '\n5.Listar atividades de um responsável\n6.Cadastrar coluna\n7.Atribuir atividade a uma coluna\n8.Sair\n')

if __name__ == '__main__':
    print('Bem vindo ao Kanban!')

    lista_de_atividades: List[Atividade] = []
    lista_de_responsaveis: List[Responsavel] = []
    lista_de_colunas: List[Coluna] = []

    opcao = True
    while opcao:
        menu()
        opcao = input("Selecione uma opção:")
        if opcao == "1":
            nome = input("Nome:")
            descricao = input("Descrição:")
            data = input("Data:")
            nome_responsavel = input ("Responsável:")
            for responsavel in lista_de_responsaveis:
                if responsavel.Nome == nome_responsavel:
                    usuario_responsavel = responsavel
                break
            else:
                usuario_responsavel = None
            coluna = False
            lista_de_atividades.append(criarAtividade(nome, descricao, data, usuario_responsavel, coluna))
            print("\n"+str(len(lista_de_atividades))+"ª atividade criada com sucesso!")

        elif opcao == "2":
            for atividade in lista_de_atividades:
                print("\n------------------------------------")
                print("Nome:",atividade.Nome)
                print("Descrição:",atividade.Descricao)
                print("Data:", atividade.Data)
                print("Responsável:", atividade.Responsavel)
                print("Coluna:", atividade.Coluna)

        elif opcao == "3":
            print("\n Cadastrando um responsável...")
            nome = input("Nome:")
            sobrenome = input("Sobrenome:")
            funcao = input("Funcao:")
            lista_de_responsaveis.append(criarResponsavel(nome, sobrenome, funcao))
            print("\n"+str(len(lista_de_responsaveis))+"ª responsável cadastrado com sucesso!")

        elif opcao == "4":
            print("\n Listando responsáveis...")
            for responsavel in lista_de_responsaveis:
                print("\n------------------------------------")
                print("Nome:",responsavel.Nome)
                print("Sobrenome:",responsavel.Sobrenome)
                print("Função:", responsavel.Funcao)

        elif opcao == "5":
            print("\n Listando atividades de um determinado responsável...")


        elif opcao == "6":
            print("\n Cadastrando uma coluna...")
            nome = input("Nome:")
            lista_de_atividades = False
            lista_de_colunas.append(criarColuna(nome, lista_de_atividades))
            print("\n"+str(len(lista_de_colunas))+"ª coluna cadastrada com sucesso!")

        elif opcao == "7":
            print("\n Atribuindo atividade a uma coluna...")

        elif opcao == "8":
            print("\n Até mais!")
            opcao = False

        elif opcao != "":
            print("\n Selecione uma opção válida (1...7)")