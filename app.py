import os

print("🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢\n")

print("1. Cadastrar restaurante")
print("2. Listar restaurante")
print("3. Ativar restaurante")
print("4. Sair\n")

opcao_escolhida = int(input("Escolha uma opção: "))

def finalizar_app():
    os.system("cls")
    print("Finalizando o App\n")


if opcao_escolhida == 1:
    print("Cadastrar Restaurante")
elif opcao_escolhida == 2:
    print("Listar Restaurantes")
elif opcao_escolhida == 3:
    print("Ativar Restaurante")
else:
    finalizar_app()
