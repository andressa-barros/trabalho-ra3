from itertools import combinations

def gerar_combinacoes(n, p):
    # gera combinações de "p" elementos a partir de um universo de "n" elementos
    # utiliza um gerador (yield) para economizar memória RAM.

    universo = range(1, n + 1)

    # combinations retorna um iterador otimizado em C
    return combinations(universo, p)

def imprimir_cardinalidade(p):
    # valida se a cardinalidade bate com o enunciado
    n = 25
    import math
    card = math.comb(n, p)
    print(f"Gerando S_{p} (C(25, {p})) - Total esperado: {card:,}")