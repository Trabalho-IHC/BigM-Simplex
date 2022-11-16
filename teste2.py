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
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

maior_linha = 0
maior_coluna = 0
maior = matriz[0][0]
for lin in range(L):
    for col in range(C):        
        if maior < matriz[lin][col]:
            maior = matriz[lin][col]
            maior_linha = lin
            maior_coluna = col

print('linha do maior: {}\ncoluna do maior: {}'.format(maior_linha, maior_coluna))

           
