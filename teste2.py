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

ultimaLinha = []
for c in range(0, C):
  ultimaLinha.append(matriz[-1][c])

print(ultimaLinha)

listaBigM = []
for c in range(0, C):
  if ultimaLinha[c] > 9999:
     


