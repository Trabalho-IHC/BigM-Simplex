import funcoes

matriz = []
L = int(input("Digite o número de linhas:"))
C = int(input("Digite o número de colunas:"))
for i in range(L):
    matriz.append([])

for l in range(0, L):
    for c in range(0, C):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))

funcoes.show_matrix(L, C, matriz)


# #CALCULA COLUNA PIVO PARA ESCALONAMENTOS
# def calc_coluna_pivo(): 
#     #ultima_posicao = matriz[-1][-1].index()
#     menor_valor = matriz[-1][0]
#     coluna = 0
#     for c in range(0, C):
#         if matriz[-1][c] != matriz[-1][-1]: #aqui precisa pegar posição ao inves do valor
#             if matriz[-1][c] < 0:
#                 if matriz[-1][c] < menor_valor:
#                     menor_valor = matriz[-1][c]
#                     coluna = c
#     return coluna

#calcula processo de producao e verifica qual menor valor
def calc_pp(): 
    lista_pp = []
    menor_valor_pp = 0
    index_menor_valor_pp = 0
    coluna_pivo = funcoes.calc_coluna_pivo(C, matriz)
    for l in range(0, L-1):
        if matriz[l][-1] == 0:
            lista_pp.append(999999)
        else:
            lista_pp.append(matriz[l][-1] / matriz[l][coluna_pivo])
    
    menor_valor_pp = min(lista_pp)
    index_menor_valor_pp = int(lista_pp.index(menor_valor_pp))
    return index_menor_valor_pp
    #return 1


#FOR PARA ZERAR BIGM
for c in range(0, C):
    matriz[-1][c] = int(matriz[-1][c] - matriz[-1][funcoes.procura_big_m(C, matriz)] * matriz[1][c])#matriz[linha do pivo][c]


funcoes.show_matrix(L, C, matriz)

