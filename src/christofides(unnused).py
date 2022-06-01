"""
Ler G = (N, M)
H ←∅ 	# H o ciclo hamiltoniano
Determine T = (N,MT) uma árvore geradora mínima de G
Defi na G0 = (N0,M0) onde N0 é o conjunto de vértices de T que possuem grau ímpar
e M0 ={(i,j) ∈ M | i,j ∈ N0}
Determine E* o 1-matching perfeito mínimo em G0
Faça G´ = (N,MT ∪ E*)
Determine um ciclo euleriano L em G´
H ← TW(L)
Imprimir H
"""