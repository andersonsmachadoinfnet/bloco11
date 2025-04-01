import random
import time

movimentos = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

def dentro_tabuleiro(x, y, N):
    return 0 <= x < N and 0 <= y < N

def movimentos_possiveis(tabuleiro, x, y, N):
    moves = []
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
            moves.append((nx, ny))
    return moves

def proximo_movimento(tabuleiro, x, y, N):
    moves = movimentos_possiveis(tabuleiro, x, y, N)
    if not moves:
        return None

    moves.sort(key=lambda move: len(movimentos_possiveis(tabuleiro, move[0], move[1], N)))
    
    return moves[0]  # Retorna o movimento com menos opções futuras

def passeio_do_cavalo(N, inicio_x=0, inicio_y=0):
    tabuleiro = [[-1] * N for _ in range(N)]
    x, y = inicio_x, inicio_y
    tabuleiro[x][y] = 0  # Posição inicial do cavalo

    for i in range(1, N * N):
        movimento = proximo_movimento(tabuleiro, x, y, N)
        if not movimento:
            print("Falha: Caminho interrompido!")
            return None
        
        x, y = movimento
        tabuleiro[x][y] = i  # Marca o movimento no tabuleiro

    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{num:2}" for num in linha))

# Definição do tamanho do tabuleiro e execução do algoritmo
N = 10  # Tabuleiro 8x8
start_time = time.time()
solucao = passeio_do_cavalo(N)
end_time = time.time()

if solucao:
    print("\nPasseio do Cavalo encontrado:")
    imprimir_tabuleiro(solucao)
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos.")
