import atividade,coluna,responsavel

def menu():
    print('\n1.Adicionar uma atividade\n2.Cadastrar um responsável\n3.Atribuir atividades'
        '\n4.Listar atividades de um responsável\n5.Cadastrar coluna\n6.Atribuir atividade a uma coluna\n7.Sair\n')

if __name__ == '__main__':
    print('Bem vindo ao Kanban"')

    opcao = True
    while opcao:
        menu()
        opcao = input("Selecione uma opção:")
        if opcao == "1":
            print("\n Adicionando uma atividade...")
        elif opcao == "2":
            print("\n Cadastrando um responsável...")
        elif opcao == "3":
            print("\n Atribuindo atividades...")
        elif opcao == "4":
            print("\n Listando atividades de um determinado responsável...")
        elif opcao == "5":
            print("\n Cadastrando uma coluna...")
        elif opcao == "6":
            print("\n Atribuindo atividade a uma coluna...")
        elif opcao == "7":
            print("\n Até mais!")
            opcao = False
        elif opcao != "":
            print("\n Selecione uma opção válida (1...7)")