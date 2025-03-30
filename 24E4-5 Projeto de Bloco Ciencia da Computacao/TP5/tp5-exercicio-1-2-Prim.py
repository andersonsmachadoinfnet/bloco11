class GrafoAlgoritmoPrim:
    def __init__(self, vertices, bairros):
        self.V = vertices  # Número de vértices
        self.bairros=bairros
        self.grafo = [[0] * vertices for _ in range(vertices)]  # Matriz de adjacência

    def adicionar_aresta(self, u, v, peso):
        # Adiciona uma aresta entre os vértices u e v com um peso.
        self.grafo[self.bairros.index(u)][self.bairros.index(v)] = peso
        self.grafo[self.bairros.index(v)][self.bairros.index(u)] = peso  # Grafo não direcionado

    def prim(self):
        # Executa o algoritmo de Prim para encontrar a Árvore Geradora Mínima.
        infinito = float('inf')
        selecionado = [False] * self.V  # Marcar os vértices incluídos na AGM
        chave = [infinito] * self.V  # Peso mínimo para incluir um vértice
        pai = [-1] * self.V  # Armazena a estrutura da AGM

        # Começamos pelo primeiro vértice
        chave[0] = 0  

        for _ in range(self.V):
            # Escolhe o vértice de menor chave que ainda não foi incluído na AGM
            minimo = infinito
            u = -1
            for v in range(self.V):
                if not selecionado[v] and chave[v] < minimo:
                    minimo = chave[v]
                    u = v

            selecionado[u] = True  # Marca o vértice como incluído na AGM

            # Atualiza os valores das chaves e define os pais dos vértices adjacentes
            for v in range(self.V):
                if 0 < self.grafo[u][v] < chave[v] and not selecionado[v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u

        # Exibindo a Árvore Geradora Mínima
        print("\nArestas da Árvore Geradora Mínima:")
        custo_total = 0
        for i in range(1, self.V):
            print(f"{self.bairros[pai[i]]} - {self.bairros[i]} (Peso: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Peso total da AGM: {custo_total}")

# Criando o grafo com 4 vértices
g = GrafoAlgoritmoPrim(4, ["A","B","C","D"])

# Adicionando as arestas e seus respectivos pesos
arestas = [
    ("A", "B", 2), ("A", "C", 3), 
    ("B", "C", 1), ("B", "D", 4), 
    ("C", "D", 5)
]

for u, v, peso in arestas:
    g.adicionar_aresta(u, v, peso)

# Executando Prim
g.prim()
