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


funcoes.zera_var_artific_linha_z(L, C, matriz)

funcoes.show_matrix(L, C, matriz)

