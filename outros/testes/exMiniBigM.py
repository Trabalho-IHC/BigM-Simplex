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
#achar posicao do maior numero
maior_linha = 0
maior_coluna = 0
maior = matriz[0][0]
for lin in range(L):
    for col in range(C):        
        if maior < matriz[lin][col]:
            maior = matriz[lin][col]
            maior_linha = lin
            maior_coluna = col
mLin = maior_linha + 1
mCol = maior_coluna + 1
#print('linha do maior: {}\ncoluna do maior: {}'.format(mLin, mCol))
bigM = matriz[maior_linha][maior_coluna]

for c in range(0, C):
    matriz[2][c] = int(matriz[2][c] - bigM * matriz[1][c])


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