import time
import math
import tracemalloc
from utils import gerar_combinacoes, estimar_memoria_materializada

def processar_conjunto(p):
    # 1. Inicia a medição de memória
    tracemalloc.start()
    
    # Valida cardinalidade esperada
    card_esperada = math.comb(25, p)
    print(f"\n{'='*50}\nS_{p} | C(25,{p}) = {card_esperada:,}")

    _, mb_estimado = estimar_memoria_materializada(25, p)
    print(f"RAM estimada (se lista): ~{mb_estimado:,.1f} MB")

    inicio = time.time()
    
    # 2. MATERIALIZAÇÃO: Força o gerador a virar uma lista real na RAM
    todas_as_combinacoes = list(gerar_combinacoes(25, p))
    contador = len(todas_as_combinacoes)
    
    tempo = time.time() - inicio
    print(f"Total gerado: {contador:,} | Tempo: {tempo:.4f}s")

    # 3. Coleta os dados de consumo de memória
    atual, pico = tracemalloc.get_traced_memory()
    
    ram_atual_mb = atual / (1024 * 1024)
    ram_pico_mb = pico / (1024 * 1024)
    
    print(f"RAM atual: {ram_atual_mb:.2f} MB; RAM pico: {ram_pico_mb:.2f} MB")    
    
    # 4. Finaliza o monitoramento e limpa a lista para liberar espaço para o próximo loop
    del todas_as_combinacoes
    tracemalloc.stop()

    return contador, tempo
    
if __name__ == "__main__":
    # Rodando do menor para o maior pico de combinações
    tamanhos = [15, 14, 13, 12, 11]
    resultados = [processar_conjunto(p) for p in tamanhos]