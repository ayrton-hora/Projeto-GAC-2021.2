import os, re, sys, time

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

def aresta_minima(N, M, H, C):
    # Vetor com o primeiro menor peso e seu vértice relacionado, vindo da etapa passada
    fst_minimum = [C[0], M[C[1]].index(C[0])]

    # Vetor para computar o próximo par (vértice aresta mínimo)
    next_minimum = [sys.maxsize, -1]

    # Encontrar o próximo par para todas as arestas do vértice encontrado na etapa passada
    for i in range(N):
        
        # Caso a posição (vértice) atual seja diferente da originada na etapa anterior,
        # seja diferente da diagonal, já pertença ao ciclo (relação i e i + 1), possua 
        # um valor mínimo (atendendo ao Minimize), salve os valores (vértice e peso)
        if (i != fst_minimum[1]) and (i != C[1]) and (i in H) and (M[C[1]][i] < next_minimum[0]):
            next_minimum[0] = M[C[1]][i]
            next_minimum[1] = i

    # Caso tenha sido encontrado o segundo par
    if next_minimum != [sys.maxsize, -1]:
        return [fst_minimum, next_minimum]

    # Erro
    else:
        raise Exception("Não foi possível computar a próxima inserção menos distante.")

def insere_aresta_1(N, M, V, H, P):
    # Novo ciclo atualizado a ser construído
    updated_cycle = [None] * (len(H) + 1)

    # Variável auxiliar
    target_pos = -1
    for i in range(N):

        # Verifica se existe uma posição entre os pares ou seja, entre i e i + 1
        if ((i > P[0][1]) and (i < P[1][1])) or ((i > P[1][1]) and (i < P[0][1])):
            target_pos = i

    # Caso a posição exista, atualize o ciclo
    if target_pos != -1:
        
        for i in range(target_pos, len(H)):
            updated_cycle[i + 1] = H[i]

        for j in range(target_pos - 1):
            updated_cycle[j] = H[j]
        
        updated_cycle[i] = V[1]

    # Caso não exista, crie um posição
    else:
        for i in range(target_pos):
            updated_cycle[i] = H[i]

        updated_cycle[target_pos] = V[1]

        for j in range(target_pos):
            updated_cycle[j + 1] = H[j]

    return updated_cycle


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
# file_name = str(input("Insira o nome do arquivo: "))
file = open(currentPath[:-3] + "tests\\five.txt", "r")
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

# Tempo final de execução
final_time = time.time()
total_time = final_time - start_time
print("Tempo de execução: %.3f ms" %total_time)
