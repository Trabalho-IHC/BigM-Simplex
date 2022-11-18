
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
        print(f'[{matriz[l][c]:^15}]', end='')
    print()

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
print('linha do maior: {}\ncoluna do maior: {}'.format(mLin, mCol))
bigM = matriz[maior_linha][maior_coluna]

#matriz[2][1] = matriz[2][1] - bigM * matriz[1][1]
#matriz[maior_linha][maior_coluna] -= bigM * matriz[1][4]
#matriz[2][c] = matriz[2][c] - bigM * matriz[1][c]


for c in range(0, C):
    matriz[2][c] = matriz[2][c] - bigM * matriz[1][c]

bigM = 0
bigM = matriz[2][1]

for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^9}]', end='')
    print()
print("////////////////////////////////////////////")

numQueEuEsqueciONOME1 = matriz[1][1]
numQueEuEsqueciONOME2 = matriz[2][1] 

for c in range(0, C):
    matriz[1][c] = matriz[1][c] / numQueEuEsqueciONOME1
    matriz[0][c] = matriz[0][c] - matriz[0][1] * matriz[1][0]
    matriz[2][c] = matriz[2][c] - numQueEuEsqueciONOME2 * matriz[1][c]
   
   
for l in range(0, L):
    for c in range(0, C):
        round(matriz[l][c], 2)
        print(f'[{matriz[l][c]:^9}]', end='')
    print()