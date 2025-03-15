class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_aeroporto(self, aeroporto):
        if aeroporto not in self.vertices:
            self.vertices[aeroporto] = {}

    def adicionar_rota(self, aeroporto1, aeroporto2, distancia):
        self.vertices[aeroporto1][aeroporto2] = distancia
        self.vertices[aeroporto2][aeroporto1] = distancia  # Grafo não direcionado

    def dijkstra(self, origem, destino):
        #Encontra a menor rota entre duas cidades usando Dijkstra.
        nao_visitados = list(self.vertices.keys())  # Lista de cidades não visitadas
        distancias = {cidade: float("inf") for cidade in self.vertices}  # Inicializa todas as distâncias como infinito
        distancias[origem] = 0  # A distância da origem para ela mesma é 0
        predecessores = {}  # Para armazenar o caminho percorrido

        while nao_visitados:
            # Encontrar o nó com a menor distância conhecida
            cidade_atual = min(nao_visitados, key=lambda cidade: distancias[cidade])

            if distancias[cidade_atual] == float("inf"):
                break  # Se a menor distância ainda for infinita, não há caminho viável

            for vizinho, distancia in self.vertices[cidade_atual].items():
                nova_distancia = distancias[cidade_atual] + distancia
                if nova_distancia < distancias[vizinho]:  # Se encontrarmos um caminho melhor
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = cidade_atual  # Armazena de onde viemos

            nao_visitados.remove(cidade_atual)  # Marca a cidade como visitada

        # Reconstrução do caminho
        caminho = []
        cidade_atual = destino
        while cidade_atual in predecessores:
            caminho.append(cidade_atual)
            cidade_atual = predecessores[cidade_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]

# Criando o mapa com 7 aeroportos
mapa_aeroportos = GrafoPoderado()
aeroportos = ["Guarulhos", "Congonhas", "Brasilia", "Galeao", "Campinas", "Confins", "Guararapes"]

# Adicionando aeroportos ao grafo
for aeroporto in aeroportos:
    mapa_aeroportos.adicionar_aeroporto(aeroporto)

# Adicionando rotas com suas respectivas distancias
rotas = [
    ("Guarulhos", "Congonhas", 34), ("Guarulhos", "Brasilia", 1000),
    ("Guarulhos", "Galeao", 400), ("Guarulhos", "Campinas", 115),
    ("Guarulhos", "Confins", 620), ("Guarulhos", "Guararapes", 2600),
    ("Galeao", "Guararapes", 2280), ("Galeao", "Confins", 475),
    ("Galeao", "Campinas", 506), ("Galeao", "Brasilia", 1150),
    ("Galeao", "Congonhas", 440),
    ("Brasilia", "Congonhas", 1005), ("Brasilia", "Guarulhos", 918),
]

for aeroporto1, aeroporto2, distancia in rotas:
    mapa_aeroportos.adicionar_rota(aeroporto1, aeroporto2, distancia)


origem = "Galeao"
destino = "Brasilia"
rota, tempo = mapa_aeroportos.dijkstra(origem, destino)

# Exibindo o resultado
print(f"Melhor rota do {origem} para {destino}: {' => '.join(rota)}. distância: {tempo} km")
