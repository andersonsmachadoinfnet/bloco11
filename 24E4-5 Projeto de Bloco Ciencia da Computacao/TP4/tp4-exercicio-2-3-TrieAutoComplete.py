class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):

        def _delete(node, word, depth):
            if depth==len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children)==0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete_child = _delete(node.children[char], word, depth+1)
            if should_delete_child:
                del node.children[char]
                return len(node.children)==0
            
            return False
        
        _delete(self.root, word, 0)

    def list_words(self):
        
        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)
            
        words=[]
        _dfs(self.root, "", words)
        return words
    
    def autocompletar(self, prefixo):
        def _starts_with(prefix):
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return False
                node = node.children[char]
            return node

        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefixo+prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)
            
        words=[]
        base = _starts_with(prefixo)
        if base==False:
            return words
        _dfs(base, "", words)
        return words
    
trie = Trie()

while True:
    op = input("Menu\n1-Adicionar palavras no dicionário;\n2-Pesquisar com autocompletar;\n9-Sair\n")
    if op == '1':
        palavra = input("Digite uma nova palavra:")
        trie.insert(palavra)
    elif op== '2':
        pesquisa = input("Digite o que pesquisar:")
        print("Sugestões:", trie.autocompletar(pesquisa))
    elif op=='9':
        break
1