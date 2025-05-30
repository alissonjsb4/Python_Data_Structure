# Classe que representa um item do marketplace
class Item:
    def __init__(self, nome, preco):
        self.nome = nome             # Nome do item
        self.preco = preco           # Preço do item
        self.proximo = None          # Ponteiro para o próximo item
        self.anterior = None         # Ponteiro para o item anterior

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"  # Como o item será exibido

# Classe que representa a lista duplamente encadeada do marketplace
class Marketplace:
    def __init__(self):
        self.head = None  # Primeiro item da lista
        self.tail = None  # Último item da lista

    # Inicializar o marketplace com dados fixos
    def inicializar(self):
        # Lista de itens iniciais (nome, preco)
        itens_iniciais = [
            ("Banana", 3.5),
            ("Maçã", 4.0),
            ("Uva", 6.0),
            ("Laranja", 2.5),
            ("Melão", 7.0)
        ]
        for nome, preco in itens_iniciais:
            self.inserir_fim(nome, preco)  # Insere cada item no final da lista
        print("Marketplace inicializado com itens padrão.")

    # Inserir item no início da lista
    def inserir_inicio(self, nome, preco):
        novo = Item(nome, preco)      # Cria novo item
        if not self.head:             # Se a lista estiver vazia
            self.head = self.tail = novo
        else:
            novo.proximo = self.head     # O novo aponta para o antigo head
            self.head.anterior = novo    # O antigo head aponta de volta para o novo
            self.head = novo             # Atualiza o head

    # Inserir item no final da lista
    def inserir_fim(self, nome, preco):
        novo = Item(nome, preco)
        if not self.tail:                 # Lista vazia
            self.head = self.tail = novo
        else:
            self.tail.proximo = novo     # O antigo tail aponta para o novo
            novo.anterior = self.tail    # O novo aponta para o antigo tail
            self.tail = novo             # Atualiza o tail

    # Remover item pelo nome
    def remover_por_nome(self, nome):
        atual = self.head
        while atual and atual.nome != nome:  # Procura o item pelo nome
            atual = atual.proximo
        if not atual:
            print("Item não encontrado.")
            return
        if atual.anterior:                   # Liga o anterior ao próximo
            atual.anterior.proximo = atual.proximo
        else:
            self.head = atual.proximo       # Se for o head, move o head
        if atual.proximo:                   # Liga o próximo ao anterior
            atual.proximo.anterior = atual.anterior
        else:
            self.tail = atual.anterior      # Se for o tail, move o tail
        print(f"Item '{nome}' removido.")

    # Verificar se um item existe
    def verificar_disponibilidade(self, nome):
        atual = self.head
        while atual:
            if atual.nome == nome:
                print(f"Item '{nome}' está disponível.")
                return True
            atual = atual.proximo
        print(f"Item '{nome}' não está disponível.")
        return False

    # Contar o número de itens
    def contar_itens(self):
        atual = self.head
        cont = 0
        while atual:
            cont += 1
            atual = atual.proximo
        print(f"Total de itens: {cont}")
        return cont

    # Inverter a lista
    def inverter(self):
        atual = self.head
        while atual:
            atual.proximo, atual.anterior = atual.anterior, atual.proximo
            atual = atual.anterior  # Avança pelo antigo próximo (agora anterior)
        self.head, self.tail = self.tail, self.head  # Troca head e tail
        print("Marketplace invertido.")

    # Inserir item em ordem crescente de preço
    def inserir_ordenado_por_preco(self, nome, preco):
        novo = Item(nome, preco)
        if not self.head or preco < self.head.preco:
            self.inserir_inicio(nome, preco)  # Insere no início se for menor
            return
        atual = self.head
        while atual.proximo and atual.proximo.preco < preco:
            atual = atual.proximo
        novo.proximo = atual.proximo
        novo.anterior = atual
        if atual.proximo:
            atual.proximo.anterior = novo
        else:
            self.tail = novo
        atual.proximo = novo

    # Exibir todos os itens da lista
    def exibir(self):
        atual = self.head
        if not atual:
            print("Marketplace vazio.")
            return
        while atual:
            print(atual)
            atual = atual.proximo

# Função principal interativa
def main():
    mp = Marketplace()  # Cria uma nova lista vazia

    while True:
        print("\n===== MENU DO MARKETPLACE =====")
        print("0. Inicializar com dados padrão")
        print("1. Inserir item no início")
        print("2. Inserir item no final")
        print("3. Remover item por nome")
        print("4. Verificar disponibilidade")
        print("5. Contar número de itens")
        print("6. Inverter lista")
        print("7. Inserir ordenado por preço")
        print("8. Exibir marketplace")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            mp.inicializar()

        elif opcao == "1":
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_inicio(nome, preco)

        elif opcao == "2":
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_fim(nome, preco)

        elif opcao == "3":
            nome = input("Nome do item a remover: ")
            mp.remover_por_nome(nome)

        elif opcao == "4":
            nome = input("Nome do item a verificar: ")
            mp.verificar_disponibilidade(nome)

        elif opcao == "5":
            mp.contar_itens()

        elif opcao == "6":
            mp.inverter()

        elif opcao == "7":
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_ordenado_por_preco(nome, preco)

        elif opcao == "8":
            mp.exibir()

        elif opcao == "9":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Inicia a aplicação
if __name__ == "__main__":
    main()# Classe que representa um item no marketplace
class Item:
    def __init__(self, nome, preco):
        self.nome = nome           # Nome do item
        self.preco = preco         # Preço do item
        self.proximo = None        # Referência para o próximo item da lista

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"  # Exibição do item

# Classe que representa o marketplace como uma lista encadeada simples
class Marketplace:
    def __init__(self):
        self.head = None  # Início da lista (cabeça)

    # Inserir um item no início da lista
    def inserir_inicio(self, nome, preco):
        novo = Item(nome, preco)   # Cria um novo item
        novo.proximo = self.head   # O próximo item será o antigo head
        self.head = novo           # Atualiza o head para o novo item

    # Inserir um item no final da lista
    def inserir_fim(self, nome, preco):
        novo = Item(nome, preco)   # Cria o novo item
        if not self.head:          # Se a lista estiver vazia
            self.head = novo       # O novo item vira o head
        else:
            atual = self.head      # Começa do início da lista
            while atual.proximo:   # Percorre até o final
                atual = atual.proximo
            atual.proximo = novo   # Adiciona o novo item ao final

    # Remover item pelo nome
    def remover_por_nome(self, nome):
        atual = self.head
        anterior = None
        while atual and atual.nome != nome:  # Busca pelo nome
            anterior = atual
            atual = atual.proximo
        if not atual:
            print("Item não encontrado.")
            return
        if not anterior:
            self.head = atual.proximo       # Removendo o primeiro item
        else:
            anterior.proximo = atual.proximo  # Pulando o item removido
        print(f"Item '{nome}' removido.")

    # Verificar se item existe
    def verificar_disponibilidade(self, nome):
        atual = self.head
        while atual:
            if atual.nome == nome:
                print(f"Item '{nome}' está disponível.")
                return True
            atual = atual.proximo
        print(f"Item '{nome}' não está disponível.")
        return False

    # Contar quantos itens há na lista
    def contar_itens(self):
        contador = 0
        atual = self.head
        while atual:
            contador += 1
            atual = atual.proximo
        print(f"Total de itens: {contador}")
        return contador

    # Inverter a lista
    def inverter(self):
        anterior = None
        atual = self.head
        while atual:
            proximo = atual.proximo      # Guarda o próximo item
            atual.proximo = anterior     # Inverte o ponteiro
            anterior = atual             # Move o anterior para o atual
            atual = proximo              # Move para o próximo da antiga ordem
        self.head = anterior             # Atualiza o head

    # Inserir item mantendo ordem crescente de preço
    def inserir_ordenado_por_preco(self, nome, preco):
        novo = Item(nome, preco)
        if not self.head or preco < self.head.preco:
            # Insere no início se a lista estiver vazia ou for menor que o head
            novo.proximo = self.head
            self.head = novo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.preco < preco:
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo

    # Exibir todos os itens
    def exibir(self):
        atual = self.head
        if not atual:
            print("Marketplace está vazio.")
        while atual:
            print(atual)
            atual = atual.proximo

# Função principal interativa
def main():
    mp = Marketplace()  # Cria uma instância da lista encadeada

    while True:
        # Exibe o menu de opções
        print("\nMenu do Marketplace")
        print("1. Inserir item no início")
        print("2. Inserir item no fim")
        print("3. Remover item pelo nome")
        print("4. Verificar disponibilidade")
        print("5. Contar itens")
        print("6. Inverter ordem")
        print("7. Inserir ordenado por preço")
        print("8. Exibir marketplace")
        print("9. Sair")

        # Lê a escolha do usuário
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_inicio(nome, preco)

        elif escolha == "2":
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_fim(nome, preco)

        elif escolha == "3":
            nome = input("Nome do item a remover: ")
            mp.remover_por_nome(nome)

        elif escolha == "4":
            nome = input("Nome do item a verificar: ")
            mp.verificar_disponibilidade(nome)

        elif escolha == "5":
            mp.contar_itens()

        elif escolha == "6":
            mp.inverter()
            print("Marketplace invertido com sucesso.")

        elif escolha == "7":
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_ordenado_por_preco(nome, preco)

        elif escolha == "8":
            print("Itens no marketplace:")
            mp.exibir()

        elif escolha == "9":
            print("Encerrando...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    main()
