estoque = []

# Função para adicionar um item ao estoque
def adicionar_item():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    
    produto = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
    estoque.append(produto)
    print(f"{nome} adicionado ao estoque!\n")

# Função para remover um item do estoque
def remover_item():
    nome = input("Nome do produto a ser removido: ")
    for produto in estoque:
        if produto['nome'] == nome:
            estoque.remove(produto)
            print(f"{nome} removido do estoque!\n")
            return
    print(f"Produto {nome} não encontrado no estoque.\n")

# Função para atualizar a quantidade ou preço de um produto
def atualizar_item():
    nome = input("Nome do produto a ser atualizado: ")
    for produto in estoque:
        if produto['nome'] == nome:
            escolha = input("Deseja atualizar a (q)uantidade ou o (p)reço? ").lower()
            if escolha == 'q':
                nova_quantidade = int(input("Nova quantidade: "))
                produto['quantidade'] = nova_quantidade
                print(f"Quantidade de {nome} atualizada para {nova_quantidade}.\n")
            elif escolha == 'p':
                novo_preco = float(input("Novo preço: "))
                produto['preco'] = novo_preco
                print(f"Preço de {nome} atualizado para R${novo_preco:.2f}.\n")
            return
    print(f"Produto {nome} não encontrado no estoque.\n")

# Função para listar todos os produtos no estoque
def listar_estoque():
    if estoque:
        print("Estoque atual:")
        for produto in estoque:
            print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")
        print()
    else:
        print("Estoque vazio.\n")

# Função para buscar um produto pelo nome
def buscar_produto():
    nome = input("Nome do produto a ser buscado: ")
    for produto in estoque:
        if produto['nome'] == nome:
            print(f"Produto encontrado: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}\n")
            return
    print(f"Produto {nome} não encontrado no estoque.\n")

# Função principal que controla o fluxo do programa
def menu():
    while True:
        print("=== Sistema de Gerenciamento de Estoque ===")
        print("1. Adicionar item ao estoque")
        print("2. Remover item do estoque")
        print("3. Atualizar item no estoque")
        print("4. Listar estoque")
        print("5. Buscar produto")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_item()
        elif opcao == '2':
            remover_item()
        elif opcao == '3':
            atualizar_item()
        elif opcao == '4':
            listar_estoque()
        elif opcao == '5':
            buscar_produto()
        elif opcao == '6':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Iniciando o programa
menu()