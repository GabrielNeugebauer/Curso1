import os

restaurantes=[]

def voltar_ao_menu_principal():
    input("\nPressione qualquer tecla para continuar... ")
    main()
def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha=("*"*len(subtitulo))
    print (linha)
    print(subtitulo)
    print (linha)
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar situação do restaurante')
    print('4. Sair\n')
def finalizar_app():
    exibir_subtitulo("Finalizando o app")
def opcao_invalida():
    input('Opção inválida escolhida, pressione qualquer tecla para voltar')
    main()
def cadastrar_restaurante():
    exibir_subtitulo("CADASTRO DE RESTAURANTES\n")
    nome_restaurante=input("Digite o nome do restaurante: ").title()
    if (restaurantes).__contains__(nome_restaurante): 
        print(f"O restaurante {nome_restaurante} já foi cadastrado anteriormente\n") 
    else:
        categoria_restaurante=input("Digite a categoria do restaurante: ").title()
        restaurantes.append({'nome':nome_restaurante, "categoria":categoria_restaurante, "ativo":False})
        print(f"Restaurante {nome_restaurante} cadastrado.")
    voltar_ao_menu_principal()
def listar_restaurantes():
    os.system("cls")
    print("Lista de restaurantes:\n\n")
    for restaurante in restaurantes:
        nome_restaurante=restaurante["nome"]
        categoria_restaurante=restaurante["categoria"]
        situacao_restaurante=restaurante["ativo"]
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {"Ativo" if situacao_restaurante == True else "Inativo"}\n')
    voltar_ao_menu_principal()
def alterar_situacao_restaurante():
    exibir_subtitulo("Digite o nome do restaurante\n")
    nome_restaurante=input()
    for i in range(len(restaurantes)):
        if restaurantes[i]["nome"].__contains__(nome_restaurante.title()):
            if restaurantes[i]["ativo"]==False:
                restaurantes[i]["ativo"]=not restaurantes[i]["ativo"]
            restaurante_encontrado=True
            print(f'{restaurantes[i]["nome"]} {"Ativado" if restaurantes[i]["ativo"] == True else "Desativado"}\n')
        break
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado. ")
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alterar_situacao_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as error:
        print (error)
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