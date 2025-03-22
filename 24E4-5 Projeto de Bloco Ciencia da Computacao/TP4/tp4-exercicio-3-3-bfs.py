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

# Criando o grafo
grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F"]
for v in vertices:
    grafo.adicionar_vertice(v)

# Adicionando arestas
arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

# Executando BFS a partir do nó "A"
print("Busca em Largura (BFS) a partir de A:")
grafo.bfs("A")
