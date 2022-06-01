import os, re, sys, time

# Busca em Largura Local
def LBFS(N, M, Neighborhood, Hi, Hi_pos):
	# Define um valor infinito máximo para o peso
	closest = sys.maxsize

	# O índice da menor aresta encontrada
	closest_index = -1

	# Percorre os vizinhos locais e define o mais próximo
	for i in range(N):
		if (i != Hi_pos) and (i not in Neighborhood) and (Hi[i] < closest):
			closest = Hi[i]
			closest_index = i
	
	# Retorna o vizinho mais próximo e seu índice na matriz
	return M[closest_index], closest_index

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
	
	# Nó inicial e seu índie
	current_node = M[0]
	current_node_pos = 0
	
	# Adicionando o índice do nó inicial à relação de vizinhança
	neighborhood.append(current_node_pos)

	# Encontrando os vizinhos mais próximos
	while len(neighborhood) < N:
		# Busca em largura local
		closest_node, current_node_pos = LBFS(N, M, neighborhood, current_node, current_node_pos) 

		# Caso ele ainda não faça parte da relação e o passo anterior seja bem sucedido,
		# Adiciona o vizinho mais próximo ao final da relação
		if (current_node_pos != -1) and (current_node_pos not in neighborhood): 
			neighborhood.append(current_node_pos)
		
		# Alterando a referência e buscando o vizinho subsequente
		current_node = closest_node 
	
	return neighborhood

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

neighborhood = bellmore_and_nemhauser(num_nodes, filtred_data)
print("Vizinhos mais próximos:")
print(neighborhood)

# Tempo final de execução
final_time = time.time()
total_time = final_time - start_time
print("Tempo de execução: %.3f ms" %total_time)