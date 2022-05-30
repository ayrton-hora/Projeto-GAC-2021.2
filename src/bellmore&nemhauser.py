# import os, re, sys, time
import os, re


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
	current_node = M[0][0]
	
	# Adicionando o nó inicial à relação de vizinhança
	neighborhood.append(current_node)

	# Encontrando os vizinhos mais próximos
	while len(neighborhood) < N:
		closest_node = DFS(current_node) # Busca em largura
		
		neighborhood.append(closest_node) # Adicionando o vizinho mais próximo ao final da relação

		current_node = closest_node # Alterando a referência e buscando o vizinho subsequente
	
	return neighborhood


# Main
currentPath = os.path.dirname(os.path.realpath(__file__))
file = open(currentPath[:-3] + "tests\\five.txt", "r")
file_data = file.readlines()
num_nodes = len(file_data)

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

bellmore_and_nemhauser(num_nodes, filtred_data)
