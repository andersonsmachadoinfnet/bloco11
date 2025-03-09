import multiprocessing

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

def buscar(node, target, result):
    if node is None:
        return
    
    if node.value == target:
        result.put(True)  
        return
    processes = []
    
    if node.left:
        p_left = multiprocessing.Process(target=buscar, args=(node.left, target, result))
        processes.append(p_left)
        p_left.start()

    if node.right:
        p_right = multiprocessing.Process(target=buscar, args=(node.right, target, result))
        processes.append(p_right)
        p_right.start()

    for p in processes:
        p.join()

def busca_em_arvore_binaria(root, target):
    result = multiprocessing.Queue()
    buscar(root, target, result)
    
    if not result.empty() and result.get():
        return True
    return False

if __name__ == "__main__":
    root = Node(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)

    alvo = 60
    encontrado = busca_em_arvore_binaria(root, alvo)
    if encontrado:
        print(f"Valor {alvo} encontrado na árvore!")
    else:
        print(f"Valor {alvo} não encontrado na árvore!")
