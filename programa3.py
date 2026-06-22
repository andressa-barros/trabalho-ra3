import time
from utils import gerar_combinacoes
from itertools import combinations

def resolver_cobertura(p_alvo, p_fonte=15):
    print(f"Iniciando Cobertura de {p_alvo} elementos com {p_fonte}...")

    # "Caderninho" rápido que anota as combinações que já resolvemos
    combinacoes_ja_cobertas = set()
    
    # A lista onde vamos guardar a resposta final do trabalho
    subconjunto_cobertura = []
    
    # Todos os números que podemos usar no trabalho (1 até 25)
    universo = set(range(1, 26))

    # Pega uma combinação de tamanho 13 por vez, sem travar o PC
    for combo_alvo in gerar_combinacoes(25, p_alvo):

        # Se a gente já resolveu essa combinação antes, pula para a próxima!
        if combo_alvo in combinacoes_ja_cobertas:
            continue

        # Pega os 13 números que o loop entregou agora
        elementos_y = set(combo_alvo)
        
        # Vê quais números de 1 a 25 NÃO estão nesses 13
        elementos_disponiveis = universo - elementos_y
        
        # Calcula quantos números faltam para chegar a 15 (neste caso, faltam 2)
        qtd_faltante = p_fonte - p_alvo
        
        # Pega os 2 primeiros números que estão sobrando para usar
        elementos_adicionais = list(elementos_disponiveis)[:qtd_faltante]

        # Junta os 13 números originais com os 2 novos, criando nossa combinação de 15!
        novo_x = tuple(sorted(list(elementos_y) + elementos_adicionais))
        
        # Guarda essa nova combinação de 15 na nossa resposta final
        subconjunto_cobertura.append(novo_x)

        # O segredo da velocidade:
        # Essa combinação de 15 que criamos resolve várias outras combinações de 13.
        # Nós geramos todas elas aqui e anotamos no "caderninho" para pular no futuro.
        for sub_combo in combinations(novo_x, p_alvo):
            combinacoes_ja_cobertas.add(sub_combo)

    # Avisa quantas combinações de 15 a gente precisou criar no total
    print(f"Tamanho final do SB_{p_fonte},{p_alvo}: {len(subconjunto_cobertura)}")
    
    # Entrega a resposta final
    return subconjunto_cobertura

if __name__ == "__main__":
    inicio = time.time()

    resultado_programa3 = resolver_cobertura(13)
    
    tempo_total = time.time() - inicio
    print(f"Tempo de execução do Programa 3: {tempo_total:.4f}s")