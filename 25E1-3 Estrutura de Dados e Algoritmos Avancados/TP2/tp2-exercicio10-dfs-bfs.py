class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def bfs(self, inicio):
        visitados = set()  
        fila = [inicio]  
        
        while fila:
            vertice = fila.pop(0)  
            if vertice not in visitados:
                print(vertice, end=" ")  
                visitados.add(vertice)  
                fila.extend(self.lista_adjacencia[vertice])  

    def dfs_recursivo(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()

        print(vertice, end=" ")  
        visitados.add(vertice)  

        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

# Criando o grafo
grafo = Grafo()
vertices = ["1", "2", "3", "4", "5", "6"]
for v in vertices:
    grafo.adicionar_vertice(v)

# Adicionando arestas
arestas = [("1", "2"), ("1", "3"), ("2", "4"), ("3", "5"), ("4", "6"), ("5", "6")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

# Executando BFS a partir do nó "1"
print("Busca em Largura (BFS) a partir de 1:")
grafo.bfs("1")
print("\nBusca em Largura (DFS) a partir de 1:")
grafo.dfs_recursivo("1")
