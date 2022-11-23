import funcoes

# matriz = []
# L = int(input("Digite o número de linhas:"))
# C = int(input("Digite o número de colunas:"))
# for i in range(L):
#     matriz.append([])


# for l in range(0, L):
#     for c in range(0, C):
#         matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
matriz = []
matriz.append([[2],[1],[1],[0],[0],[5000]])
matriz.append([[4],[5],[0],[-1],[1],[13000]])
matriz.append([[3],[7],[0],[0],[999999],[0]])
L = 2
C = 5
for l in range(0, 3):
        print(matriz[l], end='\n')

#funcoes.show_matriz(L, C, matriz)

funcoes.zera_var_artific_linha_z(L, C, matriz)
for l in range(0, 3):
        print(matriz[l], end='\n')
#funcoes.show_matriz(L, C, matriz)


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

