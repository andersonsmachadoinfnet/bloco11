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


# A matriz indica o tempo em minutos de deslocamento entre os bairros (0 para si mesmo, INF se não houver ligação direta)
grafo_cidades = [
    # A    B    C    D    E    F  
    [  0,   5,  10, INF, INF, INF],   # A
    [  5,   0,   3,   8, INF, INF],   # B
    [ 10,   3,   0,   2,   7, INF],   # C
    [INF,   8,   2,   0,   4,   6],   # D
    [INF, INF,   7,   4,   0,   5],   # E
    [INF, INF, INF,   6,   5,   0]    # F
]

# Executando o algoritmo de Floyd-Warshall
menores_caminhos = floyd_warshall(grafo_cidades)

# Exibindo a matriz resultante
print("Matriz dos menores distâncias (KM) entre todas as cidades:")
for linha in menores_caminhos:
    print(linha)
