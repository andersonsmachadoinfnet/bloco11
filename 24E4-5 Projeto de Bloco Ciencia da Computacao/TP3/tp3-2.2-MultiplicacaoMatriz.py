import multiprocessing

def multiplicar_elemento(i, j, matriz_a, matriz_b, resultado):
    soma = 0
    for k in range(3):
        soma += matriz_a[i][k] * matriz_b[k][j]
    resultado[i][j] = soma

def multiplicar_matrizes(matriz_a, matriz_b):
    resultado = multiprocessing.Manager().list([[0 for _ in range(3)] for _ in range(3)])
    processos = []

    for i in range(3):
        for j in range(3):
            p = multiprocessing.Process(target=multiplicar_elemento, args=(i, j, matriz_a, matriz_b, resultado))
            processos.append(p)
            p.start()

    for p in processos:
        p.join()

    return [list(linha) for linha in resultado]

if __name__=='__main__':
    matriz_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matriz_b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    resultado = multiplicar_matrizes(matriz_a, matriz_b)
    print("Matriz Resultado:")
    for linha in resultado:
        print(linha)
