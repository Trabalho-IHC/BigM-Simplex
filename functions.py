def show_matriz(L, matriz):
    for l in range(0, L):
        print(matriz[l], end='\n')
    print("-------------------------------")


#retorna coluna do bigM
#retorna primeiro resultado que encontrar
def procura_big_m(C, matriz):
    for c in range (0, C):
        if matriz[-1][c] > 99998:
            bigM = matriz[-1][c]
            return matriz[-1].index(bigM)

def existe_bigM(C, matriz):
    for c in range (0, C):
        if matriz[-1][c] > 99998:
            return True


def bigM(C, matriz):
    for c in range (0, C):
        if matriz[-1][c] > 99998:
            bigM = matriz[-1][c]
            return bigM

#retorna linha onde está o pivô do bigM
def calc_linha_pivo_bigM(L, C, matriz):
    lista = []
    colBigM = procura_big_m(C, matriz)
    linha = 0
    for l in range (0, L-1):
        lista.append(matriz[l][colBigM]) #insere na lista todos os valores da coluna do bigM
    for l in range(len(lista)):
        if lista[l] == 1:
            linha = lista.index(lista[l]) 
    return linha

#zera variavel artificial na linha do z e faz a operação na linha do z, distribuindo o bigM pela matriz
def zera_var_artific_linha_z(L, C, matriz):
    big_M = bigM(C, matriz)
    coluna_bigM = procura_big_m(C, matriz)
    linha_pivo_bigM = calc_linha_pivo_bigM(L, C, matriz)
    for c in range(0, C):
        if matriz[-1][c] == big_M:
            matriz[-1][c] = int(matriz[-1][c] - matriz[-1][coluna_bigM] * matriz[linha_pivo_bigM][c])
        elif not matriz[-1][c] == big_M:
            matriz[-1][c] = int(matriz[-1][c] - big_M * matriz[linha_pivo_bigM][c])
    return matriz  


#calcula coluna pivo para os escalonamentos
#menor valor na linha do z
def calc_coluna_pivo(C, matriz): 
    menor_valor = matriz[-1][0]
    coluna = 0
    for c in range(0, C):
        if matriz[-1][c] != matriz[-1][-1]:
            if matriz[-1][c] < 0:
                if matriz[-1][c] < menor_valor:
                    menor_valor = matriz[-1][c]
                    coluna = c
    return coluna

#calcula processo de producao e verifica qual menor valor
#valor do b dividido pelo valor na mesma linha e na coluna pivo
#retorna index da linha pivo
def linha_pivo(L, C, matriz): 
    lista_pp = []
    menor_valor_pp = 0
    index_menor_valor_pp = 0
    coluna_pivo = calc_coluna_pivo(C, matriz)
    for l in range(0, L-1):
        if (matriz[l][coluna_pivo] == 0) or (matriz[l][coluna_pivo] < 0):
            lista_pp.append(999999)
        elif matriz[l][-1] / matriz[l][coluna_pivo] < 0:
            lista_pp.append(999999)
        else:
            lista_pp.append(matriz[l][-1] / matriz[l][coluna_pivo])
    
    menor_valor_pp = min(lista_pp)
    index_menor_valor_pp = int(lista_pp.index(menor_valor_pp))
    return index_menor_valor_pp


def escalonamento(L, C, matriz):
    lin_pivo = linha_pivo(L, C, matriz)
    col_pivo = calc_coluna_pivo(C, matriz)
    
    cels_travadas = []

    for l in range(0, L):
        cels_travadas.append(matriz[l][col_pivo]) #joga valores da coluna pivo aqui

    for l in range(0, L):
        if l == lin_pivo:
            for c in range(0, C):
                matriz[l][c] = round(matriz[l][c] / cels_travadas[l], 5) 

    for l in range(0, L):
        if l != lin_pivo:
            for c in range(0, C):
                matriz[l][c] = round(matriz[l][c] - cels_travadas[l] * matriz[lin_pivo][c], 5)


    return matriz

def retorna_z(C, matriz):
    z = (matriz[-1][-1]) * (-1)
    return print("FO = ", z)  


def verifica_valor_negativo_linha_z(matriz):
    lista_val_z = []
    for c in range(0, 19): 
        lista_val_z.append(matriz[-1][c])
    for c in range(len(lista_val_z)):
        if lista_val_z[c] < 0:
            return True


# def caminho(L, matriz):
#     colunas_caminho = []
#     for c in range(1, 3):
#         for l in range(0, L):
#             if matriz[l][c] == 1 and matriz[l][-1] == 1: 
#                 colunas_caminho.append(c)
#     return print(colunas_caminho)     