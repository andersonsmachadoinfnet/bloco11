from collections import deque

def bfs(grafo, inicio, fim):
    fila = deque([inicio])
    
    ctrl = {inicio: None}
    
    while fila:
        bairro_atual = fila.popleft()
        
        if bairro_atual == fim:
            caminho = []
            while bairro_atual is not None:
                caminho.append(bairro_atual)
                bairro_atual = ctrl[bairro_atual]
            return caminho[::-1]  
        
        # Explorar os vizinhos
        for vizinho in grafo[bairro_atual]:
            if vizinho not in ctrl:  
                fila.append(vizinho)
                ctrl[vizinho] = bairro_atual
    
    return None  

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

caminho = bfs(grafo, 'A', 'E')
if caminho:
    print("Caminho mais curto de A a E:", caminho)
else:
    print("Não existe caminho entre A e E.")
