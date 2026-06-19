import math
import sys
from itertools import combinations

def gerar_combinacoes(n, p):
    # Gera combinações usando iterador (otimizado em C)
    return combinations(range(1, n + 1), p)

def estimar_memoria_materializada(n, p):
    # Estima RAM necessária se usássemos uma lista
    qtd = math.comb(n, p)
    amostra = tuple(range(p))
    tamanho_tupla = sys.getsizeof(amostra) + sum(sys.getsizeof(x) for x in amostra)
    mb = (qtd * tamanho_tupla) / (1024 ** 2)
    return qtd, mb