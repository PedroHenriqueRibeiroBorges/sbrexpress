import os

restaurantes = [{"nome" : "Praça", "categoria" : "Japonesa", "ativo" :False}, 
                {"nome" : "Pizzaria", "categoria" : "italiana", "ativo" :True},
                {"nome" : "Cantina", "categoria" : "lanches", "ativo" :False}
                ]

def exibir_nome_do_programa():
    print("🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢\n")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo("Finalizando o app")

def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu principal.")
    main()

def opcao_invalida():
    print("Opção inválida\n")
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    exibir_subtitulo("Cadastro de restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite o nome da categoria do restaurante{nome_do_restaurante}: ")
    dados_do_restaurante = {"nome" :nome_do_restaurante, "categoria" :categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado.")
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo("lista de restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo ="Ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu()

def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restaurante.")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso." if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    
    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
