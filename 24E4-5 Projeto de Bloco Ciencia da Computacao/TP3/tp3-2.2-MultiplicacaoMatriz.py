import numpy as np
import multiprocessing

def multiplicar_elemento(i, j, A, B, result):
    soma = 0
    for k in range(len(A)):
        soma += A[i][k] * B[k][j]
    result[i][j] = soma

def multiplicar_matrizes_paralelo(A, B):
    result = multiprocessing.Manager().list([[0 for _ in range(len(A))] for _ in range(len(A))])

    processos = []

    for i in range(len(A)):
        for j in range(len(A[0])):
            p = multiprocessing.Process(target=multiplicar_elemento, args=(i, j, A, B, result))
            processos.append(p)
            p.start()

    for p in processos:
        p.join()

    return np.array(result)

if __name__ == '__main__':
    A = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

    B = np.array([[9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]])

    resultado = multiplicar_matrizes_paralelo(A, B)

    print("Resultado da multiplicação das matrizes:")
    print(resultado)
