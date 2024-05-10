# Autoria: 
# Marianna Oteri - 2024


from queue import PriorityQueue

# Representação do grafo
grafo = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Efori': 86},
    'Efori': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Neamt': {'Iasi': 87}
}

# Distância em linha reta de cada cidade até Bucharest
heuristica = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


fila_de_prioridade = PriorityQueue()  # Inicializa a fila de prioridade 

# Função de estimativa de custo (heurística)
def custo_estimado_heuristica(no, destino):
    return heuristica[no]

def busca_a_estrela(inicio, destino):
    fila_de_prioridade.put((0, inicio))  # Insere a cidade inicial na fila com prioridade 0
    veio_de = {}  # Dicionário para armazenar o nó anterior de cada nó no caminho
    custo_atual = {}  # Dicionário para armazenar o custo acumulado até cada nó
    veio_de[inicio] = None  # O nó inicial não tem nó anterior
    custo_atual[inicio] = 0  # O custo até o nó inicial é 0
    
    while not fila_de_prioridade.empty():  # Enquanto a fila de prioridade não estiver vazia
        custo_atual_iteracao, no_atual = fila_de_prioridade.get()  # Obtém o nó com o menor custo da fila
        
        if no_atual == destino:  # Se o nó atual for o destino, retorna o caminho
            caminho = []
            while no_atual is not None:  # Reconstrói o caminho percorrendo os nós anteriores
                caminho.append(no_atual)
                no_atual = veio_de[no_atual]
            return caminho[::-1]  # Inverte o caminho e retorna
        
        for vizinho, custo in grafo[no_atual].items():  # Para cada vizinho do nó atual
            custo_novo = custo_atual[no_atual] + custo  # Calcula o novo custo até o vizinho
            if vizinho not in custo_atual or custo_novo < custo_atual[vizinho]:  # Se é um novo nó ou um caminho mais curto
                custo_atual[vizinho] = custo_novo  # Atualiza o custo acumulado até o vizinho
                prioridade = custo_novo + custo_estimado_heuristica(vizinho, destino)  # Calcula a prioridade do vizinho (custo acumulado + estimativa heurística)
                fila_de_prioridade.put((prioridade, vizinho))  # Adiciona o vizinho na fila de prioridade
                veio_de[vizinho] = no_atual  # Registra o nó atual como o anterior do vizinho
    
    return None  # Se não houver caminho até o destino, retorna None


def busca_gulosa(inicio, destino):
    # Inicialização das estruturas de dados
    fila_de_prioridade.put((heuristica[inicio], inicio))  # Adiciona o nó inicial à fila com sua heurística como prioridade
    nos_explorados = set()  # Conjunto para armazenar nós já explorados
    caminho = []  # Lista para armazenar o caminho do nó inicial ao objetivo

    while not fila_de_prioridade.empty():
        no_atual = fila_de_prioridade.get()[1]  # Obtém o nó com a menor heurística da fila

        if no_atual == destino:  # Verifica se o nó atual é o objetivo
            caminho.append(no_atual)  # Adiciona o nó objetivo ao caminho
            return caminho  # Retorna o caminho encontrado

        nos_explorados.add(no_atual)  # Marca o nó atual como explorado
        caminho.append(no_atual)  # Adiciona o nó atual ao caminho

        # Explora os vizinhos do nó atual
        for vizinho in grafo[no_atual]:
            if vizinho not in nos_explorados:  # Verifica se o vizinho não foi explorado
                fila_de_prioridade.put((heuristica[vizinho], vizinho))  # Adiciona o vizinho à fila com sua heurística como prioridade
                nos_explorados.add(vizinho)  # Marca o vizinho como explorado
    return None  # Retorna None se não encontrar um caminho até o objetivo

# Teste do algoritmo
inicio = 'Arad'
destino = 'Bucharest'
resultado_a_estrela = busca_a_estrela(inicio, destino)
resultado_gulosa = busca_gulosa(inicio,destino)

if resultado_a_estrela:
    print(f' \n A*: \n Existe caminho de {inicio} até {destino}!')
    print(f'{resultado_a_estrela}\n')
else:
    print(f' \n A*: \n Não existe caminho de {inicio} até {destino}. \n ')

if resultado_gulosa: 
    print(f' \n Gulosa: \n Existe caminho de {inicio} até {destino}!')
    print(f'{resultado_gulosa}\n')
else:
    print(f' \n Gulosa: \n Não existe caminho de {inicio} até {destino}. \n ')