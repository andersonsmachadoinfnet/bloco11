class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}  

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)  # Para grafos não direcionados

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")


grafo = Grafo()

# Adicionando vértices
for v in ["Centro", "São Domingos", "Ingá", "Icaraí", "São Lourenço", "Cubango", "Santa Rosa"]:
    grafo.adicionar_vertice(v)

arestas = [("Centro", "São Domingos"), ("Centro", "São Lourenço"), ("São Domingos", "Ingá"), ("Ingá", "Icaraí"), ("São Lourenço", "Cubango"), ("Cubango", "Santa Rosa"), ("Santa Rosa", "Icaraí")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()