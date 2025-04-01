# Aluno     : Anderson Machado
# Disciplina: 25E1_3 Estruturas de Dados e Algoritmos Avançados
# Professor : Flávio da Silva Neves
# Questão   : 7 do TP1

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
    
    def levenshtein(self, str1, str2):
        len_str1, len_str2 = len(str1), len(str2)
        matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

        for i in range(len_str1 + 1):
            for j in range(len_str2 + 1):
                if i == 0:
                    matrix[i][j] = j
                elif j == 0:
                    matrix[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = 1 + min(matrix[i - 1][j],      # Deleção
                                       matrix[i][j - 1],      # Inserção
                                       matrix[i - 1][j - 1])  # Substituição

        return matrix[len_str1][len_str2]
    
    def autocompletar_levenshtein(self, prefixo):
        for palavra in self.list_words():
            if self.levenshtein(prefixo, palavra[0:len(prefixo)])==1:
                return self.autocompletar(palavra[0:len(prefixo)])
        return ''
    
trie = Trie()
trie.insert('O Morro dos Ventos Uivantes – Emily Bront – 1847')
trie.insert('As Flores do Mal – Chales Baudelaire – 1857')
trie.insert('Em Busca do Tempo Perdido – Marcel Proust, 1913')
trie.insert('O Sol Também se Levanta – Ernest Hemingway – 1926')
trie.insert('O Som e a Fúria – William Faulkner, 1929')
trie.insert('Brejo das Almas – Carlos Drummond de Andrade, 1934')
trie.insert('As Vinhas da Ira – John Steinbeck, 1939')
trie.insert('O Apanhador no Campo de Centeio – J. D. Salinger, 1951')
trie.insert('O Tempo e o Vento – Érico Veríssimo – Década de 1950')
trie.insert('Cem Anos de Solidão – Gabriel Garcia Marquez, 1967')
trie.insert('A Hora da Estrela – Clarice Lispector – 1977')

pesquisa = 'As'
print(f"Sugestões para {pesquisa}:", trie.autocompletar(pesquisa))
pesquisa = 'Sem'
print(f"Sugestões para {pesquisa}:", trie.autocompletar_levenshtein(pesquisa))
