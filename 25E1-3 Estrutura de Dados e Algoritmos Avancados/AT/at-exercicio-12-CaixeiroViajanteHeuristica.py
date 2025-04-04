import time

def calcular_distancia(cidade1, cidade2):
    x1, y1 = cidade1
    x2, y2 = cidade2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  

def encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas):
    menor_distancia = float('inf')
    cidade_mais_proxima = None
    for cidade in cidades_nao_visitadas:
        distancia = calcular_distancia(cidade_atual, cidade)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cidade_mais_proxima = cidade
    return cidade_mais_proxima, menor_distancia

def tsp_vizinho_mais_proximo(cidades):
    cidade_inicial = cidades[0]  # Começa pela primeira cidade
    caminho = [cidade_inicial]  # Caminho percorrido
    cidades_nao_visitadas = cidades[1:]  # Lista de cidades ainda não visitadas
    distancia_total = 0

    cidade_atual = cidade_inicial
    while cidades_nao_visitadas:
        proxima_cidade, distancia = encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas)
        caminho.append(proxima_cidade)
        cidades_nao_visitadas.remove(proxima_cidade)
        distancia_total += distancia
        cidade_atual = proxima_cidade

    # Volta para a cidade inicial para completar o ciclo
    distancia_total += calcular_distancia(cidade_atual, cidade_inicial)
    caminho.append(cidade_inicial)

    return caminho, distancia_total

# Lista de cidades representadas como coordenadas (x, y)
cidades = [(0, 0), (2, 3), (5, 4), (1, 1), (7, 2), (6, 6)]

# Executando o algoritmo
start_time = time.time()
caminho, distancia = tsp_vizinho_mais_proximo(cidades)
end_time = time.time()

# Exibindo o resultado
print("Melhor caminho encontrado:", caminho)
print("Distância total percorrida:", distancia)
print(f"Tempo de execução: {end_time - start_time:.4f} segundos.")