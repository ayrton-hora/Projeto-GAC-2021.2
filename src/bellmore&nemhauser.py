import os, re, sys, time

# Busca em Largura Local
def LBFS(N, M, Hi):
	# Busca o número do nó atual
	self_pos = M.index(Hi)

	# Define um valor infinito máximo
	closest = sys.maxsize

	# Percorre os vizinhos locais e define o mais próximo
	for value in Hi:
		if value != self_pos and value < closest:
			closest = value
	
	return M[closest]

# Algoritmo de Bellmore&Nemhauser
def bellmore_and_nemhauser(N, M):
	"""
	Ler G = (N, M)
	Escolher um vértice inicial hi e inclui-lo em H ← {hi}
	Enquanto |H| < n Fazer
		Encontrar o vértice hk ∉ H mais próximo de hi
		Inserir o vértice hk após hi em H (o seu vizinho mais próximo)
		i ← k
	Fim_Enquanto
	"""

	# Vizinhos mais próximos
	neighborhood = []
	
	# Nó inicial
	current_node = M[0]
	
	# Adicionando o nó inicial à relação de vizinhança
	neighborhood.append(current_node)

	# Encontrando os vizinhos mais próximos
	while len(neighborhood) < N:
		# Busca em largura local
		closest_node = LBFS(N, M, current_node) 
		
		# Verifica se o vizinho está presente no grafo e busca sua posição
		neighbor = M.index(closest_node)

		# Caso ele ainda não faça parte da relação e o passo anterior seja bem sucedido,
		# Adiciona o vizinho mais próximo ao final da relação

		if (closest_node not in neighborhood) and (isinstance(neighbor, int)): 
			neighborhood.append(closest_node)
		
		# Alterando a referência e buscando o vizinho subsequente
		current_node = closest_node 
	
	return neighborhood

# Main

# Medindo o tempo de execução
start_time = time.time()

# Buscando o caminho atual
currentPath = os.path.dirname(os.path.realpath(__file__))

# Realizando a leitura do arquivo de teste
file = open(currentPath[:-3] + "tests\\five.txt", "r")
file_data = file.readlines()

# Determinando a quantidade de nós
num_nodes = len(file_data)

# Filtragem da entrada e criação da matriz de valores
filtred_data = []
for line in range(len(file_data)):
	filtred_line = re.sub("\n$", "", file_data[line])
	splitted_line = filtred_line.split(" ")
	column = 0
	elements = []
	for value in splitted_line:
		if value != "":
			value = float(value)
			elements.append(int(value))
			column += 1

	filtred_data.append(elements)

neighborhood = bellmore_and_nemhauser(num_nodes, filtred_data)
print(neighborhood)

# Tempo final de execução
final_time = time.time()
total_time = final_time - start_time
print("Tempo de execução: %.3f ms" %total_time)