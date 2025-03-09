import multiprocessing
import math
import time

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def contar_primos_no_intervalo(start, end):
    return sum(1 for i in range(start, end) if is_prime(i))

def contar_primos_paralelo(upper_limit):
    num_processes = multiprocessing.cpu_count()

    interval_size = upper_limit // num_processes
    ranges = [(i * interval_size + 1, (i + 1) * interval_size + 1) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], upper_limit + 1)  

    with multiprocessing.Pool(num_processes) as pool:
        result = pool.starmap(contar_primos_no_intervalo, ranges)

    return sum(result)

if __name__ == "__main__":
    upper_limit = 100000
    tempo_inicial=time.time()
    num_primos = contar_primos_paralelo(upper_limit)
    tempo_final=time.time()
    print(f"Total de números primos entre 1 e {upper_limit}: {num_primos} Paralelo em {tempo_final-tempo_inicial}")
    tempo_inicial=time.time()
    num_primos = contar_primos_no_intervalo(1, upper_limit);
    tempo_final=time.time()
    print(f"Total de números primos entre 1 e {upper_limit}: {num_primos} Sequencial em {tempo_final-tempo_inicial}")
