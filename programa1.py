import time
import math
from utils import gerar_combinacoes, estimar_memoria_materializada

def processar_conjunto(p):
    # valida cardinalidade, percorre S_p e mede tempo de execução.
    
    card_esperada = math.comb(25, p)
    print(f"\n{'='*50}\nS_{p} | C(25,{p}) = {card_esperada:,}")

    _, mb_estimado = estimar_memoria_materializada(25, p)
    print(f"RAM estimada (se lista): ~{mb_estimado:,.1f} MB")

    inicio = time.time()
    contador = 0
    for _ in gerar_combinacoes(25, p):
        contador += 1
    
    tempo = time.time() - inicio
    print(f"Total gerado: {contador:,} | Tempo: {tempo:.4f}s")
    return contador, tempo

if __name__ == "__main__":
    tamanhos = [15, 14, 13, 12, 11]
    resultados = [processar_conjunto(p) for p in tamanhos]