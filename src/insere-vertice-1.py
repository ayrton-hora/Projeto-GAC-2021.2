import os, re, sys, time

def insere_vertice_1(N, M):
    """
    Ler G = (N, M)
    Iniciar por um ciclo de vértices H
    Enquanto não for formado um ciclo hamiltoniano Fazer
    Encontrar o vértice k ∉ H, mais próximo / mais distante de qualquer dos vértices de H.
    Encontrar a aresta (i, i + 1) tal que Minimize {cik + ck i +1 – ci i + 1}
    Inserir o vértice k em H entre os vértices i e i + 1
    Fim_Enquanto
    """
    print()

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
