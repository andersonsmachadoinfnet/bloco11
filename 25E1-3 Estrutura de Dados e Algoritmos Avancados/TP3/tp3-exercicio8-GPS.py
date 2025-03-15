# Representa um valor infinito para indicar que não há conexão direta entre os vértices
INF = float('inf')

def floyd_warshall(grafo):
    # Número de vértices no grafo
    num_vertices = len(grafo)
    
    # Criando uma cópia da matriz do grafo para armazenar as menores distâncias
    dist = [[grafo[i][j] for j in range(num_vertices)] for i in range(num_vertices)]

    # Aplicação do algoritmo de Floyd-Warshall
    for k in range(num_vertices):  # Considera cada vértice como intermediário
        for i in range(num_vertices):  # Itera sobre todos os vértices de origem
            for j in range(num_vertices):  # Itera sobre todos os vértices de destino
                # Atualiza a distância mínima de i para j passando por k
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist  # Retorna a matriz com as menores distâncias entre os pares de vértices


# Definição do grafo representando 5 bairros
# 0="Centro",1="Sao Domingos",2="Inga",3="Icarai",4="Santa Rosa"
# A matriz indica o tempo em minutos de deslocamento entre os bairros (0 para si mesmo, INF se não houver ligação direta)
grafo_cidades = [
    [0, 5, INF, 7, INF],   # Cidade Centro
    [5, 0, 2, INF, INF],   # Cidade São Domingos
    [INF, 2, 0, 5, INF],   # Cidade Inga
    [7, INF, 5, 0, 4],     # Cidade Icarai
    [INF, INF, INF, 4, 0]  # Cidade Santa Rosa
]

# Executando o algoritmo de Floyd-Warshall
menores_caminhos = floyd_warshall(grafo_cidades)

# Exibindo a matriz resultante
print("Matriz dos menores tempos entre todas as cidades:")
for linha in menores_caminhos:
    print(linha)
