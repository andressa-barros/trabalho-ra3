import time
from utils import gerar_combinacoes
from itertools import combinations

def resolver_cobertura_p4(p_alvo=12, p_fonte=15):
    print(f"Iniciando Cobertura de {p_alvo} elementos com {p_fonte}...")
#mesma coisa do Programa 3, mas adaptada para alvo de 12 elementos (faltam 3 para completar 15)
#o resto igual
    combinacoes_ja_cobertas = set()
    
    subconjunto_cobertura = []
    
    universo = set(range(1, 26))

    for combo_alvo in gerar_combinacoes(25, p_alvo):

        if combo_alvo in combinacoes_ja_cobertas:
            continue

        elementos_y = set(combo_alvo)
        
        elementos_disponiveis = universo - elementos_y
        
        qtd_faltante = p_fonte - p_alvo
        
        elementos_adicionais = sorted(list(elementos_disponiveis))[:qtd_faltante]

        novo_x = tuple(sorted(list(elementos_y) + elementos_adicionais))
        
        subconjunto_cobertura.append(novo_x)

        for sub_combo in combinations(novo_x, p_alvo):
            combinacoes_ja_cobertas.add(sub_combo)

    print(f"Tamanho final do SB_{p_fonte},{p_alvo}: {len(subconjunto_cobertura)}")
    
    return subconjunto_cobertura

if __name__ == "__main__":
    inicio = time.time()

    resultado_programa4 = resolver_cobertura_p4(12)
    
    tempo_total = time.time() - inicio
    print(f"Tempo de execução do Programa 4: {tempo_total:.4f}s")