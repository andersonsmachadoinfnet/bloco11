import itertools
import math

def calcular_distancia(cidade1, cidade2):
    return math.sqrt((cidade2[0] - cidade1[0]) ** 2 + (cidade2[1] - cidade1[1]) ** 2)

def calcular_rota(cidades, percurso):
    distancia_total = 0
    for i in range(len(percurso) - 1):
        distancia_total += calcular_distancia(cidades[percurso[i]], cidades[percurso[i + 1]])
    distancia_total += calcular_distancia(cidades[percurso[-1]], cidades[percurso[0]]) 
    return distancia_total

def caixeiro_viajante(cidades):
    cidades_indices = list(range(len(cidades)))
    cidades_permutacoes = itertools.permutations(cidades_indices)
    
    melhor_distancia = float('inf')
    melhor_rota = None
    
    for percurso in cidades_permutacoes:
        distancia = calcular_rota(cidades, percurso)
        if distancia < melhor_distancia:
            melhor_distancia = distancia
            melhor_rota = percurso
    
    return melhor_rota, melhor_distancia

cidades = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}

cidades_lista = list(cidades.values())
melhor_rota, melhor_distancia = caixeiro_viajante(cidades_lista)

print("Melhor Rota (na ordem das cidades):")
for indice in melhor_rota:
    print(list(cidades.keys())[indice], end=' -> ')
print(list(cidades.keys())[melhor_rota[0]])  

print(f"\nDistância total da melhor rota: {melhor_distancia:.2f}")
