import funcoes


matriz = []
matriz.append([2,1,1,0,0,5000])
matriz.append([4,5,0,-1,1,13000])
matriz.append([3,7,0,0,999999,0])
L = 3
C = 6

funcoes.show_matriz(L, matriz)

funcoes.zera_var_artific_linha_z(L, C, matriz)

funcoes.show_matriz(L, matriz)

funcoes.escalonamento(L, C, matriz)

funcoes.show_matriz(L, matriz)

funcoes.escalonamento(L, C, matriz)

funcoes.show_matriz(L, matriz)

funcoes.retorna_z(L, matriz)
