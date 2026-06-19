from itertools import combinations
from utils import gerar_combinacoes  # importa do programa1.py

def resolver_cobertura_14():
    # algoritmo guloso para cobertura de S_14 com S_15.
  
    print("Iniciando Programa 2: Cobertura de 14 elementos...")
    
    # 1. definir o conjunto alvo (todas as combinações de 14)
    # usamos set para busca rápida (O(1))
    alvo = set(gerar_combinacoes(25, 14))
    coberto = set()
    sb_15_14 = [] # subconjunto de cobertura
    
    # 2. algoritmo guloso
    # iteramos sobre S_15
    for combo_15 in gerar_combinacoes(25, 15):
        # gera todas as sub-combinações de 14 dentro desta de 15
        sub_14 = set(combinations(combo_15, 14))
        
        # se essa combo de 15 cobre algo que ainda não foi coberto
        if not sub_14.issubset(coberto):
            sb_15_14.append(combo_15)
            coberto.update(sub_14)
            
        # critério de parada: se cobrimos tudo, para
        if len(coberto) == len(alvo):
            break
            
    print(f"Cobertura concluída!")
    print(f"Tamanho do subconjunto SB_15_14: {len(sb_15_14)}")
    return sb_15_14

if __name__ == "__main__":
    resolver_cobertura_14()