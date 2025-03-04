import concurrent.futures

def soma_parcial(arr, inicio, fim):
    return sum(arr[inicio:fim])

def soma_paralela(arr):
    num_threads = 4
    tamanho_parte = len(arr) // num_threads
    resultados = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(soma_parcial, arr, i * tamanho_parte, (i + 1) * tamanho_parte if i != num_threads - 1 else len(arr))
            for i in range(num_threads)
        ]
        
        for future in concurrent.futures.as_completed(futures):
            resultados.append(future.result())

    return sum(resultados)

arr = []
for valor in range(0,1000000):
    arr.append(valor)
resultado = soma_paralela(arr)
print(f"A soma paralela do array é: {resultado}")
