import time

N = 8  # Tamanho do tabuleiro de xadrez

movimentos = [(-2, -1), (-1, -2), (1, -2), (2, -1),
              (2, 1), (1, 2), (-1, 2), (-2, 1)]

def movimento_valido(x, y, tabuleiro):
    return 0 <= x < N and 0 <= y < N and tabuleiro[x][y] == -1

def imprimir_tabuleiro(tabuleiro):
    for i in range(N):
        for j in range(N):
            print(f"{tabuleiro[i][j]:2}", end=" ")
        print()

def resolver_cavalo(x, y, movimento_num, tabuleiro):
    if movimento_num == N * N:
        return True

    for dx, dy in movimentos:
        novo_x, novo_y = x + dx, y + dy

        if movimento_valido(novo_x, novo_y, tabuleiro):
            tabuleiro[novo_x][novo_y] = movimento_num  
            if resolver_cavalo(novo_x, novo_y, movimento_num + 1, tabuleiro):  
                return True
            tabuleiro[novo_x][novo_y] = -1

    return False

def knight_tour():
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]

    x, y = 0, 0  # Começar no canto superior esquerdo (0, 0)

    tabuleiro[x][y] = 0

    if not resolver_cavalo(x, y, 1, tabuleiro):
        print("Solução não encontrada!")
        return False

    imprimir_tabuleiro(tabuleiro)
    return True

start_time = time.time()
knight_tour()
end_time = time.time()

print(f"Tempo de execução: {end_time - start_time:.4f} segundos.")
