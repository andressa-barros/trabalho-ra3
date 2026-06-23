import time
import tracemalloc
from utils import gerar_combinacoes
from itertools import combinations

def resolver_cobertura_p2(p_alvo=14, p_fonte=15):
    print(f"Iniciando Cobertura de {p_alvo} elementos com {p_fonte}...")
    
    # 1. Inicia a medição de memória
    tracemalloc.start()
    
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
    
    # 2. Coleta os dados de consumo de memória ANTES de limpar as estruturas
    atual, pico = tracemalloc.get_traced_memory()
    
    ram_atual_mb = atual / (1024 * 1024)
    ram_pico_mb = pico / (1024 * 1024)
    
    print(f"\n{'='*40}")
    print(f"RAM atual: {ram_atual_mb:.2f} MB; RAM pico: {ram_pico_mb:.2f} MB")    
    print(f"{'='*40}\n")

    # 3. Limpeza explícita para ajudar o Garbage Collector
    del combinacoes_ja_cobertas
    tracemalloc.stop()
    
    return subconjunto_cobertura

if __name__ == "__main__":
    inicio = time.time()

    resultado_programa2 = resolver_cobertura_p2(14)
    
    tempo_total = time.time() - inicio
    print(f"Tempo de execução do Programa 2: {tempo_total:.4f}s")
    