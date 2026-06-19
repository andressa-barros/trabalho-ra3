import math
import sys
import time
from itertools import combinations

N = 25 

def gerar_combinacoes(n, p):
    # gera combinações usando iterador (otimizado em C).
    # evita alocação massiva na RAM (O(p) de espaço).

    return combinations(range(1, n + 1), p)

def estimar_memoria_materializada(n, p):
    # estima RAM necessária se usássemos uma lista (apenas para justificativa).
    qtd = math.comb(n, p)
    amostra = tuple(range(p))
    tamanho_tupla = sys.getsizeof(amostra) + sum(sys.getsizeof(x) for x in amostra)
    mb = (qtd * tamanho_tupla) / (1024 ** 2)
    return qtd, mb

def processar_conjunto(p, n=N):
    # valida cardinalidade, percorre S_p e mede tempo de execução.

    card_esperada = math.comb(n, p)
    print(f"\n{'='*50}\nS_{p} | C({n},{p}) = {card_esperada:,}")

    _, mb_estimado = estimar_memoria_materializada(n, p)
    print(f"RAM estimada (se lista): ~{mb_estimado:,.1f} MB")

    inicio = time.time()
    primeira, ultima, contador = None, None, 0

    for combo in gerar_combinacoes(n, p):
        if contador == 0: primeira = combo
        ultima = combo
        contador += 1
        # lógica de cobertura (Progs 2-5) entra aqui

    tempo = time.time() - inicio
    status = "OK" if contador == card_esperada else "DIVERGÊNCIA"
    
    print(f"Total: {contador:,} [{status}]")
    print(f"Amostra: {primeira} ... {ultima}")
    print(f"Tempo: {tempo:.4f}s")

    return contador, tempo

def executar_programa1():
    tamanhos = [15, 14, 13, 12, 11]
    resultados = [processar_conjunto(p) for p in tamanhos]

    print(f"\n{'=' * 40}\nRESUMO FINAL\n{'=' * 40}")
    print(f"{'p':>4} | {'|S_p|':>12} | {'tempo (s)':>10}")
    for i, p in enumerate(tamanhos):
        print(f"{p:>4} | {resultados[i][0]:>12,} | {resultados[i][1]:>10.4f}")

if __name__ == "__main__":
    executar_programa1()