import os, re, sys, time

# Função para retornar o próximo menor vértice a ser inserido no ciclo
def vertice_mais_proximo(N, M, H):
    # Vetor para computar o vértice menos distante e sua distância
    closest_vertex = [sys.maxsize, -1]
    
    # Para cada um dos vértices presentes no ciclo, compute que atende ao requisito
    for i in range(len(H)):

        for j in range(N):
            
            # Caso a posição (vértice) não seja a diagonal, ainda não esteja no ciclo
            # e seja a menor possível, salve os valores (vértice e peso)
            if (i != j) and (j not in H) and (M[i][j] < closest_vertex[0]):
                closest_vertex[0] = M[i][j]
                closest_vertex[1] = j

    # Caso encontre o vértice menos distante
    if closest_vertex != [sys.maxsize, -1]:
        return closest_vertex

    # Caso contrário, erro
    else:
        raise Exception("Não foi possível computar o próximo vértice menos distante.")

# Função para retornar o par de vértices (i e i + 1) onde o novo vértice será inserido
def aresta_minima(N, M, H, C):
    # Vetor com o primeiro menor peso e seu vértice relacionado, vindo da etapa passada
    fst_minimum = [C[0], M[C[1]].index(C[0])]

    # Vetor para armazenar o par de vértice i e i + 1
    pair_to_insert = [-1, -1]

    # Variável para armazenar o custo mínimo
    minimun_cost = sys.maxsize

    # Percorre todos o vértices, verificando todas as possibilidades de pares sequencias, para aqueles que pertencem ao ciclo
    for i in range(len(H)):

        if i in H:

            for j in range(len(H)):
                
                # Verifica se os vértices pertencem ao ciclo, se não correspondem à diagonal
                # e se são consecutivos
                if (i != j) and (j in H) and (j == i + 1):
                   current_minimum =  M[i][C[1]] + M[j][C[1]] - M[i][j]

                   if current_minimum < minimun_cost:
                       minimun_cost = current_minimum
                       pair_to_insert[0] = i
                       pair_to_insert[1] = j

    if minimun_cost != sys.maxsize and pair_to_insert != [-1, -1]:
        return pair_to_insert

    else:
        return [-1, -1]

# Função reponsável pela inserção do novo vértice entre o par (i e i + 1)
def insere_aresta_1(N, M, H, V, P):
    # Novo ciclo atualizado a ser construído
    updated_cycle = []

    # Percorre o ciclo antigo, adicionando os valores
    for k in H:

        # Caso encontre o primeiro vértice (i), adicione-o, seguido do novo vértice a ser inserido
        if k == P[0]:
            updated_cycle.append(k)
            updated_cycle.append(V[1])

        # Caso contrário, continue adicionando
        else:
            updated_cycle.append(k)

    return updated_cycle

# Heurística Insere-Vértice-1 ou Cheapest Insertion
def insere_vertice_1(N, M):
    """
    Ler G = (N, M)
    Iniciar por um ciclo de vértices H
    Enquanto não for formado um ciclo hamiltoniano Fazer
        Encontrar o vértice k ∉ H, mais próximo/mais distante de qualquer dos vértices de H.
        Encontrar a aresta (i, i + 1) tal que Minimize {cik + ck i +1 – ci i + 1}
        Inserir o vértice k em H entre os vértices i e i + 1
    Fim_Enquanto
    """
    # Ciclo Hamiltoniano
    hamilton_cycle = []

    # Iniciando um ciclo
    for v in range(3):
        hamilton_cycle.append(v)

    # Enquanto o ciclo completo não for hamiltoniano
    while len(hamilton_cycle) < N:

        next_vertex = vertice_mais_proximo(N, M, hamilton_cycle)

        minimum_edge = aresta_minima(N, M, hamilton_cycle, next_vertex)

        hamilton_cycle = insere_aresta_1(N, M, hamilton_cycle, next_vertex, minimum_edge)

    return hamilton_cycle

# Main
# Medindo o tempo de execução
start_time = time.time()

# Buscando o caminho atual
currentPath = os.path.dirname(os.path.realpath(__file__))

# Realizando a leitura do arquivo de teste
file_name = str(input("Insira o nome do arquivo: "))
file = open(currentPath[:-3] + "tests\\" + file_name, "r")
file_data = file.readlines()

# Determinando a quantidade de nós
num_nodes = len(file_data)

# Filtragem da entrada e criação da matriz de valores
filtred_data = []
for line in range(len(file_data)):
	filtred_line = re.sub("\n$", "", file_data[line])
	splitted_line = re.split("\s+", filtred_line)
	column = 0
	elements = []
	for value in splitted_line:
		if value != "":
			value = float(value)
			elements.append(int(value))
			column += 1

	filtred_data.append(elements)

hamilton_cycle = insere_vertice_1(num_nodes, filtred_data)
print("Ciclo Hamiltoniano:")
print(hamilton_cycle)
print(f"Número de vértices: {len(hamilton_cycle)}")

# Tempo final de execução
final_time = time.time()
total_time = final_time - start_time
print("Tempo de execução: %.3f ms" %total_time)
