
# IMPLEMENTAÇÃO COM LISTA DUPLAMENTE ENCADEADA

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

class Marketplace:
    def __init__(self):
        self.head = None
        self.tail = None

    def inicializar(self):
        itens = [("Maçã", 1.50), ("Banana", 0.90), ("Leite", 4.80), ("Pão", 2.30)]
        for nome, preco in itens:
            self.inserir_fim(nome, preco)

    def inserir_inicio(self, nome, preco):
        novo = Item(nome, preco)
        if not self.head:
            self.head = self.tail = novo
        else:
            novo.proximo = self.head
            self.head.anterior = novo
            self.head = novo

    def inserir_fim(self, nome, preco):
        novo = Item(nome, preco)
        if not self.tail:
            self.head = self.tail = novo
        else:
            self.tail.proximo = novo
            novo.anterior = self.tail
            self.tail = novo

    def remover_por_nome(self, nome):
        atual = self.head
        while atual and atual.nome != nome:
            atual = atual.proximo
        if not atual:
            print("Item não encontrado.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.head = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.tail = atual.anterior
        print(f"Item '{nome}' removido.")

    def verificar_disponibilidade(self, nome):
        atual = self.head
        while atual:
            if atual.nome == nome:
                print(f"Item '{nome}' está disponível.")
                return True
            atual = atual.proximo
        print(f"Item '{nome}' não está disponível.")
        return False

    def contar_itens(self):
        atual = self.head
        cont = 0
        while atual:
            cont += 1
            atual = atual.proximo
        print(f"Total de itens: {cont}")
        return cont

    def inverter(self):
        atual = self.head
        while atual:
            atual.proximo, atual.anterior = atual.anterior, atual.proximo
            atual = atual.anterior
        self.head, self.tail = self.tail, self.head

    def inserir_ordenado_por_preco(self, nome, preco):
        novo = Item(nome, preco)
        if not self.head or preco < self.head.preco:
            self.inserir_inicio(nome, preco)
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

    def exibir(self):
        atual = self.head
        if not atual:
            print("Marketplace vazio.")
        while atual:
            print(atual)
            atual = atual.proximo



# Função principal com menu interativo
def main():
    mp = Marketplace()  # Cria uma nova instância do marketplace (lista vazia)

    while True:
        # Menu de opções
        print("\n=== MENU DO MARKETPLACE ===")
        print("0. Inicializar com dados padrão")
        print("1. Inserir item no início")
        print("2. Inserir item no final")
        print("3. Remover item por nome")
        print("4. Verificar disponibilidade")
        print("5. Contar itens")
        print("6. Inverter ordem")
        print("7. Inserir ordenado por preço")
        print("8. Exibir marketplace")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            # Preenche a lista com alguns itens predefinidos
            mp.inicializar()

        elif opcao == "1":
            # Solicita dados ao usuário para inserir item no início
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_inicio(nome, preco)

        elif opcao == "2":
            # Solicita dados para inserir item no final
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_fim(nome, preco)

        elif opcao == "3":
            # Remove item pelo nome fornecido
            nome = input("Nome do item a remover: ")
            mp.remover_por_nome(nome)

        elif opcao == "4":
            # Verifica se o item está presente
            nome = input("Nome do item: ")
            mp.verificar_disponibilidade(nome)

        elif opcao == "5":
            # Conta o número total de itens
            mp.contar_itens()

        elif opcao == "6":
            # Inverte a lista
            mp.inverter()

        elif opcao == "7":
            # Insere o item mantendo a ordem de preço
            nome = input("Nome do item: ")
            preco = float(input("Preço do item: "))
            mp.inserir_ordenado_por_preco(nome, preco)

        elif opcao == "8":
            # Exibe todos os itens
            mp.exibir()

        elif opcao == "9":
            # Sai do programa
            print("Encerrando o programa...")
            break

        else:
            # Opção inválida
            print("Opção inválida. Tente novamente.")

# Garante que a função main seja executada apenas quando o script for chamado diretamente
if __name__ == "__main__":
    main()
