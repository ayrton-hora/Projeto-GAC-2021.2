import os, re, sys, time

# Função auxiliar para encontrar o menor vizinho de um dado nó
def minKey(N, keys, visited):
	min_value = sys.maxsize

	for i in range(N):
		if (keys[i] < min_value) and (not visited[i]):
			min_value = keys[i]
			min_index = i
	
	return min_index

# Algoritmo de Prim
# Implementação base utilizada anteriormente na disciplina
# Algoritmo sofreu pequenas alterações
# Refência base: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/?ref=gcse
def prim(N, M):
	keys = [sys.maxsize] * N
	keys[0] = 0
	
	minimum_relation = [None] * N
	minimum_relation[0] = -1
	
	shortest_distances = [False] * N
	for n in range(N):

		minimum = minKey(N, keys, shortest_distances)
		shortest_distances[minimum] = True

		for m in range(N):

			if (M[minimum][m] > 0) and (shortest_distances[m] == False) and (keys[m] > M[minimum][m]):
				keys[m] = M[minimum][m]
				minimum_relation[m] = minimum

	minimum_tree = []
	for count in range(N):
		minimum_tree.append([None] * N)

	for label in range(1, N):
		minimum_tree[minimum_relation[label]][label] = M[label][minimum_relation[label]]

	# Árvore geradora mínima
	return minimum_tree

# Algoritmo para construir o ciclo euleriano baseado na árvore geradora mínima
def euler_cycle(N, M, G):
	# Dobrando as arestas
	for i in range(N):
		for j in range(N):
			if (G[i][j] is not None):
				G[j][i] = G[i][j]
	
	# Gerando relação com os vértices
	nodes = N
	
	# Definindo o melhor ciclo (custo mínimo) com base na árvore geradora mínima
	i, j = 0, 0
	
	# Ciclo mínimo partindo do primeiro vértice
	min_cycle = [0]

	# Relação dos vértices visitados
	visited = [False] * N

	# Variável de controle (back-tracking)
	stuck = False
	while nodes > 0:

		# O menor valor do loop atual
		current = [sys.maxsize, 0]

		for j in range(N):
			
			# Caso fique preso no loop, sem referência de retorno, retorne ao vértice inicial
			if stuck:
				i = 0
				stuck = False

			# Caso não tenha sido visitado, não for nulo (na árvore geradora mínima) e for menor que o valor anterior, atualiza os valores
			if (G[i][j] is not None) and (not visited[j]) and (G[i][j] < current[0]):
				current[0] = G[i][j]
				current[1] = j
		
		# Caso tenha encontrado um menor valor
		if (current != [sys.maxsize, 0]):
			# Adiciona o menor valor ao ciclo
			min_cycle.append(current[1])
			
			# Marca como visitado
			visited[current[1]] = True 
			
			# Coleta o peso da aresta
			i = current[1]
		
			# Atualizando as variáveis de controle
			nodes -= 1

		# Realiza Back-tracking achando um próximo possível valor na hierarquia (regressivamente)
		else:
			i = j
			stuck = True
	
	# Filtragem do ciclo encontrado, remove os vértices duplicados, gerando apenas os atalhos
	visited = []
	final_cycle = []
	for step in min_cycle:
		if step not in visited:
			final_cycle.append(step)
			visited.append(step)
	
	# Adiciona o primeiro nó para fechar o ciclo
	final_cycle.append(final_cycle[0])

	# Retorna o ciclo euleriano
	return final_cycle

# Heurística Twice-Around
def twice_around(N, M):
	"""
	Ler G = (N, M)
	H ← ∅ # H o ciclo hamiltoniano
	Determinar T uma árvore geradora mínima de G
	Dobrar as arestas de T e construir um ciclo euleriano L = {li} , li ∈ N, em T
	Enquanto L ≠ ∅ Fazer # Etapa Twice-Around – TW
		Escolher sequencialmente lk ∈ L
		Se lk ∉ H então H ← H U {lk} 
		L ← L\{hk}
	Fim_Enquanto
	"""
	# Ciclo Hamiltoniano
	hamilton_cycle = []

	# Encontrar a árvore geradora mínima pelo algoritmo de Prim
	minimum_tree = prim(N, M)

	# Dobrar as arestas e constrói o ciclo euleriano
	euleriam_cycle = euler_cycle(N, M, minimum_tree)

	# Etapa Twice-Around
	for node in euleriam_cycle:
		if node not in hamilton_cycle:
			hamilton_cycle.append(node)

	# Retorna o ciclo hamiltoniano
	return hamilton_cycle

# Main
# Medindo o tempo de execução
start_time = time.time()

# Buscando o caminho atual
currentPath = os.path.dirname(os.path.realpath(__file__))

# Realizando a leitura do arquivo de teste
file_name = str(input("Insira o nome do arquivo: "))
file = open(currentPath[:-3] + "tests\\" + file_name, "r")
# file = open(currentPath[:-3] + "tests\\five.txt", "r")
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

hamilton_cycle = twice_around(num_nodes, filtred_data)
print("Ciclo Hamiltoniano:")
print(hamilton_cycle)

# Tempo final de execução
final_time = time.time()
total_time = final_time - start_time
print("Tempo de execução: %.3f ms" %total_time)
