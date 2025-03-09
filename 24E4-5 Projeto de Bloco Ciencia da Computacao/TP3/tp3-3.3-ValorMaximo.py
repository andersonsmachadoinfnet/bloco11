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

def find_max_in_subtree(node, result_queue):
    if node is None:
        result_queue.put(float('-inf'))
        return

    left_max = node.value
    right_max = node.value

    processes = []

    if node.left:
        p_left = multiprocessing.Process(target=find_max_in_subtree, args=(node.left, result_queue))
        processes.append(p_left)
        p_left.start()

    if node.right:
        p_right = multiprocessing.Process(target=find_max_in_subtree, args=(node.right, result_queue))
        processes.append(p_right)
        p_right.start()

    for p in processes:
        p.join()

    if not result_queue.empty():
        left_max = result_queue.get()
    if not result_queue.empty():
        right_max = result_queue.get()

    result_queue.put(max(node.value, left_max, right_max))

def find_max(root):
    result_queue = multiprocessing.Queue() 
    find_max_in_subtree(root, result_queue)

    if not result_queue.empty():
        return result_queue.get()
    return None

if __name__ == "__main__":
    root = Node(15)
    root.insert(10)
    root.insert(20)
    root.insert(8)
    root.insert(12)
    root.insert(17)
    root.insert(25)

    # Encontrando o valor máximo
    max_value = find_max(root)
    print(f"O valor máximo é: {max_value}")
