def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sair")

def listar(lista):
    if not lista:
        print("A lista está vazia.")
    else:
        for i, item in enumerate(lista):
            print(f"{i}: {item}")

def main():
    lista_compras = []
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            item = input("Digite o item para adicionar: ")
            lista_compras.append(item)
            print(f'"{item}" adicionado à lista.')
        elif escolha == "2":
            listar(lista_compras)
            try:
                indice = int(input("Digite o índice do item para remover: "))
                if 0 <= indice < len(lista_compras):
                    removido = lista_compras.pop(indice)
                    print(f'"{removido}" removido da lista.')
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
        elif escolha == "3":
            listar(lista_compras)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()