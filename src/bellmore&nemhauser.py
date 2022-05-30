# import os, re, sys, time
import re

"""
Ler G = (N, M)
Escolher um vértice inicial hi e inclui-lo em H ← {hi}
Enquanto |H| < n Fazer
	Encontrar o vértice hk ∉ H mais próximo de hi
	Inserir o vértice hk após hi em H (o seu vizinho mais próximo)
	i ← k
Fim_Enquanto
"""

def bellmore_and_nemhauser():
	print()


# Main
file = open("../tests/five.txt", "r")
file_data = file.readlines()

# filtred_data = []
# for line in range(len(file_data)):
# 	print(file_data[line], end="\n")
# 	# filtred_data[line] = re.sub("\n$", "", file_data[line])

num_nodes = 0
for value in file_data[0].split(" "):
	num_nodes += 1

print(num_nodes)