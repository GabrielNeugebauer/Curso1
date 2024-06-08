import os

restaurantes=[]

def voltar_ao_menu_principal():
    input("\nPressione qualquer tecla para continuar... ")
    main()
def exibir_subtitulo(subtitulo):
    os.system('cls')
    print(subtitulo)
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')
def finalizar_app():
    exibir_subtitulo("Finalizando o app")
def opcao_invalida():
    input('Opção inválida escolhida, pressione qualquer tecla para voltar')
    main()
def cadastrar_restaurante():
    exibir_subtitulo("CADASTRO DE RESTAURANTES\n")
    restaurantes.append(input("Digite o nome do restaurante: ").title())
    if (restaurantes[:-1]).__contains__(restaurantes[-1]): 
        print(f"O restaurante {restaurantes[-1]} já foi cadastrado anteriormente\n") 
        restaurantes.pop()
    else:
        print(f"Restaurante {restaurantes[-1]} cadastrado.")
    voltar_ao_menu_principal()
def listar_restaurantes():
    os.system("cls")
    print('Lista de restaurantes:\n\n',*restaurantes, sep="\n")
    voltar_ao_menu_principal()
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    exibir_subtitulo("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()
