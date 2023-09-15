# Inicializa uma lista vazia para armanezar novos usuários.
usuarios = []

# Função para adicionar um novo usuário.
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o e-mail do usuário: ")

    usuario = {
        "Nome": nome,
        "Idade": idade,
        "Email": email
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Função para mostrar todos os usuários cadastrados
def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado ainda.")
    else:
        print("Lista de usuários:")
    for i, usuario in enumerate(usuarios, start=1):
            print(f"Usuario {i}:")
            print(f"Nome: {usuario['Nome']}")
            print(f"Idade: {usuario['Idade']}")
            print(f"Email: {usuario['Email']}")
            print()

# Loop principal.
while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários cadastrados")
    print("3 - Sair") 

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        print("Saindo do programa...")  
        break
    else: 
        print("Opção inválida. Por favor, escolha outra opção!") 

