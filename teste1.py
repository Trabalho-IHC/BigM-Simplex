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
        print(f'[{matriz[l][c]:^9}]', end='')
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

matriz[2][1] = matriz[2][1] - matriz[maior_linha][maior_coluna] * matriz[1][1]
matriz[maior_linha][maior_coluna] -= matriz[maior_linha][maior_coluna] * [1][4]

for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^9}]', end='')
    print()