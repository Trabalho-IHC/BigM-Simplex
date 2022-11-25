# matriz possui 56 colunas e 36 linhas
# 10 variaveis de folga
# 20 variaveis

import functions
import matriz as mtrz

matriz = []
matriz = mtrz.export_matriz()

linhas = 0
colunas = 0

for c in range(len(matriz[-1])):
    colunas += 1

linhas = len(matriz)


for a in range(10):
    functions.zera_var_artific_linha_z(linhas, colunas, matriz)

for c in range(0, colunas):
    if c < 17:
        functions.escalonamento(linhas, colunas, matriz)

functions.show_matriz(linhas, matriz)
functions.retorna_z(colunas, matriz)