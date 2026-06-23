# Trabalho RA3 - Análise de Complexidade e Cobertura de Combinações

Este repositório contém a implementação dos programas solicitados para o trabalho prático da disciplina de **Complexidade de Algoritmos (PUC)**, abordando a geração de combinações do universo $U = \{1, 2, ..., 25\}$ e a busca por subconjuntos de cobertura ótimos $SB_{15, p} \subseteq S_{15}$ para cobrir todas as combinações de tamanho $p \in \{14, 13, 12, 11\}$.

---

## 1. Modelagem do Problema e Estratégia Algorítmica

O problema consiste em determinar um subconjunto de combinações de 15 elementos ($SB_{15, p}$) que cubra todas as combinações possíveis de tamanho $p$ do universo $U$ de 25 elementos. 
Diz-se que uma combinação $Y$ (de tamanho $p$) está coberta por $X$ (de tamanho 15) se $Y \subseteq X$.

A estratégia algorítmica adotada nos Programas 2, 3, 4 e 5 é um **Algoritmo Guloso (Greedy)** sistemático:
1. Iteramos por todas as combinações $Y \in S_p$ em ordem lexicográfica.
2. Mantemos um conjunto de controle (`combinacoes_ja_cobertas`) para registrar quais subconjuntos de tamanho $p$ já foram cobertos.
3. Se $Y$ não estiver coberto:
   - Completamos $Y$ de forma determinística adicionando os menores elementos disponíveis em $U \setminus Y$ até atingir o tamanho 15, formando o conjunto $X$.
   - Adicionamos $X$ à nossa solução de cobertura ($SB_{15, p}$).
   - Geramos todas as $\binom{15}{p}$ combinações de tamanho $p$ contidas em $X$ e as marcamos como cobertas no conjunto de controle.

---

## 2. Análise de Complexidade Assintótica

Sejam as seguintes variáveis que definem o tamanho do problema:
* $n = 25$ (tamanho do universo $U$)
* $p \in \{11, 12, 13, 14\}$ (tamanho da combinação alvo)
* $k = 15$ (tamanho do conjunto de cobertura)
* $N_p = \binom{n}{p}$ (número total de combinações alvo)
* $S_B = |SB_{15, p}|$ (tamanho final do conjunto de cobertura obtido)

### A. Complexidade de Tempo

Para cada uma das $N_p$ combinações geradas, realizamos uma verificação de pertinência no conjunto de controle (`combo_alvo in combinacoes_ja_cobertas`).
* Em Python, a busca em uma tabela hash (`set`) tem complexidade de tempo médio de $O(p)$ (necessário para calcular o hash da tupla de tamanho $p$).
* Se a combinação **não** estiver coberta (o que ocorre exatamente $S_B$ vezes), realizamos as seguintes operações:
  1. Diferença de conjuntos: $U \setminus Y$, custando $O(n)$ operações.
  2. Ordenação dos elementos disponíveis e junção: $O(n \log n + k \log k)$.
  3. Geração de todas as combinações de tamanho $p$ contidas no conjunto de cobertura de tamanho $k$: existem exatamente $\binom{k}{p}$ sub-combinações.
  4. Inserção de cada sub-combinação na tabela hash de controle: cada inserção custa em média $O(p)$ para calcular o hash e armazenar. Portanto, o custo desta etapa é $\Theta\left(\binom{k}{p} \cdot p\right)$.

A complexidade de tempo total do algoritmo é a soma do custo das verificações para todas as combinações com o custo das etapas de inserção executadas $S_B$ vezes:

$$T(n, p, k) = \Theta\left( \binom{n}{p} \cdot p + S_B \cdot \left( n \log n + k \log k + \binom{k}{p} \cdot p \right) \right)$$

Como $n = 25$ e $k = 15$ são constantes fixas no projeto, a complexidade de tempo é dominada pelo tamanho do espaço de busca $N_p = \binom{25}{p}$ e pelo número de marcações redundantes no conjunto:

$$T(p) = \Theta\left( \binom{25}{p} \cdot p + S_B \cdot \binom{15}{p} \cdot p \right)$$

### B. Complexidade de Espaço

O consumo de memória do algoritmo é dominado por duas estruturas:
1. A tabela hash de controle `combinacoes_ja_cobertas`, que no pior caso armazena todas as $N_p$ combinações de tamanho $p$. Cada combinação é uma tupla contendo $p$ inteiros.
2. A lista de saída `subconjunto_cobertura` contendo $S_B$ tuplas de tamanho $k = 15$.

Portanto, a complexidade de espaço é:

$$S(n, p, k) = \Theta\left( \binom{n}{p} \cdot p + S_B \cdot k \right)$$

Para $p = 12$, onde $\binom{25}{12} = 5.200.300$, armazenar essas tuplas em memória em Python gera um consumo real medido de aproximadamente **2,3 GB a 2,5 GB** de RAM, representando o limite físico do uso de memória de estruturas de alto nível (tuplas + sets) na linguagem.

---

## 3. Principais Gargalos Computacionais

1. **Custo de Alocação de Objetos em Python**: O Python possui um alto overhead para cada objeto alocado (uma tupla de tamanho 12 consome muito mais do que apenas 12 inteiros na memória devido a metadados do interpretador). Alocar e desalocar milhões de tuplas gera gargalos severos de coleta de lixo (Garbage Collection) e paginação de memória.
2. **Hashing de Tuplas**: Calcular repetidamente a função de hash para milhões de tuplas em loops de alta frequência satura a CPU com operações aritméticas simples de conversão de tipos.
3. **Redundância de Cobertura**: Como o algoritmo escolhe elementos de forma puramente gulosa na ordem lexicográfica, à medida que a busca avança, muitos dos subconjuntos de tamanho $p$ gerados por $X$ já foram marcados anteriormente. Isso causa uma grande quantidade de inserções redundantes e ineficientes no `set` de controle.

---

## 4. Análise de Escalabilidade e o Desafio Adicional

A solução base proposta não escala bem se aumentarmos o tamanho do universo $U$. Se aumentarmos $n$ de 25 para 30, o número de combinações de tamanho 15 salta de $3.268.760$ para $155.117.520$ (um aumento de **47 vezes**), inviabilizando o armazenamento de conjuntos em memória RAM convencional no interpretador Python padrão.

### Estratégia Otimizada: Combinatorial Number System (Combinadics)

Como resposta ao **Desafio Adicional**, uma alternativa de altíssimo desempenho consiste em eliminar o uso de tuplas e tabelas hash (`set`).

Cada combinação ordenada de tamanho $p$ de um universo $n$ pode ser mapeada de forma bijetiva (1 para 1) para um índice numérico único (Rank) no intervalo $[0, \binom{n}{p}-1]$ através da fórmula do sistema numérico combinatorial:

$$\text{Rank}(x_1, x_2, ..., x_p) = \sum_{i=1}^{p} \binom{x_i - 1}{i}$$

#### Vantagens da Estratégia Otimizada:
* **Uso de Memória Reduzido a $O(1)$ por Combinação**: Em vez de armazenar tuplas pesadas em um `set`, mantemos um `bytearray` de tamanho $\binom{n}{p}$ onde cada byte representa se a combinação daquele índice está coberta (0 ou 1). Para $p=12$, o uso de memória cai de **2,3 GB para apenas 4,96 MB** (uma redução de quase 500x).
* **Velocidade Aumentada (C-Level Access)**: Verificar e marcar se uma combinação está coberta se torna uma indexação direta de array contíguo em memória ($\Theta(1)$ real e de baixíssimo nível), eliminando a necessidade de hashing de tuplas.

---

## 5. Comparativo de Resultados e Desempenho

A tabela abaixo sumariza as cardinalidades teóricas e os dados empíricos observados durante a execução dos algoritmos da solução proposta:

| Programa | Alvo ($p$) | Cardinalidade $\lvert S_p \rvert$ | Tamanho da Cobertura $\lvert SB_{15,p} \rvert$ | Tempo de Execução (s) | RAM Estimada (se materializado) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Programa 1** | Todos | - | - | 1.1s (total) | - |
| **Programa 2** | 14 | 4.457.400 | 1.961.256 | 16.8s | ~2,3 GB |
| **Programa 3** | 13 | 5.200.300 | 1.144.066 | 45.4s | ~2,5 GB |
| **Programa 4** | 12 | 5.200.300 | 646.646 | 93.3s | ~2,3 GB |
| **Programa 5** | 11 | 4.457.400 | 352.716 | 138.1s | ~1,8 GB |

### Discussão dos Resultados de Cobertura
Uma combinação de tamanho 15 contém exatamente $\binom{15}{p}$ subconjuntos de tamanho $p$. 
* Para $p=14$, o limite teórico mínimo de conjuntos de cobertura é $\lceil 4.457.400 / 15 \rceil = 297.160$. O algoritmo guloso obteve $1.961.256$ conjuntos de cobertura.
* A diferença entre o obtido e o mínimo teórico aumenta conforme $p$ diminui. Isso ocorre porque a busca gulosa lexicográfica simples sofre do efeito de agrupamento (clustering) nos primeiros elementos do universo, cobrindo repetidamente as mesmas combinações. 
* Para otimizar o tamanho de $SB_{15, p}$ (reduzir a quantidade de conjuntos de 15), técnicas de **Programação Inteira** ou metaheurísticas (como **Algoritmos Genéticos** ou **Simulated Annealing**) seriam necessárias para explorar o espaço de coberturas de forma não sequencial.