# Instituto Infnet
# Aluno     : Anderson Soares Miler Machado
# Turma     : 24E4_5
# Disciplina: Projeto de bloco

class No:
    # classe que implementa um nó
    def __init__(self, value):
        self.value = value
        self.esq   = None
        self.dir   = None

class ArvoreBinaria:
    # Classe que representa uma arvore binária
    def __init__(self):
        self.raiz = None
    
    def add(self, value):
        if self.raiz is None:
            self.raiz = No(value)
        else:
            self._add(self.raiz, value)
    
    def _add(self, current, value):
        if value < current.value:
            if current.esq is None:
                current.esq = No(value)
            else:
                self._add(current.esq, value)
        else:
            if current.dir is None:
                current.dir = No(value)
            else:
                self._add(current.dir, value)
    
    def search(self, value):
        return self._search(self.raiz, value)
    
    def _search(self, current, value):
        if current is None:
            return False
        if current.value==value:
            return True
        if value < current.value:
            return self._search(current.esq, value)
        else:
            return self._search(current.dir, value)
    
    def valida(self):
        return self._valida(self.raiz)
    
    def _valida(self, current):
        lRet = True
        if current is None:
            return True
        if (current.esq is not None and current.value<current.esq.value) or (current.dir is not None and current.value>current.dir.value):
            return False
        if (self._valida(current.esq)==False):
            return False
        if (self._valida(current.dir)==False):
            return False
        return lRet
        
        
    def remover(self, value):
        self.raiz = self._remover(self.raiz, value)
    
    def _remover(self, current, value):
        if current is None:
            return current
        
        if value<current.value:
            current.esq = self._remover(current.esq, value)
        elif value>current.value:
            current.dir = self._remover(current.dir, value)
        else:
            if current.esq is None and current.dir is None:
                return None
            if current.esq is None:
                return current.dir
            if current.dir is None:
                return current.esq
            min_larger_node = self._get_min(current.dir)
            current.value = min_larger_node.value
            current.dir = self._remover(current.dir, min_larger_node.value)
        return current
    
    def _get_min(self, current):
        while current.esq is not None:
            current = current.esq
        return current
    
    def inorder(self):
        # percorrer esquerda -> raiz -> direita
        result = []
        self._inorder(self.raiz, result)
        return result
    
    def _inorder(self, current, result):
        if current is not None:
            self._inorder(current.esq, result)
            result.append(current.value)
            self._inorder(current.dir, result)
    
    def preorder(self):
        # percorrer raiz -> esq - > direita
        result = []
        self._preorder(self.raiz, result)
        return result
    
    def _preorder(self, current, result):
        if current is not None:
            result.append(current.value)
            self._preorder(current.esq, result)
            self._preorder(current.dir, result)
    
    def postorder(self):
        # percorrer esq -> dir -> raiz
        result = []
        self._postorder(self.raiz, result)
        return result
    
    def _postorder(self, current, result):
        if current is not None:
            self._postorder(current.esq, result)
            self._postorder(current.dir, result)
            result.append(current.value)
    
    def height(self):
        return self._height(self.raiz)
    
    def _height(self, current):
        if current is None:
            return -1
        left_height = self._height(current.esq)
        right_height= self._height(current.dir)
        return 1 + max(left_height, right_height)

    def _alteraValorDoNo(self, value):
        self.raiz.value=value
    
tree = ArvoreBinaria()
for value in [50, 30, 70, 20, 60, 80]:
    print(f'Adicionando {value}')
    tree.add(value)
    print(f'BST Válida? {tree.valida()}')

print(f'Árvore inicial: {tree.inorder()}')
print(f'BST Válida? {tree.valida()}')
print('Alterando valor do nó a força')
tree._alteraValorDoNo(5)
print(f'Árvore Final: {tree.inorder()}')
print(f'BST Válida? {tree.valida()}')

