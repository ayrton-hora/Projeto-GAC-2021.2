"""
Ler G = (N, M)
H ← ∅ 			# H o ciclo hamiltoniano
Determinar T uma árvore geradora mínima de G
Dobrar as arestas de T e construir um ciclo euleriano L = {li} , li ∈ N, em T
Enquanto L ≠ ∅ Fazer # Etapa Twice-Around – TW
	Escolher sequencialmente lk ∈ L
	Se lk ∉ H então H ← H ∪ {lk} 
	L ← L\{hk}
Fim_Enquanto
"""