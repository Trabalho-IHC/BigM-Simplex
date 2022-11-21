# def printarMatriz(L, C, matriz):
#     for l in range(0, L):
#         for c in range(0, C):
#             print(f'[{matriz[l][c]:^13}]', end='')
#     print()
# print("\n-------------------------------\n")
matriz = []
L = int(input("Digite o número de linhas:"))
C = int(input("Digite o número de colunas:"))
for i in range(L):
    matriz.append([])

for l in range(0, L):
    for c in range(0, C):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))

for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^13}]', end='')
    print()
print("\n-------------------------------\n")

def procura_big_m1():
    for c in range (0, C):
        if matriz[-1][c] > 99998:
            bigM = matriz[-1][c]
            return matriz[-1].index(bigM) #retorna coluna onde está o valor


#eu nao sei se essa coluna se chama coluna pivo, mas é a coluna q nois pega pra fazer as conta
def calc_coluna_pivo(): 
    ultima_posicao = matriz[-1][-1].index()
    menor_posicao = matriz[-1][0]
    coluna = 0 #só pra printar no console pra ver o valor
    for c in range(C):
        if matriz[-1][c] < 0:
            if matriz[-1][c] != matriz[-1][-1]:
                if menor_posicao < matriz[-1][c]:    
                    menor_posicao = matriz[-1][c]
                    coluna = c
                    return coluna
    print("calculo da coluna pivo: ", coluna)

#calcula pp e verifica qual menor valor
def calc_pp(): 
    lista_pp = []
    menor_valor_pp = 0
    index_menor_valor_pp = 0
    for l in range(0, L):
        if not l == 2: #se chegar na ultima linha ele é pra sair do for
            if matriz[l][-1] == 0:
                lista_pp.append(999999)
            else:
                lista_pp.append(matriz[l][-1] / matriz[l][calc_coluna_pivo()])
    menor_valor_pp = min(lista_pp)
    index_menor_valor_pp = lista_pp.index(menor_valor_pp)
    print("calc_pp - lista_pp: ", lista_pp)
    print("calc_pp - menor valor pp: ", menor_valor_pp)
    print("calc_pp - index menor valor: ", index_menor_valor_pp)
    return index_menor_valor_pp


for c in range(0, C):
    matriz[-1][c] = int(matriz[-1][c] - matriz[-1][procura_big_m1()] * matriz[calc_pp()][c])


for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^13}]', end='')
    print()

print("\n-------------------------------\n")

celulaTravadaL1_1 = matriz[0][1]
celulaTravadaL2_1 = matriz[1][1]
celulaTravadaL3_1 = matriz[2][1] 


for c in range(0, C):
    matriz[1][c] = round(matriz[1][c] / celulaTravadaL2_1, 1)
    matriz[0][c] = round(matriz[0][c] - celulaTravadaL1_1 * matriz[1][c], 1)
    matriz[2][c] = round(matriz[2][c] - celulaTravadaL3_1 * matriz[1][c], 1)
   
   
for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^13}]', end='')
    print()
#printarMatriz(L, C, matriz)

print("\n-------------------------------\n")

celulaTravadaL1_2 = matriz[0][0]
celulaTravadaL2_2 = matriz[1][0]
celulaTravadaL3_2 = matriz[2][0] 

for c in range(0, C):
    matriz[0][c] = round(matriz[0][c] / celulaTravadaL1_2, 1)
    matriz[1][c] = round(matriz[1][c] - celulaTravadaL2_2 * matriz[0][c], 1)
    matriz[2][c] = round(matriz[2][c] - celulaTravadaL3_2 * matriz[0][c], 1)

for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^13}]', end='')
    print()
#printarMatriz(L, C, matriz)

print("\n-------------------------------\n")

x1 = matriz[0][5]
x2 = matriz[1][5]
z = ((matriz[2][5]) * (-1))
print("x1 = ",x1)
print("x2 = ",x2)
print("z = ",z)