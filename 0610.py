#MATRIZ
import numpy as np

M = [[1, 3], [5, 6]]

#print(M[0][0]) #[0] se refere a linha e o [1] a coluna 

for i in [0, 1]:
    for j in [0, 1]:
        print(M[i][j])
        
#OUTRO MODO
for linha in range(len(M)): #range -> sequencia de elementos do 0 ao 1
    for coluna in range(len(M)):
        print(M[linha][coluna])

#SOMA DE MATRIZES
N = [[6, 7], [8, 9]]
S = [[0, 0], [0, 0]] #OUTRO MODO -> [[0 for in in range(len(M))] for j in range(len(M))]

for linha in range(len(M)): #range -> sequencia de elementos do 0 ao 1
    for coluna in range(len(M)):
        S[linha][coluna] = M[linha][coluna] + N[linha][coluna]
print(np.array(S))

