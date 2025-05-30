# Sumário das Operações Implementadas:
# Este bloco serve como um guia rápido para as funções disponíveis na classe Marketplace.
# Todas as explicações detalhadas sobre a lógica de cada função estão dentro do código,
# em forma de comentários linha a linha, conforme solicitado.
#
# Operações Simples:
# - Inserir no Início:         Marketplace.insert_at_beginning(name, price)
#   Adiciona um novo item ao início da lista do marketplace.
# - Inserir no Final:          Marketplace.insert_at_end(name, price)
#   Adiciona um novo item ao final da lista do marketplace.
# - Remover por Nome:          Marketplace.remove_by_name(name)
#   Remove a primeira ocorrência de um item com o nome especificado.
# - Verificar Disponibilidade: Marketplace.check_availability(name)
#   Verifica se um item com o nome especificado está presente no marketplace.
#
# Operações Intermediárias:
# - Contar Itens:              Marketplace.count_items()
#   Retorna o número total de itens cadastrados no marketplace.
# - Inverter Ordem:            Marketplace.reverse_order()
#   Inverte a ordem de todos os itens na lista do marketplace.
# - Inserir Ordenado por Preço: Marketplace.insert_sorted_by_price(name, price)
#   Insere um novo item mantendo a lista ordenada em ordem crescente de preço.
#
# Função Auxiliar:
# - Exibir Marketplace:        Marketplace.display_marketplace()
#   Imprime todos os itens atualmente no marketplace.

# Definição da classe Node (Nó)
# Esta classe representa um único item dentro do nosso marketplace.
# Cada nó contém os dados do item (nome e preço) e um ponteiro para o próximo nó na sequência.
class Node:
    # O método __init__ é o construtor da classe Node.
    # Ele é chamado sempre que um novo objeto Node é criado.
    def __init__(self, name, price):
        # self.name armazena o nome do item.
        # É uma string que identifica o item no marketplace.
        self.name = name
        # self.price armazena o preço do item.
        # É um valor numérico (float ou int) usado para ordenação.
        self.price = price
        # self.next_node é o ponteiro para o próximo nó na lista encadeada.
        # Inicialmente, ele é None, indicando que este nó ainda não aponta para nenhum outro.
        self.next_node = None

    # O método __str__ define a representação em string de um objeto Node.
    # É útil para imprimir o nó de forma legível.
    def __str__(self):
        # Retorna uma string formatada com o nome e o preço do item.
        return f"Item: {self.name}, Preço: R${self.price:.2f}"

# Definição da classe Marketplace
# Esta classe gerencia a lista encadeada de itens.
# Ela mantém uma referência ao primeiro nó da lista (head).
class Marketplace:
    # O método __init__ é o construtor da classe Marketplace.
    def __init__(self):
        # self.head é o ponteiro para o primeiro nó da lista.
        # Se a lista estiver vazia, self.head será None.
        self.head = None

    # --- Operações Simples ---

    # 1. Inserir no Início (insert_at_beginning)
    # Adiciona um novo item (Nó) ao início da lista de itens do marketplace.
    # Complexidade de Tempo: O(1) - tempo constante, pois não depende do tamanho da lista.
    def insert_at_beginning(self, name, price):
        # Cria um novo objeto Node com o nome e preço fornecidos.
        new_node = Node(name, price)
        # O ponteiro 'next_node' do novo nó é definido para apontar para o 'head' atual da lista.
        # Isso faz com que o novo nó se torne o primeiro e o antigo 'head' venha depois dele.
        new_node.next_node = self.head
        # O 'head' da lista é atualizado para ser o novo nó.
        # Agora, o novo nó é oficialmente o primeiro elemento da lista.
        self.head = new_node
        # Imprime uma mensagem de confirmação.
        print(f"'{name}' adicionado ao início do marketplace.")

    # 2. Inserir no Final (insert_at_end)
    # Adiciona um novo item (Nó) ao final da lista de itens do marketplace.
    # Complexidade de Tempo: O(N) - tempo linear, pois pode ser necessário percorrer toda a lista.
    def insert_at_end(self, name, price):
        # Cria um novo objeto Node com o nome e preço fornecidos.
        new_node = Node(name, price)
        # Verifica se a lista está vazia (se o head é None).
        if self.head is None:
            # Se a lista estiver vazia, o novo nó se torna o head.
            self.head = new_node
            # Imprime uma mensagem de confirmação.
            print(f"'{name}' adicionado ao final do marketplace (lista estava vazia).")
            # Retorna para encerrar a função.
            return

        # Se a lista não estiver vazia, precisamos encontrar o último nó.
        # 'current' é um ponteiro temporário que começa no head.
        current = self.head
        # Percorre a lista até encontrar o último nó.
        # O último nó é aquele cujo 'next_node' é None.
        while current.next_node:
            # Move 'current' para o próximo nó.
            current = current.next_node
        # Quando o loop termina, 'current' é o último nó da lista.
        # O 'next_node' do último nó é definido para apontar para o novo nó.
        # Isso efetivamente adiciona o novo nó ao final da lista.
        current.next_node = new_node
        # Imprime uma mensagem de confirmação.
        print(f"'{name}' adicionado ao final do marketplace.")

    # 3. Remover por Nome (remove_by_name)
    # Remove a primeira ocorrência de um item com um nome especificado do marketplace.
    # Complexidade de Tempo: O(N) - tempo linear, pois pode ser necessário percorrer toda a lista.
    def remove_by_name(self, name):
        # 'current' é um ponteiro que percorre a lista.
        current = self.head
        # 'previous' é um ponteiro que sempre acompanha 'current', ficando um passo atrás.
        previous = None

        # Percorre a lista enquanto 'current' não for None (não chegou ao final)
        # e o nome do item atual não for o nome que queremos remover.
        while current and current.name!= name:
            # 'previous' avança para a posição de 'current'.
            previous = current
            # 'current' avança para o próximo nó.
            current = current.next_node

        # Após o loop, verifica-se o motivo da saída:
        # Se 'current' é None, significa que o item não foi encontrado na lista.
        if current is None:
            # Imprime uma mensagem informando que o item não foi encontrado.
            print(f"Item '{name}' não encontrado no marketplace.")
            # Retorna para encerrar a função.
            return

        # Se 'previous' é None, significa que o item a ser removido é o 'head' da lista.
        if previous is None:
            # O 'head' da lista é atualizado para ser o próximo nó de 'current'.
            # Isso efetivamente remove o antigo head.
            self.head = current.next_node
        else:
            # Se o item a ser removido não é o head, 'previous' aponta para o nó antes de 'current'.
            # O 'next_node' de 'previous' é atualizado para apontar para o nó depois de 'current'.
            # Isso "pula" o nó 'current', removendo-o da sequência da lista.
            previous.next_node = current.next_node
        # Imprime uma mensagem de confirmação.
        print(f"Item '{name}' removido do marketplace.")

    # 4. Verificar Disponibilidade (check_availability)
    # Verifica se um item com um determinado nome existe no marketplace.
    # Complexidade de Tempo: O(N) - tempo linear, pois pode ser necessário percorrer toda a lista.
    def check_availability(self, name):
        # 'current' é um ponteiro que percorre a lista, começando pelo head.
        current = self.head
        # Percorre a lista enquanto 'current' não for None (não chegou ao final).
        while current:
            # Compara o nome do item atual com o nome que estamos procurando.
            if current.name == name:
                # Se os nomes forem iguais, o item foi encontrado.
                print(f"Item '{name}' está disponível no marketplace.")
                # Retorna True para indicar que o item foi encontrado.
                return True
            # Move 'current' para o próximo nó.
            current = current.next_node
        # Se o loop terminar e o item não foi encontrado, significa que 'current' se tornou None.
        print(f"Item '{name}' NÃO está disponível no marketplace.")
        # Retorna False para indicar que o item não foi encontrado.
        return False

    # --- Operações Intermediárias ---

    # 5. Contar Itens (count_items)
    # Conta o número total de itens atualmente registrados no marketplace.
    # Complexidade de Tempo: O(N) - tempo linear, pois é necessário visitar cada nó.
    def count_items(self):
        # Inicializa um contador de itens.
        count = 0
        # 'current' é um ponteiro que percorre a lista, começando pelo head.
        current = self.head
        # Percorre a lista enquanto 'current' não for None (não chegou ao final).
        while current:
            # Incrementa o contador para cada nó encontrado.
            count += 1
            # Move 'current' para o próximo nó.
            current = current.next_node
        # Imprime o número total de itens.
        print(f"Total de itens cadastrados no marketplace: {count}")
        # Retorna o valor final do contador.
        return count

    # 6. Inverter Ordem (reverse_order)
    # Inverte a ordem de todos os itens no marketplace.
    # O último item se torna o primeiro e vice-versa.
    # Complexidade de Tempo: O(N) - tempo linear, pois cada nó é processado uma vez.
    def reverse_order(self):
        # 'previous' é um ponteiro que aponta para o nó anterior. Começa como None.
        previous = None
        # 'current' é o ponteiro que percorre a lista, começando pelo head.
        current = self.head
        # 'next_temp' é um ponteiro temporário para armazenar o próximo nó antes de mudar o link.

        # Percorre a lista enquanto 'current' não for None.
        while current:
            # Armazena o próximo nó de 'current' em 'next_temp'.
            # Isso é crucial para não perder o restante da lista ao reverter o ponteiro.
            next_temp = current.next_node
            # O ponteiro 'next_node' do 'current' é revertido para apontar para 'previous'.
            # Esta é a etapa central da inversão.
            current.next_node = previous
            # 'previous' avança para a posição de 'current'.
            previous = current
            # 'current' avança para o nó que foi armazenado em 'next_temp'.
            current = next_temp
        # Quando o loop termina, 'current' é None e 'previous' aponta para o que era o último nó.
        # O 'head' da lista é atualizado para ser 'previous', que agora é o novo primeiro nó.
        self.head = previous
        # Imprime uma mensagem de confirmação.
        print("Ordem dos itens no marketplace invertida com sucesso.")

    # 7. Inserir Mantendo Ordem Crescente de Preço (insert_sorted_by_price)
    # Insere um novo item no marketplace, garantindo que toda a lista de itens permaneça
    # ordenada em ordem crescente com base em seus preços.
    # Complexidade de Tempo: O(N) - tempo linear, pois pode ser necessário percorrer a lista para encontrar o ponto de inserção.
    def insert_sorted_by_price(self, name, price):
        # Cria um novo objeto Node com o nome e preço fornecidos.
        new_node = Node(name, price)

        # Caso 1: A lista está vazia ou o novo nó deve ser o novo head (menor preço).
        # Se o head é None (lista vazia) OU o preço do novo nó é menor ou igual ao preço do head atual.
        if self.head is None or new_node.price <= self.head.price:
            # O 'next_node' do novo nó aponta para o head atual.
            new_node.next_node = self.head
            # O novo nó se torna o novo head da lista.
            self.head = new_node
            # Imprime uma mensagem de confirmação.
            print(f"'{name}' (R${price:.2f}) adicionado ao marketplace (início, mantendo ordem).")
            # Retorna para encerrar a função.
            return

        # Caso 2: O novo nó deve ser inserido em algum lugar no meio ou no final da lista.
        # 'current' é um ponteiro que percorre a lista, começando pelo head.
        current = self.head
        # 'previous' é um ponteiro que acompanha 'current', ficando um passo atrás.
        previous = None

        # Percorre a lista enquanto 'current' não for None (não chegou ao final)
        # E o preço do novo nó for MAIOR que o preço do nó 'current'.
        # Isso significa que ainda não encontramos o ponto de inserção.
        while current and new_node.price > current.price:
            # 'previous' avança para a posição de 'current'.
            previous = current
            # 'current' avança para o próximo nó.
            current = current.next_node

        # Após o loop, 'current' é o nó onde o novo nó deve ser inserido ANTES,
        # ou 'current' é None (significa que o novo nó deve ser inserido no final).
        # O 'next_node' do novo nó aponta para 'current'.
        new_node.next_node = current
        # O 'next_node' de 'previous' (o nó antes do ponto de inserção) aponta para o novo nó.
        previous.next_node = new_node
        # Imprime uma mensagem de confirmação.
        print(f"'{name}' (R${price:.2f}) adicionado ao marketplace (meio/final, mantendo ordem).")

    # --- Função Auxiliar ---

    # Exibir Marketplace (display_marketplace)
    # Imprime todos os itens atualmente no marketplace, do início ao fim.
    # Complexidade de Tempo: O(N) - tempo linear, pois é necessário visitar cada nó.
    def display_marketplace(self):
        # 'current' é um ponteiro que percorre a lista, começando pelo head.
        current = self.head
        # Verifica se a lista está vazia.
        if current is None:
            # Imprime uma mensagem se o marketplace estiver vazio.
            print("O marketplace está vazio.")
            # Retorna para encerrar a função.
            return

        # Imprime um cabeçalho para a lista de itens.
        print("\n--- Itens no Marketplace ---")
        # Percorre a lista enquanto 'current' não for None.
        while current:
            # Imprime a representação em string do nó atual (definida em Node.__str__).
            print(current)
            # Move 'current' para o próximo nó.
            current = current.next_node
        # Imprime um rodapé para a lista de itens.
        print("----------------------------")

# --- Função Principal para Demonstração (main) ---
# Esta função demonstra o uso de todas as operações implementadas na classe Marketplace.
def main():
    # Cria uma instância da classe Marketplace.
    marketplace = Marketplace()

    # Demonstração das Operações Simples:

    print("\n--- Demonstração de Operações Simples ---")

    # 1. Inserir no Início
    marketplace.insert_at_beginning("Teclado Mecânico", 350.00)
    marketplace.insert_at_beginning("Mouse Gamer", 120.00)
    marketplace.display_marketplace() # Exibe: Mouse Gamer, Teclado Mecânico

    # 2. Inserir no Final
    marketplace.insert_at_end("Monitor Ultrawide", 1500.00)
    marketplace.insert_at_end("Webcam HD", 200.00)
    marketplace.display_marketplace() # Exibe: Mouse Gamer, Teclado Mecânico, Monitor Ultrawide, Webcam HD

    # 4. Verificar Disponibilidade
    marketplace.check_availability("Teclado Mecânico") # Deve encontrar
    marketplace.check_availability("Fone de Ouvido")   # Não deve encontrar

    # 3. Remover por Nome
    marketplace.remove_by_name("Mouse Gamer") # Remove o head
    marketplace.display_marketplace() # Exibe: Teclado Mecânico, Monitor Ultrawide, Webcam HD

    marketplace.remove_by_name("Webcam HD") # Remove o último
    marketplace.display_marketplace() # Exibe: Teclado Mecânico, Monitor Ultrawide

    marketplace.remove_by_name("Monitor Ultrawide") # Remove o do meio (agora o último)
    marketplace.display_marketplace() # Exibe: Teclado Mecânico

    marketplace.remove_by_name("Item Inexistente") # Tenta remover item que não existe
    marketplace.display_marketplace() # Exibe: Teclado Mecânico

    marketplace.remove_by_name("Teclado Mecânico") # Remove o último item, deixando a lista vazia
    marketplace.display_marketplace() # Exibe: O marketplace está vazio.

    # Demonstração das Operações Intermediárias:

    print("\n--- Demonstração de Operações Intermediárias ---")

    # Adiciona alguns itens para as demonstrações intermediárias
    marketplace.insert_at_end("Cadeira Gamer", 800.00)
    marketplace.insert_at_end("Microfone USB", 250.00)
    marketplace.insert_at_end("Placa de Vídeo", 2500.00)
    marketplace.insert_at_end("SSD 1TB", 400.00)
    marketplace.display_marketplace()

    # 5. Contar Itens
    marketplace.count_items() # Deve contar 4 itens

    # 6. Inverter Ordem
    print("\nMarketplace antes da inversão:")
    marketplace.display_marketplace()
    marketplace.reverse_order()
    print("Marketplace depois da inversão:")
    marketplace.display_marketplace() # Ordem invertida

    # 7. Inserir Mantendo Ordem Crescente de Preço
    print("\nInserindo itens mantendo a ordem crescente de preço:")
    # Primeiro, esvazia o marketplace para uma demonstração limpa de inserção ordenada
    marketplace = Marketplace() # Reinicia o marketplace
    marketplace.insert_sorted_by_price("Fone de Ouvido", 180.00) # Insere no início (lista vazia)
    marketplace.insert_sorted_by_price("Webcam Full HD", 220.00) # Insere depois do fone
    marketplace.insert_sorted_by_price("Mouse Pad Grande", 50.00) # Insere antes do fone (novo head)
    marketplace.insert_sorted_by_price("Monitor 4K", 2000.00) # Insere no final
    marketplace.insert_sorted_by_price("Teclado Compacto", 300.00) # Insere no meio
    marketplace.display_marketplace() # Deve estar ordenado por preço: Mouse Pad, Fone, Webcam, Teclado, Monitor

    # 5. Contar Itens novamente
    marketplace.count_items() # Deve contar 5 itens

    print("\nDemonstrações concluídas!")

# Garante que a função main() seja chamada apenas quando o script é executado diretamente.
if __name__ == "__main__":
    main()
