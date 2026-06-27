# Agenda de Contato Interativa
agenda = []

def exibir_menu():
    print("\n===== Agenda de Contatos =====")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    print("============================")
    escolha = input("Escolha uma opção: ")
    return escolha
def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contato = {"nome": nome, "telefone": telefone}
    agenda.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
def listar_contatos():
    if not agenda:
        print("Nenhum contato na agenda.")
    else:
        print("\nContatos na Agenda:")
        for idx, contato in enumerate(agenda, start=1):
            print(f"{idx}. Nome: {contato['nome']}, Telefone: {contato['telefone']}")
while True:
    escolha = exibir_menu()
    if escolha == '1':
        adicionar_contato()
    elif escolha == '2':
        listar_contatos()
    elif escolha == '3':
        print("Saindo da agenda. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
        