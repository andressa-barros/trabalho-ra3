from itertools import combinations
from utils import gerar_combinacoes

def resolver_cobertura(p_alvo, p_fonte=15):
    print(f"Iniciando Cobertura de {p_alvo} elementos com {p_fonte}...")
    
    alvo = set(gerar_combinacoes(25, p_alvo))
    coberto = set()
    subconjunto_cobertura = []
    
    for combo in gerar_combinacoes(25, p_fonte):
        sub_alvos = set(combinations(combo, p_alvo))
        
        if not sub_alvos.issubset(coberto):
            subconjunto_cobertura.append(combo)
            coberto.update(sub_alvos)
            
        if len(coberto) == len(alvo):
            break
            
    print(f"Tamanho do SB_15_{p_alvo}: {len(subconjunto_cobertura)}")
    return subconjunto_cobertura

if __name__ == "__main__":
    resolver_cobertura(14)