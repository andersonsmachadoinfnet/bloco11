import multiprocessing

class Grafo:
    def __init__(self):
        self.graph = {}

    def add(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) 

def dfs_parallel(graph, node, visited, result_queue):
    visited.add(node)  
    result_queue.put(node)
    processes = []
    for neighbor in graph[node]:
        if neighbor not in visited:
            p = multiprocessing.Process(target=dfs_parallel, args=(graph, neighbor, visited, result_queue))
            processes.append(p)
            p.start()

    for p in processes:
        p.join()

def dfs(graph, start):
    visited = set() 
    result_queue = multiprocessing.Queue() 
    dfs_parallel(graph, start, visited, result_queue)

    visited_nodes = []
    while not result_queue.empty():
        visited_nodes.append(result_queue.get())

    return visited_nodes

if __name__ == "__main__":
    g = Grafo()
    g.add(0, 1)
    g.add(0, 2)
    g.add(1, 3)
    g.add(1, 4)
    g.add(2, 5)

    no_ini = 0
    print(f"Iniciando a busca em profundidade a partir do nó {no_ini}...")

    visitados = dfs(g.graph, no_ini)
    print(f"Nós visitados: {visitados}")
