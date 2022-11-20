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


# ultimaLinha = []
# for c in range(0, C):
#   ultimaLinha.append(matriz[-1][c])

# print(ultimaLinha)

# listaBigM = []
# for c in range(0, C):
#   if ultimaLinha[c] > 9999:

def procura_big_m1():
    for c in range (0, C):
        if matriz[-1][c] > 99998:
            bigM = matriz[-1][c]
            return matriz[-1].index(bigM) #retorna coluna onde está o valor


for c in range(0, C):
    matriz[2][c] = int(matriz[2][c] - matriz[-1][procura_big_m1()] * matriz[1][c])


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