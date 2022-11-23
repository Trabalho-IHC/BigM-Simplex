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


# #ARRUMAR 
# def escalonamento():
#     linha_pivo = funcoes.linha_pivo(L, C, matriz)
#     coluna_pivo = funcoes.calc_coluna_pivo(C, matriz)
#     # matriz_antiga = []
#     # matriz_antiga = matriz
#     for l in range(0, L):
#         if l == linha_pivo:
#             for c in range(0, C):
#                 matriz[l][c] = matriz[l][c] / matriz[l][coluna_pivo] 

#     for l in range(0, L):
#         if l != linha_pivo:
#             for c in range(0, C):
#                 print("antes da operacao ", matriz[l][c])
#                 print("matriz[l][coluna_pivo] ", matriz[l][coluna_pivo])
#                 print("matriz[linha_pivo()][calc_coluna_pivo()]", matriz[funcoes.linha_pivo(L, C, matriz)][funcoes.calc_coluna_pivo(C, matriz)])
#                 matriz[l][c] = matriz[l][c] - matriz[l][coluna_pivo] * matriz[funcoes.linha_pivo(L, C, matriz)][funcoes.calc_coluna_pivo(C, matriz)]
#                 print("depois da operacao ", matriz[l][c])
#                 print("-------------------")   
#     return matriz  

# escalonamento()
#funcoes.show_matriz(L, C, matriz)

