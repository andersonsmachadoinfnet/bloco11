import time

class GrafoAlgoritmoPrim:
    def __init__(self, vertices, bairros):
        self.V = vertices  # Número de vértices
        self.bairros=bairros
        self.grafo = [[0] * vertices for _ in range(vertices)]  # Matriz de adjacência

    def adicionar_aresta(self, u, v, peso):
        # Adiciona uma aresta entre os vértices u e v com um peso.
        self.grafo[self.bairros.index(u)][self.bairros.index(v)] = peso
        self.grafo[self.bairros.index(v)][self.bairros.index(u)] = peso  # Grafo não direcionado

    def prim(self):
        # Executa o algoritmo de Prim para encontrar a Árvore Geradora Mínima.
        infinito = float('inf')
        selecionado = [False] * self.V  # Marcar os vértices incluídos na AGM
        chave = [infinito] * self.V  # Peso mínimo para incluir um vértice
        pai = [-1] * self.V  # Armazena a estrutura da AGM

        # Começamos pelo primeiro vértice
        chave[0] = 0  

        for _ in range(self.V):
            # Escolhe o vértice de menor chave que ainda não foi incluído na AGM
            minimo = infinito
            u = -1
            for v in range(self.V):
                if not selecionado[v] and chave[v] < minimo:
                    minimo = chave[v]
                    u = v

            selecionado[u] = True  # Marca o vértice como incluído na AGM

            # Atualiza os valores das chaves e define os pais dos vértices adjacentes
            for v in range(self.V):
                if 0 < self.grafo[u][v] < chave[v] and not selecionado[v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u

        # Exibindo a Árvore Geradora Mínima
        print("\nArestas da Árvore Geradora Mínima:")
        custo_total = 0
        for i in range(1, self.V):
            print(f"{self.bairros[pai[i]]} - {self.bairros[i]} (R$: {self.grafo[i][pai[i]]} mil)")
            custo_total += self.grafo[i][pai[i]]
        print(f"Peso total da AGM: R$ {custo_total} mil")

# Criando o grafo com 6 vértices
g = GrafoAlgoritmoPrim(6, ["Niteroi","Sao Goncalo","Itaborai","Tangua","Marica","Rio Bonito"])


# Adicionando as arestas e seus respectivos pesos
arestas = [
    ("Niteroi", "Sao Goncalo", 140), ("Niteroi", "Marica", 490), ("Sao Goncalo", "Itaborai", 300),
    ("Sao Goncalo", "Marica", 390), ("Itaborai", "Marica", 270), ("Itaborai", "Tangua", 160),
    ("Tangua", "Marica", 410), ("Tangua", "Rio Bonito", 110), ("Rio Bonito", "Marica", 500)
]

for u, v, peso in arestas:
    g.adicionar_aresta(u, v, peso)

# Executando Prim
tempo_inicial=time.time()
g.prim()
tempo_final=time.time()
print(f"Pequeno   : {tempo_final-tempo_inicial}")


# Criando o grafo com 6 vértices
g = GrafoAlgoritmoPrim(92, ["Angra dos Reis","Aperibé","Araruama","Areal","Armação dos Búzios","Arraial do Cabo",
                            "Barra do Piraí","Barra Mansa","Belford Roxo","Bom Jardim","Bom Jesus do Itabapoana",
                            "Cabo Frio","Cachoeiras de Macacu","Cambuci","Campos dos Goytacazes","Cantagalo",
                            "Carapebus","Cardoso Moreira","Carmo","Casimiro de Abreu","Comendador Levy Gasparian",
                            "Conceição de Macabu","Cordeiro","Duas Barras","Duque de Caxias","Engenheiro Paulo de Frontin",
                            "Guapimirim","Iguaba Grande","Itaboraí","Itaguaí","Italva","Itaocara","Itaperuna",
                            "Itatiaia","Japeri","Laje do Muriaé","Macaé","Macuco","Magé","Mangaratiba","Maricá",
                            "Mendes","Mesquita","Miguel Pereira","Miracema","Natividade","Nilópolis","Niterói",
                            "Nova Friburgo","Nova Iguaçu","Paracambi","Paraíba do Sul","Paraty","Paty do Alferes",
                            "Petrópolis","Pinheiral","Piraí","Porciúncula","Porto Real","Quatis","Queimados",
                            "Quissamã","Resende","Rio Bonito","Rio Claro","Rio das Flores","Rio das Ostras",
                            "Rio de Janeiro","Santa Maria Madalena","Santo Antônio de Pádua","São Fidélis",
                            "São Francisco de Itabapoana","São Gonçalo","São João da Barra","São João de Meriti",
                            "São José de Ubá","São José do Vale do Rio Preto","São Pedro da Aldeia",
                            "São Sebastião do Alto","Sapucaia","Saquarema","Seropédica","Silva Jardim",
                            "Sumidouro","Tanguá","Teresópolis","Trajano de Moraes","Três Rios",
                            "Valença","Varre-Sai","Vassouras","Volta Redonda"])


# Adicionando as arestas e seus respectivos pesos
arestas = [
    ("Niterói", "São Gonçalo", 140), ("Niterói", "Maricá", 490), ("São Gonçalo", "Itaboraí", 300),
    ("São Gonçalo", "Maricá", 390), ("Itaboraí", "Maricá", 270), ("Itaboraí", "Tanguá", 160),
    ("Tanguá", "Maricá", 410), ("Tanguá", "Rio Bonito", 110), ("Rio Bonito", "Maricá", 500),
    ("Angra dos Reis","Aperibé",410),("Araruama","Areal",290),("Armação dos Búzios","Arraial do Cabo",250),
    ("Barra do Piraí","Barra Mansa",400),("Belford Roxo","Bom Jardim",380),("Bom Jesus do Itabapoana","Cabo Frio",100),
    ("Cachoeiras de Macacu","Cambuci",150),("Campos dos Goytacazes","Cantagalo",190),
    ("Carapebus","Cardoso Moreira",270),("Carmo","Casimiro de Abreu",800),("Comendador Levy Gasparian","Conceição de Macabu",700),
    ("Cordeiro","Duas Barras",500),("Duque de Caxias","Engenheiro Paulo de Frontin",200),
    ("Guapimirim","Iguaba Grande",140),("Itaboraí","Itaguaí",600),("Italva","Itaocara",220),("Itaperuna","Itatiaia",90),
    ("Japeri","Laje do Muriaé",20),("Macaé","Macuco",300),("Magé","Mangaratiba",140),("Maricá","Mendes",300),
    ("Mesquita","Miguel Pereira",270),("Miracema","Natividade",300),("Nilópolis","Niterói",45),
    ("Nova Friburgo","Nova Iguaçu",80),("Paracambi","Paraíba do Sul",210),("Paraty","Paty do Alferes",30),
    ("Petrópolis","Pinheiral",900),("Piraí","Porciúncula",500),("Porto Real","Quatis",450),("Queimados","Quissamã",100),
    ("Resende","Rio Bonito",300),("Rio Claro","Rio das Flores",250),("Rio das Ostras","Rio de Janeiro",270),
    ("Santa Maria Madalena","Santo Antônio de Pádua",90),("São Fidélis","São Francisco de Itabapoana",130),
    ("São Gonçalo","São João da Barra",80),("São João de Meriti","São José de Ubá",75),
    ("São José do Vale do Rio Preto","São Pedro da Aldeia",170),
    ("São Sebastião do Alto","Sapucaia",20),("Saquarema","Seropédica",200),("Silva Jardim","Sumidouro",260),
    ("Tanguá","Teresópolis",140),("Trajano de Moraes","Três Rios",90),
    ("Valença","Varre-Sai",20),("Vassouras","Volta Redonda",75),
    ("Angra dos Reis","Rio de Janeiro",200),("Aperibé","Rio de Janeiro",260),("Araruama","Rio de Janeiro",130),
    ("Areal","Rio de Janeiro",157),("Armação dos Búzios","Rio de Janeiro",165),("Arraial do Cabo","Rio de Janeiro",160),
    ("Barra do Piraí","Rio de Janeiro",90),("Barra Mansa","Rio de Janeiro",75),("Belford Roxo","Rio de Janeiro",45),
    ("Bom Jardim","Rio de Janeiro",190),("Bom Jesus do Itabapoana","Rio de Janeiro",260),
    ("Cabo Frio","Rio de Janeiro",160),("Cachoeiras de Macacu","Rio de Janeiro",90),("Cambuci","Rio de Janeiro",250),
    ("Campos dos Goytacazes","Rio de Janeiro",315),("Cantagalo","Rio de Janeiro",215),
    ("Carapebus","Rio de Janeiro",200),("Cardoso Moreira","Rio de Janeiro",210),("Carmo","Rio de Janeiro",190),
    ("Casimiro de Abreu","Rio de Janeiro",165),("Comendador Levy Gasparian","Rio de Janeiro",190),
    ("Conceição de Macabu","Rio de Janeiro",220),("Cordeiro","Rio de Janeiro",250),("Duas Barras","Rio de Janeiro",270),
    ("Duque de Caxias","Rio de Janeiro",30),("Engenheiro Paulo de Frontin","Rio de Janeiro",300),
    ("Guapimirim","Rio de Janeiro",110),("Iguaba Grande","Rio de Janeiro",90),("Itaboraí","Rio de Janeiro",60),
    ("Itaguaí","Rio de Janeiro",170),("Italva","Rio de Janeiro",270),("Itaocara","Rio de Janeiro",260),
    ("Itaperuna","Rio de Janeiro",310),("Itatiaia","Rio de Janeiro",180),("Japeri","Rio de Janeiro",35),
    ("Laje do Muriaé","Rio de Janeiro",150),("Macaé","Rio de Janeiro",175),("Macuco","Rio de Janeiro",200),
    ("Magé","Rio de Janeiro",75),("Mangaratiba","Rio de Janeiro",74),("Maricá","Rio de Janeiro",110),
    ("Mendes","Rio de Janeiro",170),("Mesquita","Rio de Janeiro",60),("Miguel Pereira","Rio de Janeiro",125),
    ("Miracema","Rio de Janeiro",280),("Natividade","Rio de Janeiro",310),("Nilópolis","Rio de Janeiro",45),
    ("Niterói","Rio de Janeiro",13),("Nova Friburgo","Rio de Janeiro",115),("Nova Iguaçu","Rio de Janeiro",46),
    ("Paracambi","Rio de Janeiro",55),("Paraíba do Sul","Rio de Janeiro",180),("Paraty","Rio de Janeiro",145),
    ("Paty do Alferes","Rio de Janeiro",165),("Petrópolis","Rio de Janeiro",114),("Pinheiral","Rio de Janeiro",90),
    ("Piraí","Rio de Janeiro",170),("Porciúncula","Rio de Janeiro",260),("Porto Real","Rio de Janeiro",25),
    ("Quatis","Rio de Janeiro",190),("Queimados","Rio de Janeiro",55),("Quissamã","Rio de Janeiro",130),
    ("Resende","Rio de Janeiro",260),("Rio Bonito","Rio de Janeiro",75),("Rio Claro","Rio de Janeiro",130),
    ("Rio das Flores","Rio de Janeiro",140),("Rio das Ostras","Rio de Janeiro",140),
    ("Santa Maria Madalena","Rio de Janeiro",235),("Santo Antônio de Pádua","Rio de Janeiro",290),
    ("São Fidélis","Rio de Janeiro",235),("São Francisco de Itabapoana","Rio de Janeiro",290),("São Gonçalo","Rio de Janeiro",35),
    ("São João da Barra","Rio de Janeiro",140),("São João de Meriti","Rio de Janeiro",55),
    ("São José de Ubá","Rio de Janeiro",200),("São José do Vale do Rio Preto","Rio de Janeiro",210),
    ("São Pedro da Aldeia","Rio de Janeiro",110),("São Sebastião do Alto","Rio de Janeiro",115),("Sapucaia","Rio de Janeiro",150),
    ("Saquarema","Rio de Janeiro",200),("Seropédica","Rio de Janeiro",90),("Silva Jardim","Rio de Janeiro",80),
    ("Sumidouro","Rio de Janeiro",200),("Tanguá","Rio de Janeiro",75),("Teresópolis","Rio de Janeiro",90),
    ("Trajano de Moraes","Rio de Janeiro",160),("Três Rios","Rio de Janeiro",135),
    ("Valença","Rio de Janeiro",200),("Varre-Sai","Rio de Janeiro",210),("Vassouras","Rio de Janeiro",175),
    ("Volta Redonda","Rio de Janeiro",135)
]

for u, v, peso in arestas:
    g.adicionar_aresta(u, v, peso)

# Executando Prim
tempo_inicial=time.time()
g.prim()
tempo_final=time.time()
print(f"Pequeno   : {tempo_final-tempo_inicial}")
