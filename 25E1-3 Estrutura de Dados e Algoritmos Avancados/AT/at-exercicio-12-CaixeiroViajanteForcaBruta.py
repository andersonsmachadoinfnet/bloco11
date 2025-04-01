import itertools
import time

def calcular_distancia_total(permutacao, matriz_distancias):
    distancia_total = 0
    for i in range(len(permutacao) - 1):
        cidade_atual = permutacao[i]
        cidade_proxima = permutacao[i + 1]
        distancia_total += matriz_distancias[cidade_atual][cidade_proxima]
    cidade_inicial = permutacao[0]
    cidade_final = permutacao[-1]
    distancia_total += matriz_distancias[cidade_final][cidade_inicial]
    return distancia_total

def tsp_forca_bruta(matriz_distancias):
    cidades = range(len(matriz_distancias))
    permutacoes = itertools.permutations(cidades)
    
    melhor_distancia = float('inf')
    melhor_permutacao = None
    
    for perm in permutacoes:
        distancia = calcular_distancia_total(perm, matriz_distancias)
        if distancia < melhor_distancia:
            melhor_distancia = distancia
            melhor_permutacao = perm
    
    return melhor_distancia, melhor_permutacao

# Matriz de Adjacência para 6 cidades (distancias)
matriz_distancias = [
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 30, 40],
    [15, 35, 0, 30, 20, 50],
    [20, 25, 30, 0, 15, 20],
    [25, 30, 20, 15, 0, 10],
    [30, 40, 50, 20, 10, 0]
]

start_time = time.time()
melhor_distancia, melhor_permutacao = tsp_forca_bruta(matriz_distancias)
end_time = time.time()

print("Melhor distância:", melhor_distancia)
print("Melhor permutação:", melhor_permutacao)
print(f"Tempo de execução: {end_time - start_time:.4f} segundos.")