from typing import List
import datetime
from atividade import *
from atividade import Atividade
from responsavel import *
from responsavel import Responsavel
from coluna import *
from coluna import Coluna


def menu():
    print('\n1.Cadastrar uma atividade'
          '\n2.Listar todas as atividades'
          '\n3.Cadastrar um responsável'
          '\n4.Listar responsáveis'
          '\n5.Listar atividades de um responsável'
          '\n6.Cadastrar coluna'
          '\n7.Listar atividades de uma coluna'
          '\n8.Sair'
          '\n')

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
            try:
                data = datetime.datetime.strptime(input("Data:"),"%d/%m/%Y")
            except ValueError:
                print("Valor inválido, informe a data no padrão (DD/MM/AAAA)...")
                data = datetime.datetime.strptime(input("Data:"),"%d/%m/%Y")
            nome_responsavel = input ("Responsável:")
            nome_coluna = input("Coluna:")

            for responsavel in lista_de_responsaveis:
                if responsavel.Nome == nome_responsavel:
                    usuario_responsavel = responsavel
                break
            else:
                usuario_responsavel = None
            for coluna in lista_de_colunas:
                if coluna.Nome == nome_coluna:
                    coluna_atividade = coluna
                    coluna.Lista_de_atividades.append(criarAtividade(nome, descricao, data, usuario_responsavel, coluna_atividade))
                break
            else:
                coluna_atividade = None

            lista_de_atividades.append(criarAtividade(nome, descricao, data, usuario_responsavel, coluna_atividade))
            print("\n"+str(len(lista_de_atividades))+"ª atividade criada com sucesso! Pressione enter para continuar...")
            input("")

        elif opcao == "2":
            for atividade in lista_de_atividades:
                print("\n------------------------------------")
                print("Nome:",atividade.Nome)
                print("Descrição:",atividade.Descricao)
                print("Data:", atividade.Data.strftime("%d/%m/%Y"))
                if atividade.Responsavel != None:
                    print("Responsável:", atividade.Responsavel.Nome, atividade.Responsavel.Sobrenome)
                if atividade.Coluna != None:
                    print("Coluna:", atividade.Coluna.Nome)
            print("\nPressione enter para continuar...")
            input("")

        elif opcao == "3":
            print("\n Cadastrando um responsável...")
            nome = input("Nome:")
            sobrenome = input("Sobrenome:")
            funcao = input("Funcao:")
            lista_de_responsaveis.append(criarResponsavel(nome, sobrenome, funcao))
            print("\n"+str(len(lista_de_responsaveis))+"ª responsável cadastrado com sucesso! Pressione enter para continuar...")
            input("")

        elif opcao == "4":
            print("\n Listando responsáveis...")
            for responsavel in lista_de_responsaveis:
                print("\n------------------------------------\n")
                print("Nome:",responsavel.Nome)
                print("Sobrenome:",responsavel.Sobrenome)
                print("Função:", responsavel.Funcao)
            print("\nPressione enter para continuar...")
            input("")

        elif opcao == "5":
            print("\n Listando atividades de um determinado responsável...")
            nome_responsavel = input ("Responsável:")
            for atividade in lista_de_atividades:
                if atividade.Responsavel.Nome == nome_responsavel:
                    print("\n------------------------------------\n")
                    print("Nome:",atividade.Nome)
                    print("Descrição:",atividade.Descricao)
                    print("Data:", atividade.Data)
                    print("Responsável:", atividade.Responsavel.Nome, atividade.Responsavel.Sobrenome)
                    print("Coluna:", atividade.Coluna)
            else:
                print("\n Responsável não encontrado!")
            print("\nPressione enter para continuar...")
            input("")

        elif opcao == "6":
            print("\n Cadastrando uma coluna...")
            nome = input("Nome:")
            lista_de_atividades = []
            lista_de_colunas.append(criarColuna(nome, lista_de_atividades))
            print("\n"+str(len(lista_de_colunas))+"ª coluna cadastrada com sucesso!")

        elif opcao == "7":
            print("\n Listando atividades de uma determinada coluna...")
            nome_coluna = input ("Coluna:")
            for coluna in lista_de_colunas:
                if coluna.Nome == nome_coluna:
                    for atividade in coluna.Lista_de_atividades:
                        print("\n------------------------------------")
                        print("Nome:",atividade.Nome)
                        print("Descrição:",atividade.Descricao)
                        print("Data:", atividade.Data)
                        print("Responsável:", atividade.Responsavel.Nome, atividade.Responsavel.Sobrenome)
                        print("Coluna:", atividade.Coluna.Nome)
                break
            else:
                print("\n Coluna não encontrada!")
            print("\nPressione enter para continuar...")
            input("")

        elif opcao == "8":
            print("\n Até mais!")
            opcao = False

        elif opcao != "":
            print("\n Selecione uma opção válida (1...7)")