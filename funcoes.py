def show_matrix(L, C, matriz):
  print("\n")
  for l in range(0, L):
    for c in range(0, C):
        print(f'[{matriz[l][c]:^13}]', end='')
    print()
print("-------------------------------")
print("\n")

#FUNCAO QUE RETORNA COLUNA ONDE ESTÁ O BIGM
#RETORNA PRIMEIRO RESULTADO QUE ENCONTRAR
def procura_big_m(C, matriz):
    for c in range (0, C):
        if matriz[-1][c] > 99998:
            bigM = matriz[-1][c]
            return matriz[-1].index(bigM) #retorna coluna onde está o valor do bigM



#CALCULA COLUNA PIVO PARA ESCALONAMENTOS
def calc_coluna_pivo(C, matriz): 
    #ultima_posicao = matriz[-1][-1].index()
    menor_valor = matriz[-1][0]
    coluna = 0
    for c in range(0, C):
        if matriz[-1][c] != matriz[-1][-1]: #aqui precisa pegar posição ao inves do valor
            if matriz[-1][c] < 0:
                if matriz[-1][c] < menor_valor:
                    menor_valor = matriz[-1][c]
                    coluna = c
    return coluna