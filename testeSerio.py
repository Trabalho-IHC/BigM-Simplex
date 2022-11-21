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


def procura_big_m():
    for c in range (0, C):
        if matriz[-1][c] > 99998:
            bigM = matriz[-1][c]
            return matriz[-1].index(bigM) #retorna coluna onde está o valor

for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^13}]', end='')
    print()
print("\n-------------------------------\n")

#print("big M: ", procura_big_m())

def calc_coluna_pivo(): 
    #ultima_posicao = matriz[-1][-1].index()
    menor_valor = matriz[-1][0]
    coluna = 0
    for c in range(0, C):
        if matriz[-1][c] != matriz[-1][-1]:
            if matriz[-1][c] < 0:
                #print("passou 1")
                print("matriz -1 c: ", matriz[-1][c])
                #print("passou 2")
                if matriz[-1][c] < menor_valor:
                    print("passou 3")
                    print("matriz -1 c: ", matriz[-1][c])
                    print("menor valor: ", menor_valor)     
                    menor_valor = matriz[-1][c]
                    coluna = c
    #teste = matriz[-1][coluna].index(menor_valor)
    return coluna

print("coluna pivo: ", calc_coluna_pivo())

#calcula pp e verifica qual menor valor
def calc_pp(): 
    lista_pp = []
    menor_valor_pp = 0
    index_menor_valor_pp = 0
    coluna_pivo = calc_coluna_pivo()
    for l in range(0, L-1):
        #if not l == 2: #se chegar na ultima linha ele é pra sair do for
        if matriz[l][-1] == 0:
            lista_pp.append(999999)
        else:
            lista_pp.append(matriz[l][-1] / matriz[l][coluna_pivo])
            #lista_pp.append(1)
    
    menor_valor_pp = min(lista_pp)
    index_menor_valor_pp = int(lista_pp.index(menor_valor_pp))
    # print("calc_pp - lista_pp: ", lista_pp)
    # print("calc_pp - menor valor pp: ", menor_valor_pp)
    # print("calc_pp - index menor valor: ", index_menor_valor_pp)
    return index_menor_valor_pp


# for c in range(0, C):
#     print("matriz antesssss da operacao: ", matriz[-1][c])

for c in range(0, C):
    # print("matriz antes da operacao: ", matriz[-1][c])
    # print("c antes ", c)
    # print("big m ", matriz[-1][procura_big_m()])
    # print("pp ", matriz[calc_pp()][c])
    matriz[-1][c] = int(matriz[-1][c] - matriz[-1][procura_big_m()] * matriz[calc_pp()][c])
    # print("matriz depois da operacao: ", matriz[-1][c])
    # print("c depois ", c)

for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^13}]', end='')
    print()

print("\n-------------------------------\n")

