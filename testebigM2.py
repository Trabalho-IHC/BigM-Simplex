import funcoes

matriz = []
matriz.append([1,0,1,0,0,4])
matriz.append([0,2,0,1,0,12])
matriz.append([3,2,0,0,1,18])
matriz.append([-3,-5,0,0,99999,0])

L = 4
C = 6

funcoes.show_matriz(L, matriz)

funcoes.zera_var_artific_linha_z(L, C, matriz)

funcoes.show_matriz(L, matriz)

funcoes.escalonamento(L, C, matriz)

funcoes.show_matriz(L, matriz)

funcoes.escalonamento(L, C, matriz)

funcoes.show_matriz(L, matriz)

funcoes.escalonamento(L, C, matriz)

funcoes.show_matriz(L, matriz)

funcoes.retorna_z(L, matriz)
