class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap mínimo"""
        menor = indice
        esq = 2 * indice + 1  # Filho esquerdo
        dir = 2 * indice + 2  # Filho direito

        if esq < tamanho and self.heap[esq][1] < self.heap[menor][1]:
            menor = esq
        if dir < tamanho and self.heap[dir][1] < self.heap[menor][1]:
            menor = dir

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify(menor, tamanho)

    def inserir(self, identificador, prioridade, tempo_estimado):
        """Insere um novo elemento na fila de tarefa"""
        self.heap.append([identificador, prioridade, tempo_estimado])
        indice = len(self.heap) - 1

        # Ajusta o heap para manter a propriedade do heap mínimo
        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice][1] < self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break
    
    def alterar_prioridade(self, nome, prioridade):
        for item in self.heap:
            if item[0]==nome:
                item[1]=prioridade
        self._heapify(0, len(self.heap))
        

    def remover(self):
        """Remove o item de menor prioridade da fila"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # O item de menor prioridade está na raiz (índice 0)
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Reajusta o heap após remover o item
        self._heapify(0, len(self.heap))

        return raiz

    def esta_vazia(self):
        """Verifica se a fila de prioridade está vazia"""
        return len(self.heap) == 0

    def ordenado(self):
        """Ordena todos os elementos da fila de prioridade"""
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())
        return resultado


fila = MinHeap()
fila.inserir('192.168.0.2', 2, 0.200)
fila.inserir('192.168.0.3', 3, 0.200)
fila.inserir('192.168.0.5', 5, 0.200)
fila.inserir('192.168.0.4', 4, 0.200)
fila.inserir('192.168.0.1', 1, 0.200)
fila.alterar_prioridade('192.168.0.4',6)
print('Item ', fila.remover()[0], ' removido') # remove o 1o item = 192.168.0.1

ordenados = fila.ordenado()
# Exibindo a fila de prioridade ordenada
print("\nFila de Prioridade Ordenada (do menor para o maior):")
for item in ordenados:
    print(f"Pacote: {item[0]}, Prioridade: {item[1]}")
